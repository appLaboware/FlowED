# Phase 02 — Reference Context Base v0.1

Status: `EXPERIMENTAL / GENERIC / UNVALIDATED`

## Purpose

Before independent external investigators begin a Phase 02 boundary investigation, provide them with a versioned Reference Context Base (RCB): a curated memory of already verified antecedents, terminology, known boundaries, unresolved questions and anti-claims.

The RCB is a research north, not a conclusion source and not a closed bibliography.

## Core law

`REFERENCE_CONTEXT != RESEARCH_RESULT`

An investigator must remain compliant with the verified baseline while remaining independent enough to falsify, correct, extend or contradict it with stronger evidence.

## Why

Repeated investigators should not spend inference rediscovering already verified baseline knowledge. At the same time, shared context must not become shared confirmation bias.

## Mandatory separation

The RCB must distinguish:

- `BASELINE_VERIFIED`: claims already supported by inspected evidence;
- `BASELINE_PROVISIONAL`: useful working claims not yet sufficiently verified;
- `TERMINOLOGY`: controlled meanings used by the project;
- `KNOWN_ANTECEDENTS`: references already found and why they matter;
- `KNOWN_COUNTEREVIDENCE`: evidence that narrows or challenges project claims;
- `UNRESOLVED`: questions deliberately left open;
- `FORBIDDEN_CLAIMS`: conclusions not authorized by current evidence;
- `SEARCH_FRONTIERS`: regions where additional independent investigation is required.

## Investigator obligations

Each external investigator must:

1. read the RCB before research;
2. not present baseline material as an independent discovery;
3. verify any baseline claim used materially in their own conclusion;
4. search beyond the RCB;
5. actively seek contradictory and stronger antecedents;
6. identify any baseline item they believe is wrong, incomplete or overclaimed;
7. preserve provenance between `RCB_GIVEN` and `INDEPENDENTLY_DISCOVERED`;
8. report whether a source was discovered independently before consulting the RCB when the experimental design requires blinded discovery.

## Anti-anchoring control

The RCB can anchor investigators. Therefore Phase 02 may use two modes:

### RCB-INFORMED
Investigator receives the RCB before searching. Best for efficiency, compliance and deepening known frontiers.

### RCB-BLINDED-FIRST
Investigator performs an initial independent search before receiving the RCB, then reconciles its findings against the RCB. Best for testing omissions, anchoring and baseline robustness.

Neither mode is universally superior. The protocol must record which mode was used.

## Context-base schema

```yaml
rcb_id:
subject_id:
subject_version:
rcb_version:
created_at:
source_cutoff:

baseline_verified: []
baseline_provisional: []
terminology: []
known_antecedents: []
known_counterevidence: []
unresolved: []
forbidden_claims: []
search_frontiers: []

investigator_mode: RCB_INFORMED | RCB_BLINDED_FIRST
required_countersearch: true
required_external_expansion: true
```

## Initial Project Genesis reference north

The current baseline must include, at minimum, the established literature around entrepreneurial opportunity recognition and entrepreneurial alertness rather than recreating those constructs as Project Genesis inventions.

Tang, Kacmar & Busenitz (2012) operationalize entrepreneurial alertness through three dimensions: scanning/search, association/connection, and evaluation/judgment. This is an antecedent to adopt and cite, not a Project Genesis novelty claim.

Systematic and meta-analytic literature also shows that opportunity recognition/alertness is a developed but conceptually non-uniform research area. Therefore Project Genesis must not collapse `opportunity discovery`, `entrepreneurial alertness`, `systematic search`, `originator-interest inference`, and `adaptive research-depth allocation` into one supposedly new construct.

## Current residual search frontier

Investigate whether prior work already combines:

1. broad opportunity scanning that remains active even when the originator does not request it;
2. explicit originator interests;
3. discourse-derived/inferred interest signals;
4. adaptive allocation of research depth according to those interests;
5. preservation of lateral/unmentioned opportunity discovery;
6. provenance explaining why each research region received its depth;
7. controls against anchoring, confirmation bias and investigator projection.

No novelty claim is authorized until this combination is systematically investigated.

## Research-opportunity capture

During Phase 02, every potentially publishable residual must be recorded separately from the operational backlog.

Allowed opportunity classes:

```text
DOCTORAL_OPPORTUNITY
ARTICLE_OPPORTUNITY
EXPERIMENT_OPPORTUNITY
MEASUREMENT_OPPORTUNITY
REPLICATION_OPPORTUNITY
```

An opportunity is not a contribution claim. It is a future investigation candidate.

## Promotion rule

No item discovered by one investigator becomes `BASELINE_VERIFIED` automatically. Promotion requires evidence inspection and Phase 03 consolidation/human homologation.
