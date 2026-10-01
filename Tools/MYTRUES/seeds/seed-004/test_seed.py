#!/usr/bin/env python3
import json
import subprocess
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MANIFEST_PATH = Path(__file__).with_name("manifest.json")
MANIFEST = json.loads(MANIFEST_PATH.read_text())

PROVIDERS = {
    "senior-a": "http://127.0.0.1:18081",
    "senior-b": "http://127.0.0.1:18082",
}

EXPECTED_CODES = {
    "azure.aci.smb_volume_permissions_root",
    "wordpress.canonical_host_mismatch",
    "cloudflare.healthcheck_stale_backend",
    "wordpress.installer_ssl_redirect_loop",
    "azure.aci.quota_environment_exhausted",
    "azure.region_edge_reachability",
    "sqlite.dropin_stub_deployed",
    "wordpress.maintenance_transient",
    "php.extension_missing",
    "git.dubious_ownership",
    "docker.network_wrong_bridge",
    "docker.volume_uid_mismatch",
    "wordpress.wpconfig_missing_abspath",
    "azure.resourcegroup_delete_slow",
    "provider.no_api_captcha",
    "observability.novel_failure_never_seen",
}

DIVERGENT_CODES = {
    "php.extension_missing",
    "wordpress.maintenance_transient",
    "sqlite.dropin_stub_deployed",
    "git.dubious_ownership",
}

CONTROL_CODE = "observability.novel_failure_never_seen"


def wait(url):
    for _ in range(60):
        try:
            with urllib.request.urlopen(url + "/healthz", timeout=2) as response:
                if response.status == 200:
                    return
        except Exception:
            pass
        time.sleep(1)
    raise RuntimeError(f"service not ready: {url}")


def call(method, url, payload=None):
    data = None if payload is None else json.dumps(payload).encode()
    request = urllib.request.Request(
        url,
        data=data,
        method=method,
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(request, timeout=5) as response:
        return response.status, json.load(response)


def request_for(case, provider):
    return {
        "protocol": "mytrues.decision/v1",
        "requestId": f"seed004-{provider}-{case['failure_code']}",
        "subject": {
            "kind": "failure",
            "code": case["failure_code"],
        },
        "context": case["context"],
        "constraints": {
            "automation": "automatic",
            "maxRisk": "low",
        },
    }


cases = MANIFEST["cases"]
codes = {case["failure_code"] for case in cases}

assert len(cases) == 16, len(cases)
assert codes == EXPECTED_CODES, sorted(codes ^ EXPECTED_CODES)

counts = {
    provider: sum(
        1 for case in cases if provider in (case.get("decisions") or {})
    )
    for provider in PROVIDERS
}
assert counts == {"senior-a": 11, "senior-b": 8}, counts

shared = {
    case["failure_code"]
    for case in cases
    if set((case.get("decisions") or {}).keys()) == set(PROVIDERS)
}
assert shared == DIVERGENT_CODES, shared

control = next(case for case in cases if case["failure_code"] == CONTROL_CODE)
assert not control.get("decisions"), control

for url in PROVIDERS.values():
    wait(url)

observed = {}
control_status_urls = {}

for case in cases:
    code = case["failure_code"]
    observed[code] = {}

    for provider, url in PROVIDERS.items():
        expected = (case.get("decisions") or {}).get(provider)
        status, payload = call(
            "POST",
            url + "/v1/decisions/resolve.failure",
            request_for(case, provider),
        )

        observed[code][provider] = {
            "status": status,
            "decision": payload.get("decision", {}).get("id"),
        }

        if expected:
            assert status == 200, (code, provider, status, payload)
            assert payload["status"] == "decided"
            assert payload["provider"]["id"] == provider
            assert payload["decision"]["id"] == expected["id"]
            assert payload["selected"]["action"] == expected["action"]
        else:
            assert status == 202, (code, provider, status, payload)
            assert payload["status"] == "awaiting-provider-decision"
            assert payload["provider"]["id"] == provider

            if code == CONTROL_CODE:
                control_status_urls[provider] = payload["statusUrl"]

for code in DIVERGENT_CODES:
    a = observed[code]["senior-a"]
    b = observed[code]["senior-b"]
    assert a["status"] == b["status"] == 200
    assert a["decision"] != b["decision"], (code, a, b)

assert set(control_status_urls) == set(PROVIDERS)

# Persistence proof: restart only processes, preserving the provider-specific SQLite volumes.
subprocess.run(
    ["docker", "compose", "restart", "mytrues-senior-a", "mytrues-senior-b"],
    cwd=ROOT,
    check=True,
)

for url in PROVIDERS.values():
    wait(url)

# Seeded provider memories remain available after restart.
for code in sorted(DIVERGENT_CODES):
    case = next(item for item in cases if item["failure_code"] == code)
    for provider, url in PROVIDERS.items():
        expected = case["decisions"][provider]
        status, payload = call(
            "POST",
            url + "/v1/decisions/resolve.failure",
            {
                **request_for(case, provider),
                "requestId": f"seed004-restart-{provider}-{code}",
            },
        )
        assert status == 200
        assert payload["decision"]["id"] == expected["id"]

# Pending control requests also survive process restart in each provider's own SQLite.
for provider, url in PROVIDERS.items():
    status, payload = call("GET", url + control_status_urls[provider])
    assert status == 202
    assert payload["status"] == "awaiting-provider-decision"
    assert payload["provider"]["id"] == provider

print(
    json.dumps(
        {
            "seed": MANIFEST.get("seed"),
            "version": MANIFEST.get("version"),
            "cases": len(cases),
            "provider_decision_counts": counts,
            "divergent_codes": sorted(DIVERGENT_CODES),
            "control_code": CONTROL_CODE,
            "control_behavior": {
                "senior-a": "202 awaiting-provider-decision",
                "senior-b": "202 awaiting-provider-decision",
            },
            "provider_scoped_memory_after_restart": "PASS",
            "result": "PASS",
        },
        indent=2,
    )
)
