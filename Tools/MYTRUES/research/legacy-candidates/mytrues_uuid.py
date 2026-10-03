# ARCHAEOLOGY COPY — NOT NORMATIVE OR RUNTIME-APPROVED
# Source repository: MultiUni/MultiUniOS_p
# Source path: .initproj/tools/MyTrues/tools/mytrues_uuid.py
# Source blob SHA: 66674b938865bdc78b47d1a8ee140791d313a1d0

#!/usr/bin/env python3
"""
@ai-context
Purpose: Ensure truth UUIDs and metadata.
Domain: mytrues/uuid
Dependencies: argparse, uuid
Rules:
    - Keep IDs stable once assigned
    - Avoid rewriting unchanged files
"""
import argparse
import os
import sys
import uuid
from datetime import datetime, timezone


def iter_truth_dirs(root):
    exclude = {"docs", "tools", "logo", "_DEV", "_LEGACY", ".git", ".mytrues-data"}
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in exclude and not d.startswith(".")]
        if dirpath == root:
            continue
        if "README.md" in filenames:
            yield dirpath


def ensure_truth_yaml(truth_dir):
    meta_path = os.path.join(truth_dir, "truth.yaml")
    if os.path.exists(meta_path):
        return False

    title = os.path.basename(truth_dir)
    readme_path = os.path.join(truth_dir, "README.md")
    try:
        with open(readme_path, "r", encoding="utf-8") as handle:
            for line in handle:
                if line.strip().startswith("# "):
                    title = line.strip()[2:]
                    break
    except OSError:
        pass

    now = datetime.now(timezone.utc).isoformat()
    truth_id = str(uuid.uuid4())
    with open(meta_path, "w", encoding="utf-8") as handle:
        handle.write(f"truth_id: {truth_id}\n")
        handle.write(f"created_at: {now}\n")
        handle.write(f"updated_at: {now}\n")
        handle.write("status: active\n")
        handle.write(f"title: \"{title}\"\n")
    return True


def main():
    parser = argparse.ArgumentParser(description="MyTrues UUID backfill")
    parser.add_argument("--root", required=True, help="MyTrues root directory")
    args = parser.parse_args()

    created = 0
    for truth_dir in iter_truth_dirs(args.root):
        if ensure_truth_yaml(truth_dir):
            created += 1

    print(f"Created truth.yaml for {created} entries")
    return 0


if __name__ == "__main__":
    sys.exit(main())
