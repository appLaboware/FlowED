#!/usr/bin/env python3
"""
DecisionPort POC.

Contract:
  resolve(failure_code, context) -> approved deterministic decision or no-match
  retain(decision_id, execution_id, outcome) -> records observed result

Exact approved cases are authoritative.
Vector retrieval is deliberately candidate-only and never auto-executes.
"""

import argparse
import base64
import json
import re
import sys
import urllib.error
import urllib.request

URL = "http://127.0.0.1:7474/db/neo4j/query/v2"
AUTH = "Basic " + base64.b64encode(b"neo4j:ideos-decision-lab").decode()

def query(statement, parameters=None):
    payload = json.dumps({
        "statement": statement,
        "parameters": parameters or {}
    }).encode()
    req = urllib.request.Request(
        URL,
        data=payload,
        headers={
            "Authorization": AUTH,
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            body = json.load(r)
    except urllib.error.HTTPError as e:
        detail = e.read().decode(errors="replace")
        raise RuntimeError(f"Neo4j HTTP {e.code}: {detail}") from e

    if body.get("errors"):
        raise RuntimeError(json.dumps(body["errors"]))

    return body.get("data", {})

def split_cypher_statements(text):
    """Split on semicolons only when they are outside quoted string literals."""
    statements = []
    current = []
    quote = None
    escaped = False

    for ch in text:
        if escaped:
            current.append(ch)
            escaped = False
            continue

        if ch == "\\":
            current.append(ch)
            escaped = True
            continue

        if quote:
            current.append(ch)
            if ch == quote:
                quote = None
            continue

        if ch in {"'", '"'}:
            current.append(ch)
            quote = ch
            continue

        if ch == ";":
            statement = "".join(current).strip()
            if statement:
                statements.append(statement)
            current = []
            continue

        current.append(ch)

    tail = "".join(current).strip()
    if tail:
        statements.append(tail)

    if quote:
        raise ValueError("Unterminated quoted string in Cypher seed")

    return statements


def seed(path):
    text = open(path, "r", encoding="utf-8").read()
    statements = split_cypher_statements(text)
    for statement in statements:
        query(statement)
    print(json.dumps({"seeded": len(statements), "status": "ok"}))

def resolve(code, context):
    q = """
    MATCH (f:Failure {code:$code})-[:RESOLVED_BY]->(d:Decision {status:'approved'})
          -[:EXECUTES]->(a:Action)
    OPTIONAL MATCH (d)-[:REQUIRES]->(g:Guard)
    RETURN d.id AS decision_id,
           d.automation AS automation,
           d.risk AS risk,
           d.priority AS priority,
           d.userNotice AS user_notice,
           a.id AS action_id,
           collect({key:g.key,value:g.value}) AS guards
    ORDER BY d.priority DESC
    """
    data = query(q, {"code": code})
    rows = data.get("values", [])
    fields = data.get("fields", [])
    if not rows:
        print(json.dumps({
            "matched": False,
            "failure_code": code,
            "execution_allowed": False
        }))
        return 2

    for row in rows:
        item = dict(zip(fields, row))
        guards = [g for g in item.get("guards", []) if g.get("key")]
        guards_ok = all(str(context.get(g["key"], "")).lower() == str(g["value"]).lower()
                        for g in guards)
        execution_allowed = (
            item.get("automation") == "automatic"
            and item.get("risk") == "low"
            and guards_ok
        )
        item.update({
            "matched": True,
            "failure_code": code,
            "guards_ok": guards_ok,
            "execution_allowed": execution_allowed,
        })
        print(json.dumps(item, ensure_ascii=False))
        return 0 if execution_allowed else 3

    return 2

def retain(decision_id, execution_id, outcome):
    if outcome not in {"success", "failure"}:
        raise ValueError("outcome must be success or failure")
    counter = "successCount" if outcome == "success" else "failureCount"
    q = f"""
    MATCH (d:Decision {{id:$decision_id}})
    SET d.{counter}=coalesce(d.{counter},0)+1,
        d.lastOutcome=$outcome,
        d.lastExecution=$execution_id,
        d.lastObservedAt=datetime()
    CREATE (e:Execution {{
      id:$execution_id,
      outcome:$outcome,
      observedAt:datetime()
    }})
    MERGE (d)-[:OBSERVED_IN]->(e)
    RETURN d.id AS decision_id,
           d.successCount AS success_count,
           d.failureCount AS failure_count,
           d.lastOutcome AS last_outcome
    """
    data = query(q, {
        "decision_id": decision_id,
        "execution_id": execution_id,
        "outcome": outcome,
    })
    print(json.dumps({
        "fields": data.get("fields", []),
        "values": data.get("values", [])
    }, ensure_ascii=False))

def graph_summary():
    q = """
    MATCH (f:Failure)-[:RESOLVED_BY]->(d:Decision)-[:EXECUTES]->(a:Action)
    OPTIONAL MATCH (d)-[:REQUIRES]->(g:Guard)
    RETURN f.code AS failure,
           d.id AS decision,
           a.id AS action,
           d.status AS status,
           d.successCount AS successes,
           d.failureCount AS failures,
           collect(g.id) AS guards
    ORDER BY failure
    """
    data = query(q)
    print(json.dumps({
        "fields": data.get("fields", []),
        "values": data.get("values", [])
    }, ensure_ascii=False))

def main():
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="cmd", required=True)

    ps = sub.add_parser("seed")
    ps.add_argument("path")

    pr = sub.add_parser("resolve")
    pr.add_argument("--failure-code", required=True)
    pr.add_argument("--context", default="{}")

    pt = sub.add_parser("retain")
    pt.add_argument("--decision-id", required=True)
    pt.add_argument("--execution-id", required=True)
    pt.add_argument("--outcome", required=True)

    sub.add_parser("summary")

    args = p.parse_args()

    if args.cmd == "seed":
        seed(args.path)
    elif args.cmd == "resolve":
        context = json.loads(args.context)
        raise SystemExit(resolve(args.failure_code, context))
    elif args.cmd == "retain":
        retain(args.decision_id, args.execution_id, args.outcome)
    elif args.cmd == "summary":
        graph_summary()

if __name__ == "__main__":
    main()
