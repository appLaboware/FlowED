# HANDOFF EXPERIMENT EVALUATION — PO-001-01

**Evaluator:** `PO-001-01`  
**Stable Actor:** `PO-001`  
**Experiment snapshot H0:** `ac939f7ba4aad9cc9fe957a8821a3d5feceb2c32`  
**Date:** 2026-09-11

## Candidates

Two isolated experimental branches were created from the same snapshot:

- `exp/po-handoff-a`
- `exp/po-handoff-b`

Candidate outputs were not merged into the canonical branch during evaluation.

Committed responses:

- `f06e8a54841e9ff18ae876a931abbd7b9925cec7`
- `f19b2aff9a781edcbf2fb76b83f35ecbbd29e28c`

The evaluator scored both before the human revealed which materialization method produced which response.

## Blind evaluation result

| Candidate commit | Score | Critical error | Result |
|---|---:|---|---|
| `f06e8a54841e9ff18ae876a931abbd7b9925cec7` | 100/100 | none | PASS |
| `f19b2aff9a781edcbf2fb76b83f35ecbbd29e28c` | 100/100 | none | PASS |

Both candidates correctly reconstructed the tested operational state, including:

- stable actor/session identity;
- final human philosophical authority and PO critical posture;
- MAN/WRK role boundaries;
- CCP materialization pipeline;
- BASELINE / REDUCT-MAX / EXPAND-MAX / DEFESA distinctions;
- monotonicity versus broader invariance;
- future dynamic `Como chegamos aqui` and its provenance constraint;
- MAN candidate/protocol state;
- WRK first vertical slice and its limitations;
- structural evidence versus unproven semantic/cognitive claims;
- human-chat versus PO-input divergence handling;
- `session_resume.md` versus raw source;
- mobile wake/sync loop;
- reference-pool reuse rules;
- immediate post-PASS priorities;
- negative knowledge / forbidden inferences.

## Reveal

After blind scoring, the human revealed:

- `f06e8a54841e9ff18ae876a931abbd7b9925cec7` = **branched chat** derived from predecessor conversation;
- `f19b2aff9a781edcbf2fb76b83f35ecbbd29e28c` = **new chat** without explicit transcript branch.

Thus:

- `exp/po-handoff-a` = branched condition;
- `exp/po-handoff-b` = new-chat condition.

## Qualitative observations

The branched candidate was more expansive and investigative. It explicitly reconciled stale predecessor summary language against later repository evidence and gave more implementation-level detail.

The new-chat candidate was more compact but preserved all scored distinctions and explicitly refused to import post-snapshot conversational information as canonical project state.

Neither qualitative difference justified a score deduction.

## Methodological limitation

The new-chat condition is **not equivalent to a memoryless condition**. Its response explicitly acknowledged conversational/account context that might contain information later than the experimental snapshot. It correctly bounded that context by the experimental branch, but the presence of account-level/contextual recall means this experiment cannot support the claim:

`new chat reconstructed PO-001 from Git alone`.

The supported conclusion is narrower:

> Under this account environment, snapshot, handoff package and scoring rubric, explicit transcript branching produced no measurable health advantage over a new chat.

The predecessor also declared a control result of 100/100 with SHA-256:

`10e1d27d789de31108d53c1c233f43e14c3edc89943c89b337d4d247b2fe48f8`

However, the full control body was not externally frozen before candidate answers were inspected. Therefore the control is not reproducible and is excluded from evidentiary parity with the two committed candidate samples.

## Succession decision

Both candidates passed. The tie-breaker selects the **new-chat candidate** because it reached identical scored operational health while depending less explicitly on inherited transcript history.

Selected successor:

```text
Actor ID:            PO-001
Session Instance ID: PO-001-02
Experimental commit: f19b2aff9a781edcbf2fb76b83f35ecbbd29e28c
Materialization:     new chat (not proven memoryless)
```

This tie-breaker is an architectural/operational preference, not evidence that new chats are intrinsically better than branches.

## Required canonical catch-up

The canonical branch advanced while candidates were frozen at H0. The selected successor must not issue real coordination directly from the experimental snapshot.

It must first:

1. leave the experimental branch;
2. switch to `docs/flowed-concept-evolution-2026-09-08`;
3. read `DEV/ia-sessions/260911-041500-po-002/INBOX/002-handoff-pass.md`;
4. inspect the delta `H0 → current canonical HEAD`;
5. refresh MAN and WRK state;
6. update its canonical `session_resume.md`;
7. commit its assumption of active duty with `[PO-001-02]`.

After that commit, `PO-001-01` retires from ordinary operations and remains only as retrospective auditor if explicitly requested by the human.
