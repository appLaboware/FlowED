#!/usr/bin/env python3
import importlib
import json
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

from cases import CASES

PROTOCOL = "mytrues.decision/v1"
ENGINE_MODULE = os.environ.get("MYTRUES_ENGINE", "fixtures.engine_fqdn")
PORT = int(os.environ.get("PORT", "8080"))

Engine = importlib.import_module(ENGINE_MODULE).Engine
engine = Engine()


def problem(handler, status, title, detail):
    payload = {
        "type": f"https://mytrues.dev/problems/{title.lower().replace(' ', '-')}",
        "title": title,
        "status": status,
        "detail": detail,
    }
    body = json.dumps(payload).encode()
    handler.send_response(status)
    handler.send_header("Content-Type", "application/problem+json")
    handler.send_header("Content-Length", str(len(body)))
    handler.end_headers()
    handler.wfile.write(body)


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/healthz":
            body = json.dumps({"status": "ok", "engine": engine.name}).encode()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return
        problem(self, 404, "Not Found", "Unknown endpoint")

    def do_POST(self):
        if self.path != "/v1/decisions/resolve.failure":
            return problem(self, 404, "Decision Not Found", "Unknown decision key")

        try:
            length = int(self.headers.get("Content-Length", "0"))
            request = json.loads(self.rfile.read(length))
        except Exception as exc:
            return problem(self, 400, "Invalid Request", str(exc))

        if request.get("protocol") != PROTOCOL:
            return problem(self, 400, "Invalid Protocol", "Unsupported protocol version")

        subject = request.get("subject") or {}
        code = subject.get("code")
        candidates = [
            c for c in CASES.get(code, [])
            if c["status"] == "approved"
        ]
        if not candidates:
            return problem(self, 404, "No Decision", f"No approved case for {code}")

        try:
            selected = engine.choose(request, candidates)
        except LookupError as exc:
            return problem(self, 409, "No Applicable Decision", str(exc))

        context = request["context"]
        endpoint_value = context.get(selected["context_key"])
        if not endpoint_value:
            return problem(self, 409, "Guard Failed", selected["guard"])

        payload = {
            "protocol": PROTOCOL,
            "requestId": request["requestId"],
            "status": "decided",
            "decision": {"id": selected["id"]},
            "selected": {
                "action": selected["action"],
                "result": {
                    "endpoint": {
                        "type": selected["endpoint_type"],
                        "value": endpoint_value,
                        "scheme": "http",
                    }
                },
            },
            "guards": [
                {"key": selected["guard"], "satisfied": True}
            ],
            "notice": selected["notice"],
            "meta": {
                "engine": engine.name,
                "policyVersion": engine.version,
            },
        }

        body = json.dumps(payload).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        traceparent = self.headers.get("traceparent")
        if traceparent:
            self.send_header("traceparent", traceparent)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, fmt, *args):
        print(fmt % args)


if __name__ == "__main__":
    print(f"MyTrues reference service on :{PORT}; engine={engine.name}")
    ThreadingHTTPServer(("0.0.0.0", PORT), Handler).serve_forever()
