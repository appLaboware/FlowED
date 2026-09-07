# BOUNDARY-CONSOLIDATED-RECORD

## 0. METADATA

- `subject_id:`
- `subject_version:`
- `protocol_version:`
- `consolidation_date:`
- `included_consultant_reports: []`
- `excluded_nonconforming_reports: []`

## 1. EXECUTIVE CONSOLIDATED BOUNDARY

## 2. INPUT REPORT QUALITY SUMMARY

## 3. CONSOLIDATION METHOD

## 4. APPLICABLE BOUNDARY CLASSES

Mark each as `APPLICABLE | NOT_APPLICABLE | PARTIAL`:

- `THEORETICAL_SCIENTIFIC_BOUNDARY:`
- `PROFESSIONAL_PRACTICE_BOUNDARY:`
- `OPERATIONAL_BOUNDARY:`
- `MARKET_SERVICE_PATTERN_BOUNDARY:`
- `IMPLEMENTATION_TOOLING_BOUNDARY:`

## 5. THEORETICAL / SCIENTIFIC BOUNDARY

When applicable.

## 6. PROFESSIONAL / PRACTICE BOUNDARY

## 7. OPERATIONAL BOUNDARY

## 8. MARKET / SERVICE-PATTERN BOUNDARY

When applicable.

## 9. IMPLEMENTATION / TOOLING BOUNDARY

When applicable.

## 10. ESTABLISHED ELEMENTS TO ADOPT / ATTRIBUTE

## 11. PARTIALLY COVERED ELEMENTS

## 12. CONFLICTING EVIDENCE

## 13. UNRESOLVED ELEMENTS

## 14. NOT FOUND IN CONSOLIDATED SCOPE

This section never means proof of global nonexistence.

## 15. CLOSEST ANTECEDENTS / PRACTICES

## 16. CONSULTANT DIVERGENCES

```yaml
divergence_id:
subject:
consultant_positions: []
source_quality_difference:
terminology_difference:
scope_difference:
actual_evidence_conflict:
resolution: RESOLVED | PARTIAL | UNRESOLVED
notes:
```

## 17. CONSOLIDATED CLAIM REGISTER

```yaml
consolidated_claim_id:
claim:
status: ESTABLISHED | STRONGLY_SUPPORTED | PARTIALLY_COVERED | CONFLICTING | ADJACENT_ONLY | UNRESOLVED | NOT_FOUND_IN_CONSOLIDATED_SCOPE
consultant_claim_refs: []
source_refs: []
support_summary:
counterevidence_summary:
uncertainty:
search_scope:
```

## 18. SOURCE DEPENDENCE / DUPLICATION ANALYSIS

## 19. ORIGINATOR INTENDED HORIZON

Trace only to the homologated Phase 01 record.

## 20. POSSIBLE GAIN VECTORS

For each:

```yaml
gain_vector_id:
origin: ORIGINATOR_EXPLICIT | BOUNDARY_DERIVED | CONDUCTOR_HYPOTHESIS | CONSULTANT_PROPOSED
originator_horizon_ref:
gain_class:
opportunity_statement:
known_boundary_refs: []
evidence_refs: []
why_it_may_matter:
possible_realization_forms: []
uncertainty:
risks: []
```

## 21. LONG-HORIZON ASSISTED BACKLOG

For each preserved item:

```yaml
backlog_item_id:
originator_horizon_ref:
gain_vector_ref:
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

This is not a sprint backlog or implementation commitment.

## 22. WHAT REMAINS FORBIDDEN TO CLAIM

## 23. HUMAN REVIEW / HOMOLOGATION

- `human_reviewed: YES | NO`
- `corrections:`
- `homologated: YES | NO`
- `statement:`

## 24. FINAL STATE

Exactly one:

```text
CONSOLIDATION_INSUFFICIENT
BOUNDARY_PARTIAL
BOUNDARY_HOMOLOGABLE
```
