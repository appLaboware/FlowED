# ARCHAEOLOGY COPY — NOT NORMATIVE OR RUNTIME-APPROVED
# Source repository: MultiUni/MultiUniOS_p
# Source path: .initproj/tools/MyTrues/tools/mytrues_merge.py
# Source blob SHA: 2ad72acc97d65bbb93f5d91f5bc656cd236aef81

#!/usr/bin/env python3
"""
@ai-context
Purpose: Merge MyTrues exports and report conflicts.
Domain: mytrues/merge
Dependencies: argparse, json
Rules:
    - Keep conflict reporting deterministic
    - Never drop records silently
"""
import argparse
import json
import sys
from datetime import datetime, timezone


def load_jsonl(path):
    items = []
    with open(path, "r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            items.append(json.loads(line))
    return items


def index_by_id(items):
    return {item.get("truth_id"): item for item in items if item.get("truth_id")}


def diff(a, b):
    changes = {}
    keys = set(a.keys()) | set(b.keys())
    for key in keys:
        if a.get(key) != b.get(key):
            changes[key] = {"local": a.get(key), "remote": b.get(key)}
    return changes


def merge_report(local_items, remote_items):
    local_map = index_by_id(local_items)
    remote_map = index_by_id(remote_items)

    report = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "conflicts": [],
        "only_local": [],
        "only_remote": [],
    }

    for truth_id, item in local_map.items():
        if truth_id not in remote_map:
            report["only_local"].append(truth_id)
            continue
        changes = diff(item, remote_map[truth_id])
        if changes:
            report["conflicts"].append({
                "truth_id": truth_id,
                "changes": changes,
            })

    for truth_id in remote_map:
        if truth_id not in local_map:
            report["only_remote"].append(truth_id)

    return report


def main():
    parser = argparse.ArgumentParser(description="MyTrues merge (POC)")
    parser.add_argument("--local", required=True, help="Local JSONL export")
    parser.add_argument("--remote", required=True, help="Remote JSONL export")
    parser.add_argument("--out", required=True, help="Output report JSON")
    args = parser.parse_args()

    local_items = load_jsonl(args.local)
    remote_items = load_jsonl(args.remote)
    report = merge_report(local_items, remote_items)

    with open(args.out, "w", encoding="utf-8") as handle:
        json.dump(report, handle, ensure_ascii=False, indent=2)

    print(f"Conflicts: {len(report['conflicts'])}")
    print(f"Only local: {len(report['only_local'])}")
    print(f"Only remote: {len(report['only_remote'])}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
