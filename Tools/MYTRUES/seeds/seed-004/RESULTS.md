# RESULTS — seed-004

Status: **PASS**.

## Accepted Actions evidence

Workflow:

`MyTrues seed-004 conformance`

Successful run:

- run: `36874885444`;
- job: `seed-004`;
- conclusion: `success`.

Evidence class: **EVIDENCE-B**.

## Manifest proved

The workflow loaded `manifest.json` and asserted exactly sixteen failure codes.

Provider decision counts:

- senior-a: **11**;
- senior-b: **8**.

Shared divergent cases: **4**.

- `php.extension_missing`;
- `wordpress.maintenance_transient`;
- `sqlite.dropin_stub_deployed`;
- `git.dubious_ownership`.

For each of those four codes both providers returned `200 decided` and different
provider decision IDs.

## Provider-specific behavior

For every seeded case the workflow called both provider endpoints.

- provider listed in the manifest -> `200 decided` with the exact seeded decision ID;
- provider not listed for that case -> `202 awaiting-provider-decision`.

This proves that the same open protocol does not imply a global/shared truth.

## Unknown control

`observability.novel_failure_never_seen` has no seeded decision for either provider.

Both returned:

`202 awaiting-provider-decision`

The control did not auto-heal and no decision was invented.

## Restart persistence

The workflow restarted both MyTrues provider processes without removing their SQLite
volumes.

After restart:

- all four shared divergent seeded decisions remained immediately available;
- the two provider-specific pending control requests remained pending;
- senior-a and senior-b remained isolated.

The job log printed:

- `SEED-004 SIXTEEN CASES: PASS`;
- `SENIOR-A 11 / SENIOR-B 8: PASS`;
- `FOUR DIVERGENT SHARED CASES: PASS`;
- `UNKNOWN CONTROL PAUSES BOTH PROVIDERS: PASS`;
- `PROVIDER MEMORY SURVIVES RESTART: PASS`.

## What this does not prove

seed-004 is a **conformance fixture**, not a scientific decision benchmark.

It does not prove:

- that any seeded decision is globally optimal;
- that provider A is better than provider B;
- CBR/MCDA/Bayesian/LTR superiority;
- production provider authentication;
- cross-host durability;
- any proprietary MyTrues Core algorithm.

The contexts/decisions are sanitized reference cases as declared in `README.md`.
