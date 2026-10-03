#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, os, sqlite3, subprocess, sys, time, urllib.error, urllib.request
from pathlib import Path
from typedb.driver import TypeDB, TransactionType, Credentials, DriverOptions, DriverTlsConfig

ROOT=Path(__file__).resolve().parents[4]
HERE=Path(__file__).resolve().parent
PROVIDER=ROOT/"Tools"/"MYTRUES"/"reference"/"provider_server.py"
SCHEMA=ROOT/"Tools"/"MyTrues"/"typedb-poc-bridge"/"00-schema.tql"
TYPEDB_DB="mytrues_cognitive_retrieval_v1"
OPT=DriverOptions(DriverTlsConfig.disabled())

def post(url,payload):
    req=urllib.request.Request(url,data=json.dumps(payload).encode(),headers={"Content-Type":"application/json"},method="POST")
    try:
        with urllib.request.urlopen(req,timeout=10) as r:
            return r.status,json.loads(r.read())
    except urllib.error.HTTPError as e:
        return e.code,json.loads(e.read())

def get(url):
    with urllib.request.urlopen(url,timeout=10) as r:
        return r.status,json.loads(r.read())

def wait(url):
    deadline=time.time()+30
    last=None
    while time.time()<deadline:
        try:
            code,_=get(url)
            if code==200:return
        except Exception as e:last=e
        time.sleep(.25)
    raise RuntimeError(last)

def decision_payload(ev):
    return {
      "id":ev["decision_id"],
      "action":ev["action"],
      "result":ev["result"],
      "guards":[{"key":"benchmark-ingestion","satisfied":True}],
      "notice":ev["rationale"],
    }

def apply_facts(ctx,ev):
    for k,v in (ev.get("facts") or {}).items():
        ctx[k]=v
    return ctx

