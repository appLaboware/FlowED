#!/usr/bin/env python3
import hashlib
import json
import os
import re
import sqlite3
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

PROTOCOL = "mytrues.decision/v1"
PROVIDER_ID = os.environ.get("MYTRUES_PROVIDER_ID", "provider-unknown")
PROFILE = os.environ.get("MYTRUES_PROVIDER_PROFILE", "fqdn")
PORT = int(os.environ.get("PORT", "8080"))
DB_PATH = os.environ.get("MYTRUES_DB_PATH", "/data/mytrues.db")

SAFE_KEYS = {
    "runtime",
    "database",
    "os",
    "missing_extension",
    "error_class",
    "dependency_type",
}
SENSITIVE = re.compile(
    r"(secret|token|password|credential|client|tenant|subscription|domain|host|url|ip|repo|user|account|resource)",
    re.I,
)


def connect():
    db = sqlite3.connect(DB_PATH)
    db.row_factory = sqlite3.Row
    return db


def init_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    with connect() as db:
        db.executescript(
            """
            CREATE TABLE IF NOT EXISTS meta (
              key TEXT PRIMARY KEY,
              value TEXT NOT NULL
            );

            CREATE TABLE IF NOT EXISTS decisions (
              failure_code TEXT PRIMARY KEY,
              decision_json TEXT NOT NULL,
              source TEXT NOT NULL,
              created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
              updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            );

            CREATE TABLE IF NOT EXISTS decision_requests (
              id TEXT PRIMARY KEY,
              request_json TEXT NOT NULL,
              decision_json TEXT,
              created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
              resolved_at TEXT
            );
            """
        )
        db.execute(
            "INSERT OR IGNORE INTO meta(key,value) VALUES('knowledge_revision','1')"
        )

        if PROFILE == "fqdn":
            seed = {
                "id": "decision.dns.use_azure_provider_fqdn",
                "action": "delivery.use_provider_endpoint",
                "resultTemplate": {
                    "endpoint": {
                        "type": "hostname",
                        "contextKey": "azure_provider_fqdn",
                        "scheme": "http",
                    }
                },
                "guards": [
                    {"key": "azure_provider_fqdn_available", "satisfied": True}
                ],
                "notice": "Custom DNS is unavailable; this provider chose the Azure hostname.",
            }
        else:
            seed = {
                "id": "decision.dns.expose_public_ip",
                "action": "delivery.use_provider_endpoint",
                "resultTemplate": {
                    "endpoint": {
                        "type": "ip",
                        "contextKey": "azure_public_ip",
                        "scheme": "http",
                    }
                },
                "guards": [
                    {"key": "azure_public_ip_available", "satisfied": True}
                ],
                "notice": "Custom DNS is unavailable; this provider chose the public IP.",
            }

        db.execute(
            """
            INSERT OR IGNORE INTO decisions(failure_code,decision_json,source)
            VALUES(?,?,?)
            """,
            (
                "dns.requested_provider_credentials_missing",
                json.dumps(seed),
                "provider-seed",
            ),
        )


def knowledge_revision():
    with connect() as db:
        row = db.execute(
            "SELECT value FROM meta WHERE key='knowledge_revision'"
        ).fetchone()
        return int(row["value"])


def bump_revision(db):
    row = db.execute(
        "SELECT value FROM meta WHERE key='knowledge_revision'"
    ).fetchone()
    value = int(row["value"]) + 1
    db.execute(
        "UPDATE meta SET value=? WHERE key='knowledge_revision'",
        (str(value),),
    )
    return value


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
    context = request.get("context", {})
    abstract = {k: abstract_value(k, v) for k, v in context.items()}
    return {
        "failureCode": request["subject"]["code"],
        "abstractContext": abstract,
        "sandboxFixture": {
            "runtime": context.get("runtime", "generic"),
            "database": context.get("database", "generic"),
            "domain": "sandbox.example.invalid",
            "public_ip": "203.0.113.10",
            "secret": "<synthetic-secret>",
        },
    }


def materialize(decision, request):
    result = decision.get("result")
    if result is not None:
        return decision

    template = decision.get("resultTemplate", {})
    endpoint = template.get("endpoint")
    if endpoint:
        key = endpoint["contextKey"]
        value = request.get("context", {}).get(key)
        if value is None:
            raise LookupError(f"required context value is missing: {key}")
        materialized = dict(decision)
        materialized["result"] = {
            "endpoint": {
                "type": endpoint["type"],
                "value": value,
                "scheme": endpoint.get("scheme", "http"),
            }
        }
        return materialized

    raise LookupError("decision has no materializable result")


def load_decision(failure_code):
    with connect() as db:
        row = db.execute(
            "SELECT decision_json FROM decisions WHERE failure_code=?",
            (failure_code,),
        ).fetchone()
        return json.loads(row["decision_json"]) if row else None


