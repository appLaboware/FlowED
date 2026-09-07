# Project Genesis — Live Self-Dogfood

Status: `ACTIVE / DOGFOOD / UNVALIDATED`

## Purpose

This directory is simultaneously:

1. a live execution of Project Genesis against Project Genesis itself;
2. a reference example of how Project Genesis is expected to be used;
3. a source of implementation requirements discovered by actual use;
4. an evidence trail for changing the protocol, schemas, tool boundaries and UX.

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

### B. Implementation evidence

What this execution reveals that Project Genesis itself must support as product/protocol behavior.

A dogfood run is incomplete if it records only the analysis result and does not capture the implementation consequence.

## Run structure

Each step should record, when applicable:

```text
INPUT
SCOPE
CURRENT FACTORIZATION
SEARCH / EVIDENCE PROCEDURE
EVIDENCE SET
OBSERVATIONS
DECISIONAL EFFECT
ΔD(split)
POSITION
OPEN UNCERTAINTIES
NEXT FACTORIZATION DECISION
IMPLEMENTATION REQUIREMENTS DISCOVERED
```

No global `IDEA SCORE` or automatic GO/NO-GO is permitted.

## Current live run

`001-COARSE-POSITIONING.md`

The first run asks only whether Project Genesis can be treated as one sourcing unit or must be decomposed further.
