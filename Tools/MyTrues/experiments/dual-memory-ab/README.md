# MyTrues Dual-Memory A/B — EXP-001

Purpose: preserve two independent cognition-memory lines long enough to compare retrieval behavior on the same source cognition stream.

This experiment intentionally does **not** merge, normalize away, or "improve" either implementation.

## Line A — existing provider/reference memory

Reuses unchanged:

- `Tools/MYTRUES/reference/provider_server.py`
- protocol `mytrues.decision/v1`
- existing SQLite provider-memory behavior

The reference model is exercised exactly as implemented, including its current `failure_code` keyed decision update semantics.

## Line B — Atom / Occurrence / Binding

Reuses unchanged:

- `Tools/MyTrues/typedb-poc-bridge/00-schema.tql`
- TypeDB CE 3.12.1
- the MyTrues Memory Primitive:
  - Atom
  - Occurrence <: Atom
  - Binding(Occurrence, Key, Value)

Corrections and supersessions are represented as new occurrences/relations rather than destructive replacement.

## Neutral input

`cognition-stream.json` is the common source stream. It is not a storage schema.

The first case intentionally contains:

1. an observation;
2. decision v1;
3. new evidence;
4. decision v2 superseding v1.

Both stores receive the same semantic sequence.

## Retrieval questions

The harness asks both persisted representations:

1. What is the current decision?
2. What decision existed immediately before it?
3. Can the explicit supersession relation be recovered?
4. Can the original observation context be recovered?
5. How many distinct decisions for the case remain recoverable?

The comparison is deterministic and does not use an LLM to score the answers.

## Claim boundary

This experiment compares the open provider/reference v0.2 behavior with the TypeDB incidence model **for historical cognition retrieval**.

It is not an overall product benchmark. It must not be used to claim that the private production MCP/PostgreSQL implementation has exactly the same persistence semantics unless that implementation is independently inspected and tested.

## Isolation

Everything runs in ephemeral local stores in GitHub Actions:

- temporary SQLite database;
- temporary TypeDB database/container.

No writes are made to the live MCP, production PostgreSQL, persistent Azure TypeDB, or Cloudflare.
