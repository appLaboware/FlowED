#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import sqlite3
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.request
from pathlib import Path

from typedb.driver import TypeDB, TransactionType, Credentials, DriverOptions, DriverTlsConfig

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[3]
STREAM_PATH = HERE / "cognition-stream.json"
PROVIDER_SERVER = REPO / "Tools" / "MYTRUES" / "reference" / "provider_server.py"
TYPEDB_SCHEMA = REPO / "Tools" / "MyTrues" / "typedb-poc-bridge" / "00-schema.tql"

PROVIDER_PORT = 18091
PROVIDER_BASE = f"http://127.0.0.1:{PROVIDER_PORT}"
TYPEDB_DB = "mytrues_dual_memory_ab_001"
TYPEDB_OPTIONS = DriverOptions(DriverTlsConfig.disabled())


def post_json(url: str, payload: dict) -> tuple[int, dict]:
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode(),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            return response.status, json.loads(response.read())
    except urllib.error.HTTPError as error:
        return error.code, json.loads(error.read())


def get_json(url: str) -> tuple[int, dict]:
    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            return response.status, json.loads(response.read())
    except urllib.error.HTTPError as error:
        return error.code, json.loads(error.read())


def wait_http(url: str, seconds: int = 30) -> None:
    deadline = time.time() + seconds
    last = None
    while time.time() < deadline:
        try:
            status, _ = get_json(url)
            if status == 200:
                return
        except Exception as exc:
            last = exc
        time.sleep(0.25)
    raise RuntimeError(f"service not ready: {url}: {last}")


def provider_decision(event: dict) -> dict:
    return {
        "id": event["decision_id"],
        "action": event["action"],
        "result": event["result"],
        "guards": [{"key": "ab_test_guard", "satisfied": True}],
        "notice": event["reason"],
    }


def recursive_contains(value, needle: str) -> bool:
    if isinstance(value, dict):
        return any(recursive_contains(v, needle) for v in value.values())
    if isinstance(value, list):
        return any(recursive_contains(v, needle) for v in value)
    return value == needle


def run_provider_line(stream: dict) -> dict:
    events = stream["events"]
    obs = next(e for e in events if e["kind"] == "observation")
    decisions = [e for e in events if e["kind"] == "decision"]
    assert len(decisions) == 2

    with tempfile.TemporaryDirectory(prefix="mytrues-ab-provider-") as tmp:
        db_path = str(Path(tmp) / "provider.db")
        env = os.environ.copy()
        env.update(
            {
                "MYTRUES_PROVIDER_ID": "ab-provider-reference",
                "MYTRUES_PROVIDER_PROFILE": "fqdn",
                "MYTRUES_DB_PATH": db_path,
                "PORT": str(PROVIDER_PORT),
            }
        )
        proc = subprocess.Popen(
            [sys.executable, str(PROVIDER_SERVER)],
            env=env,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
        )
        try:
            wait_http(PROVIDER_BASE + "/healthz")

            request = {
                "protocol": "mytrues.decision/v1",
                "requestId": "ab-request-001",
                "subject": {"kind": "failure", "code": obs["failure_code"]},
                "context": obs["context"],
                "constraints": {"automation": "recommend-only", "maxRisk": "low"},
            }

            status, pending = post_json(PROVIDER_BASE + "/v1/decisions/resolve.failure", request)
            assert status == 202, (status, pending)
            drid = pending["decisionRequestId"]

            status, first = post_json(
                PROVIDER_BASE + f"/v1/provider/decision-requests/{drid}/resolution",
                {"decision": provider_decision(decisions[0])},
            )
            assert status == 200
            first_selected = first["decision"]["id"]

            status, second = post_json(
                PROVIDER_BASE + f"/v1/provider/decision-requests/{drid}/resolution",
                {"decision": provider_decision(decisions[1])},
            )
            assert status == 200
            second_selected = second["decision"]["id"]

            status, current = post_json(PROVIDER_BASE + "/v1/decisions/resolve.failure", request)
            assert status == 200
            current_id = current["decision"]["id"]

            db = sqlite3.connect(db_path)
            db.row_factory = sqlite3.Row
            try:
                decision_rows = list(db.execute("SELECT * FROM decisions WHERE failure_code=?", (obs["failure_code"],)))
                request_rows = list(db.execute("SELECT * FROM decision_requests"))
            finally:
                db.close()

            persisted_docs = []
            for row in decision_rows:
                persisted_docs.append(json.loads(row["decision_json"]))
            for row in request_rows:
                persisted_docs.append(json.loads(row["request_json"]))
                if row["decision_json"]:
                    persisted_docs.append(json.loads(row["decision_json"]))

            v1_present = any(recursive_contains(doc, decisions[0]["decision_id"]) for doc in persisted_docs)
            v2_present = any(recursive_contains(doc, decisions[1]["decision_id"]) for doc in persisted_docs)
            unique_decisions = [
                did
                for did in (decisions[0]["decision_id"], decisions[1]["decision_id"])
                if any(recursive_contains(doc, did) for doc in persisted_docs)
            ]
            original_context = json.loads(request_rows[0]["request_json"])["context"] if request_rows else None
            current_doc = json.loads(decision_rows[0]["decision_json"]) if decision_rows else {}

            return {
                "implementation": "Tools/MYTRUES/reference/provider_server.py",
                "storage": "SQLite reference provider memory",
                "first_resolution_observed": first_selected,
                "second_resolution_observed": second_selected,
                "current_decision": current_id,
                "persisted_previous_decision": decisions[0]["decision_id"] if v1_present else None,
                "persisted_current_decision": decisions[1]["decision_id"] if v2_present else None,
                "persisted_decision_ids": unique_decisions,
                "persisted_decision_count": len(unique_decisions),
                "original_context": original_context,
                "supersession_link": current_doc.get("supersedes"),
                "row_counts": {
                    "decisions": len(decision_rows),
                    "decision_requests": len(request_rows),
                },
            }
        finally:
            proc.terminate()
            try:
                proc.wait(timeout=5)
            except subprocess.TimeoutExpired:
                proc.kill()


