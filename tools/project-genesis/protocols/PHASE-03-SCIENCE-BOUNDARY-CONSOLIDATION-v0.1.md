# Phase 03 — Science-Boundary Consolidation v0.1

Status: `EXPERIMENTAL / GENERIC / UNVALIDATED`

## Goal

Consolidate multiple independent Phase 02 reports into one normalized scientific/practical boundary record without majority voting and without erasing divergence.

## Entry gate

Required:

- homologated Phase 01 understanding record;
- at least two independent Phase 02 reports, unless the originator explicitly accepts a single-source consolidation;
- every included report must pass the Phase 02 hard-validation summary or be explicitly marked `NON_CONFORMING` and excluded from factual authority.

## Consolidation method

For every material proposition:

1. identify all consultant claims that address the proposition;
2. normalize terminology without changing meaning;
3. map supporting sources and source-verification states;
4. detect duplicated/copy-derived evidence;
5. separate convergence from shared-source dependence;
6. preserve contradictions;
7. privilege evidence quality over consultant count;
8. produce a consolidated status and uncertainty statement;
9. trace the conclusion back to consultant report IDs and source IDs.

## No-majority-vote law

Three consultants repeating one weak or copied source do not outweigh one consultant presenting stronger primary evidence.

`CONSENSUS_COUNT != EVIDENCE_STRENGTH`.

## Consolidated statuses

```text
ESTABLISHED
STRONGLY_SUPPORTED
PARTIALLY_COVERED
CONFLICTING
ADJACENT_ONLY
UNRESOLVED
NOT_FOUND_IN_CONSOLIDATED_SCOPE
```

`NOT_FOUND_IN_CONSOLIDATED_SCOPE` never means global nonexistence.

## Mandatory dual boundary

The output must separately state:

```text
THEORETICAL_BOUNDARY
APPLICATION_BOUNDARY
```

A concept may be theoretically established while lacking mature implementation, or be widely implemented without a mature formal theory.

## Required provenance

Every consolidated claim must include:

```yaml
consolidated_claim_id:
claim:
status:
consultant_claim_refs: []
source_refs: []
support_summary:
counterevidence_summary:
uncertainty:
search_scope:
```

## Exit artifact naming

```text
<subject-slug>__SB-CONSOLIDATED__<YYYYMMDD>__v<NN>.md
```

Example:

```text
project-genesis__SB-CONSOLIDATED__20260907__v01.md
```

## Exit gate

The consolidated record must answer, without novelty verdict:

1. What is already established conceptually?
2. What methods/formalizations are already established?
3. What is empirically supported?
4. What is already implemented in practice?
5. What is only partially covered?
6. What remains unresolved under the search scope?
7. Where do consultants disagree and why?
8. Which claims lack sufficient evidence?
9. What must be adopted/attributed in all downstream work?
10. What questions are now admissible for Phase 04 investigation?

## Output state

Exactly one:

```text
CONSOLIDATION_INSUFFICIENT
SCIENCE_BOUNDARY_PARTIAL
SCIENCE_BOUNDARY_HOMOLOGABLE
```

Only `SCIENCE_BOUNDARY_HOMOLOGABLE`, followed by human review, authorizes Phase 04.