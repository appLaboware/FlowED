# ARCHAEOLOGY COPY — NOT NORMATIVE OR RUNTIME-APPROVED
# Source repository: MultiUni/MultiUniOS_p
# Source path: .initproj/tools/MyTrues/tools/mytrues_export.py
# Source blob SHA: 78c24e5258ea34add46bc0d5a01ceaa50a8839b6

#!/usr/bin/env python3
"""
@ai-context
Purpose: Export MyTrues truths to JSONL/CSV.
Domain: mytrues/export
Dependencies: argparse, json
Rules:
    - Preserve IDs and metadata
    - Do not mutate source files
"""
import argparse
import json
import os
import sys


def read_yaml_simple(path):
    data = {}
    try:
        with open(path, "r", encoding="utf-8") as handle:
            for line in handle:
                if not line.strip() or line.lstrip().startswith("#"):
                    continue
                if ":" not in line:
                    continue
                key, value = line.split(":", 1)
                data[key.strip()] = value.strip().strip('"').strip("'")
    except OSError:
        return data
    return data


def iter_truths(root):
    exclude = {"docs", "tools", "logo", "_DEV", "_LEGACY", ".git", ".mytrues-data"}
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in exclude and not d.startswith(".")]
        if dirpath == root:
            continue
        if "truth.yaml" in filenames and "README.md" in filenames:
            yield dirpath


def export_jsonl(root, out_path):
    items = 0
    with open(out_path, "w", encoding="utf-8") as out:
        for truth_dir in iter_truths(root):
            meta = read_yaml_simple(os.path.join(truth_dir, "truth.yaml"))
            try:
                with open(os.path.join(truth_dir, "README.md"), "r", encoding="utf-8") as handle:
                    content = handle.read()
            except OSError:
                content = ""
            item = {
                "truth_id": meta.get("truth_id"),
                "title": meta.get("title"),
                "status": meta.get("status"),
                "created_at": meta.get("created_at"),
                "updated_at": meta.get("updated_at"),
                "owner": meta.get("owner"),
                "path": os.path.relpath(truth_dir, root),
                "content": content,
            }
            out.write(json.dumps(item, ensure_ascii=False) + "\n")
            items += 1
    return items


def main():
    parser = argparse.ArgumentParser(description="MyTrues export (POC)")
    parser.add_argument("--root", required=True, help="MyTrues root directory")
    parser.add_argument("--out", required=True, help="Output JSONL path")
    args = parser.parse_args()

    count = export_jsonl(args.root, args.out)
    print(f"Exported {count} truths")
    return 0


if __name__ == "__main__":
    sys.exit(main())
