# Evidence — MYTRUES-DUAL-MEMORY-AB-001

Date: 2026-10-03

Branch: `experiment/mytrues-dual-memory-ab`

GitHub Actions run: `37088924902`

Job: `111104880712`

Result: **PASS**

## Scope

Same neutral cognition stream was materialized independently into:

- Line A: existing open `Tools/MYTRUES/reference/provider_server.py` behavior, using its SQLite provider memory unchanged;
- Line B: existing `Atom / Occurrence / Binding` schema over TypeDB CE 3.12.1 unchanged.

No live MCP, PostgreSQL, persistent Azure TypeDB, DNS, or production data was modified.

## Cognition sequence

1. observation of one case;
2. decision v1;
3. new evidence;
4. decision v2 superseding v1.

## Retrieval results

| Retrieval question | Provider reference | Atom/Occurrence/Binding |
|---|---:|---:|
| Current decision recoverable | PASS | PASS |
| Immediately previous decision recoverable | FAIL | PASS |
| Explicit supersession relation recoverable | FAIL | PASS |
| Original observation context recoverable | PASS | PASS |
| Two distinct decisions remain recoverable | FAIL | PASS |

Observed deterministic score:

- provider reference: **2/5**
- Atom/Occurrence/Binding: **5/5**

Observed persisted state after v2:

- provider reference current decision: `decision.ab.v2`
- provider reference previous decision: not recoverable from persisted reference state
- provider reference recoverable decision count: `1`
- provider reference supersession link: absent

- TypeDB current decision: `decision.ab.v2`
- TypeDB previous decision: `decision.ab.v1`
- TypeDB recoverable decision count: `2`
- TypeDB supersession relation: explicit `key:supersedes`

## Interpretation boundary

This is evidence about **historical cognition retrieval under re-resolution**.

It does not establish an overall product ranking.

In particular, the open provider reference is designed around operational decision resolution and currently stores one decision per `failure_code` using update semantics. The result therefore demonstrates a mismatch with historical cognition retrieval requirements, not a failure to meet its original operational contract.

The private production MCP/PostgreSQL implementation was not treated as structurally identical to the open SQLite reference and must be independently inspected/tested before extending this result to it.

## Reproducibility

Experiment source:

- `Tools/MyTrues/experiments/dual-memory-ab/cognition-stream.json`
- `Tools/MyTrues/experiments/dual-memory-ab/compare_memory_models.py`
- `.github/workflows/mytrues-dual-memory-ab.yml`