def tq(s: str) -> str:
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n") + '"'


def typedb_connect():
    last = None
    for _ in range(60):
        try:
            driver = TypeDB.driver(
                "127.0.0.1:1729",
                Credentials("admin", "password"),
                TYPEDB_OPTIONS,
            )
            list(driver.databases.all())
            return driver
        except Exception as exc:
            last = exc
            try:
                driver.close()
            except Exception:
                pass
            time.sleep(0.5)
    raise RuntimeError(f"TypeDB unavailable: {last}")


def atom_literal(value) -> str:
    return "literal:" + json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def event_occurrence_id(event_id: str) -> str:
    return "occ:ab:" + event_id.split(":", 1)[-1]


def event_bindings(stream: dict, event: dict) -> dict[str, str]:
    bindings = {
        "key:type": f"kind:{event['kind']}",
        "key:case": stream["case_id"],
        "key:source-event": event["event_id"],
    }
    kind = event["kind"]
    if kind == "observation":
        bindings["key:failure-code"] = "failure:" + event["failure_code"]
        for key, value in sorted(event["context"].items()):
            bindings[f"key:context/{key}"] = atom_literal(value)
    elif kind == "evidence":
        bindings["key:statement"] = atom_literal(event["statement"])
        bindings["key:about"] = event["about"]
    elif kind == "decision":
        bindings["key:decision-id"] = event["decision_id"]
        bindings["key:action"] = "action:" + event["action"]
        bindings["key:reason"] = atom_literal(event["reason"])
        bindings["key:based-on"] = event_occurrence_id(event["based_on"])
        if event.get("supersedes"):
            bindings["key:supersedes"] = event_occurrence_id(event["supersedes"])
        for key, value in sorted(event["result"].items()):
            bindings[f"key:result/{key}"] = atom_literal(value)
    return bindings


def attr_string(concept):
    return concept.as_attribute().get_string()


def rows(tx, query: str):
    return list(tx.query(query).resolve().as_concept_rows())


