# Project Genesis — Live Self-Dogfood

Status: `ACTIVE / DOGFOOD / UNVALIDATED`

## Purpose

This directory is simultaneously:

1. a live execution of Project Genesis against Project Genesis itself;
2. a reference example of how Project Genesis is expected to be used;
3. a source of implementation requirements discovered by actual use;
4. an evidence trail for changing the protocol, schemas, tool boundaries and UX;
5. the incubation surface where the viability protocol is allowed to emerge from observed use rather than being frozen before experience.

The dogfood MUST NOT assume that the current Project Genesis decomposition is correct.

## Rule of execution

We do not decompose every imaginable part up front.

We begin at the coarsest useful representation and split only when a split materially changes at least one of:

- sourcing / realization strategy;
- candidate correspondence;
- transformation strategy;
- architectural relation;
- exclusivity interpretation;
- evidence confidence;
- risk, license, cost or ownership decision.

This is the PMFN stopping principle applied to the tool itself.

## Dual-output rule

Every live step produces two outputs at the same time:

### A. Use evidence

What the tool concluded about Project Genesis.

### B. Implementation/protocol evidence

What this execution reveals that Project Genesis itself must support or change as product/protocol behavior.

A dogfood run is incomplete if it records only the analysis result and does not capture the implementation/protocol consequence.

## Creative parallel-development rule

The protocol, the implementation requirements, the usage example and the analyzed project evolve together.

```text
MANUAL / CREATIVE ATTEMPT
        ↓
LIVE USE
        ↓
OBSERVED FAILURE OR GAIN
        ↓
PROTOCOL RULE
        ↓
IMPLEMENTATION REQUIREMENT
        ↓
NEXT LIVE USE
```

No correction is accepted as merely editorial when it reflects a methodological defect. The missing or inadequate rule must be identified.

## Run structure

Each step should record, when applicable:

```text
INPUT
SCOPE
CURRENT DECISION QUESTION
CURRENT FACTORIZATION
SEARCH / EVIDENCE PROCEDURE
EVIDENCE SET
OBSERVATIONS
DECISIONAL EFFECT
ΔD(split)
POSITION
OPEN UNCERTAINTIES
NEXT FACTORIZATION DECISION
PROTOCOL RULES DISCOVERED
IMPLEMENTATION REQUIREMENTS DISCOVERED
```

No global `IDEA SCORE` or automatic GO/NO-GO is permitted.

## Live artifacts

- `001-COARSE-POSITIONING.md` — first coarse sourcing scan; proved further factorization was materially necessary.
- `002-PREMATURE-MATERIALIZATION-INCIDENT.md` — records the InitProj premature-materialization incident and the need for authorization gating.
- `003-FOREIGN-PROTOTYPE-INGEST-INITPROJ-PR2.md` — ingests useful atoms from the InitProj PR without importing its authority or topology.
- `004-VIABILITY-DISCOVERY-FIRST-PASS.md` — first explicit viability/discovery pass and first rules derived from observed use.
- `PROTOCOL-DRAFT-v0.1.md` — first emergent viability-discovery protocol consolidated from the live runs; not validated or frozen.

## Current next run

Apply `PROTOCOL-DRAFT-v0.1.md` manually to the first narrower factor:

```text
A1 — elicitation / assumptions
```

The human may first perform an unconstrained/manual version. The protocol run must then preserve the delta and turn methodological corrections into explicit protocol evolution.