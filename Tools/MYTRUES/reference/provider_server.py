#!/usr/bin/env python3
import hashlib
import json
import os
import re
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse

PROTOCOL = "mytrues.decision/v1"
PROVIDER_ID = os.environ.get("MYTRUES_PROVIDER_ID", "provider-unknown")
PROFILE = os.environ.get("MYTRUES_PROVIDER_PROFILE", "fqdn")
PORT = int(os.environ.get("PORT", "8080"))

requests_store = {}
learned = {}
knowledge_revision = 1

SAFE_KEYS = {"runtime", "database", "os", "missing_extension", "error_class", "dependency_type"}
SENSITIVE = re.compile(r"(secret|token|password|credential|client|tenant|subscription|domain|host|url|ip|repo|user|account|resource)", re.I)

def known_dns(request):
    c=request.get("context", {})
    if PROFILE == "fqdn" and c.get("azure_provider_fqdn_available"):
        return {
          "id":"decision.dns.use_azure_provider_fqdn",
          "action":"delivery.use_provider_endpoint",
          "result":{"endpoint":{"type":"hostname","value":c.get("azure_provider_fqdn"),"scheme":"http"}},
          "guards":[{"key":"azure_provider_fqdn_available","satisfied":True}],
          "notice":"Custom DNS is unavailable; this provider chose the Azure hostname."
        }
    if PROFILE == "ip" and c.get("azure_public_ip_available"):
        return {
          "id":"decision.dns.expose_public_ip",
          "action":"delivery.use_provider_endpoint",
          "result":{"endpoint":{"type":"ip","value":c.get("azure_public_ip"),"scheme":"http"}},
          "guards":[{"key":"azure_public_ip_available","satisfied":True}],
          "notice":"Custom DNS is unavailable; this provider chose the public IP."
        }
    return None

def abstract_value(key, value):
    if SENSITIVE.search(key):
        return "<redacted>"
    if key in SAFE_KEYS:
        return value
    if isinstance(value, (bool, int, float)):
        return value
    if value is None:
        return None
    if isinstance(value, list):
        return ["<item>" for _ in value]
    if isinstance(value, dict):
        return {k: abstract_value(k, v) for k, v in value.items()}
    return "<string>"

def make_case_packet(request):
    context=request.get("context", {})
    abstract={k:abstract_value(k,v) for k,v in context.items()}
    return {
      "failureCode":request["subject"]["code"],
      "abstractContext":abstract,
      "sandboxFixture":{
        "runtime": context.get("runtime", "generic"),
        "database": context.get("database", "generic"),
        "domain":"sandbox.example.invalid",
        "public_ip":"203.0.113.10",
        "secret":"<synthetic-secret>"
      }
    }

def response_for(request, decision):
    return {
      "protocol":PROTOCOL,
      "requestId":request["requestId"],
      "status":"decided",
      "provider":{"id":PROVIDER_ID},
      "decision":{"id":decision["id"]},
      "selected":{"action":decision["action"],"result":decision["result"]},
      "guards":decision.get("guards", []),
      "notice":decision.get("notice", ""),
      "meta":{"policyVersion":"reference-0.2","knowledgeRevision":knowledge_revision}
    }

def pending_for(request, drid):
    return {
      "protocol":PROTOCOL,
      "requestId":request["requestId"],
      "status":"awaiting-provider-decision",
      "provider":{"id":PROVIDER_ID},
      "decisionRequestId":drid,
      "statusUrl":f"/v1/decision-requests/{drid}",
      "casePacket":make_case_packet(request)
    }

class Handler(BaseHTTPRequestHandler):
    def send_json(self, status, payload, location=None):
        body=json.dumps(payload).encode()
        self.send_response(status)
        self.send_header("Content-Type","application/json")
        if location:
            self.send_header("Location", location)
        tp=self.headers.get("traceparent")
        if tp:
            self.send_header("traceparent", tp)
        self.send_header("Content-Length",str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def read_json(self):
        return json.loads(self.rfile.read(int(self.headers.get("Content-Length","0"))))

    def do_GET(self):
        if self.path == "/healthz":
            return self.send_json(200,{"status":"ok","provider":PROVIDER_ID})
        m=re.fullmatch(r"/v1/decision-requests/([^/]+)", self.path)
        if m:
            drid=m.group(1)
            item=requests_store.get(drid)
            if not item:
                return self.send_json(404,{"status":"not-found"})
            if item.get("decision"):
                return self.send_json(200,response_for(item["request"],item["decision"]))
            return self.send_json(202,pending_for(item["request"],drid))
        return self.send_json(404,{"status":"not-found"})

    def do_POST(self):
        global knowledge_revision
        if self.path == "/v1/decisions/resolve.failure":
            request=self.read_json()
            code=request.get("subject",{}).get("code")
            decision=learned.get(code)
            if not decision and code == "dns.requested_provider_credentials_missing":
                decision=known_dns(request)
            if decision:
                return self.send_json(200,response_for(request,decision))

            raw=f"{PROVIDER_ID}:{request.get('requestId')}:{code}".encode()
            drid="dr-"+hashlib.sha256(raw).hexdigest()[:16]
            requests_store.setdefault(drid,{"request":request,"decision":None})
            payload=pending_for(request,drid)
            return self.send_json(202,payload,payload["statusUrl"])

        m=re.fullmatch(r"/v1/provider/decision-requests/([^/]+)/resolution", self.path)
        if m:
            drid=m.group(1)
            item=requests_store.get(drid)
            if not item:
                return self.send_json(404,{"status":"not-found"})
            payload=self.read_json()
            decision=payload["decision"]
            code=item["request"]["subject"]["code"]
            learned[code]=decision
            item["decision"]=decision
            knowledge_revision += 1
            return self.send_json(200,response_for(item["request"],decision))

        return self.send_json(404,{"status":"not-found"})

    def log_message(self, fmt, *args):
        print(f"[{PROVIDER_ID}] "+fmt%args)

if __name__ == "__main__":
    print(f"MyTrues provider={PROVIDER_ID} profile={PROFILE} port={PORT}")
    ThreadingHTTPServer(("0.0.0.0",PORT),Handler).serve_forever()