def read_bindings(tx, oid: str) -> dict[str, str]:
    query = f"""match
      $o isa occurrence, has atom-id {tq(oid)};
      $b isa binding, links (occurrence: $o, key: $k, value: $v);
      $k has atom-id $key;
      $v has atom-id $value;
    select $key, $value;"""
    return {
        attr_string(row.get("key")): attr_string(row.get("value"))
        for row in rows(tx, query)
    }


def run_typedb_line(stream: dict) -> dict:
    occurrence_payloads = []
    occurrence_ids = set()
    atom_ids = set()

    for event in stream["events"]:
        oid = event_occurrence_id(event["event_id"])
        occurrence_ids.add(oid)
        bindings = event_bindings(stream, event)
        occurrence_payloads.append((oid, bindings))
        atom_ids.add(oid)
        for key, value in bindings.items():
            atom_ids.add(key)
            atom_ids.add(value)

    driver = typedb_connect()
    try:
        if driver.databases.contains(TYPEDB_DB):
            driver.databases.get(TYPEDB_DB).delete()
        driver.databases.create(TYPEDB_DB)

        with driver.transaction(TYPEDB_DB, TransactionType.SCHEMA) as tx:
            tx.query(TYPEDB_SCHEMA.read_text()).resolve().as_ok()
            tx.commit()

        with driver.transaction(TYPEDB_DB, TransactionType.WRITE) as tx:
            for aid in sorted(atom_ids):
                typ = "occurrence" if aid in occurrence_ids else "atom"
                tx.query(
                    f"insert $a isa {typ}, has atom-id {tq(aid)}, has lexical {tq(aid)};"
                ).resolve()
            tx.commit()

        with driver.transaction(TYPEDB_DB, TransactionType.WRITE) as tx:
            for oid, bindings in occurrence_payloads:
                for key, value in bindings.items():
                    tx.query(
                        f"""match
                          $o isa occurrence, has atom-id {tq(oid)};
                          $k isa atom, has atom-id {tq(key)};
                          $v isa atom, has atom-id {tq(value)};
                        insert $b isa binding, links (occurrence: $o, key: $k, value: $v);"""
                    ).resolve()
            tx.commit()

        with driver.transaction(TYPEDB_DB, TransactionType.READ) as tx:
            decision_oids = []
            for oid in sorted(occurrence_ids):
                b = read_bindings(tx, oid)
                if b.get("key:type") == "kind:decision":
                    decision_oids.append(oid)

            decision_bindings = {oid: read_bindings(tx, oid) for oid in decision_oids}
            superseded = {
                b["key:supersedes"]
                for b in decision_bindings.values()
                if "key:supersedes" in b
            }
            current_oids = [oid for oid in decision_oids if oid not in superseded]
            assert len(current_oids) == 1, current_oids
            current_oid = current_oids[0]
            current_b = decision_bindings[current_oid]

            prior_oid = current_b.get("key:supersedes")
            prior_b = decision_bindings.get(prior_oid, {}) if prior_oid else {}

            obs_oid = event_occurrence_id("evt:observation-001")
            obs_b = read_bindings(tx, obs_oid)
            original_context = {}
            for key, value in obs_b.items():
                if key.startswith("key:context/"):
                    original_context[key.split("/", 1)[1]] = json.loads(value[len("literal:"):])

            occurrence_count = len(rows(tx, "match $o isa occurrence; select $o;"))
            binding_count = len(rows(tx, "match $b isa binding; select $b;"))

            return {
                "implementation": "Atom/Occurrence/Binding over TypeDB",
                "storage": f"TypeDB CE database {TYPEDB_DB}",
                "current_decision": current_b.get("key:decision-id"),
                "persisted_previous_decision": prior_b.get("key:decision-id"),
                "persisted_current_decision": current_b.get("key:decision-id"),
                "persisted_decision_ids": [
                    decision_bindings[oid].get("key:decision-id") for oid in decision_oids
                ],
                "persisted_decision_count": len(decision_oids),
                "original_context": original_context,
                "supersession_link": {
                    "from": current_b.get("key:decision-id"),
                    "to": prior_b.get("key:decision-id"),
                    "binding": "key:supersedes",
                }
                if prior_b
                else None,
                "counts": {
                    "occurrences": occurrence_count,
                    "bindings": binding_count,
                },
            }
    finally:
        driver.close()


