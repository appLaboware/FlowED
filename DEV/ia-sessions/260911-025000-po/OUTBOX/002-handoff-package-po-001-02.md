# HANDOFF PACKAGE — PO-001-01 → PO-001-02

**Actor continuity:** `PO-001`
**Predecessor:** `PO-001-01`
**Successor candidate:** `PO-001-02`
**Repository:** `appLaboware/FlowED`
**Branch:** `docs/flowed-concept-evolution-2026-09-08`
**Snapshot observed before this package:** `73ad98c53bcec3fa4eccb4b0ac636964f512d807`

## 1. Mission of PO-001

Coordinate the two AI fronts and act as critical consultant to the human:

- `MAN-001`: manifesto review and human-facing cognitive projection experiments;
- `WRK-001`: executable CCP materializer POC.

The human is final philosophical authority, but PO must criticize technically/scientifically/architecturally weak decisions rather than agree automatically.

## 2. Working architecture

```text
preserved source/log
→ marking/indexing
→ structured CCP
→ projection contract
→ adapter
→ structured/compiled projection
```

Important concepts:

- cognitive primacy does not imply visual primacy;
- mandatory cognitive minimum depends on consumer/task/risk/authority/context;
- microprojection / cognitive density zoom;
- semantic/epistemic invariance across projections;
- monotonicity primarily on the density axis;
- human and AI adapters;
- `Como chegamos aqui` as future dynamic projection from preserved raw sources, not manual retrospective storytelling.

## 3. MAN front

Current editorial model:

```text
REDUCT-MAX ← ... ← BASELINE → ... → EXPAND-MAX
                         │
                         ↓
                      DEFESA
```

Key distinctions:

- `BASELINE` is the calibrated central editorial projection, not the epistemic source;
- density monotonicity applies mainly horizontally;
- invariance applies across the whole projection family;
- `DEFESA` is an argumentative projection of CCP, not the entire CCP;
- an optional micro-CCP scaffold may precede BASELINE during authoring;
- `Como chegamos aqui` must not be manually reconstructed in current MAN work;
- expertise→density is only a local manifesto heuristic, not a universal CCP rule.

P2.3 remains a candidate unless a later commit says otherwise. Read MAN session state and latest commits before assuming status.

## 4. WRK front — latest observed delivery

Latest observed commit at handoff preparation:

`73ad98c53bcec3fa4eccb4b0ac636964f512d807`

Message:

`[WRK-001] feat(ccp-poc): compile traceable P2.3 projections with test evidence`

Worker reports first vertical POC at:

`POC/ccp-materializer/`

Reported pipeline: preserved real source → 14 curated non-destructive markings → typed CCP JSON → explicit projection contract → adapter → REDUCT-MAX / BASE / DEFESA outputs with provenance.

Reported validation: Python 3.12.14, 8 tests passing, offline/std-lib execution.

Critical limits explicitly reported by WRK and not to be silently upgraded into stronger claims:

- current adapter materializes existing redactings; it does not generate or revise manifesto text;
- markings are curated, not automatic semantic extraction;
- structural integrity/coverage do **not** prove semantic equivalence or cognitive monotonicity;
- source is an editorial P2.3 document, not raw chat/log;
- approval state is not inferred;
- DEFESA is not final density level and its summarized cognitive path is not historical chronology;
- `Como chegamos aqui` needs an appropriate event/history source and separate contract before scope expands.

A successor must inspect the commit and current branch rather than rely only on this summary.

## 5. Communication and provenance model

- Human talks directly with each ChatGPT session.
- PO → MAN/WRK via each actor's `INBOX/`.
- MAN/WRK → PO via `OUTBOX/`, commits and session state.
- Each actor keeps a chronological cognitive `session_resume.md`.
- Meaningful direct human input is marked `HUMAN_CHAT`; PO instructions may be `PO_INBOX`; actor reasoning may be `SELF_ANALYSIS`.
- Divergence between human direction and PO guidance must be recorded. Human decision prevails operationally, but PO later evaluates it critically.
- `NOVO INPUT` is the minimal ordinary wake/sync command after bootstrap.

## 6. Scientific references

Shared pool:

`docs/research/REFERENCE-POOL.md`

Check before new research. Reuse only when the source truly supports the new claim and is sufficiently current. Add newly consulted useful references. Avoid citation laundering.

## 7. Session identity change

From this handoff onward, distinguish stable actor from physical session:

```text
Actor ID: PO-001
predecessor instance: PO-001-01
successor instance:   PO-001-02
```

New commits should use Session Instance ID in the prefix. Existing `[PO-001]`, `[MAN-001]`, `[WRK-001]` commits are historical pre-session-prefix records.

## 8. Immediate priorities for successor after PASS

1. inspect and critically evaluate the first WRK vertical POC, especially whether its contracts preserve the intended distinctions without overclaiming semantic guarantees;
2. keep MAN free to continue ordinary manifesto work unless a CCP-specific correction is needed;
3. monitor new human-chat deltas through actor session resumes and commits;
4. continue refining the mobile/multi-session protocol from observed evidence rather than prematurely PR-ing InitProj;
5. do not authorize the next `Como chegamos aqui` implementation merely because WRK named it as next target — first assess source suitability and contract.

## 9. Negative knowledge / do-not-assume

Do not assume:

- ChatGPT memory is the canonical project state;
- a summary equals raw source;
- a commit author identity distinguishes ChatGPT sessions;
- EXPAND/REDUCT are separate truths;
- more experienced consumers always need less information;
- current POC proves semantic equivalence, comprehension benefit or monotonicity;
- current P2.3 source can establish the real historical path of creation;
- `DEFESA` equals `Como chegamos aqui`;
- absence of a reference from the pool proves absence in literature;
- human authority means human decisions are beyond criticism.

## 10. Transition state

`PO-001-01` remains evaluator until the successor answers the cognitive health test and receives explicit `PASS`.

The successor must not start coordinating MAN/WRK before that verdict.
