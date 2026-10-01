# MyTrues

> Migration target: `MyTrues/mytrues`

MyTrues is a **domain-generic decision protocol**.

It lets a client consult a selected decision provider without embedding that
provider's memory, storage or decision process in the client.

IDEOS is one client of MyTrues. MyTrues itself is not DevOps-specific.

## Reference interaction

Known decision:

`request -> provider MyTrues -> approved decision -> resume`

Unknown decision:

`request -> pending -> sanitized context -> authorized provider/human -> explicit resolution -> retain in that provider -> resume`

Different providers may legitimately resolve the same case differently.

## Current executable profile — v0.2

The current reference implementation was first exercised for operational failure
resolution and therefore exposes a `failure_code`-oriented v0.2 profile.

That profile remains the accepted executable reference until a versioned generic
schema supersedes it. The repository reorganization does not silently rewrite
the already-proved v0.2 contract.

See:

- `protocol/`;
- `reference/provider_server.py`;
- `conformance/test_protocol.py`;
- `docs/GENERIC-PROTOCOL.md`;
- `docs/ALGORITHM-BOUNDARY.md`.

## CCP documentary layer

A registered decision may be associated with a **CCP Record** — the documentary
record of the Caminho Cognitivo do Criador that led to the decision.

CCP preserves provenance/context; it is not the decision algorithm.

See `docs/CCP-RECORD.md` and `docs/legacy-ccp/`.

## Open-first boundary

Everything already public remains open:

- protocols and schemas;
- standards;
- published algorithms;
- reference implementations;
- conformance tests;
- baseline heuristics;
- generic adapters.

Provider data may remain private.

`core/` remains empty of proprietary decision logic until the Science Frontier
Gate is passed.

## Current proved behavior

The reference implementation already proves:

- two independent provider MyTrues instances;
- same protocol, different known decisions;
- unknown case -> `202 awaiting-provider-decision`;
- sanitized case packet;
- explicit provider resolution;
- provider-scoped learning;
- paused request -> resumable;
- SQLite memory survives restart.

`seed-004` remains a **conformance fixture, not a scientific benchmark**.

## Repository structure

- `protocol/` — open interoperability contract;
- `reference/` — open reference service;
- `memory/` — reference/historical memory material;
- `conformance/` — protocol/behavior tests;
- `docs/` — generic protocol, algorithm boundary and CCP documentary lineage;
- `open/` — open-surface statement;
- `core/` — reserved for future demonstrably original added value.
