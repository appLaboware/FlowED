#!/usr/bin/env python3
"""FLDP — minimal portable CLI for the FlowDisP POC."""

from __future__ import annotations
import argparse, hashlib, json, shutil, zipfile
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TEMPLATES = ROOT / "templates"
MODES = {"product", "academic", "method", "architecture"}
KINDS = {"input", "chat", "evidence"}

class VisibleTextParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []
        self._skip = 0
    def handle_starttag(self, tag, attrs):
        t = tag.lower()
        if t in {"script", "style", "noscript"}:
            self._skip += 1
        elif not self._skip and t in {"p","div","br","li","tr","h1","h2","h3","h4"}:
            self.parts.append("\n")
    def handle_endtag(self, tag):
        t = tag.lower()
        if t in {"script", "style", "noscript"} and self._skip:
            self._skip -= 1
        elif not self._skip and t in {"p","div","li","tr","h1","h2","h3","h4"}:
            self.parts.append("\n")
    def handle_data(self, data):
        if not self._skip:
            self.parts.append(data)
    def text(self):
        lines = []
        for line in "".join(self.parts).splitlines():
            clean = " ".join(line.split())
            if clean:
                lines.append(clean)
        return "\n".join(lines) + ("\n" if lines else "")

def now_iso():
    return datetime.now(timezone.utc).isoformat()

