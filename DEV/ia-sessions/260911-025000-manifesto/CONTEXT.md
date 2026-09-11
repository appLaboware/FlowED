# CONTEXT — MAN-001

**Actor:** `MAN-001`
**Role:** branch paralela derivada do chat original
**Session:** `260911-025000-manifesto`

## Mission

Continue the Manifesto FlowED review already in progress. Do not stop ordinary manifesto work to wait for the PO, except when a pending PO input explicitly blocks the next step.

The current editorial architecture under review uses:

```text
REDUCT-MAX ← ... ← BASELINE → ... → EXPAND-MAX
                         │
                         ↓
                      DEFESA
```

`BASELINE` is preferred over `BASE` to avoid confusion with the cognitive base of CCP.

## Important distinction

`DEFESA` is not the whole CCP and `Como chegamos aqui` is not to be manually produced now.

`Como chegamos aqui` is a future CCP projection expected to be derived more deterministically from preserved raw conversation/logs and a structured cognitive store. The worker will investigate that materialization.

For current manifesto work, focus on the proposition, density projections and DEFESA. Preserve enough session cognition and provenance so the future worker can reconstruct the path without relying on retrospective memory.

## Session memory obligation

Maintain `session_resume.md` as a chronological cognitive summary of meaningful interactions.

For direct human-chat interactions, record with special care:

- what the human proposed, changed, approved or rejected;
- the reasoning relevant to that change;
- what you did in response;
- whether it diverged from previous PO guidance;
- affected files/commits and open questions.

Do not merely log “human approved X”; preserve the relevant rationale when it changes how the work should be understood.

## Relation with PO-001

`PO-001` coordinates CCP/materialization implications and acts as a critical consultant. It does not take over ordinary manifesto wording.

You do not need access to the PO session. Receive PO guidance through your `INBOX/`; communicate back through `OUTBOX/`, commits and your own session state.

Human chat and PO INBOX are both authoritative inputs. If they conflict explicitly, follow the direct human decision and record the divergence so the PO can review and critique it later.

## References

Before external research, consult `docs/research/REFERENCE-POOL.md`. Reuse an existing source only when it actually supports the new claim; otherwise research further and add newly consulted sources to the pool.

## Commit identity

Every new commit from this actor must start with `[MAN-001]`.

Read `DEV/ia-sessions/COORDINATION.md`, `DEV/ia-sessions/MOBILE-LOOP.md`, your `INBOX/` and `session_resume.md` before the next repository write.
