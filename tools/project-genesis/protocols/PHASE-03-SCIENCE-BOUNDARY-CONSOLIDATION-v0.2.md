# Phase 03 — Science / Practice Boundary Consolidation v0.2

Status: `EXPERIMENTAL / GENERIC / UNVALIDATED`

## Goal

Consolidate multiple independent Phase 02 reports into one normalized scientific/practical boundary record without majority voting and without erasing divergence.

The output must also expose evidence-backed **gain vectors** that become a long-horizon assisted backlog. These are not commitments, roadmap items or recommendations to implement. They are structured possibilities that emerge only after the known boundary has been consolidated.

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

## Boundary classes

The protocol is domain-neutral. `SCIENCE` is not mandatory when the investigated domain is primarily operational, commercial, organizational, artisanal or service-oriented.

The consolidated record must expose only the boundary classes applicable to the case, while always distinguishing evidence type:

```text
THEORETICAL / SCIENTIFIC BOUNDARY   — when applicable
PROFESSIONAL / PRACTICE BOUNDARY
OPERATIONAL BOUNDARY
MARKET / SERVICE-PATTERN BOUNDARY   — when applicable
IMPLEMENTATION / TOOLING BOUNDARY   — when applicable
```

For a furniture-service case, for example, professional practice, commercial operation, service design, CRM, lead management, customer journey and marketing practice may carry more authority than academic literature for some questions.

## Gain-vector extraction

Only after the boundary is consolidated may the conductor derive possible gains by comparing:

```text
ORIGINATOR_INTENDED_HORIZON
        ×
CONSOLIDATED CURRENT BOUNDARY
        ↓
POSSIBLE GAIN VECTORS
```

A gain vector is a traceable possibility for improvement, extension, differentiation, reuse, productization, service derivation or capability development.

Examples of gain classes:

```text
EFFICIENCY_GAIN
QUALITY_GAIN
CUSTOMER_EXPERIENCE_GAIN
COMMERCIAL_GAIN
MARKETING_GAIN
OPERATIONAL_GAIN
KNOWLEDGE_GAIN
AUTOMATION_GAIN
REUSE_GAIN
PRODUCTIZATION_GAIN
SERVICE_DERIVATION_GAIN
DATA_ASSET_GAIN
PLATFORMIZATION_GAIN
RISK_REDUCTION_GAIN
```

The list is extensible.

## Long-horizon assisted backlog

Validated gain vectors may enter a `LONG-HORIZON-BACKLOG`.

This backlog is not a sprint backlog and is not an implementation commitment.

Each item must include:

```yaml
backlog_item_id:
originator_horizon_ref:
gain_class:
opportunity_statement:
known_boundary_refs: []
evidence_refs: []
why_it_may_matter:
possible_realization_forms: []
uncertainty:
dependencies: []
risks: []
status: OBSERVED | HYPOTHESIS | EVIDENCE_SUPPORTED | REJECTED | DEFERRED
human_interest: UNKNOWN | LOW | MEDIUM | HIGH
```

`possible_realization_forms` may include, without forcing any one form:

```text
PROCESS
SERVICE
CONSULTING
METHOD
CONTENT
TRAINING
CATALOG
DIGITAL_PRODUCT
SOFTWARE
SAAS
INTEGRATION
DATA_PRODUCT
PARTNERSHIP
OTHER
```

## Anti-contamination rule

The conductor must not back-project Phase 03 gain vectors into Phase 01 as though the originator originally requested them.

Every gain vector must be marked as either:

```text
ORIGINATOR_EXPLICIT
BOUNDARY_DERIVED
CONDUCTOR_HYPOTHESIS
CONSULTANT_PROPOSED
```

This preserves genealogy and prevents later opportunities from rewriting the original idea.

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
<subject-slug>__BOUNDARY-CONSOLIDATED__<YYYYMMDD>__v<NN>.md
```

Example:

```text
project-genesis__BOUNDARY-CONSOLIDATED__20260907__v01.md
```

## Exit gate

The consolidated record must answer, without novelty verdict:

1. What is already established conceptually, when theory applies?
2. What methods/formalizations are established?
3. What is empirically supported?
4. What is established professional or operational practice?
5. What is already implemented in practice/tools/services?
6. What is only partially covered?
7. What remains unresolved under the search scope?
8. Where do consultants disagree and why?
9. Which claims lack sufficient evidence?
10. What must be adopted/attributed in all downstream work?
11. Which possible gain vectors are visible relative to the originator's intended horizon?
12. Which of those vectors deserve preservation in the long-horizon backlog?

## Output state

Exactly one:

```text
CONSOLIDATION_INSUFFICIENT
BOUNDARY_PARTIAL
BOUNDARY_HOMOLOGABLE
```

Only `BOUNDARY_HOMOLOGABLE`, followed by human review, permits the next downstream investigation.