def build_matrix(stream: dict, provider: dict, typedb: dict) -> list[dict]:
    obs = next(e for e in stream["events"] if e["kind"] == "observation")
    decisions = [e for e in stream["events"] if e["kind"] == "decision"]
    expected_current = decisions[1]["decision_id"]
    expected_prior = decisions[0]["decision_id"]

    return [
        {
            "question": "What is the current decision?",
            "expected": expected_current,
            "provider_reference": provider["current_decision"],
            "provider_pass": provider["current_decision"] == expected_current,
            "atom_occurrence_binding": typedb["current_decision"],
            "atom_occurrence_binding_pass": typedb["current_decision"] == expected_current,
        },
        {
            "question": "What decision existed immediately before the current one?",
            "expected": expected_prior,
            "provider_reference": provider["persisted_previous_decision"],
            "provider_pass": provider["persisted_previous_decision"] == expected_prior,
            "atom_occurrence_binding": typedb["persisted_previous_decision"],
            "atom_occurrence_binding_pass": typedb["persisted_previous_decision"] == expected_prior,
        },
        {
            "question": "Can the store recover the explicit supersession relation?",
            "expected": f"{expected_current} supersedes {expected_prior}",
            "provider_reference": provider["supersession_link"],
            "provider_pass": bool(provider["supersession_link"]),
            "atom_occurrence_binding": typedb["supersession_link"],
            "atom_occurrence_binding_pass": bool(typedb["supersession_link"]),
        },
        {
            "question": "Can the original observation context still be recovered?",
            "expected": obs["context"],
            "provider_reference": provider["original_context"],
            "provider_pass": provider["original_context"] == obs["context"],
            "atom_occurrence_binding": typedb["original_context"],
            "atom_occurrence_binding_pass": typedb["original_context"] == obs["context"],
        },
        {
            "question": "How many distinct decisions for this case remain recoverable?",
            "expected": 2,
            "provider_reference": provider["persisted_decision_count"],
            "provider_pass": provider["persisted_decision_count"] == 2,
            "atom_occurrence_binding": typedb["persisted_decision_count"],
            "atom_occurrence_binding_pass": typedb["persisted_decision_count"] == 2,
        },
    ]


def main() -> None:
    stream = json.loads(STREAM_PATH.read_text())
    provider = run_provider_line(stream)
    typedb = run_typedb_line(stream)
    matrix = build_matrix(stream, provider, typedb)

    report = {
        "experiment": stream["experiment"],
        "scope": {
            "provider_reference": "Existing open v0.2 provider/reference behavior, reused unchanged.",
            "atom_occurrence_binding": "Existing TypeDB primitive/schema, reused unchanged.",
            "claim_boundary": (
                "This tests historical cognition retrieval after re-resolution. "
                "It is not an overall product benchmark and does not characterize "
                "the private production MCP/PostgreSQL implementation beyond the open reference behavior exercised here."
            ),
        },
        "source_stream": stream,
        "provider_reference": provider,
        "atom_occurrence_binding": typedb,
        "retrieval_matrix": matrix,
        "scores": {
            "provider_reference": sum(1 for row in matrix if row["provider_pass"]),
            "atom_occurrence_binding": sum(1 for row in matrix if row["atom_occurrence_binding_pass"]),
            "questions": len(matrix),
        },
    }
    print(json.dumps(report, indent=2, ensure_ascii=False))

    # The experiment succeeds when both implementations behave consistently
    # with their existing models. We do not rewrite either side to force parity.
    assert provider["first_resolution_observed"] == "decision.ab.v1"
    assert provider["second_resolution_observed"] == "decision.ab.v2"
    assert provider["current_decision"] == "decision.ab.v2"
    assert typedb["current_decision"] == "decision.ab.v2"
    assert typedb["persisted_previous_decision"] == "decision.ab.v1"
    assert typedb["persisted_decision_count"] == 2
    print(
        "DUAL_MEMORY_AB_PASS "
        f"provider={report['scores']['provider_reference']}/{len(matrix)} "
        f"typedb={report['scores']['atom_occurrence_binding']}/{len(matrix)}"
    )


if __name__ == "__main__":
    main()
