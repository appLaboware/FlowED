#!/usr/bin/env python3
import json
import subprocess
import time
import urllib.request
from pathlib import Path

from jsonschema import Draft202012Validator, validate

A = "http://127.0.0.1:18081"
B = "http://127.0.0.1:18082"

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_DIR = ROOT / "protocol" / "schemas"

SCHEMA_FILES = {
    "request": "decision-request.schema.json",
    "response": "decision-response.schema.json",
    "pending": "decision-pending.schema.json",
    "resolution": "provider-resolution.schema.json",
    "problem": "problem.schema.json",
}

SCHEMAS = {
    name: json.loads((SCHEMA_DIR / filename).read_text())
    for name, filename in SCHEMA_FILES.items()
}

for name, schema in SCHEMAS.items():
    Draft202012Validator.check_schema(schema)
    schema_id = schema.get("$id", "")
    assert "/protocol/0.2/" in schema_id, f"{name} schema is not identified as v0.2: {schema_id}"


def check(instance, schema_name):
    validate(instance=instance, schema=SCHEMAS[schema_name])


def wait(url):
    for _ in range(60):
        try:
            if urllib.request.urlopen(url + "/healthz", timeout=2).status == 200:
                return
        except Exception:
            time.sleep(1)
    raise RuntimeError(url)


def call(method, url, payload=None):
    data = None if payload is None else json.dumps(payload).encode()
    request = urllib.request.Request(
        url,
        data=data,
        method=method,
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(request, timeout=5) as response:
        return response.status, dict(response.headers), json.load(response)


for url in (A, B):
    wait(url)

# Same known problem, different provider knowledge -> different outcome.
dns = {
    "protocol": "mytrues.decision/v1",
    "requestId": "dns-1",
    "subject": {
        "kind": "failure",
        "code": "dns.requested_provider_credentials_missing",
    },
    "context": {
        "azure_provider_fqdn_available": True,
        "azure_provider_fqdn": "site.example.invalid",
        "azure_provider_port": 8080,
        "azure_public_ip_available": True,
        "azure_public_ip": "203.0.113.42",
    },
    "constraints": {
        "automation": "automatic",
        "maxRisk": "low",
    },
}
check(dns, "request")

sa, _, da = call("POST", A + "/v1/decisions/resolve.failure", dns)
sb, _, db = call("POST", B + "/v1/decisions/resolve.failure", dns)

assert sa == sb == 200
check(da, "response")
check(db, "response")

assert da["provider"]["id"] == "senior-a"
assert da["selected"]["result"]["endpoint"]["type"] == "hostname"
assert db["provider"]["id"] == "senior-b"
assert db["selected"]["result"]["endpoint"]["type"] == "ip"

# Unknown problem -> both providers pause instead of inventing.
unknown = {
    "protocol": "mytrues.decision/v1",
    "requestId": "php-unknown-1",
    "subject": {
        "kind": "failure",
        "code": "runtime.php.extension_missing",
    },
    "context": {
        "runtime": "php",
        "database": "mysql",
        "missing_extension": "pdo_mysql",
        "customer_domain": "customer.example.invalid",
        "AZURE_CLIENT_ID": "synthetic-client-id-must-not-leak",
        "public_ip": "198.51.100.77",
    },
    "constraints": {
        "automation": "automatic",
        "maxRisk": "low",
    },
}
check(unknown, "request")

pa, ha, pba = call("POST", A + "/v1/decisions/resolve.failure", unknown)
pb, hb, pbb = call("POST", B + "/v1/decisions/resolve.failure", unknown)

assert pa == pb == 202
check(pba, "pending")
check(pbb, "pending")
assert ha.get("Location") == pba["statusUrl"]
assert hb.get("Location") == pbb["statusUrl"]
assert pba["status"] == pbb["status"] == "awaiting-provider-decision"

serialized = json.dumps(pba)
for forbidden in (
    "customer.example.invalid",
    "synthetic-client-id-must-not-leak",
    "198.51.100.77",
):
    assert forbidden not in serialized

assert pba["casePacket"]["abstractContext"]["runtime"] == "php"
assert pba["casePacket"]["abstractContext"]["missing_extension"] == "pdo_mysql"

# Human senior A resolves the synthetic case.
resolution = {
    "decision": {
        "id": "decision.php.install_pdo_mysql",
        "action": "runtime.install_missing_extension",
        "result": {
            "extension": "pdo_mysql",
            "strategy": "install-and-retry",
        },
        "guards": [{"key": "runtime_is_php", "satisfied": True}],
        "notice": (
            "Provider senior-a approved installation of the missing "
            "PHP extension and retry."
        ),
    }
}
check(resolution, "resolution")

drid_a = pba["decisionRequestId"]
status, _, resolved = call(
    "POST",
    A + f"/v1/provider/decision-requests/{drid_a}/resolution",
    resolution,
)
assert status == 200
check(resolved, "response")
assert resolved["status"] == "decided"

# Existing paused request now becomes resumable.
status, _, after = call("GET", A + f"/v1/decision-requests/{drid_a}")
assert status == 200
check(after, "response")
assert after["decision"]["id"] == "decision.php.install_pdo_mysql"

# Prove provider memory is durable, not only process memory.
subprocess.run(
    ["docker", "compose", "restart", "mytrues-senior-a", "mytrues-senior-b"],
    check=True,
)
for url in (A, B):
    wait(url)

# A remembers after restart.
repeat = dict(unknown)
repeat["requestId"] = "php-unknown-after-restart"
check(repeat, "request")
status, _, learned = call("POST", A + "/v1/decisions/resolve.failure", repeat)
assert status == 200
check(learned, "response")
assert learned["decision"]["id"] == "decision.php.install_pdo_mysql"

# B did not inherit A's knowledge, and its original request remains pending after restart.
status, _, still = call("GET", B + pbb["statusUrl"])
assert status == 202
check(still, "pending")
assert still["status"] == "awaiting-provider-decision"

print(
    json.dumps(
        {
            "protocol": "PASS",
            "schema_version": "0.2",
            "schema_conformance": {
                "meta_schema": "PASS",
                "request": "PASS",
                "response": "PASS",
                "pending": "PASS",
                "provider_resolution": "PASS",
                "problem_schema_definition": "PASS",
            },
            "provider_choice_changes_dns_outcome": {
                "senior-a": da["selected"]["result"],
                "senior-b": db["selected"]["result"],
            },
            "unknown_case": {
                "senior-a_initial": "awaiting-provider-decision",
                "senior-a_after_human": "decided",
                "senior-a_after_restart": "decided-immediately",
                "senior-b_after_restart": "still-awaiting-provider-decision",
            },
            "anonymization": "PASS",
            "persistent_provider_memory": "PASS",
        },
        indent=2,
    )
)
