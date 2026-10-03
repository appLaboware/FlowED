#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,sqlite3
from pathlib import Path

def load_cases(db):
    out={}
    for row in db.execute("SELECT rowid,* FROM decision_requests ORDER BY rowid"):
        req=json.loads(row["request_json"])
        case_id=(req.get("context") or {}).get("benchmark_case_id")
        if not case_id:continue
        out[case_id]={
          "request_rowid":row["rowid"],
          "request":req,
          "request_decision":json.loads(row["decision_json"]) if row["decision_json"] else None,
          "failure_code":req["subject"]["code"],
        }
    for case_id,data in out.items():
        row=db.execute("SELECT rowid,* FROM decisions WHERE failure_code=?",(data["failure_code"],)).fetchone()
        data["current_row"]=dict(row) if row else None
        data["current"]=json.loads(row["decision_json"]) if row else None
    return out

def decision_docs(case):
    docs=[]
    for doc in [case.get("request_decision"),case.get("current")]:
        if doc and doc.get("id") and all(x.get("id")!=doc.get("id") for x in docs):
            docs.append(doc)
    return docs

def answer(q,case):
    kind=q["kind"]
    docs=decision_docs(case)
    current=case.get("current")
    req=case["request"]
    if kind=="current_decision":
        return current.get("id") if current else None
    if kind=="decision_count":
        return len(docs)
    if kind=="previous_decision":
        return docs[-2]["id"] if len(docs)>=2 else None
    if kind=="first_decision":
        return docs[0]["id"] if docs else None
    if kind=="current_rationale":
        return current.get("notice") if current else None
    if kind=="previous_rationale":
        return docs[-2].get("notice") if len(docs)>=2 else None
    if kind=="original_context_value":
        return (req.get("context") or {}).get(q["key"])
    if kind=="current_context_value":
        # The reference request is the persisted decision-time context.
        return (req.get("context") or {}).get(q["key"])
    if kind=="trigger_event_of_current":
        return None
    if kind=="superseded_by_current":
        return None
    if kind=="event_count_by_kind":
        return None
    raise KeyError(kind)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--db",required=True)
    ap.add_argument("--questions",required=True)
    ap.add_argument("--out",required=True)
    args=ap.parse_args()
    qs=json.loads(Path(args.questions).read_text())["questions"]
    db=sqlite3.connect(args.db);db.row_factory=sqlite3.Row
    try:cases=load_cases(db)
    finally:db.close()
    answers={}
    for q in qs:
        case=cases.get(q["case_id"])
        answers[q["id"]]=answer(q,case) if case else None
    result={
      "retriever":"provider-reference-v0.2",
      "source":"Tools/MYTRUES/reference/provider_server.py persisted SQLite state",
      "answers":answers
    }
    Path(args.out).write_text(json.dumps(result,indent=2,ensure_ascii=False))
    print(f"PROVIDER_RETRIEVAL_PASS answers={len(answers)}")

if __name__=="__main__":main()
