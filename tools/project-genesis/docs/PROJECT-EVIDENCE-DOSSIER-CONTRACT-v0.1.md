# Project Genesis — Project Evidence Dossier Contract

Status: `INCUBATION / DOGFOODING`

## Purpose

Define the minimum evidence package produced by the discovery/pre-consultation stage before naming, repository materialization or human specialist review.

## Principle

> **Not a verdict. A position.**

The dossier must characterize where a proposal stands under the investigated scope and evidence set. It must never collapse the result into an `IDEA SCORE` or imply probability of success.

## Human-readable dossier

Recommended projection:

```text
01_ORIGINAL_IDEA.md
02_INTERVIEW_FACTS.md
03_PROBLEM_MODEL.md
04_CAPABILITY_MAP.md
05_EXISTING_SOLUTIONS.md
06_REUSE_PROFILE.md
07_EXCLUSIVITY_PROFILE.md
08_EVIDENCE_PROFILE.md
09_OPEN_ASSUMPTIONS.md
10_IDEA_EVOLUTION.md
11_HUMAN_ALIGNMENT.md
12_CONSULTANT_BRIEF.md
```

The exact filenames are projections, not semantic authority. A machine-readable canonical representation may generate them.

## Position profile

The profile must keep independent dimensions separate.

```text
P   = observed pertinence
EC  = existing coverage
XC  = conceptual exclusivity
XA  = architectural exclusivity
XE  = execution exclusivity
FR  = residual factorization
EM  = evidence maturity
RC  = research/search coverage
```

No aggregate final grade is required or recommended.

Example fingerprint:

```text
P78 · EC64 · XC34 · XA87 · XE76 · FR18 · EM62 · RC74
```

The fingerprint is descriptive, not prescriptive.

## Reuse / realization profile

Realization must not be reduced prematurely to a single ordinal ladder. The dossier should represent at least:

```text
provenance:
  existing | modified | invented | unknown

transformation:
  none | configure | extend | adapt | unknown

architecture:
  direct | compose | reconfigure | unknown

source:
  OSS | COTS | internal | outsourced | service | standard | unknown
```

This permits architectural composition to be represented independently from component provenance.

## Residual Factorization

`FR` is the portion of the required solution whose realization still requires owned factorization under the investigated evidence and admissibility constraints.

`FR` does **not** mean world novelty.

A high or low FR must not be interpreted as high or low innovation value.

## Evidence profile

Every substantive claim must be linked to evidence metadata where applicable:

- source;
- source type;
- collection date;
- recency;
- quality/reliability assessment;
- independence from other sources;
- search coverage;
- confidence;
- counterevidence;
- unresolved uncertainty.

An exclusivity observation without research coverage and evidence confidence is incomplete.

## Click-through rule

Every displayed metric or categorical conclusion should be explainable by drilling down to:

```text
CLAIM
  ↓
DERIVATION / CRITERIA
  ↓
EVIDENCE
  ↓
COUNTEREVIDENCE
  ↓
UNCERTAINTY
  ↓
PROVENANCE
```

The system must not expose an unexplained number as if it were intrinsic truth.

## Temporal identity

An assessment is a snapshot:

```text
assessment_id
protocol_version
assessment_date
proposal_version
evidence_snapshot
search_scope
position_profile
```

The same proposal may legitimately have different profiles at different moments because markets, software, standards, research and project boundaries change.

## Candidate and consultant projections

The candidate projection should emphasize understanding, evidence, alternatives and unresolved choices.

The consultant projection should emphasize:

- what no longer needs to be rediscovered;
- where evidence is strongest;
- where evidence is weak;
- what changed during the dialogue;
- what decisions remain open;
- what requires human expertise.

Both projections must derive from the same canonical evidence graph/package.

## Prohibited interpretations

The dossier must not claim, without separately validated evidence:

- probability of commercial success;
- patentability;
- legal freedom to operate;
- proven world novelty;
- scientific validation of the protocol itself;
- mandatory GO/NO-GO decision.
