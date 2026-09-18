import json, subprocess, sys, tempfile
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
CLI = ROOT/"fldp.py"
def run(*args):
    return subprocess.run([sys.executable, str(CLI), *map(str,args)], text=True, capture_output=True, check=True)
def main():
    with tempfile.TemporaryDirectory() as td:
        base = Path(td); case = base/"case"
        run("init", case, "--mode", "product", "--case-id", "TEST-001")
        assert (case/"CASE.md").exists()
        assert (case/"rounds"/"001"/"RESEARCHER-PROMPT.md").exists()
        html = base/"raw.html"
        html.write_text("<html><body><h1>Hello</h1><script>bad()</script><p>Evidence text</p></body></html>", encoding="utf-8")
        run("ingest", case, html, "--kind", "chat")
        sm = json.loads((case/"SOURCE-MAP.json").read_text(encoding="utf-8"))
        assert len(sm)==1 and sm[0]["sha256"]
        text = (case/sm[0]["normalized"]).read_text(encoding="utf-8")
        assert "Hello" in text and "Evidence text" in text and "bad()" not in text
        run("new-round", case, "--actor", "ABR-002")
        assert (case/"rounds"/"002"/"ROUND-BRIEF.md").exists()
        assert "STRUCTURE_OK" in run("validate", case).stdout
        out = base/"case.zip"; run("pack", case, "--output", out)
        assert out.exists() and out.stat().st_size>0
    print("OK")
if __name__ == "__main__":
    main()
