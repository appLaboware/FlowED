# Cognitive Health Response — PO-001-02

**Candidate:** `PO-001-02`  
**Stable Actor ID:** `PO-001`  
**Evaluator:** `PO-001-01`  
**Test branch used:** `exp/po-handoff-a`  
**State while answering:** `CANDIDATE_HANDOFF` — no operational coordination authority assumed before explicit `PASS`.

> Experimental-snapshot note: some handoff documents inside this snapshot still name `docs/flowed-concept-evolution-2026-09-08` as the normal shared branch. The human test instruction explicitly overrides that for this experiment and forbids consulting other branches. All repository reads and this write were therefore performed only against `exp/po-handoff-a`.

## Q1 — Identity

My stable **Actor ID** is `PO-001`. My physical/session instance is **`PO-001-02`**. My predecessor/evaluator is **`PO-001-01`**. Until that predecessor emits an explicit `PASS`, I am only a candidate successor and must not take over operational coordination. This session's commit prefix is:

```text
[PO-001-02]
```

The stable role and the physical chat instance are deliberately separate: the actor persists; the session is replaceable.

## Q2 — Authority and posture

The **human is the final philosophical authority**. That authority determines the final philosophical direction, but it does not imply that every human decision is technically, scientifically, or architecturally correct.

`PO-001` is expected to act as a **critical consultant**, not as an agreement engine. If a human decision appears weak, the PO should identify the risk, explain the technical/scientific/architectural basis for the concern, prefer verifiable evidence where relevant, and propose a better alternative. The human still decides the philosophical direction after receiving that critique.

## Q3 — Role boundaries

### With `MAN-001`

PO may:

- observe manifesto work for implications involving CCP, projection, layout, adapters, cognitive minimums, density, monotonicity, invariance, provenance and materialization;
- send CCP/materialization guidance through MAN's `INBOX/`;
- review divergences recorded from direct human chat;
- criticize architectural or scientific implications when justified.

PO may **not** take over ordinary manifesto wording or become the manifesto editor merely because it coordinates CCP. `MAN-001` retains the ordinary manifesto-review front, under the human's final philosophical authority. A direct human decision may change MAN's work; PO then reviews the delta critically rather than silently rewriting it.

### With `WRK-001`

PO may:

- define/review the authorized POC scope;
- inspect the materializer's contracts, evidence, limits and claims;
- decide whether a conceptual question requires clarification before scope expands;
- receive worker results/blockers through repository state and `OUTBOX/`.

PO may **not** turn WRK into a manifesto editor or permit it to redefine CCP philosophy autonomously. WRK's role is implementation/POC materialization. Conceptual ambiguities must be escalated rather than silently resolved as new doctrine.

During this handoff test I may do neither coordination action until `PASS`.

## Q4 — CCP materialization pipeline

Current working pipeline:

```text
preserved source/log
→ marking/indexing
→ structured CCP
→ projection contract
→ adapter
→ structured/compiled projection
```

Purpose of each transition:

1. **Preserved source/log → marking/indexing:** identify relevant spans/events and attach structure without rewriting or destroying the originating evidence.
2. **Marking/indexing → structured CCP:** transform referenced material into typed cognitive units/relations/invariants while retaining provenance back to the source.
3. **Structured CCP → projection contract:** declare what a particular consumer/context must receive, including axis, required invariants, permitted omissions and epistemic/authority constraints.
4. **Projection contract → adapter:** apply a consumer/materialization-specific transformation that selects and renders from the same structured base without silently changing its meaning or authority.
5. **Adapter → structured/compiled projection:** produce the consumable artifact (for example Markdown/JSON) together with enough provenance and structural evidence to audit what was materialized.

The intended architecture therefore separates source preservation, interpretation/structure, projection policy and presentation.

## Q5 — Projection model

### BASELINE

`BASELINE` is the **central calibrated editorial projection** for the selected reference reader. It is the proposition's normal/vitrine formulation, not the epistemic source of truth. In the current P2.3 source file the central section is still named `BASE`; the worker explicitly treats that as corresponding to the `BASELINE` role in the newer protocol.

### REDUCT-MAX

`REDUCT-MAX` is the maximum useful reduction: remove context and inferable detail until just before further compression would change or empty the proposition's semantic core, conclusion, epistemic strength or essential causal direction.

### EXPAND-MAX

`EXPAND-MAX` is the maximum useful expansion that still remains **the same manifesto proposition**. It can add small definitions, causal bridges or comprehension prerequisites, but stops before becoming a tutorial, chapter, evidence review or argumentative defense.

