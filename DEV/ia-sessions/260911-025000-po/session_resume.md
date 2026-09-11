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

### First protocol validation cycle

The first real sync cycle completed successfully.

The human did not merely paste the PO bootstrap command into MAN-001. Before it, the human added an explanation of why the conversation had been derived, why work was being split, and why repository-based coordination should reduce manual transport of context.

MAN-001 correctly preserved this as a separate `HUMAN_CHAT` event in `session_resume.md`, including the human rationale, then recorded the `PO_INBOX` alignment as a distinct event. It explicitly declared `DIVERGENCE: none` because the two inputs were compatible.

Relevant commits:

- `f5c62b0d487c1ff3a76b51f4f72dffda334f7349` — MAN OUTBOX confirming PO input consumption;
- `e94b6784d99632d6b18203d86f63bf3cb6485918` — density protocol aligned with PO refinements;
- `091f5767607555798b87d26609f29979eff1c054` — MAN session resume preserving the human-chat rationale and the PO-input execution separately.

This validates an important part of the operating model:

```text
raw human interaction
→ structured session cognition with source attribution
→ operational action
→ OUTBOX / document update / commit
```

The human can therefore alter or enrich work directly in a parallel chat without manually relaying the entire interaction to PO, as long as the actor records the cognitive delta, provenance and divergence state in its session resume.

### Candidate InitProj learning from this cycle

Do not open a PR yet. Accumulate more real cycles first.

Current candidate deltas for InitProj/mobile multi-chat operation:

- stable Actor IDs and commit prefixes;
- explicit source attribution such as `HUMAN_CHAT`, `PO_INBOX`, `SELF_ANALYSIS`;
- chronological cognitive `session_resume.md` rather than only task status;
- mandatory divergence recording when direct human instruction changes or conflicts with upstream guidance;
- human as physical scheduler of chats, not information bus;
- a minimal wake/sync command after bootstrap;
- repository as shared coordination surface across ChatGPT branches/sessions.

These are observations from use, not yet canonical InitProj rules.

## Communication model

- Human talks directly with each ChatGPT session.
- PO communicates to MAN/WRK through their `INBOX/`.
- MAN/WRK communicate to PO through `OUTBOX/`, commits and session state.
- Human should not have to copy full conversations among sessions.
- `NOVO INPUT` is the minimal wake/sync command after bootstrap.

Inputs from human chat and PO INBOX are both valid operational inputs. When they conflict explicitly, the direct human decision prevails because the human is final philosophical authority, but the divergence must be recorded so PO can critically review it afterward.

## Scientific reference reuse

A shared pool is established at `docs/research/REFERENCE-POOL.md`.

Actors should check it before new research, reuse only when pertinent, and record newly consulted references with explicit support/limits to avoid both repeated research and citation laundering.

## Next expected events

1. MAN-001 continues ordinary manifesto review under the aligned density protocol.
2. Human later creates/starts WRK-001 (potentially via ChatGPT Work) and gives only repository bootstrap.
3. PO monitors repository on each human return; there is no background monitoring.
4. After several successful MAN/WRK cycles, PO evaluates whether the observed mobile multi-chat practices are mature enough to propose a PR back to InitProj.
