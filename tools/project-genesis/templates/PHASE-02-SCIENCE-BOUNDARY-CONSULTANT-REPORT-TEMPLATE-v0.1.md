# SCIENCE-BOUNDARY-CONSULTANT-REPORT

## 0. METADATA

- `subject_id:`
- `subject_version:`
- `consultant_id:`
- `protocol_version:`
- `run_date:`
- `independent_run_confirmed: YES | NO`
- `external_reports_seen: YES | NO`

## 1. EXECUTIVE BOUNDARY SUMMARY

## 2. SEARCH STRATEGY

## 3. SEARCH SCOPE AND LIMITATIONS

## 4. CONCEPTUAL PRIOR-ART MAP

## 5. METHOD / FORMALIZATION MAP

## 6. EMPIRICAL-EVIDENCE MAP

## 7. APPLICATION / IMPLEMENTATION MAP

## 8. CLOSEST ANTECEDENTS

## 9. ESTABLISHED ELEMENTS THAT MUST BE ADOPTED / ATTRIBUTED

## 10. PARTIALLY COVERED ELEMENTS

## 11. UNRESOLVED ELEMENTS

## 12. COUNTEREVIDENCE / ANTITHESES

## 13. THEORETICAL BOUNDARY

## 14. APPLICATION BOUNDARY

## 15. POSSIBLE RESIDUAL QUESTIONS — NOT NOVELTY CLAIMS

## 16. REQUIRED SOURCE REGISTER

For every material source create one block:

```yaml
source_id:
canonical_reference:
title:
authors_or_institution:
year:
venue_or_publisher:
doi_or_canonical_url:
identity_verified: YES | NO
content_inspected: YES | NO
claim_support_verified: YES | NO
verification_notes:
```

## 17. REQUIRED CLAIM REGISTER

For every material claim create one block:

```yaml
claim_id:
claim:
claim_type: CONCEPT | METHOD | EMPIRICAL_RESULT | IMPLEMENTATION | STANDARD | ADJACENT
coverage: KNOWN_ESTABLISHED | KNOWN_PARTIAL | ADJACENT | CONFLICTING_EVIDENCE | UNRESOLVED | NOT_FOUND_IN_SCOPE
evidence_state: DISCOVERED | IDENTITY_VERIFIED | CLAIM_VERIFIED | CONTRADICTED | UNRESOLVED
source_ids: []
exact_support:
what_source_does_not_establish:
counterevidence:
uncertainty:
relevance_to_subject:
```

## 18. CLAIM → EVIDENCE → COUNTEREVIDENCE → UNCERTAINTY TRACE

## 19. COVERAGE / CONFIDENCE COMMENTARY

Do not produce a single global score.

## 20. RECOMMENDED NEXT SEARCHES

## 21. HARD VALIDATION SUMMARY

Fill all fields:

```yaml
all_material_claims_have_source_ids: YES | NO
all_material_sources_identity_verified: YES | NO
all_claim_verified_items_content_checked: YES | NO
unsupported_claims_marked_unresolved: YES | NO
not_found_treated_as_nonexistence: YES | NO
novelty_verdict_issued: YES | NO
commercial_verdict_issued: YES | NO
build_abandon_verdict_issued: YES | NO
independent_run_preserved: YES | NO
```

A report with any of the following is NON-CONFORMING:

```text
all_material_claims_have_source_ids = NO
unsupported_claims_marked_unresolved = NO
not_found_treated_as_nonexistence = YES
novelty_verdict_issued = YES
commercial_verdict_issued = YES
build_abandon_verdict_issued = YES
independent_run_preserved = NO
```

## 22. FINAL STATE

Exactly one:

```text
BOUNDARY_INSUFFICIENT
BOUNDARY_PARTIAL
BOUNDARY_READY_FOR_CONSOLIDATION
```

## 23. CONSULTANT ATTESTATION

```text
I confirm that this report distinguishes verified source support from inference and unresolved claims, and that I did not use another consultant's report in this run.
```