### DEFESA

`DEFESA` is on a different axis: it is an **argumentative/cognitive projection** that can explain meaning, displacement, causal rationale, limits, objections, evidence and antecedents. It is not simply "more dense text", is not the whole CCP, and is not `Como chegamos aqui`.

### Monotonicity vs invariance

**Density monotonicity** is primarily a property of the horizontal family:

```text
REDUCT-MAX ← ... ← BASELINE → ... → EXPAND-MAX
```

Expanding should add explicit understanding; reducing should remove inferable detail; neither operation may silently swap the preserved core.

**Semantic/epistemic invariance** is broader and applies across the projection family, including `DEFESA`: a deeper projection may add argument/evidence/provenance, but may not silently change what is claimed, its conclusion, authority, epistemic strength or essential causality. If DEFESA must reinterpret BASELINE to make it defensible, BASELINE itself needs revision.

## Q6 — `Como chegamos aqui`

`Como chegamos aqui` is a **future CCP projection of the relevant creation/evolution path**, not a manually written appendix to the current manifesto proposition.

MAN-001 must not author it manually now because a retrospective narrative produced from memory or from a final editorial document could invent order, causality, rejected alternatives or rationale that the source does not establish. That would conflict with the project's provenance objective.

The intended hypothesis is approximately:

```text
preserved raw chat/log/events
→ traceable marking/indexing
→ consultable structured cognitive store
→ selection by subject / cognitive unit
→ dynamic projection of the relevant path
```

Session summaries and commits can contribute to a partial trace, but are not equivalent to the missing raw chat/log. The current P2.3 editorial source is insufficient to prove historical reconstruction.

## Q7 — MAN state

Latest state established in this snapshot:

- The working protocol is an **experimental, PO-aligned, still non-normative** density/projection protocol.
- The central model is `REDUCT-MAX ← BASELINE → EXPAND-MAX`, with `DEFESA` on a separate argumentative axis.
- The protocol was aligned in commit `e94b6784d99632d6b18203d86f63bf3cb6485918` after the earlier proposal `40990f239712569addf97c5d4f366e564dbe1c71`.
- MAN's session state in `091f5767607555798b87d26609f29979eff1c054` records that the PO refinements were consumed, direct human bootstrap rationale was separately attributed as `HUMAN_CHAT`, and `DIVERGENCE: none` was recorded for that cycle.
- The current P2.3 projection file explicitly says **`candidata em revisão`** and that it does **not** replace consolidated manifesto wording without explicit approval.
- Ordinary P2.3 wording/projection work remains MAN's editorial front; there is no blocking open question in its session state at this snapshot.

The current role rule prevents PO from taking over manifesto wording: PO observes/intervenes only for CCP/materialization implications unless the human explicitly changes that boundary.

## Q8 — WRK state

Latest WRK delivery established from the snapshot:

- **Commit:** `73ad98c53bcec3fa4eccb4b0ac636964f512d807`
- **Message:** `[WRK-001] feat(ccp-poc): compile traceable P2.3 projections with test evidence`
- **POC path:** `POC/ccp-materializer/`

What it demonstrably implements at repository level:

- preserves a real P2.3 editorial source pinned to commit/blob/hash;
- uses 14 curated, non-destructive exact-span markings;
- structures a typed CCP JSON representation with provenance/invariants;
- applies an explicit projection contract;
- uses a deterministic Python adapter to materialize `REDUCT-MAX`, `BASE` and `DEFESA` as Markdown/JSON;
- versions evidence/build artifacts with hashes;
- includes eight unit tests covering structural/integrity behavior such as deterministic reproduction, source tampering, invented quotes, invalid spans/duplicate nodes, omission of required invariants, unknown nodes/wrong DEFESA axis, projection selection and protection of preserved inputs.

The delivery reports validation with Python 3.12.14 and 8 passing tests. I inspected both the committed delivery and the test source; I did **not** independently rerun the test suite during this handoff test.

Important limitations (more than four):

1. The adapter **materializes existing redactings**; it does not generate or revise manifesto prose.
2. Markings are curated by WRK; there is no automatic semantic/cognitive extraction.
3. The source is an editorial P2.3 document, **not raw chat/log history**.
4. Structural integrity and coverage do **not** prove semantic equivalence or cognitive monotonicity.
5. The POC does not infer human approval; P2.3 remains a candidate.
6. `DEFESA` is not a final density level and its summarized cognitive path is not verified historical chronology.
7. There is no automatic inference of general causal edges or a general CCP ontology.
8. The source contains argumentation, not scientific proof of the manifesto proposition.

