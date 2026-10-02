#!/usr/bin/env python3
from __future__ import annotations
import json, os, sys
from typedb.driver import TypeDB, TransactionType, Credentials, DriverOptions, DriverTlsConfig

DB="mytrues_memory_poc_v0"
PW=os.environ["TYPEDB_ADMIN_PASSWORD"]
OPT=DriverOptions(DriverTlsConfig.disabled())

def attr_string(c):
    return c.as_attribute().get_string()

def rows(tx,q):
    return list(tx.query(q).resolve().as_concept_rows())

def bindings(tx, oid):
    q=f'''match
      $o isa occurrence, has atom-id "{oid}";
      $b isa binding, links (occurrence: $o, key: $k, value: $v);
      $k has atom-id $key;
      $v has atom-id $value;
    select $key, $value;'''
    return {attr_string(r.get("key")):attr_string(r.get("value")) for r in rows(tx,q)}

tests=[]
detail={}
with TypeDB.driver("127.0.0.1:1729", Credentials("admin",PW), OPT) as driver:
    assert driver.databases.contains(DB), f"database {DB} missing"
    with driver.transaction(DB,TransactionType.READ) as tx:
        occ_count=len(rows(tx,"match $o isa occurrence; select $o;"))
        bind_count=len(rows(tx,"match $b isa binding; select $b;"))
        tests.append(("T01-counts",occ_count==8 and bind_count==45))
        detail["counts"]={"occurrences":occ_count,"bindings":bind_count}

        npm=bindings(tx,"occ:npm-failure-001")
        decision=bindings(tx,"occ:decision-pnpm-001")
        influence=bindings(tx,"occ:influence-001")
        relcorr=bindings(tx,"occ:relation-correction-001")
        alias=bindings(tx,"occ:variable-alias-001")
        correction=bindings(tx,"occ:correction-001")
        decl=bindings(tx,"occ:semantic-declaration-001")
        evo=bindings(tx,"occ:schema-evolution-001")

        tests.append(("T02-decision-is-occurrence",
            decision.get("key:type")=="kind:decision"
            and decision.get("key:based-on")=="occ:npm-failure-001"
            and decision.get("key:selected")=="tool:pnpm"))

        tests.append(("T03-cognitive-path",
            influence.get("key:source")=="occ:npm-failure-001"
            and influence.get("key:target")=="occ:decision-pnpm-001"
            and decision.get("key:based-on")=="occ:npm-failure-001"))

        tests.append(("T04-relation-is-occurrence",
            influence.get("key:type")=="kind:influence"))

        tests.append(("T05-relation-is-versionable",
            relcorr.get("key:type")=="kind:correction"
            and relcorr.get("key:corrects")=="occ:influence-001"))

        # Append-only representation: original occurrence still states the
        # original alias while a distinct correction occurrence refers to it.
        tests.append(("T06-append-only-correction",
            alias.get("key:expected")=="variable:DATABASE_URL"
            and alias.get("key:actual")=="variable:MY_DATABASE"
            and correction.get("key:corrects")=="occ:variable-alias-001"
            and correction.get("key:reason")=="reason:prod-only-alias"))

        tests.append(("T07-relation-name-is-knowledge",
            decl.get("key:subject")=="kind:influence"
            and decl.get("key:is-a")=="kind:relation-kind"))

        tests.append(("T08-cognitive-schema-versioned-as-data",
            evo.get("key:from")=="schema:v1"
            and evo.get("key:to")=="schema:v2"
            and evo.get("key:introduced")=="concept:action"))

        # Keys themselves are atoms, not physical attribute names.
        q='''match $a isa atom, has atom-id "key:tool"; select $a;'''
        tests.append(("T09-key-is-atom",len(rows(tx,q))==1))

        # An occurrence is also an atom and can therefore be the value of another occurrence.
        q='''match
          $o isa occurrence, has atom-id "occ:decision-pnpm-001";
          $b isa binding, links (value: $o);
        select $b;'''
        tests.append(("T10-occurrence-can-be-referenced",len(rows(tx,q))>=1))

        detail["path"]=[
          "occ:npm-failure-001",
          "occ:influence-001",
          "occ:decision-pnpm-001",
          "occ:relation-correction-001"
        ]
        detail["original_alias"]=alias
        detail["correction"]=correction

failed=[name for name,ok in tests if not ok]
report={
  "model":"MyTrues Memory Primitive v0",
  "database":DB,
  "tests":[{"name":n,"pass":ok} for n,ok in tests],
  "detail":detail,
  "pass":not failed
}
print(json.dumps(report,indent=2,ensure_ascii=False))
if failed:
    print("FAILED: "+", ".join(failed),file=sys.stderr)
    raise SystemExit(1)
print("QUALIFICATION_PASS T01-T10")
