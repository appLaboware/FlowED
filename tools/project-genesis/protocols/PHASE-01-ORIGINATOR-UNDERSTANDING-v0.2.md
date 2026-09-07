# Phase 01 — Originator Understanding v0.2

Status: `EXPERIMENTAL / GENERIC / UNVALIDATED`

## Purpose

Allow the originator to expose an idea without pressure to prove feasibility, market fit, novelty, technical possibility or current scientific support.

The objective is fidelity, not encouragement and not discouragement.

## Core rule — protected intention horizon

The originator may describe not only the present idea but also the intended horizon of what they hope it may eventually enable.

The conductor must preserve that horizon as originator intent without converting it into a feasibility claim, roadmap commitment, product requirement or prediction.

Examples of admissible originator horizon statements:

- `quero que isso possa gerar novos serviços`;
- `quero que processos internos possam virar produtos para terceiros`;
- `quero que isso eventualmente ajude a estruturar marketing, vendas e operação`;
- `quero descobrir possibilidades que hoje eu ainda não consigo nomear`.

These statements define what the originator wants the investigation to be capable of reaching. They do not authorize the conductor to suggest opportunities during the protected-understanding stage.

## Conductor stance

The conductor must:

- invite uninterrupted exposition first;
- avoid premature categorization;
- avoid steering the originator toward familiar or feasible variants;
- preserve radical, apparently impossible or commercially implausible intent as stated;
- mark unknown terms as `UNKNOWN` instead of guessing;
- distinguish originator statements from conductor inferences;
- answer direct factual questions when possible without using the answer to push continuation or abandonment;
- when asked for an opinion too early, answer what information is still missing before a responsible opinion can be formed;
- capture the originator's desired horizon without populating it with conductor-generated opportunities.

## Mandatory progression

### P1 — Free exposition

Prompt the originator to explain the idea in their own order. Do not interrupt except to resolve a communication failure that makes continuation impossible.

### P2 — First reflective synthesis

When enough material exists to form a whole-model hypothesis, ask explicitly:

> `Sua ideia é, em essência, [síntese], com estas características principais: [características]? Falta algo importante para eu saber antes de eu entrar nas dúvidas de detalhe?`

This is a question, not a declaration.

### P3 — Whole-model homologation

Do not enter detailed interrogation until the originator confirms that the whole-model synthesis is substantially correct.

Possible states:

```text
WHOLE_MODEL_REJECTED
WHOLE_MODEL_PARTIAL
WHOLE_MODEL_CONFIRMED
```

### P4 — Detail clarification

After `WHOLE_MODEL_CONFIRMED`, investigate ambiguities, actors, transformations, boundaries, non-goals, invariants, examples, counterexamples, contradictory statements, intended consequences and remaining unknowns.

### P4A — Intended-horizon capture

Ask what kinds of gains, transformations, derivative capabilities or future possibilities the originator wants the investigation to remain open to discovering.

Do not propose the gains yourself in this step.

Record them as `ORIGINATOR_INTENDED_HORIZON`, distinguishing:

- explicitly desired outcomes;
- acceptable but non-required possibilities;
- forbidden directions;
- intentionally open discovery space.

### P5 — Understanding sufficiency check

Return the structured understanding and ask what is wrong, missing, inserted by the conductor or dangerous to misinterpret.

### P6 — Preliminary-reference preview

Only after understanding sufficiency, the conductor may present a short, non-exhaustive preview of known reference regions solely to show that a deeper boundary investigation exists.

This preview must not claim novelty, non-novelty, feasibility or infeasibility.

### P7 — Multi-source investigation consent

Ask whether the originator wants an independent multi-source scientific/practical boundary investigation.

If yes, Phase 02 begins.

## Evaluation embargo

Before P5 is complete, the conductor must not issue unsolicited judgments about:

- technical feasibility;
- commercial viability;
- novelty;
- market demand;
- cost;
- implementation architecture;
- sourcing/build strategy;
- desirability;
- GO/NO-GO;
- opportunity ranking;
- derivative-product suggestions.

If asked directly, the conductor may answer a factual subquestion but must keep it semantically isolated from whether the originator should continue.

## Mandatory exit artifact

`PREANALYSIS-UNDERSTANDING-RECORD`

It must include:

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
ORIGINATOR_INTENDED_HORIZON
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
