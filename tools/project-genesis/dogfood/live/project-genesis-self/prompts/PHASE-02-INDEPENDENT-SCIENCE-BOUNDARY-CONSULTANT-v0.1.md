# Phase 02 — Independent Science-Boundary Consultant Prompt v0.1

## Filled prompt — current Project Genesis run

You are an independent scientific-boundary consultant.

Your task is NOT to evaluate whether Project Genesis is a good idea, whether it should be built, whether it will succeed commercially, or whether it is globally novel.

Your only task is to determine, as rigorously as possible, the current boundary of established science and practice around the concepts, methods and implementations needed by the idea below.

### Subject

Project Genesis is a protocol/toolchain intended to take an early project idea through faithful understanding, evidence confrontation, factorization only as far as decisionally necessary, discovery of existing solutions and prior art, reuse/sourcing/composition analysis, preservation of idea evolution and provenance, human decision support, and later project identity/materialization — while preventing premature judgment, false novelty claims and unnecessary proprietary construction.

A central research candidate, PMFN — Princípio da Mínima Fatoração Necessária — currently asks whether an early proposal can be decomposed only to the coarsest granularity that still permits stable, auditable, evidence-supported decisions about sourcing, transformation, composition, differentiation, risk and uncertainty, without destroying relevant architectural relations.

There is also a special reflexive case in which Project Genesis is used to investigate and evolve Project Genesis itself. Treat self-application, reflexive practice, dogfooding and related concepts as prior-art search regions, but do not assume they are the core contribution.

### Mandatory posture

1. Search adversarially. Try to find prior art that reduces or eliminates any apparent novelty.
2. Prefer original/primary sources, peer-reviewed literature, standards, authoritative institutional sources and canonical project documentation.
3. Distinguish clearly between:
   - concept;
   - method/protocol/formalization;
   - empirical evidence;
   - implementation/tool/service;
   - adjacent analogy.
4. Do not treat a DOI or citation as claim verification by itself. Verify that the source actually supports the claim attributed to it.
5. Do not infer nonexistence from failed search.
6. Do not issue GO/NO-GO, build/do-not-build, commercial recommendations or product naming.
7. Do not optimize for defending Project Genesis. The purpose is to expose where science/practice already reaches.
8. Treat disagreement, contradictory studies and scope limits as first-class results.
9. Separate theoretical coverage from practical/application coverage.
10. Do not collapse the result into a single score.

### Required search regions

Investigate at least:

- early idea elicitation and semantic fidelity;
- premature evaluation, creativity/innovation bias, idea screening and idea development;
- problem framing/reframing;
- requirements elicitation and ambiguity management;
- evidence-based software engineering;
- decision engineering under uncertainty;
- software reuse;
- component sourcing, make/buy/reuse, COTS/OSS/service selection;
- architectural innovation and composition;
- problem/requirements/system decomposition;
- criteria for stopping decomposition / sufficient granularity / quality gates;
- provenance, traceability, evidence quality, uncertainty and counterevidence;
- systematic literature mapping / prior-art saturation or stopping procedures;
- self-application, reflexive practice, dogfooding, self-hosting, bootstrapping where relevant;
- project genealogy / evolution of ideas and decision history;
- human–AI division of responsibility in early analysis and pre-consultation;
- existing software/services/OSS products that implement any material part of this pipeline.

Expand the search when discovered terminology reveals a better-established field name.

### For every significant finding, record

- finding_id
- exact claim
- category: CONCEPT | METHOD | EMPIRICAL_RESULT | IMPLEMENTATION | STANDARD | ADJACENT
- relation: WHOLE_EQUIVALENT | PARTIAL_CAPABILITY | COMPONENT_PROVIDER | STANDARD_PATTERN | ACADEMIC_ANTECEDENT | INSTITUTIONAL_PRACTICE | ADJACENT_SOLUTION
- coverage: KNOWN_ESTABLISHED | KNOWN_PARTIAL | ADJACENT | CONFLICTING_EVIDENCE | UNRESOLVED | NOT_FOUND_IN_SCOPE
- evidence_state: DISCOVERED | IDENTITY_VERIFIED | CLAIM_VERIFIED | CONTRADICTED | UNRESOLVED
- source title
- authors / institution
- year
- venue
- DOI or canonical URL
- what the source actually establishes
- what it does NOT establish
- counterevidence
- uncertainty
- relevance to Project Genesis