def response_for(request, decision):
    selected = materialize(decision, request)
    return {
        "protocol": PROTOCOL,
        "requestId": request["requestId"],
        "status": "decided",
        "provider": {"id": PROVIDER_ID},
        "decision": {"id": selected["id"]},
        "selected": {
            "action": selected["action"],
            "result": selected["result"],
        },
        "guards": selected.get("guards", []),
        "notice": selected.get("notice", ""),
        "meta": {
            "policyVersion": "reference-open-0.3",
            "knowledgeRevision": knowledge_revision(),
        },
    }


def pending_for(request, drid):
    return {
        "protocol": PROTOCOL,
        "requestId": request["requestId"],
        "status": "awaiting-provider-decision",
        "provider": {"id": PROVIDER_ID},
        "decisionRequestId": drid,
        "statusUrl": f"/v1/decision-requests/{drid}",
        "casePacket": make_case_packet(request),
    }


class Handler(BaseHTTPRequestHandler):
    def send_json(self, status, payload, location=None):
        body = json.dumps(payload).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        if location:
            self.send_header("Location", location)
        traceparent = self.headers.get("traceparent")
        if traceparent:
            self.send_header("traceparent", traceparent)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def read_json(self):
        length = int(self.headers.get("Content-Length", "0"))
        return json.loads(self.rfile.read(length))

    def do_GET(self):
        if self.path == "/healthz":
            return self.send_json(
                200,
                {
                    "status": "ok",
                    "provider": PROVIDER_ID,
                    "knowledgeRevision": knowledge_revision(),
                },
            )

        match = re.fullmatch(r"/v1/decision-requests/([^/]+)", self.path)
        if match:
            drid = match.group(1)
            with connect() as db:
                row = db.execute(
                    "SELECT request_json,decision_json FROM decision_requests WHERE id=?",
                    (drid,),
                ).fetchone()
            if not row:
                return self.send_json(404, {"status": "not-found"})

            request = json.loads(row["request_json"])
            if row["decision_json"]:
                return self.send_json(
                    200,
                    response_for(request, json.loads(row["decision_json"])),
                )
            return self.send_json(202, pending_for(request, drid))

        return self.send_json(404, {"status": "not-found"})

    def do_POST(self):
        if self.path == "/v1/decisions/resolve.failure":
            request = self.read_json()
            if request.get("protocol") != PROTOCOL:
                return self.send_json(400, {"status": "invalid-protocol"})

            code = request.get("subject", {}).get("code")
            decision = load_decision(code)
            if decision:
                try:
                    return self.send_json(200, response_for(request, decision))
                except LookupError:
                    pass

            raw = f"{PROVIDER_ID}:{request.get('requestId')}:{code}".encode()
            drid = "dr-" + hashlib.sha256(raw).hexdigest()[:16]
            with connect() as db:
                db.execute(
                    """
                    INSERT OR IGNORE INTO decision_requests(id,request_json)
                    VALUES(?,?)
                    """,
                    (drid, json.dumps(request)),
                )

            payload = pending_for(request, drid)
            return self.send_json(202, payload, payload["statusUrl"])

        match = re.fullmatch(
            r"/v1/provider/decision-requests/([^/]+)/resolution",
            self.path,
        )
        if match:
            drid = match.group(1)
            payload = self.read_json()
            decision = payload["decision"]

            with connect() as db:
                row = db.execute(
                    "SELECT request_json FROM decision_requests WHERE id=?",
                    (drid,),
                ).fetchone()
                if not row:
                    return self.send_json(404, {"status": "not-found"})

                request = json.loads(row["request_json"])
                code = request["subject"]["code"]

                db.execute(
                    """
                    INSERT INTO decisions(failure_code,decision_json,source)
                    VALUES(?,?,?)
                    ON CONFLICT(failure_code) DO UPDATE SET
                      decision_json=excluded.decision_json,
                      source=excluded.source,
                      updated_at=CURRENT_TIMESTAMP
                    """,
                    (code, json.dumps(decision), "human-provider"),
                )
                db.execute(
                    """
                    UPDATE decision_requests
                    SET decision_json=?,resolved_at=CURRENT_TIMESTAMP
                    WHERE id=?
                    """,
                    (json.dumps(decision), drid),
                )
                bump_revision(db)

            return self.send_json(200, response_for(request, decision))

        return self.send_json(404, {"status": "not-found"})

    def log_message(self, fmt, *args):
        print(f"[{PROVIDER_ID}] " + fmt % args)


if __name__ == "__main__":
    init_db()
    print(
        f"MyTrues provider={PROVIDER_ID} profile={PROFILE} "
        f"db={DB_PATH} port={PORT}"
    )
    ThreadingHTTPServer(("0.0.0.0", PORT), Handler).serve_forever()