def sha256(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as f:
        for chunk in iter(lambda: f.read(1024*1024), b""):
            h.update(chunk)
    return h.hexdigest()

def render(name, values):
    text = (TEMPLATES/name).read_text(encoding="utf-8")
    for k, v in values.items():
        text = text.replace("{{"+k+"}}", v)
    return text

def ensure_case(case):
    case = Path(case)
    state = case/"STATE.json"
    if not state.exists():
        raise SystemExit(f"Not a FlowDisP case: {case}")
    return json.loads(state.read_text(encoding="utf-8"))

def write_state(case, state):
    state["updated_at"] = now_iso()
    (case/"STATE.json").write_text(json.dumps(state, indent=2, ensure_ascii=False)+"\n", encoding="utf-8")

def scaffold_round(case, number, actor):
    rdir = case/"rounds"/f"{number:03d}"
    rdir.mkdir(parents=True, exist_ok=False)
    vals = {"ROUND": f"{number:03d}", "ACTOR": actor}
    for src in ["ROUND-BRIEF.md","RESEARCHER-PROMPT.md","SEARCH-TRACE.md","EVIDENCE-LEDGER.md","ROUND-REPORT.md","OWNER-REVIEW.md"]:
        (rdir/src).write_text(render(src, vals), encoding="utf-8")

def cmd_init(args):
    case = Path(args.case_dir).resolve()
    if case.exists() and any(case.iterdir()):
        raise SystemExit(f"Directory is not empty: {case}")
    case.mkdir(parents=True, exist_ok=True)
    for p in ["raw/input","raw/chat","raw/evidence","normalized","rounds","owner"]:
        (case/p).mkdir(parents=True, exist_ok=True)
    vals = {"CASE_ID": args.case_id, "MODE": args.mode.upper()}
    (case/"CASE.md").write_text(render("CASE.md", vals), encoding="utf-8")
    (case/"owner"/"CONVERGENCE-REVIEW.md").write_text(render("CONVERGENCE-REVIEW.md", vals), encoding="utf-8")
    (case/"owner"/"APPROVED-EVIDENCE-PACK.md").write_text(render("APPROVED-EVIDENCE-PACK.md", vals), encoding="utf-8")
    (case/"SOURCE-MAP.json").write_text("[]\n", encoding="utf-8")
    state = {"case_id":args.case_id,"mode":args.mode,"status":"OPEN","created_at":now_iso(),"updated_at":now_iso(),"rounds":[{"number":1,"actor":args.actor}]}
    write_state(case, state)
    scaffold_round(case, 1, args.actor)
    print(case)

def normalize_file(src, out):
    src, out = Path(src), Path(out)
    suffix = src.suffix.lower()
    if suffix in {".txt",".md"}:
        text = src.read_text(encoding="utf-8", errors="replace")
    elif suffix in {".html",".htm"}:
        parser = VisibleTextParser()
        parser.feed(src.read_text(encoding="utf-8", errors="replace"))
        text = parser.text()
    else:
        return False
    out.write_text(text, encoding="utf-8")
    return True

def cmd_ingest(args):
    case = Path(args.case_dir).resolve()
    ensure_case(case)
    map_path = case/"SOURCE-MAP.json"
    records = json.loads(map_path.read_text(encoding="utf-8"))
    for raw_name in args.files:
        src = Path(raw_name).resolve()
        if not src.is_file():
            raise SystemExit(f"File not found: {src}")
        dest_dir = case/"raw"/args.kind
        dest = dest_dir/src.name
        if dest.exists():
            stem, suffix, i = dest.stem, dest.suffix, 2
            while dest.exists():
                dest = dest_dir/f"{stem}-{i}{suffix}"
                i += 1
        shutil.copy2(src, dest)
        digest = sha256(dest)
        norm_rel = None
        norm = case/"normalized"/f"{args.kind}-{dest.stem}.txt"
        if normalize_file(dest, norm):
            norm_rel = str(norm.relative_to(case))
        records.append({"id":f"S{len(records)+1:04d}","kind":args.kind,"raw":str(dest.relative_to(case)),"sha256":digest,"normalized":norm_rel,"ingested_at":now_iso()})
        print(f"{dest.name}\t{digest}")
    map_path.write_text(json.dumps(records, indent=2, ensure_ascii=False)+"\n", encoding="utf-8")

def cmd_new_round(args):
    case = Path(args.case_dir).resolve()
    state = ensure_case(case)
    existing = [int(p.name) for p in (case/"rounds").iterdir() if p.is_dir() and p.name.isdigit()]
    number = max(existing, default=0)+1
    scaffold_round(case, number, args.actor)
    state.setdefault("rounds", []).append({"number":number,"actor":args.actor})
    write_state(case, state)
    print(f"round {number:03d} actor={args.actor}")

def cmd_validate(args):
    case = Path(args.case_dir).resolve()
    state = ensure_case(case)
    missing = []
    for rel in ["CASE.md","STATE.json","SOURCE-MAP.json","owner/CONVERGENCE-REVIEW.md","owner/APPROVED-EVIDENCE-PACK.md"]:
        if not (case/rel).exists():
            missing.append(rel)
    rounds = sorted(p for p in (case/"rounds").iterdir() if p.is_dir()) if (case/"rounds").exists() else []
    if not rounds:
        missing.append("rounds/<at least one>")
    req = ["ROUND-BRIEF.md","RESEARCHER-PROMPT.md","SEARCH-TRACE.md","EVIDENCE-LEDGER.md","ROUND-REPORT.md","OWNER-REVIEW.md"]
    for r in rounds:
        for name in req:
            if not (r/name).exists():
                missing.append(str((r/name).relative_to(case)))
    sm = json.loads((case/"SOURCE-MAP.json").read_text(encoding="utf-8")) if (case/"SOURCE-MAP.json").exists() else []
    chats = [x for x in sm if x.get("kind")=="chat"]
    print(f"case_id={state.get('case_id')} mode={state.get('mode')} rounds={len(rounds)} sources={len(sm)} raw_chats={len(chats)}")
    if missing:
        print("MISSING:")
        for rel in missing:
            print("- "+rel)
        raise SystemExit(2)
    if not chats:
        print("WARNING no raw researcher chat has been ingested yet")
    print("STRUCTURE_OK")

def cmd_pack(args):
    case = Path(args.case_dir).resolve()
    ensure_case(case)
    out = Path(args.output).resolve() if args.output else case.with_name(case.name+".zip")
    with zipfile.ZipFile(out, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for p in sorted(case.rglob("*")):
            if p.is_file():
                zf.write(p, arcname=str(Path(case.name)/p.relative_to(case)))
    print(out)

def parser():
    p = argparse.ArgumentParser(prog="fldp", description="FlowDisP POC helper")
    sp = p.add_subparsers(dest="cmd", required=True)
    x = sp.add_parser("init"); x.add_argument("case_dir"); x.add_argument("--mode", required=True, choices=sorted(MODES)); x.add_argument("--case-id", default="FDP-AR-001"); x.add_argument("--actor", default="ABR-001"); x.set_defaults(func=cmd_init)
    x = sp.add_parser("ingest"); x.add_argument("case_dir"); x.add_argument("files", nargs="+"); x.add_argument("--kind", required=True, choices=sorted(KINDS)); x.set_defaults(func=cmd_ingest)
    x = sp.add_parser("new-round"); x.add_argument("case_dir"); x.add_argument("--actor", default="ABR-001"); x.set_defaults(func=cmd_new_round)
    x = sp.add_parser("validate"); x.add_argument("case_dir"); x.set_defaults(func=cmd_validate)
    x = sp.add_parser("pack"); x.add_argument("case_dir"); x.add_argument("--output"); x.set_defaults(func=cmd_pack)
    return p

def main():
    args = parser().parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