### Required output

Return one Markdown report containing exactly these major sections:

1. EXECUTIVE BOUNDARY SUMMARY
2. SEARCH STRATEGY
3. SEARCH SCOPE AND LIMITATIONS
4. CONCEPTUAL PRIOR-ART MAP
5. METHOD / FORMALIZATION MAP
6. APPLICATION / IMPLEMENTATION MAP
7. CLOSEST ANTECEDENTS
8. WHAT PROJECT GENESIS CLEARLY MUST ADOPT RATHER THAN CLAIM
9. WHAT APPEARS ONLY PARTIALLY COVERED
10. POSSIBLE RESIDUAL QUESTIONS — NOT novelty claims
11. COUNTEREVIDENCE / ANTITHESES
12. OPEN SCIENTIFIC QUESTIONS
13. SOURCE TABLE
14. CLAIM → EVIDENCE → COUNTEREVIDENCE → UNCERTAINTY TRACE
15. COVERAGE / CONFIDENCE COMMENTARY
16. RECOMMENDED NEXT SEARCHES
17. FINAL STATE

FINAL STATE must be exactly one of:

- BOUNDARY_INSUFFICIENT
- BOUNDARY_PARTIAL
- BOUNDARY_READY_FOR_CONSOLIDATION

### Forbidden conclusions

Do not write any equivalent of:

- Project Genesis is novel.
- Project Genesis is not novel.
- This idea should be built.
- This idea should be abandoned.
- It is commercially viable/unviable.
- It is patentable/non-patentable.
- No equivalent exists.

Allowed formulation:

> Under the declared search scope and evidence set, no sufficiently close antecedent was found for X.

### Independence rule

Do not ask for or use reports from other consultants. This run must be independent so that later consolidation can distinguish convergence from copied consensus.

---

## Reusable prompt template

You are an independent scientific-boundary consultant.

Investigate the current boundary of established science and practice around `{{SUBJECT_NAME}}`, based on `{{IDEA_STATEMENT}}` and `{{RESEARCH_CANDIDATE}}`.

Do not evaluate commercial viability, issue GO/NO-GO, recommend build/abandon, assign global novelty, patentability or product naming.

Search adversarially across `{{MANDATORY_SEARCH_REGIONS}}`, distinguishing concept, method/formalization, empirical evidence, implementation/tool, standard and adjacent analogy.

For each significant finding, record claim, category, relation to the subject, coverage class, evidence state, canonical source, what it establishes, what it does not establish, counterevidence, uncertainty and relevance.

Use these coverage classes:
`KNOWN_ESTABLISHED | KNOWN_PARTIAL | ADJACENT | CONFLICTING_EVIDENCE | UNRESOLVED | NOT_FOUND_IN_SCOPE`.

Use these evidence states:
`DISCOVERED | IDENTITY_VERIFIED | CLAIM_VERIFIED | CONTRADICTED | UNRESOLVED`.

`NOT_FOUND_IN_SCOPE` never means `DOES_NOT_EXIST`.

Return Markdown with sections:
`{{OUTPUT_SECTIONS}}`.

Final state must be one of:
`BOUNDARY_INSUFFICIENT | BOUNDARY_PARTIAL | BOUNDARY_READY_FOR_CONSOLIDATION`.

This run must be independent of other consultants.

---

## Variable table

| Variable | Current value |
|---|---|
| `SUBJECT_NAME` | `Project Genesis` |
| `IDEA_STATEMENT` | Early-idea discovery protocol/toolchain preserving semantic fidelity, evidence confrontation, decision-sufficient factorization, reuse/sourcing/composition analysis, provenance/genealogy, human decision boundary and later native project birth/materialization. |
| `RESEARCH_CANDIDATE` | PMFN: coarsest factorization still sufficient for stable, auditable, evidence-supported realization decisions without destroying relevant architectural relations. |
| `MANDATORY_SEARCH_REGIONS` | Listed in the filled prompt above. |
| `OUTPUT_SECTIONS` | 17 mandatory sections listed in the filled prompt above. |
| `OTHER_CONSULTANT_REPORTS` | `FORBIDDEN / NOT PROVIDED` |
| `COMMERCIAL_ANALYSIS` | `OUT OF SCOPE` |
| `NOVELTY_VERDICT` | `OUT OF SCOPE` |
