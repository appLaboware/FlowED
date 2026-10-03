#!/usr/bin/env python3
from __future__ import annotations
import json, os, time
from pathlib import Path
from typedb.driver import TypeDB, TransactionType, Credentials, DriverOptions, DriverTlsConfig

ROOT=Path(__file__).resolve().parent
DB="mytrues_memory_poc_v0"
DESIRED=os.environ["TYPEDB_ADMIN_PASSWORD"]
OPTIONS=DriverOptions(DriverTlsConfig.disabled())

def q(s:str)->str:
    return '"' + s.replace('\\','\\\\').replace('"','\\"').replace('\n','\\n') + '"'

def connect():
    last=None
    for password in (DESIRED, "password"):
        try:
            d=TypeDB.driver("127.0.0.1:1729", Credentials("admin",password), OPTIONS)
            list(d.databases.all())
            return d,password
        except Exception as exc:
            last=exc
            try:d.close()
            except Exception:pass
    raise RuntimeError(f"Cannot authenticate to local TypeDB: {last}")

data=json.loads((ROOT/"canonical-memory.json").read_text())
occs=data["occurrences"]
occids={o["id"] for o in occs}
atomids=set()
for o in occs:
    atomids.add(o["id"]); atomids.update(o["bindings"]); atomids.update(o["bindings"].values())

driver,used=connect()
try:
    if not driver.databases.contains(DB):
        driver.databases.create(DB)
        with driver.transaction(DB,TransactionType.SCHEMA) as tx:
            tx.query((ROOT/"00-schema.tql").read_text()).resolve().as_ok(); tx.commit()
        with driver.transaction(DB,TransactionType.WRITE) as tx:
            for aid in sorted(atomids):
                typ="occurrence" if aid in occids else "atom"
                tx.query(f'insert $a isa {typ}, has atom-id {q(aid)}, has lexical {q(aid.split(":",1)[-1])};').resolve()
            tx.commit()
        with driver.transaction(DB,TransactionType.WRITE) as tx:
            for o in occs:
                for key,value in o["bindings"].items():
                    tx.query(f'''match
                      $o isa occurrence, has atom-id {q(o["id"])};
                      $k isa atom, has atom-id {q(key)};
                      $v isa atom, has atom-id {q(value)};
                    insert $b isa binding, links (occurrence: $o, key: $k, value: $v);''').resolve()
            tx.commit()
    if used != DESIRED:
        driver.users.get("admin").update_password(DESIRED)
finally:
    driver.close()

driver,_=connect()
try:
    with driver.transaction(DB,TransactionType.READ) as tx:
        occurrences=len(list(tx.query("match $o isa occurrence; select $o;").resolve().as_concept_rows()))
        bindings=len(list(tx.query("match $b isa binding; select $b;").resolve().as_concept_rows()))
    assert occurrences==8, occurrences
    assert bindings==45, bindings
    print(f"READY database={DB} occurrences={occurrences} bindings={bindings}")
finally:
    driver.close()
