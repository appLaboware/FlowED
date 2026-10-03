#!/usr/bin/env python3
from __future__ import annotations
import argparse,json
from collections import defaultdict
from pathlib import Path

DIMENSIONS={
 "current_decision":"present-state",
 "decision_count":"history",
 "previous_decision":"history",
 "first_decision":"history",
 "current_rationale":"rationale",
 "previous_rationale":"history+rationale",
 "original_context_value":"context",
 "current_context_value":"context",
 "trigger_event_of_current":"causality",
 "superseded_by_current":"relations",
 "event_count_by_kind":"history",
}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--questions",required=True)
    ap.add_argument("--answer-key",required=True)
    ap.add_argument("--provider",required=True)
    ap.add_argument("--typedb",required=True)
    ap.add_argument("--json-out",required=True)
    ap.add_argument("--md-out",required=True)
    args=ap.parse_args()

    qs=json.loads(Path(args.questions).read_text())["questions"]
    expected=json.loads(Path(args.answer_key).read_text())["answers"]
    provider=json.loads(Path(args.provider).read_text())["answers"]
    typedb=json.loads(Path(args.typedb).read_text())["answers"]

    rows=[]
    totals={"provider":0,"typedb":0}
    dims=defaultdict(lambda:{"questions":0,"provider":0,"typedb":0})
    cases=defaultdict(lambda:{"questions":0,"provider":0,"typedb":0})
    for q in qs:
        qid=q["id"]; exp=expected[qid]
        pa=provider.get(qid); ta=typedb.get(qid)
        pp=pa==exp; tp=ta==exp
        totals["provider"]+=int(pp);totals["typedb"]+=int(tp)
        dim=DIMENSIONS[q["kind"]]
        dims[dim]["questions"]+=1;dims[dim]["provider"]+=int(pp);dims[dim]["typedb"]+=int(tp)
        cases[q["case_id"]]["questions"]+=1;cases[q["case_id"]]["provider"]+=int(pp);cases[q["case_id"]]["typedb"]+=int(tp)
        rows.append({
          "id":qid,"case_id":q["case_id"],"question":q["text"],"kind":q["kind"],"dimension":dim,
          "expected":exp,
          "provider":{"answer":pa,"pass":pp},
          "typedb":{"answer":ta,"pass":tp},
        })

    report={
      "benchmark":"MYTRUES-COGNITIVE-RETRIEVAL-V1",
      "blindness":"Retrievers read questions and persisted backend state; only scorer reads answer-key.json.",
      "questions":len(qs),
      "scores":{
        "provider_reference":{"correct":totals["provider"],"total":len(qs)},
        "atom_occurrence_binding":{"correct":totals["typedb"],"total":len(qs)},
      },
      "by_dimension":dict(dims),
      "by_case":dict(cases),
      "results":rows,
      "claim_boundary":"Compares retrieval from the open provider/reference persistence and the TypeDB incidence model. It is not an overall product ranking and does not yet score the private production MCP/PostgreSQL cognition persistence."
    }
    Path(args.json_out).write_text(json.dumps(report,indent=2,ensure_ascii=False))

    md=[
      "# MYTRUES-COGNITIVE-RETRIEVAL-V1",
      "",
      "Blind deterministic retrieval benchmark.",
      "",
      f"- Questions: **{len(qs)}**",
      f"- Provider/reference: **{totals['provider']}/{len(qs)}**",
      f"- Atom/Occurrence/Binding: **{totals['typedb']}/{len(qs)}**",
      "",
      "## By dimension",
      "",
      "| Dimension | Questions | Provider | Atom/Occurrence/Binding |",
      "|---|---:|---:|---:|",
    ]
    for name,data in sorted(dims.items()):
        md.append(f"| {name} | {data['questions']} | {data['provider']}/{data['questions']} | {data['typedb']}/{data['questions']} |")
    md += ["","## Per question","","| ID | Question | Provider | TypeDB |","|---|---|---:|---:|"]
    for row in rows:
        md.append(f"| {row['id']} | {row['question']} | {'PASS' if row['provider']['pass'] else 'FAIL'} | {'PASS' if row['typedb']['pass'] else 'FAIL'} |")
    md += ["","## Boundary","",report["claim_boundary"],""]
    Path(args.md_out).write_text("\n".join(md))

    assert len(provider)==len(qs), (len(provider),len(qs))
    assert len(typedb)==len(qs), (len(typedb),len(qs))
    print(f"COGNITIVE_RETRIEVAL_BENCHMARK_COMPLETE provider={totals['provider']}/{len(qs)} typedb={totals['typedb']}/{len(qs)}")

if __name__=="__main__":main()