def materialize_provider(corpus,db_path):
    port=18092
    base=f"http://127.0.0.1:{port}"
    env=os.environ.copy()
    env.update({
      "MYTRUES_PROVIDER_ID":"cognitive-retrieval-reference",
      "MYTRUES_PROVIDER_PROFILE":"fqdn",
      "MYTRUES_DB_PATH":str(db_path),
      "PORT":str(port),
    })
    proc=subprocess.Popen([sys.executable,str(PROVIDER)],env=env,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
    applied={}
    try:
        wait(base+"/healthz")
        for case in corpus["cases"]:
            ctx=dict(case["base_context"])
            ctx["benchmark_case_id"]=case["case_id"]
            first_decision=None
            for ev in case["events"]:
                if ev["kind"]!="decision":
                    apply_facts(ctx,ev)
                    continue
                first_decision=ev
                break
            if not first_decision:
                continue
            request={
              "protocol":"mytrues.decision/v1",
              "requestId":"req-"+case["case_id"].replace(":","-"),
              "subject":{"kind":"failure","code":case["failure_code"]},
              "context":ctx,
              "constraints":{"automation":"recommend-only","maxRisk":"low"},
            }
            status,pending=post(base+"/v1/decisions/resolve.failure",request)
            if status!=202:
                raise RuntimeError((case["case_id"],status,pending))
            drid=pending["decisionRequestId"]
            decisions=[e for e in case["events"] if e["kind"]=="decision"]
            for ev in decisions:
                status,result=post(base+f"/v1/provider/decision-requests/{drid}/resolution",{"decision":decision_payload(ev)})
                if status!=200:
                    raise RuntimeError((case["case_id"],ev["id"],status,result))
            applied[case["case_id"]]={"decision_request_id":drid,"applied_decisions":[e["decision_id"] for e in decisions]}
    finally:
        proc.terminate()
        try:proc.wait(timeout=5)
        except subprocess.TimeoutExpired:proc.kill()
    print("PROVIDER_MATERIALIZED",json.dumps(applied,sort_keys=True))

def q(s):
    return '"'+str(s).replace("\\","\\\\").replace('"','\\"').replace("\n","\\n")+'"'

def literal(v):
    return "literal:"+json.dumps(v,ensure_ascii=False,sort_keys=True,separators=(",",":"))

def occ_id(case_id,event_id):
    return "occ:bench:"+case_id.split(":",1)[-1]+":"+event_id.split(":",1)[-1]

def context_occ(case_id):
    return "occ:bench:"+case_id.split(":",1)[-1]+":base-context"

def collect_typedb(corpus):
    occs=[]
    atom_ids=set()
    occ_ids=set()
    for case in corpus["cases"]:
        co=context_occ(case["case_id"])
        cb=[("key:type","kind:context"),("key:case",case["case_id"])]
        for k,v in sorted(case["base_context"].items()):
            cb.append((f"key:fact/{k}",literal(v)))
        occs.append((co,cb))
        occ_ids.add(co)
        for ev in case["events"]:
            oid=occ_id(case["case_id"],ev["id"])
            b=[
              ("key:type","kind:"+ev["kind"]),
              ("key:case",case["case_id"]),
              ("key:event-id",ev["id"]),
              ("key:at",literal(ev["at"])),
            ]
            if ev.get("statement") is not None:
                b.append(("key:statement",literal(ev["statement"])))
            for k,v in sorted((ev.get("facts") or {}).items()):
                b.append((f"key:fact/{k}",literal(v)))
            if ev["kind"]=="decision":
                b += [
                  ("key:decision-id",ev["decision_id"]),
                  ("key:action","action:"+ev["action"]),
                  ("key:rationale",literal(ev["rationale"])),
                ]
                if ev.get("trigger"):
                    b.append(("key:trigger",occ_id(case["case_id"],ev["trigger"])))
                if ev.get("supersedes"):
                    b.append(("key:supersedes",occ_id(case["case_id"],ev["supersedes"])))
                for alt in ev.get("rejected") or []:
                    b.append(("key:rejected",alt))
                for k,v in sorted((ev.get("result") or {}).items()):
                    b.append((f"key:result/{k}",literal(v)))
            occs.append((oid,b))
            occ_ids.add(oid)
    for oid,b in occs:
        atom_ids.add(oid)
        for k,v in b:
            atom_ids.add(k);atom_ids.add(v)
    return occs,occ_ids,atom_ids

def connect_typedb():
    last=None
    for _ in range(90):
        try:
            d=TypeDB.driver("127.0.0.1:1729",Credentials("admin","password"),OPT)
            list(d.databases.all());return d
        except Exception as e:
            last=e
            try:d.close()
            except Exception:pass
            time.sleep(.5)
    raise RuntimeError(last)

def materialize_typedb(corpus):
    occs,occ_ids,atoms=collect_typedb(corpus)
    d=connect_typedb()
    try:
        if d.databases.contains(TYPEDB_DB):d.databases.get(TYPEDB_DB).delete()
        d.databases.create(TYPEDB_DB)
        with d.transaction(TYPEDB_DB,TransactionType.SCHEMA) as tx:
            tx.query(SCHEMA.read_text()).resolve().as_ok();tx.commit()
        with d.transaction(TYPEDB_DB,TransactionType.WRITE) as tx:
            for aid in sorted(atoms):
                typ="occurrence" if aid in occ_ids else "atom"
                tx.query(f'insert $a isa {typ}, has atom-id {q(aid)}, has lexical {q(aid)};').resolve()
            tx.commit()
        with d.transaction(TYPEDB_DB,TransactionType.WRITE) as tx:
            for oid,b in occs:
                for key,value in b:
                    tx.query(f'''match
                      $o isa occurrence, has atom-id {q(oid)};
                      $k isa atom, has atom-id {q(key)};
                      $v isa atom, has atom-id {q(value)};
                    insert $x isa binding, links (occurrence: $o, key: $k, value: $v);''').resolve()
            tx.commit()
        print(f"TYPEDB_MATERIALIZED database={TYPEDB_DB} occurrences={len(occs)}")
    finally:d.close()

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--corpus",required=True)
    ap.add_argument("--provider-db",required=True)
    args=ap.parse_args()
    corpus=json.loads(Path(args.corpus).read_text())
    p=Path(args.provider_db)
    p.parent.mkdir(parents=True,exist_ok=True)
    if p.exists():p.unlink()
    materialize_provider(corpus,p)
    materialize_typedb(corpus)
    print("MATERIALIZATION_PASS")

if __name__=="__main__":main()
