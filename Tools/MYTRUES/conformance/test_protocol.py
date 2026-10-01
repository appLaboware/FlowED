#!/usr/bin/env python3
import json
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUEST = json.loads((ROOT / "protocol/examples/dns-failure.request.json").read_text())


def wait(url):
    for _ in range(60):
        try:
            with urllib.request.urlopen(url + "/healthz", timeout=2) as r:
                if r.status == 200:
                    return
        except Exception:
            pass
        time.sleep(1)
    raise RuntimeError(f"service not ready: {url}")


def decide(url):
    body = json.dumps(REQUEST).encode()
    req = urllib.request.Request(
        url + "/v1/decisions/resolve.failure",
        data=body,
        method="POST",
        headers={
            "Content-Type": "application/json",
            "traceparent": "00-4bf92f3577b34da6a3ce929d0e0e4736-00f067aa0ba902b7-01",
        },
    )
    with urllib.request.urlopen(req, timeout=5) as r:
        assert r.status == 200
        assert r.headers.get("traceparent")
        return json.load(r)


def assert_common(x):
    assert x["protocol"] == "mytrues.decision/v1"
    assert x["requestId"] == REQUEST["requestId"]
    assert x["status"] == "decided"
    assert x["selected"]["action"] == "delivery.use_provider_endpoint"
    assert x["guards"][0]["satisfied"] is True
    assert x["notice"]
    assert x["meta"]["engine"]


for url in ("http://127.0.0.1:18081", "http://127.0.0.1:18082"):
    wait(url)

fqdn = decide("http://127.0.0.1:18081")
ip = decide("http://127.0.0.1:18082")

assert_common(fqdn)
assert_common(ip)

assert fqdn["selected"]["result"]["endpoint"] == {
    "type": "hostname",
    "value": REQUEST["context"]["azure_provider_fqdn"],
    "scheme": "http",
}

assert ip["selected"]["result"]["endpoint"] == {
    "type": "ip",
    "value": REQUEST["context"]["azure_public_ip"],
    "scheme": "http",
}

assert fqdn["decision"]["id"] != ip["decision"]["id"]
assert fqdn["meta"]["engine"] != ip["meta"]["engine"]

print(json.dumps({
    "protocol": "PASS",
    "same_request": REQUEST["requestId"],
    "mytrues_fqdn": fqdn,
    "mytrues_ip": ip,
}, indent=2))