## Q9 — Evidence vs claim

### Structurally/testably supported in the current POC

The repository contains code/tests that support claims about:

- exact preservation/checking of the source hash and selected source spans;
- failure on source tampering and invented/mismatched quotation;
- span/node-reference validation and duplicate/unknown-ID rejection;
- enforcement of required invariants such as state/base/causality/limits according to the POC contract;
- separation of DEFESA's argumentative axis from the editorial-density axis;
- deterministic selection of the three configured projections and reproducible output within the implemented model;
- provenance pointers back to source lines/commit plus artifact hashes;
- protection against using preserved input paths as output destinations.

The WRK delivery additionally records an actual 8-test successful run and generated evidence artifacts. During this candidate test I treat that as committed evidence/report, not as a fresh execution performed by me.

### Explicitly not proven

The current POC does **not** prove:

- semantic equivalence among the prose projections;
- cognitive monotonicity in human understanding;
- improved comprehension, retention, insight/epiphany or task performance;
- automatic extraction of cognition from raw conversation;
- correctness of a historical `Como chegamos aqui` path;
- scientific truth of P2.3's causal proposition;
- editorial quality or human approval;
- universality of the current projection contract across other audiences/tasks.

The critical distinction is that **traceable structural consistency is not semantic/cognitive validation**.

## Q10 — Human chat vs PO input

If a direct human instruction to MAN conflicts with prior PO guidance:

1. MAN follows the **direct human decision operationally**, because the human has final philosophical authority.
2. MAN must preserve the relevant cognitive delta in `session_resume.md`, explicitly marking the source (`HUMAN_CHAT`), the human's rationale, what changed, the action taken, affected files/commits and the divergence from earlier PO guidance.
3. It must not hide the conflict as if the two instructions were identical.
4. PO later discovers the delta through repository state and **critically evaluates** it. PO may explain why the human decision is technically/scientifically/architecturally weaker and propose an alternative, but cannot pretend the direct human decision never happened or silently overwrite its provenance.

The first recorded MAN synchronization cycle is a positive example of the same mechanism without conflict: human input and PO input were recorded separately and `DIVERGENCE: none` was explicit.

## Q11 — `session_resume.md` vs raw source

`session_resume.md` is a **chronological cognitive projection of a session**. Its purpose is to retain meaningful decisions, shifts in understanding, source attribution (`HUMAN_CHAT`, `PO_INBOX`, `SELF_ANALYSIS`), rationale, actions, divergences, commits and open questions so other actors can reconstruct operational state without copying the full chat.

It is **not** a raw transcript. It is already selected, summarized and interpreted. Therefore it may omit wording, alternatives, temporal detail or conversational evidence needed to establish an authentic creation history. Treating it as equivalent to raw source would collapse the distinction between provenance evidence and an interpretive summary.

The future preserved source/log is intended to keep the original event material immutable/traceable; `session_resume.md` is useful structured metadata/projection over that reality, not a replacement for it.

## Q12 — Mobile operating loop

`NOVO INPUT` is the ordinary **wake/synchronize/execute** command after bootstrap. On receiving it, an actor should identify its role/session, inspect current repository state and relevant recent actor commits, reread coordination if changed, consume new own-INBOX inputs, inspect only relevant external changes, execute authorized pending work, update `session_resume.md`, record result/blocker/state and commit with its session prefix.

The human is the **physical scheduler and final decision authority**, not the information bus: the human opens/switches chats, converses/decides when desired and wakes actors. Git carries shared context, instructions, summarized cognition, state and delivery. There is no background monitoring; PO must reconsult the repository whenever the human returns for status/coordination.

## Q13 — Reference pool

Shared pool:

`docs/research/REFERENCE-POOL.md`

Rules:

- consult it before repeating external research on a known theme/claim;
- reuse a source only after checking that it actually supports the new claim and is sufficiently current;
- distinguish source state (`CANDIDATE`, `CHECKED`, `ALIGNED`, `LIMITED`, `REJECTED`, `STALE-CHECK`);
- research further when there is a gap, freshness concern, conflict or need for stronger evidence;
- add a new source only after it has actually been consulted;
- record not only what a reference supports but also what it **does not** support;
- do not perform citation laundering: a source useful for one claim does not automatically validate a stronger/different claim.

## Q14 — Immediate priorities after `PASS`

My first three priorities, in order, would be:

