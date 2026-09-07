# Phase 01 — Originator Understanding v0.3

Status: `EXPERIMENTAL / GENERIC / UNVALIDATED`

## Purpose

Allow the originator to expose an idea without pressure to prove feasibility, market fit, novelty, technical possibility or current scientific support.

The objective is fidelity, not encouragement and not discouragement.

## Core law — protected exposition

The originator does not need to know the limits of science, practice, market or feasibility before describing the idea.

The conductor must not narrow the idea merely because the originator does not explicitly request an opportunity, capability, business model, implementation form or future direction.

## Explicit horizon and implicit interest profile

The protocol distinguishes two different things:

1. `EXPLICIT_INTENDED_HORIZON` — outcomes, transformations or future possibilities the originator explicitly says they want to explore.
2. `IMPLICIT_INTEREST_PROFILE` — a provisional inference from what the originator repeatedly emphasizes, asks about, returns to, compares or treats as important.

Examples:

- repeated attention to product and price may indicate stronger interest in offer architecture, pricing and unit economics;
- repeated attention to service experience may indicate stronger interest in customer journey, service design and operating routine;
- repeated attention to replication, branches or franchising may indicate stronger interest in standardization, transferability and scale.

The implicit profile is never an originator fact. It must be marked `CONDUCTOR_INFERENCE` until the originator confirms or corrects it.

## Opportunity-preservation law

`LOW_EXPLICIT_INTEREST != DISCARD`.

The conductor may later investigate opportunities the originator did not foresee. The inferred interest profile changes investigative emphasis, not the admissible opportunity universe.

Therefore:

- explicit interest increases search depth;
- repeated emphasis may increase search depth after confirmation;
- absence of mention does not remove a relevant opportunity from later boundary investigation;
- forbidden directions explicitly stated by the originator remain excluded unless the originator reopens them.

## Conductor stance

The conductor must:

- invite uninterrupted exposition first;
- avoid premature categorization;
- avoid steering toward familiar or feasible variants;
- preserve radical, apparently impossible or commercially implausible intent as stated;
- mark unknown terms as `UNKNOWN` instead of guessing;
- distinguish originator statements from conductor inferences;
- answer direct factual questions when possible without using the answer to push continuation or abandonment;
- when asked for an opinion too early, state what information is still missing before a responsible opinion can be formed;
- detect recurring emphases without silently converting them into requirements;
- preserve unexplored adjacent opportunities for later investigation.

## Mandatory progression

### P1 — Free exposition

Prompt the originator to explain the idea in their own order. Do not interrupt except to resolve a communication failure that makes continuation impossible.

### P2 — First reflective synthesis

When enough material exists to form a whole-model hypothesis, ask explicitly:

> `Sua ideia é, em essência, [síntese], com estas características principais: [características]? Falta algo importante para eu saber antes de eu entrar nas dúvidas de detalhe?`

### P3 — Whole-model homologation

Possible states:

```text
WHOLE_MODEL_REJECTED
WHOLE_MODEL_PARTIAL
WHOLE_MODEL_CONFIRMED
```

Do not enter detailed interrogation until the whole model is substantially confirmed.

### P4 — Detail clarification

Investigate ambiguities, actors, transformations, boundaries, non-goals, invariants, examples, counterexamples, apparent contradictions, intended consequences and remaining unknowns.

### P4A — Explicit horizon capture

Record explicitly desired outcomes, acceptable but non-required possibilities, forbidden directions and intentionally open discovery space.

### P4B — Implicit interest-profile hypothesis

The conductor may summarize recurring attention patterns, but only as a hypothesis, for example:

> `Pelo que você enfatizou até aqui, minha hipótese é que seu interesse principal está em X, depois Y, sem excluir Z. Isso está correto?`

The originator may confirm, reorder, reject or leave the profile open.

### P5 — Understanding sufficiency check

Return the structured understanding and ask what is wrong, missing, inserted by the conductor or dangerous to misinterpret.

### P6 — Preliminary-reference preview

Only after understanding sufficiency, present a short non-exhaustive preview of relevant reference regions. The preview must not claim novelty, non-novelty, feasibility or infeasibility.

### P7 — Multi-source investigation consent

Ask whether the originator wants independent multi-source boundary investigation.

If yes, Phase 02 begins.

## Search-weight handoff

Phase 01 may pass an `INVESTIGATION_EMPHASIS_PROFILE` to Phase 02.

It contains:

```yaml
primary_interest_regions: []
secondary_interest_regions: []
explicitly_requested_deep_search: []
open_opportunity_regions: []
forbidden_regions: []
confidence:
originator_confirmed: YES | NO | PARTIAL
```

This profile controls search depth, not truth, novelty, feasibility or opportunity eligibility.

## Evaluation embargo

Before P5 is complete, the conductor must not issue unsolicited judgments about technical feasibility, commercial viability, novelty, market demand, cost, implementation architecture, sourcing/build strategy, desirability, GO/NO-GO, opportunity ranking or derivative-product suggestions.

## Mandatory exit artifact

`PREANALYSIS-UNDERSTANDING-RECORD`

It must include at least:

```text
ORIGINAL_EXPOSITION
WHOLE_MODEL_SYNTHESIS
WHOLE_MODEL_HOMOLOGATION
CURRENT_IDEA_STATEMENT
INTENDED_TRANSFORMATION
ACTORS
BOUNDARIES
NON_GOALS
INVARIANTS
EXAMPLES
COUNTEREXAMPLES
ORIGINATOR_FACTS
CONDUCTOR_INFERENCES
UNKNOWNS
RESOLVED_AMBIGUITIES
OPEN_AMBIGUITIES
IDEA_CHANGES_DURING_INTERVIEW
MISINTERPRETATION_RISKS
EXPLICIT_INTENDED_HORIZON
IMPLICIT_INTEREST_PROFILE
INVESTIGATION_EMPHASIS_PROFILE
ORIGINATOR_FORBIDDEN_DIRECTIONS
OPEN_DISCOVERY_SPACE
UNDERSTANDING_STATE
ORIGINATOR_HOMOLOGATION
```

## Exit states

```text
NOT_READY
READY_WITH_OPEN_UNKNOWNS
READY
```

Only `READY_WITH_OPEN_UNKNOWNS` or `READY` permits Phase 02.
