# SESSION RESUME — PO-001

**Session:** `260911-025000-po`
**Actor:** `PO-001`
**Role:** coordinator / CCP materialization PO / critical consultant

## Current mission

Coordinate two parallel continuities:

- `MAN-001`: manifesto revision and human-facing cognitive projection experiments;
- `WRK-001`: future executable CCP materializer POC.

The human remains final philosophical authority. PO-001 is expected to criticize human decisions when evidence or architecture suggests a better path rather than merely agree.

## Current architecture

Working pipeline:

```text
preserved source/log
→ marking/indexing
→ structured CCP
→ projection contract
→ adapter
→ structured/compiled projection
```

Current concepts under investigation include:

- primacy of cognition without mandatory visual primacy;
- cognitive minimum by audience/task/risk/authority;
- density zoom / microprojection;
- semantic invariance across projections;
- density monotonicity;
- human and AI adapters;
- dynamic projection of `Como chegamos aqui` from preserved raw sources.

## MAN-001 state

MAN-001 proposed a density workflow in commit `40990f239712569addf97c5d4f366e564dbe1c71` using:

```text
REDUCT-MAX ← ... ← BASELINE → ... → EXPAND-MAX
                         │
                         ↓
                      DEFESA
```

PO review accepts the core model with refinements:

- `BASELINE` accepted as preferable to `BASE`;
- monotonicity applies primarily to density axis;
- invariance is broader rule across all projections;
- `DEFESA` is not whole CCP;
- `Como chegamos aqui` is future dynamic projection and must not be manually authored now;
- optional micro-CCP can be used as temporary authoring scaffold, not as the historical path;
- expertise alone must not become universal density rule.

MAN-001 must maintain chronological `session_resume.md`, especially capturing direct human-chat changes, rationale and divergences from PO guidance.

## Communication model

- Human talks directly with each ChatGPT session.
- PO communicates to MAN/WRK through their `INBOX/`.
- MAN/WRK communicate to PO through `OUTBOX/`, commits and session state.
- Human should not have to copy full conversations among sessions.
- `NOVO INPUT` is the minimal wake/sync command after bootstrap.

## Scientific reference reuse

A shared pool is established at `docs/research/REFERENCE-POOL.md`.

Actors should check it before new research, reuse only when pertinent, and record newly consulted references with explicit support/limits to avoid both repeated research and citation laundering.

## Next expected events

1. MAN-001 consumes PO introduction/alignment input, revises its density protocol draft and begins tagged commits `[MAN-001]`.
2. Human later creates/starts WRK-001 (potentially via ChatGPT Work) and gives only repository bootstrap.
3. PO monitors repository on each human return; there is no background monitoring.
