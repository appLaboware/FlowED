# SESSION-CLOSE-005

Date: 2026-10-01

Status: **DONE**

Scope authority: user-defined north for session 005.

This close means the **declared north of this session is complete**. It does not mean
R0–R8 of the wider evolution program are complete. Deferred work is isolated in
`Tools/EVOLUTION/NEXT.md`.

## 1. Honest IDEOS audit + INVENTORY/ROADMAP

**DONE.**

Authoritative audit:

`Tools/IDEOS/experiments/AUDIT.md`

Every historical EXP-001..007 path has an honest `RESULTS.md`; the repository also
records the two historical EXP-005 experiments separately as EXP-005A/EXP-005B.

Accepted states:

| Experiment | Final audited state | Primary evidence | Class |
|---|---|---|---|
| EXP-001 PHP+MySQL | PASS | Actions `36769533522` | A |
| EXP-002 containerized Porter | PASS, license-qualified afterward | Actions `36769533522` | A |
| EXP-003 Azure trust | PARTIAL: OIDC/RG read/write proved; own ACI E2E not run | Actions `36795844036` | A+D |
| EXP-004 dual target | NOT PROVEN; startup failures had zero jobs | audited workflow runs | D for capability |
| EXP-005A GRyCAP IM | PASS Docker; Azure OIDC connector incompatibility recorded | Actions `36800909647`, `36801390616` | A |
| EXP-005B Porter one-command Azure | PASS | Actions `36796448509` | A |
| EXP-006 PHP+MySQL+DNS | NOT PROVEN; missing DNS bootstrap observed before materialization | Actions `36805070315` | A for failure / D for intended capability |
| EXP-007 decision memory | PASS historically; ephemeral Neo4j retain limitation recorded | Actions `36806662068` | A+B |

Non-inheritance is explicit: later experiments do not retroactively turn earlier
failed/partial experiments into passes.

`Tools/EVOLUTION/INVENTORY.md` and `ROADMAP.md` were normalized so evidence-class
cells use only A/B/C/D or explicit combinations such as A+B/A+D.

Open capabilities remain marked open rather than promoted.

## 2. MyTrues protocol reference v0.2

**DONE for the declared session criterion.**

Reference runtime:

- provider-scoped SQLite;
- two independent providers;
- open request/decision/pending/resolution protocol;
- unknown case pauses;
- sanitized case packet;
- explicit provider resolution;
- resume;
- provider-scoped retention;
- restart persistence.

Schemas under `Tools/MYTRUES/protocol/schemas/` identify protocol schema version 0.2
and are validated against JSON Schema Draft 2020-12 by the Actions conformance workflow.

Accepted runs:

- `36871180992` — v0.2 schema/behavior acceptance;
- `36874885791` — revalidation with seed-support code present;
- `36875218233` — latest successful conformance after
  `ALGORITHM-BOUNDARY.md` storage/seed alignment.

Evidence class: **B**.

The accepted conformance proves:

- `MYTRUES V0.2 SCHEMAS: PASS`;
- `TWO INDEPENDENT PROVIDER MYTRUES: PASS`;
- `UNKNOWN CASE PAUSES: PASS`;
- `HUMAN TEACH -> RESUME: PASS`;
- `PROVIDER-SCOPED LEARNING: PASS`;
- `MEMORY SURVIVES RESTART: PASS`;
- `ANONYMIZED CASE PACKET: PASS`.

`Tools/MYTRUES/docs/ALGORITHM-BOUNDARY.md` now matches the reference code:

- SQLite is the executable reference store;
- `MYTRUES_SEED_MANIFEST` is data initialization, not algorithm;
- unknown cases still follow `202 awaiting-provider-decision`;
- Neo4j is not a runtime dependency;
- no proprietary Core behavior is claimed.

## 3. seed-004 bridge

**DONE.**

Package:

`Tools/MYTRUES/seeds/seed-004/`

Contains exactly 16 sanitized failure codes:

1. `azure.aci.smb_volume_permissions_root`
2. `wordpress.canonical_host_mismatch`
3. `cloudflare.healthcheck_stale_backend`
4. `wordpress.installer_ssl_redirect_loop`
5. `azure.aci.quota_environment_exhausted`
6. `azure.region_edge_reachability`
7. `sqlite.dropin_stub_deployed`
8. `wordpress.maintenance_transient`
9. `php.extension_missing`
10. `git.dubious_ownership`
11. `docker.network_wrong_bridge`
12. `docker.volume_uid_mismatch`
13. `wordpress.wpconfig_missing_abspath`
14. `azure.resourcegroup_delete_slow`
15. `provider.no_api_captcha`
16. `observability.novel_failure_never_seen`

Actions workflow:

`.github/workflows/mytrues-004-seed.yml`

Accepted runs:

- `36874885444` — first accepted execution;
- `36875190145` — successful revalidation after results materialization.

Evidence class: **B**.

Proved:

- 16 cases loaded;
- senior-a decisions: **11**;
- senior-b decisions: **8**;
- four shared cases return divergent provider decisions:
  - `php.extension_missing`;
  - `wordpress.maintenance_transient`;
  - `sqlite.dropin_stub_deployed`;
  - `git.dubious_ownership`;
- the control `observability.novel_failure_never_seen` returns
  `202 awaiting-provider-decision` for **both** providers;
- provider SQLite memory and pending requests survive process restart;
- providers remain isolated.

`seed-004` is explicitly a **conformance fixture, not a scientific benchmark**.

## 4. Storage/license gate from banca

**RECORDED AND ENFORCED IN DOCUMENTATION.**

Decision:

- Neo4j Community/GPLv3: **RED** for product-runtime baseline;
- Porter administrative MongoDB 8.0/SSPL path: **RED** transitively for product baseline;
- SQLite remains MyTrues reference runtime.

Historical experiments remain truthful:

- EXP-007 really executed Neo4j;
- EXP-002 really observed Porter Mongo administrative runtime.

But neither observation authorizes those technologies as product-runtime dependencies.

Updated authorities include:

- `Tools/EVOLUTION/INVENTORY.md`;
- `Tools/EVOLUTION/ROADMAP.md`;
- `Tools/EVOLUTION/DOSSIERS/memory-and-retrieval.md`;
- `Tools/MYTRUES/memory/neo4j/README.md`;
- EXP-002/EXP-007 `RESULTS.md`;
- `Tools/IDEOS/experiments/AUDIT.md`.

## 5. Actions-only evidence boundary

The session obeyed the execution rule:

- repository operations through GitHub;
- runtime evidence through GitHub Actions;
- no local shell evidence used.

Known Actions limitation retained honestly:

`actions/upload-artifact@v4` attempt in run `36870956574` ended
`startup_failure` with zero jobs.

Because GitHub exposed no narrower job-level cause, the accepted statement remains:

**not executable in actions in the current repository configuration**, with no invented
root cause.

Job logs/runs remain the accepted evidence surface for this session.

## 6. Not closed by this session

The following are intentionally **not** claimed done:

- all Porter/CNAB R1 capabilities;
- alternate Porter storage with acceptable license;
- OpenAPI full validation/migration;
- RFC 9457 full conformance;
- CloudEvents/AsyncAPI/PROV;
- production authentication for provider resolution;
- durable cross-host orchestration;
- scientific decision baselines;
- decision-quality benchmark;
- Science Frontier claim;
- proprietary MyTrues Core.

These are recorded in `Tools/EVOLUTION/NEXT.md` and/or the wider `ROADMAP.md`.

## Definition-of-done check

- [x] EXP audit honest and RESULTS present;
- [x] INVENTORY/ROADMAP evidence classes aligned with observed state;
- [x] MyTrues v0.2 schemas validated in Actions;
- [x] pause -> sanitize -> resolve -> resume proved in Actions;
- [x] ALGORITHM-BOUNDARY aligned with current reference code;
- [x] seed-004 contains all 16 required codes;
- [x] provider-specific/divergent decisions proved;
- [x] unknown control pauses both providers;
- [x] provider memory survives restart;
- [x] Neo4j/Mongo license gates documented without rewriting history;
- [x] non-executable Actions artifact boundary documented;
- [x] out-of-north work moved to NEXT.md.

# DONE
