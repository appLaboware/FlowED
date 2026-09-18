#!/usr/bin/env python3
"""Experimental CCP slice: preserved document -> annotations -> CCP -> projections."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import sys


class ValidationError(ValueError):
    pass


def require(condition, message):
    if not condition:
        raise ValidationError(message)


def encoded(data):
    return json.dumps(data, ensure_ascii=False, indent=2) + "\n"


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def unique_ids(values, label):
    require(isinstance(values, list) and all(isinstance(v, str) for v in values),
            label + ": expected list of IDs")
    require(len(values) == len(set(values)), label + ": duplicate IDs")
    return set(values)


def structure(inputs):
    index = read_json(inputs / "markings.json")
    require(index["schema_version"] == 1, "unsupported markings version")
    source = index["source"]
    require(source["file"] == "source.md", "unsupported source path")
    raw = (inputs / source["file"]).read_bytes()
    require(hashlib.sha256(raw).hexdigest() == source["sha256"], "source SHA-256 mismatch")
    git_blob = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
    require(git_blob == source["git_blob_sha"], "source Git blob mismatch")
    origin = read_json(inputs / "source-origin.json")
    require(all(source.get(k) == v for k, v in origin.items()), "origin metadata mismatch")
    require(re.fullmatch(r"[0-9a-f]{40}", source["commit"]), "invalid source commit")
    lines = raw.decode("utf-8").splitlines()
    nodes = {}
    for mark in index["marks"]:
        key, start, end = mark["id"], mark["start_line"], mark["end_line"]
        require(re.fullmatch(r"[a-z0-9-]+", key) and key not in nodes, "invalid/duplicate node ID")
        require(type(start) is int and type(end) is int and 1 <= start <= end <= len(lines),
                "invalid source span: " + key)
        quote = "\n".join(lines[start - 1:end])
        require(quote == mark["quote"], "source quote mismatch: " + key)
        url = (f'https://github.com/{source["repository"]}/blob/{source["commit"]}/'
               f'{source["path"]}#L{start}-L{end}')
        nodes[key] = {"id": key, "kind": mark["kind"], "text": quote,
                      "provenance": {"source_sha256": source["sha256"],
                                     "start_line": start, "end_line": end, "url": url}}
    invariants = unique_ids(index["invariants"], "unit invariants")
    require(invariants <= nodes.keys(), "unknown unit invariant")
    require(index["canonical"] in invariants, "canonical rendering must be invariant")
    for kind in ("epistemic-status", "causality", "limits"):
        require(any(nodes[k]["kind"] == kind for k in invariants), "missing invariant kind: " + kind)
    return {"schema_version": 1, "unit_id": index["unit_id"], "title": index["title"],
            "source": source, "annotation": index["annotation"],
            "canonical": index["canonical"], "invariants": index["invariants"], "nodes": nodes}


def validate_contract(ccp, contract):
    require(contract["schema_version"] == 1, "unsupported contract version")
    require(contract["adapter"] == "markdown-json-v1", "unsupported adapter")
    require(contract["unit_id"] == ccp["unit_id"], "contract unit mismatch")
    required = unique_ids(contract["required_invariants"], "contract invariants")
    require(set(ccp["invariants"]) <= required <= ccp["nodes"].keys(), "contract loses invariants")
    require(set(contract["projections"]) == {"REDUCT-MAX", "BASE", "DEFESA"},
            "first slice requires REDUCT-MAX, BASE and DEFESA")
    for name, spec in contract["projections"].items():
        render = unique_ids(spec["render"], name + " render")
        retain = unique_ids(spec["retain"], name + " retain")
        omitted = unique_ids(spec["allowed_omissions"], name + " omissions")
        require(bool(render) and render <= retain, name + ": rendered node not retained")
        require(required <= retain, name + ": required invariant omitted")
        require(not retain & omitted and retain | omitted == ccp["nodes"].keys(),
                name + ": coverage/omission partition invalid")
        expected_axis = "argumentation" if name == "DEFESA" else "editorial-density"
        require(spec["axis"] == expected_axis, name + ": invalid projection axis")


def project(ccp, contract, name):
    spec = contract["projections"][name]
    return {"schema_version": 1, "unit_id": ccp["unit_id"], "projection": name,
            "axis": spec["axis"], "consumer": spec["consumer"],
            "source": ccp["source"], "annotation": ccp["annotation"],
            "canonical": ccp["canonical"], "required_invariants": contract["required_invariants"],
            "render_order": spec["render"], "allowed_omissions": spec["allowed_omissions"],
            "nodes": {key: ccp["nodes"][key] for key in spec["retain"]}}


def markdown(bundle):
    nodes = bundle["nodes"]
    status = next(n["text"] for n in nodes.values() if n["kind"] == "epistemic-status")
    parts = [f'# {bundle["unit_id"]} — {bundle["projection"]}', status,
             "Fonte: documento editorial preservado; não é transcrição integral do chat.",
             "Autoridade registrada: " + bundle["source"]["authority"],
             "Compilação experimental de trechos existentes. Equivalência semântica não verificada automaticamente."]
    for key in bundle["render_order"]:
        node = nodes[key]
        parts += [node["text"], f'[Fonte de {key}]({node["provenance"]["url"]})']
    parts += ["## Núcleo preservado e proveniência",
              "O JSON desta projeção contém integralmente os elementos abaixo, inclusive os que não estão na superfície de leitura."]
    for key in bundle["required_invariants"]:
        parts.append(f'- [{key}]({nodes[key]["provenance"]["url"]})')
    parts += [f'[Projeção estruturada]({bundle["projection"]}.json)',
              "Omissões autorizadas neste contrato: " + ", ".join(bundle["allowed_omissions"])]
    return "\n\n".join(parts) + "\n"


def compile_poc(inputs, output, projection=None, unit=None):
    inputs, output = Path(inputs).resolve(), Path(output).resolve()
    require(output != inputs and inputs not in output.parents and output not in inputs.parents,
            "output must be separate from preserved inputs")
    ccp = structure(inputs)
    require(unit is None or unit == ccp["unit_id"], "unknown unit")
    contract = read_json(inputs / "projection-contract.json")
    validate_contract(ccp, contract)
    require(projection is None or projection in contract["projections"], "unknown projection")
    names = [projection] if projection else list(contract["projections"])
    artifacts = {"ccp.json": encoded(ccp), "contract.json": encoded(contract),
                 "source.md": (inputs / "source.md").read_text(encoding="utf-8")}
    for name in names:
        bundle = project(ccp, contract, name)
        artifacts[name + ".json"] = encoded(bundle)
        artifacts[name + ".md"] = markdown(bundle)
    report = {"unit_id": ccp["unit_id"], "projections": names,
              "checks": ["source SHA-256", "Git blob", "exact spans", "contract coverage", "required invariants"],
              "semantic_equivalence": "not automatically verified",
              "artifacts": {name: hashlib.sha256(content.encode()).hexdigest()
                            for name, content in artifacts.items()}}
    artifacts["build-report.json"] = encoded(report)
    # Validate the complete build before writing any artifact. Reject symlinks.
    for name in artifacts:
        require(not (output / name).is_symlink(), "output artifact is a symlink")
    output.mkdir(parents=True, exist_ok=True)
    for name, content in artifacts.items():
        (output / name).write_text(content, encoding="utf-8", newline="\n")
    return report


def main():
    root = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--inputs", type=Path, default=root / "inputs")
    parser.add_argument("--output", type=Path, default=root / "output")
    parser.add_argument("--unit", default="P2.3")
    parser.add_argument("--projection", choices=["REDUCT-MAX", "BASE", "DEFESA"])
    args = parser.parse_args()
    try:
        result = compile_poc(args.inputs, args.output, args.projection, args.unit)
    except (ValidationError, KeyError, TypeError, OSError, ValueError) as exc:
        print("BUILD FAILED: " + str(exc), file=sys.stderr)
        return 1
    print("Built " + result["unit_id"] + ": " + ", ".join(result["projections"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
