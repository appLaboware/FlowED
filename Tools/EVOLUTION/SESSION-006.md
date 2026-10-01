# SESSION-006

Date: 2026-10-01

Status: **ACTIVE**

Authorized north: **R0 -> R1**, in this order.

## R0 — experimental discipline

Close only with executable/reconstructable evidence for:

1. canonical external-resource inventory per run:
   - creator/authority;
   - location/scope;
   - cost/accounting state;
   - cleanup mechanism;
2. ownership/tagging convention that makes cleanup scoped, safe and idempotent;
3. cost/duration/quota explicitly recorded in every RESULTS.md;
4. exact versions explicitly recorded in every RESULTS.md;
5. durable post-run evidence retention.

Artifact-retention investigation must first minimize and reproduce the historical
`actions/upload-artifact@v4` startup failure from run `36870956574`.
If it remains unavailable, prove a concrete durable alternative whose evidence is
accessible after the originating workflow run.

## R1 — exhaust Porter/CNAB upstream

Only after R0 is closed.

Priority gate:

- exhaust official Porter storage mechanisms without modifying upstream;
- MongoDB 8.0 / SSPL remains RED for product-runtime baseline;
- identify whether any currently shipped/supported Porter storage path has an
  acceptable product license and prove it by execution where applicable;
- a negative result is acceptable if the upstream surface is genuinely exhausted.

Then:

- legacy dependency output wiring (R1-P02);
- Dependencies v2/shared (R1-P03);
- signing/verification;
- secrets plugins;
- experimental file sources;
- MCP analyze_failure;
- Azure uninstall in the same accepted lifecycle experiment;
- same contract across Docker/Azure.

## Immutable rules

- upstream is immutable;
- no proprietary replacement while upstream/config/plugin paths remain;
- every runtime claim cites a GitHub Actions run URL;
- if a workflow cannot execute, record exactly `not executable in actions` and
  only the cause actually evidenced;
- seed-004 remains a conformance fixture, never a scientific benchmark;
- work outside this north goes to `Tools/EVOLUTION/NEXT.md`;
- final closure artifact is `Tools/EVOLUTION/SESSION-CLOSE-006.md`.

## Done

`SESSION-CLOSE-006.md` exists with:

- R0 closed;
- every R1 requested item classified by observed evidence;
- unresolved upstream limitations stated without local invention;
- ROADMAP/INVENTORY/NEXT aligned to the observed state.
