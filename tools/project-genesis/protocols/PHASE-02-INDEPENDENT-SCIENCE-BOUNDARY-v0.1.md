# Phase 02 — Independent Science-Boundary Investigation v0.1

Status: `EXPERIMENTAL / GENERIC / UNVALIDATED`

## Goal

Determine how far established science and practice already reach around the homologated idea, without issuing a final novelty, feasibility or commercial verdict.

## Entry gate

Required input:

- homologated `PREANALYSIS-UNDERSTANDING-RECORD`;
- Phase 01 state = `READY` or `READY_WITH_OPEN_UNKNOWNS`;
- explicit originator request for multi-source investigation.

## Independent-run rule

Each consultant receives the same canonical Phase 01 record and the same response schema.

Consultants must not see one another's reports before consolidation.

## Mandatory evidence discipline

Every material factual claim must carry:

```text
CLAIM_ID
CLAIM
CLAIM_TYPE
EVIDENCE_STATE
SOURCE_ID
CANONICAL_REFERENCE
EXACT_SUPPORT
SCOPE_LIMIT
COUNTEREVIDENCE
UNCERTAINTY
```

`EVIDENCE_STATE` is one of:

```text
DISCOVERED
IDENTITY_VERIFIED
CLAIM_VERIFIED
CONTRADICTED
UNRESOLVED
```

A claim may influence the scientific boundary only when its state is `CLAIM_VERIFIED`, or when explicitly retained as unresolved/conflicting evidence.

## Anti-hallucination hard rule

The consultant must not present a source as verified merely because a citation, DOI, title or URL looks plausible.

For each source used materially, the report must confirm:

1. source identity exists;
2. canonical reference resolves;
3. authors/institution and year match;
4. venue or publisher matches where applicable;
5. the source content actually supports the attributed claim;
6. unsupported extrapolations are separated from source-supported statements.

If any step cannot be confirmed, mark `UNRESOLVED`.

## Required coverage dimensions

At minimum investigate:

- concept;
- method/protocol/formalization;
- empirical evidence;
- standards/institutional practice;
- practical implementation/tool/service;
- strongest adjacent antecedents;
- contradictory or limiting evidence;
- theoretical coverage;
- application coverage.

## Forbidden outputs

No consultant may conclude:

- `NOVEL`;
- `NOT NOVEL`;
- `BUILD`;
- `DO NOT BUILD`;
- `COMMERCIALLY VIABLE`;
- `COMMERCIALLY UNVIABLE`;
- patentability;
- definitive nonexistence.

Allowed:

> `Under the declared search scope, no sufficiently close antecedent was found for X.`

## Exit artifact

One normalized `SCIENCE-BOUNDARY-CONSULTANT-REPORT` per consultant.

## File naming

```text
<subject-slug>__SB-CONSULTANT__<consultant-id>__<YYYYMMDD>__v<NN>.md
```

Example:

```text
project-genesis__SB-CONSULTANT__C03__20260907__v01.md
```

The consultant ID is opaque and does not imply ranking.

## Exit state

Exactly one:

```text
BOUNDARY_INSUFFICIENT
BOUNDARY_PARTIAL
BOUNDARY_READY_FOR_CONSOLIDATION
```