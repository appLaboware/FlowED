#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,time
from pathlib import Path
from typedb.driver import TypeDB,TransactionType,Credentials,DriverOptions,DriverTlsConfig

DB="mytrues_cognitive_retrieval_v1"
OPT=DriverOptions(DriverTlsConfig.disabled())

def q(s):
    return '"'+str(s).replace("\\","\\\\").replace('"','\\"')+'"'

def attr(c):return c.as_attribute().get_string()
def rows(tx,s):return list(tx.query(s).resolve().as_concept_rows())

def connect():
    last=None
    for _ in range(60):
        try:
            d=TypeDB.driver("127.0.0.1:1729",Credentials("admin","password"),OPT)
            list(d.databases.all());return d
        except Exception as e:
            last=e
            try:d.close()
            except Exception:pass
            time.sleep(.5)
    raise RuntimeError(last)

def decode(v):
    if isinstance(v,str) and v.startswith("literal:"):
        try:return json.loads(v[len("literal:"):])
        except Exception:return v[len("literal:"):]
    return v

def load_case(tx,case_id):
    query=f'''match
      $o isa occurrence, has atom-id $oid;
      $bc isa binding, links (occurrence: $o, key: $ck, value: $cv);
      $ck has atom-id "key:case";
      $cv has atom-id {q(case_id)};
      $b isa binding, links (occurrence: $o, key: $k, value: $v);
      $k has atom-id $key;
      $v has atom-id $value;
    select $oid, $key, $value;'''
    occ={}
    for r in rows(tx,query):
        oid,key,value=attr(r.get("oid")),attr(r.get("key")),attr(r.get("value"))
        occ.setdefault(oid,{}).setdefault(key,[]).append(value)
    return occ

def one(b,key):
    vals=b.get(key) or []
    return vals[0] if vals else None

def at_value(b):
    v=one(b,"key:at")
    return decode(v) if v else ""

def decision_entries(occ):
    out=[]
    for oid,b in occ.items():
        if one(b,"key:type")=="kind:decision":
            out.append((at_value(b),oid,b))
    return sorted(out,key=lambda x:x[0])

def event_entries(occ):
    out=[]
    for oid,b in occ.items():
        if one(b,"key:type")!="kind:context":
            out.append((at_value(b),oid,b))
    return sorted(out,key=lambda x:x[0])

def event_id_for_occ(occ,oid):
    return one(occ.get(oid,{}),"key:event-id")

def decision_id_for_occ(occ,oid):
    return one(occ.get(oid,{}),"key:decision-id")

def answer(question,occ):
    kind=question["kind"]
    decisions=decision_entries(occ)
    current=decisions[-1] if decisions else None
    previous=decisions[-2] if len(decisions)>=2 else None
    first=decisions[0] if decisions else None

    if kind=="current_decision":return one(current[2],"key:decision-id") if current else None
    if kind=="previous_decision":return one(previous[2],"key:decision-id") if previous else None
    if kind=="first_decision":return one(first[2],"key:decision-id") if first else None
    if kind=="decision_count":return len(decisions)
    if kind=="current_rationale":return decode(one(current[2],"key:rationale")) if current else None
    if kind=="previous_rationale":return decode(one(previous[2],"key:rationale")) if previous else None
    if kind=="trigger_event_of_current":
        target=one(current[2],"key:trigger") if current else None
        return event_id_for_occ(occ,target) if target else None
    if kind=="superseded_by_current":
        target=one(current[2],"key:supersedes") if current else None
        return decision_id_for_occ(occ,target) if target else None
    if kind=="original_context_value":
        for oid,b in occ.items():
            if one(b,"key:type")=="kind:context":
                return decode(one(b,"key:fact/"+question["key"]))
        return None
    if kind=="current_context_value":
        state={}
        for oid,b in occ.items():
            if one(b,"key:type")=="kind:context":
                for key,vals in b.items():
                    if key.startswith("key:fact/"):
                        state[key.split("/",1)[1]]=decode(vals[0])
        cutoff=current[0] if current else "9999"
        for at,oid,b in event_entries(occ):
            if at>cutoff:break
            for key,vals in b.items():
                if key.startswith("key:fact/"):
                    state[key.split("/",1)[1]]=decode(vals[0])
        return state.get(question["key"])
    if kind=="event_count_by_kind":
        wanted="kind:"+question["event_kind"]
        return sum(1 for _,_,b in event_entries(occ) if one(b,"key:type")==wanted)
    raise KeyError(kind)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--questions",required=True)
    ap.add_argument("--out",required=True)
    args=ap.parse_args()
    questions=json.loads(Path(args.questions).read_text())["questions"]
    driver=connect()
    answers={}
    try:
        with driver.transaction(DB,TransactionType.READ) as tx:
            cache={}
            for question in questions:
                cid=question["case_id"]
                if cid not in cache:cache[cid]=load_case(tx,cid)
                answers[question["id"]]=answer(question,cache[cid])
    finally:driver.close()
    result={
      "retriever":"atom-occurrence-binding-typedb",
      "source":"TypeDB persisted incidence graph only",
      "answers":answers
    }
    Path(args.out).write_text(json.dumps(result,indent=2,ensure_ascii=False))
    print(f"TYPEDB_RETRIEVAL_PASS answers={len(answers)}")

if __name__=="__main__":main()
