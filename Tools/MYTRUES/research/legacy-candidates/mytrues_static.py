# ARCHAEOLOGY COPY — NOT NORMATIVE OR RUNTIME-APPROVED
# Source repository: MultiUni/MultiUniOS_p
# Source path: .initproj/tools/MyTrues/tools/mytrues_static.py
# Source blob SHA: abc0a6b6f447229c774f61ff441abe9972c2b0be

#!/usr/bin/env python3
"""
@ai-context
Purpose: Generate static docs from MyTrues truths.
Domain: mytrues/static-docs
Dependencies: argparse, os
Rules:
    - Render from source of truth only
    - Avoid side effects outside output dir
"""
import argparse
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
    exclude = {"docs", "tools", "logo", "_DEV", "_LEGACY", ".git", ".mytrues-data", ".consolidated"}
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in exclude and not d.startswith(".")]
        if dirpath == root:
            continue
        if "truth.yaml" in filenames and "README.md" in filenames:
            yield dirpath


def generate_static(root, out_path):
    truths = sorted(iter_truths(root))
    with open(out_path, "w", encoding="utf-8") as out:
        out.write("# MyTrues — Documentação Estática\n\n")
        out.write(f"Total de verdades: {len(truths)}\n\n")
        out.write("## Índice\n\n")
        for truth_dir in truths:
            meta = read_yaml_simple(os.path.join(truth_dir, "truth.yaml"))
            title = meta.get("title") or os.path.basename(truth_dir)
            anchor = title.lower().replace(" ", "-")
            out.write(f"- [{title}](#{anchor})\n")
        out.write("\n---\n\n")

        for truth_dir in truths:
            meta = read_yaml_simple(os.path.join(truth_dir, "truth.yaml"))
            title = meta.get("title") or os.path.basename(truth_dir)
            out.write(f"## {title}\n\n")
            out.write(f"- truth_id: {meta.get('truth_id','N/A')}\n")
            out.write(f"- status: {meta.get('status','N/A')}\n")
            out.write(f"- created_at: {meta.get('created_at','N/A')}\n")
            out.write(f"- updated_at: {meta.get('updated_at','N/A')}\n\n")
            try:
                with open(os.path.join(truth_dir, "README.md"), "r", encoding="utf-8") as handle:
                    out.write(handle.read())
                    out.write("\n\n---\n\n")
            except OSError:
                out.write("(README.md não encontrado)\n\n---\n\n")


def main():
    parser = argparse.ArgumentParser(description="MyTrues static docs generator")
    parser.add_argument("--root", required=True, help="MyTrues root directory")
    parser.add_argument("--out", required=True, help="Output markdown path")
    args = parser.parse_args()

    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    generate_static(args.root, args.out)
    print(f"Static docs written to {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