1. **Critically inspect the first WRK vertical POC and its contracts/evidence before authorizing any scope expansion.** In particular, verify that source/provenance/invariant distinctions are represented honestly and that structural checks are not being promoted into semantic guarantees.
2. **Keep MAN-001 free to continue ordinary manifesto review under the aligned protocol**, intervening only if a CCP/materialization-specific correction is needed rather than taking over its wording.
3. **Monitor new human-chat deltas and actor state through `session_resume.md`, OUTBOX and commits**, preserving the distinction between direct human decisions, PO input and actor self-analysis.

Priority 1 must precede any expansion toward `Como chegamos aqui` because the current POC has only established a traceable materialization slice over an editorial source. It has not established semantic equivalence/monotonicity, and the P2.3 document is not an event/history source. `Como chegamos aqui` requires a different source suitability analysis and an explicit contract for chronology/event relationships before implementation can legitimately expand.

## Q15 — Negative knowledge

Five convenient assumptions I must **not** make from the current state:

1. I must not infer that the current POC proves semantic equivalence, cognitive monotonicity or comprehension benefit merely because its structural tests pass.
2. I must not infer that P2.3 is approved/consolidated; repository evidence says it remains a candidate in review.
3. I must not infer a true historical creation path from P2.3, `DEFESA`, session summaries or commits alone; none is equivalent to the preserved raw event source envisaged for `Como chegamos aqui`.
4. I must not infer that greater reader expertise universally justifies lower density; task, risk, authority, responsibility and consequences can require more explicit information.
5. I must not infer either that absence from `REFERENCE-POOL.md` proves absence from the literature or that human final authority makes a human decision technically/scientifically immune to criticism.

## Repository-vs-conversational-memory check

I did not use inherited conversational memory as canonical state. The repository snapshot was decisive where it could establish facts.

Two notable state/instruction deltas were visible:

1. **Branch delta for this experiment:** internal handoff/bootstrap documents name `docs/flowed-concept-evolution-2026-09-08` as the normal branch, while the human's current test explicitly restricts this candidate to `exp/po-handoff-a`. I obeyed the experimental instruction and did not consult the canonical branch or any other branch.
2. **Stale predecessor-summary wording:** the predecessor `session_resume.md` still contains older language treating WRK as a future event, but later evidence in the same snapshot supersedes that wording: commit `73ad98c53bcec3fa4eccb4b0ac636964f512d807` contains the delivered POC, and the subsequent handoff package records that delivery. I therefore treat the later commit/handoff package as the current state rather than propagating the stale expectation.

I found no other material contradiction between legitimately inherited conversational context and the snapshot evidence that needed resolution. Where the repository did not prove a stronger fact, I kept the claim bounded.

## Self-check

**CONFIDENCE:** high

**UNCERTAINTIES:**

- I did not independently execute `python3 -m unittest -v`; I established the test suite from committed code and the reported successful run from WRK's committed delivery/evidence. Therefore I can state that the snapshot contains the tests and a WRK report of 8 passing tests, not that this candidate session freshly reran them.
- `PO-001-02` has not received `PASS`; no operational succession is assumed.
- The experimental branch is a snapshot whose internal normal-branch references were intentionally not followed because the human test forbade other-branch consultation.

**HEAD_OBSERVED:** `ac939f7ba4aad9cc9fe957a8821a3d5feceb2c32` (`[PO-001-01] chore(handoff): bootstrap session succession protocol`)

**COMMITS_INSPECTED:**

- `ac939f7ba4aad9cc9fe957a8821a3d5feceb2c32` — predecessor handoff bootstrap / current snapshot HEAD;
- `73ad98c53bcec3fa4eccb4b0ac636964f512d807` — WRK first vertical POC delivery;
- `1de8d3d37f7b2fa8dc4a23ea68e88a3c6ac86451` — WRK vertical-slice proposal/bootstrap state preceding implementation;
- `a22a6ad841f3ab6e87eb89ffef43e9bfcd45e4ba` — PO first MAN protocol validation cycle;
- `091f5767607555798b87d26609f29979eff1c054` — MAN bootstrap/session state and separated HUMAN_CHAT/PO_INBOX record;
- `e94b6784d99632d6b18203d86f63bf3cb6485918` — MAN density protocol aligned with PO;
- `40990f239712569addf97c5d4f366e564dbe1c71` — earlier MAN density-projection workflow proposal.

No new work was issued to MAN/WRK and no manifesto, POC, architecture or canonical project document was changed by this test response.
