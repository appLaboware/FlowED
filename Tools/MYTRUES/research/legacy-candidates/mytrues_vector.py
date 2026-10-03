# ARCHAEOLOGY COPY — NOT NORMATIVE OR RUNTIME-APPROVED
# Source repository: MultiUni/MultiUniOS_p
# Source path: .initproj/tools/MyTrues/tools/mytrues_vector.py
# Source blob SHA: ccd5905ae2c98b3ce273095fa31e3f9150bd8617

#!/usr/bin/env python3
"""
@ai-context
Purpose: Lightweight vector store and query for MyTrues.
Domain: mytrues/vector
Dependencies: argparse, json, sqlite3
Rules:
    - Keep schema stable
    - Avoid external service dependencies
"""
import argparse
import json
import os
import re
import sqlite3
import sys
from datetime import datetime, timezone

DEFAULT_DIM = 256


def tokenize(text):
    return re.findall(r"[a-zA-Z0-9_]+", text.lower())


def embed(text, dim=DEFAULT_DIM):
    vec = [0.0] * dim
    for token in tokenize(text):
        idx = hash(token) % dim
        vec[idx] += 1.0
    norm = sum(v * v for v in vec) ** 0.5
    if norm > 0:
        vec = [v / norm for v in vec]
    return vec


def ensure_db(db_path):
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    conn = sqlite3.connect(db_path)
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS truths (
            id TEXT PRIMARY KEY,
            truth_id TEXT,
            path TEXT,
            title TEXT,
            content TEXT,
            vector TEXT,
            created_at TEXT
        )
        """
    )
    try:
        conn.execute("ALTER TABLE truths ADD COLUMN truth_id TEXT")
    except sqlite3.OperationalError:
        pass
    conn.commit()
    return conn


def read_title(text, fallback):
    for line in text.splitlines():
        if line.strip().startswith("# "):
            return line.strip()[2:]
    return fallback


def read_truth_id(meta_path):
    try:
        with open(meta_path, "r", encoding="utf-8") as handle:
            for line in handle:
                if line.strip().startswith("truth_id:"):
                    return line.split(":", 1)[1].strip()
    except OSError:
        return None
    return None


def iter_truth_dirs(root):
    exclude = {"docs", "tools", "logo", "_DEV", "_LEGACY", ".git", ".mytrues-data", ".consolidated"}
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in exclude and not d.startswith(".")]
        if dirpath == root:
            continue
        rel = os.path.relpath(dirpath, root)
        top = rel.split(os.sep)[0]
        if top in {"docs", "tools", "logo"}:
            continue
        if "truth.yaml" in filenames and "README.md" in filenames:
            yield dirpath


def index_dir(root, db_path, dim=DEFAULT_DIM):
    conn = ensure_db(db_path)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM truths")
    conn.commit()

    count = 0
    for truth_dir in iter_truth_dirs(root):
        truth_id = read_truth_id(os.path.join(truth_dir, "truth.yaml"))
        for filename in os.listdir(truth_dir):
            if filename.startswith(".") or not filename.lower().endswith(".md"):
                continue
            path = os.path.join(truth_dir, filename)
            try:
                with open(path, "r", encoding="utf-8") as handle:
                    content = handle.read()
            except OSError:
                continue

            rel = os.path.relpath(path, root)
            title = read_title(content, os.path.splitext(os.path.basename(path))[0])
            vector = embed(content, dim=dim)

            cursor.execute(
                """
                INSERT OR REPLACE INTO truths (id, truth_id, path, title, content, vector, created_at)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    rel,
                    truth_id,
                    rel,
                    title,
                    content,
                    json.dumps(vector),
                    datetime.now(timezone.utc).isoformat(),
                ),
            )
            count += 1

    conn.commit()
    conn.close()
    return count


def cosine(a, b):
    return sum(x * y for x, y in zip(a, b))


def query(db_path, text, topk=3, dim=DEFAULT_DIM):
    conn = ensure_db(db_path)
    cursor = conn.cursor()
    vector = embed(text, dim=dim)

    rows = cursor.execute("SELECT id, truth_id, path, title, content, vector FROM truths").fetchall()
    scored = []
    for row_id, truth_id, path, title, content, vec_json in rows:
        try:
            vec = json.loads(vec_json)
        except json.JSONDecodeError:
            continue
        score = cosine(vector, vec)
        if score <= 0:
            continue
        snippet = " ".join(content.split())[:240]
        scored.append({
            "id": row_id,
            "truth_id": truth_id,
            "path": path,
            "title": title,
            "score": round(score, 4),
            "snippet": snippet,
        })

    scored.sort(key=lambda x: x["score"], reverse=True)
    return scored[:topk]


def main():
    parser = argparse.ArgumentParser(description="MyTrues Vector Store (POC)")
    subparsers = parser.add_subparsers(dest="command", required=True)

    parser_index = subparsers.add_parser("index", help="Index markdown files")
    parser_index.add_argument("--root", required=True, help="Root directory to scan")
    parser_index.add_argument("--db", required=True, help="SQLite DB path")
    parser_index.add_argument("--dim", type=int, default=DEFAULT_DIM, help="Vector dimension")

    parser_query = subparsers.add_parser("query", help="Query indexed truths")
    parser_query.add_argument("--db", required=True, help="SQLite DB path")
    parser_query.add_argument("--text", required=True, help="Query text")
    parser_query.add_argument("--topk", type=int, default=3, help="Top K results")
    parser_query.add_argument("--dim", type=int, default=DEFAULT_DIM, help="Vector dimension")

    args = parser.parse_args()

    if args.command == "index":
        count = index_dir(args.root, args.db, dim=args.dim)
        print(f"Indexed {count} markdown files")
        return 0

    if args.command == "query":
        results = query(args.db, args.text, topk=args.topk, dim=args.dim)
        for item in results:
            print(json.dumps(item, ensure_ascii=False))
        return 0

    return 1


if __name__ == "__main__":
    sys.exit(main())
