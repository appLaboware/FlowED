#!/usr/bin/env python3
"""
Reference Neo4j decision-memory adapter promoted from IDEOS EXP-007.

This is storage/retrieval infrastructure, not the proprietary MyTrues ranking engine.
"""

import argparse
import base64
import json
import os
import urllib.error
import urllib.request

URL = os.environ.get("MYTRUES_NEO4J_HTTP", "http://127.0.0.1:7474/db/neo4j/query/v2")
USER = os.environ.get("MYTRUES_NEO4J_USER", "neo4j")
PASSWORD = os.environ.get("MYTRUES_NEO4J_PASSWORD", "mytrues-lab")
AUTH = "Basic " + base64.b64encode(f"{USER}:{PASSWORD}".encode()).decode()


def query(statement, parameters=None):
    payload = json.dumps({"statement": statement, "parameters": parameters or {}}).encode()
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
        with urllib.request.urlopen(req, timeout=15) as response:
            body = json.load(response)
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode(errors="replace")
        raise RuntimeError(f"Neo4j HTTP {exc.code}: {detail}") from exc

    if body.get("errors"):
        raise RuntimeError(json.dumps(body["errors"]))
    return body.get("data", {})


def split_cypher_statements(text):
    statements, current = [], []
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
    statements = split_cypher_statements(open(path, encoding="utf-8").read())
    for statement in statements:
        query(statement)
    print(json.dumps({"seeded": len(statements), "status": "ok"}))


def candidates(failure_code):
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
    """
    print(json.dumps(query(q, {"code": failure_code}), ensure_ascii=False))


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
    print(json.dumps(query(q, {
        "decision_id": decision_id,
        "execution_id": execution_id,
        "outcome": outcome,
    }), ensure_ascii=False))


def main():
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)

    p_seed = sub.add_parser("seed")
    p_seed.add_argument("path")

    p_candidates = sub.add_parser("candidates")
    p_candidates.add_argument("--failure-code", required=True)

    p_retain = sub.add_parser("retain")
    p_retain.add_argument("--decision-id", required=True)
    p_retain.add_argument("--execution-id", required=True)
    p_retain.add_argument("--outcome", required=True)

    args = parser.parse_args()
    if args.command == "seed":
        seed(args.path)
    elif args.command == "candidates":
        candidates(args.failure_code)
    elif args.command == "retain":
        retain(args.decision_id, args.execution_id, args.outcome)


if __name__ == "__main__":
    main()
