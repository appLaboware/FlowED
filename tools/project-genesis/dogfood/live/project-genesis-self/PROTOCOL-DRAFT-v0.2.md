# Project Genesis — Viability Discovery Protocol Draft v0.2

Status: `EMERGENT / DOGFOOD-DERIVED / UNVALIDATED`
Date: 2026-09-07
Supersedes operationally: `PROTOCOL-DRAFT-v0.1.md`
Derived from: runs 001–006 plus Phase 01 protection and Reflexive Discovery overlay

## 1. Protocol boundary

This protocol begins only after a protected understanding phase has established a sufficiently faithful representation of the idea.

> **NO EVALUATION BEFORE UNDERSTANDING SUFFICIENCY.**

Prior-art, sourcing, feasibility and differentiation analysis MUST NOT silently redefine the idea under investigation.

## 2. Founding rule

> **The protocol does not decide whether an idea is good or bad. It positions the idea against evidence, prior art and realization alternatives so a human can decide what to do.**

## 3. Canonical high-level flow

```text
PHASE 01 — INVESTIGATIVE UNDERSTANDING
        ↓
ORIGINATOR HOMOLOGATION
        ↓
DEFINE CURRENT DECISION QUESTION
        ↓
SEARCH WHOLE EQUIVALENTS
        ↓
WHOLE ADMISSIBLE COVERAGE?
   ├─ sufficient → record; no sourcing-driven split required
   └─ insufficient / heterogeneous
          ↓
PROPOSE MINIMUM SPLIT
          ↓
DECLARE WHAT DECISION CHANGES
          ↓
ΔD(split) MATERIAL?
   ├─ no → reject split
   └─ yes
          ↓
SEARCH PRIOR ART / REALIZATION OPTIONS PER FACTOR
          ↓
VERIFY CRITICAL SOURCES
          ↓
CLASSIFY KNOWN / ADJACENT / COMPOSABLE / RESIDUAL / UNKNOWN
          ↓
MAP REALIZATION MULTIDIMENSIONALLY
          ↓
REGISTER COVERAGE / CONFIDENCE / COUNTEREVIDENCE
          ↓
REPEAT ONLY WHERE DECISIONALLY NECESSARY
```

## 4. Whole-before-parts rule

Before the first sourcing-driven factorization, search for admissible whole equivalents.

This does not prohibit semantic clarification splits needed during Phase 01. It prohibits needless engineering decomposition before checking whether an existing whole realization already satisfies the current need.

## 5. Split admission rule

A split is admitted only when it materially changes at least one decision dimension:

```text
sourcing
candidate correspondence
transformation
architecture/composition
differentiation/exclusivity
risk
license
cost
ownership
evidence confidence
open uncertainty
```

Candidate representation:

```yaml
split_id:
parent_factor:
child_factors: []
changed_decisions: []
rationale:
delta_d: qualitative | experimental_numeric
```

No validated numerical scale for `ΔD` or `ε` currently exists.

## 6. PMFN stopping rule — narrowed by prior art

Project Genesis MUST NOT claim novelty for generic decomposition stopping.

Generic stopping criteria, systems-engineering decomposition gates and requirements/architecture granularity have established prior art.

The PMFN-specific hypothesis is narrower:

> Continue decomposition only while a split materially changes evidence-backed sourcing, transformation, composition, differentiation, risk or uncertainty decisions in early project discovery.

Candidate formal scaffold:

```text
F* = argmin Complexity(F)
subject to DecisionSufficiency(F) = true
```

and experimentally:

```text
continue while ΔD(split) >= ε
```

This remains an unvalidated research hypothesis.

## 7. Prior-art collision rule

Prior art can:

```text
invalidate a claimed contribution
narrow a contribution
supply a reusable mechanism
supply a comparator
supply a representation
create a new uncertainty
```

It MUST NOT automatically produce:

```text
PROJECT_GO
PROJECT_NO_GO
COMMERCIAL_SUCCESS
COMMERCIAL_FAILURE
```

A collision changes the research/product position, not the human decision by itself.

## 8. Known / adjacent / residual classification

Every material factor or research claim should be classifiable as one of:

```text
KNOWN_ADOPT
ADJACENT_ADAPT
COMPOSABLE
RESIDUAL_HYPOTHESIS
UNKNOWN
```

A `RESIDUAL_HYPOTHESIS` is not a novelty finding.

## 9. Evidence relation classes

Candidate evidence relations include:

```text
WHOLE_EQUIVALENT
PARTIAL_CAPABILITY
COMPONENT_PROVIDER
STANDARD_PATTERN
ADJACENT_SOLUTION
ACADEMIC_ANTECEDENT
INSTITUTIONAL_PRACTICE
COMMERCIAL_ANALOG
COUNTEREVIDENCE
```

## 10. Critical-source verification

A discovered citation or URL is not yet authoritative evidence.

Before a source materially changes a protocol or research claim, minimally verify:

```text
source identity
venue/publisher or canonical host
DOI/canonical reference when applicable
direct relevance to the claim
```

Verification state:

```text
DISCOVERED
IDENTITY_VERIFIED
CLAIM_VERIFIED
CONTRADICTED
UNRESOLVED
```

## 11. Evidence record

```yaml
claim_id:
claim:
status: fact | inference | hypothesis
factor_id:
evidence_relation:
sources: []
verification_state:
search_scope:
search_date:
coverage:
confidence:
counterevidence: []
assumptions: []
open_questions: []
```

## 12. Sourcing ontology — adopt before invent

Project Genesis should reuse established component-origin concepts where applicable, including:

```text
in-house
OSS
COTS
outsourced
```

and extend only where early-project discovery requires additional realization classes such as service/API/standard/human process.

Any extension must preserve mappings to established sourcing vocabulary.

## 13. Realization model — multidimensional

The canonical model MUST NOT assume that `COMPOSE` is a single rung in a linear ladder.

Current candidate:

```yaml
provenance: existing | modified | invented | unknown
transformation: none | configure | extend | adapt | unknown
architecture: direct | compose | reconfigure | unknown
source: OSS | COTS | service | standard | internal | outsourced | unknown
```

The familiar human-facing ladder may exist only as a projection where useful.

## 14. Residual terminology

Operationally prefer:

```text
FR = Residual Factorization
```

because:

```text
no admissible existing solution found
        !=
world novelty demonstrated
```

`MNI` / residual invention may be studied as a separate research construct only when evidence justifies the stronger semantic claim.

## 15. Position dimensions remain separate

Do not collapse into one idea score.

Candidate dimensions:

```text
P   — observed pertinence
EC  — existing coverage
XC  — conceptual exclusivity
XA  — architectural exclusivity
XE  — execution exclusivity
FR  — residual factorization
EM  — evidence maturity
RC  — research coverage
```

Interpretation law:

> No exclusivity measure is interpretable without the coverage and evidence quality of the investigation that produced it.

## 16. Out-of-order artifact quarantine

Useful work may arrive before the canonical phase that would normally produce it.

Such an artifact may be ingested as evidence but MUST NOT:

- advance the authorized process stage;
- materialize a project/capability;
- establish domain sovereignty;
- overwrite a homologated idea representation;
- bypass Phase 01.

## 17. Foreign artifact ingestion

Foreign artifacts enter as:

```text
FOREIGN / NON-AUTHORITATIVE EVIDENCE
```

Atom-level decisions:

```text
ADOPT
ADAPT
RETAIN_AS_HYPOTHESIS
REJECT
```

Never inherit topology, naming, ownership, maturity or process order automatically.

## 18. Reflexive Discovery rule

When Project Genesis analyzes Project Genesis, the Reflexive Discovery overlay applies.

Self-derived conclusions must preserve evidence origin and cannot become generic rules solely because the same process reproduces them.

Rules discovered only in self-dogfood remain overlay/local candidates until challenged by external cases.

## 19. Prior-art collision register

Each collision should record:

```yaml
original_claim:
prior_art_source:
verification_state:
overlap:
effect: preserved | narrowed | falsified | adopted_as_substrate | comparator
new_residual_hypothesis:
```

This prevents losing the genealogy of why a research claim changed.

## 20. Research residual ledger

Maintain explicit lists for:

```text
KNOWN / ADOPTED SUBSTRATE
ADJACENT PRIOR ART
COMPOSABLE MECHANISMS
CANDIDATE RESIDUAL
FALSIFIED RESIDUAL
OPEN UNCERTAINTY
```

The product is allowed to remain broad by composition even when the scientific residual becomes narrow.

## 21. Pre-materialization gate

Materialization is blocked while any relevant state remains:

```text
DISCOVERY_INCOMPLETE
DOMAIN_OWNERSHIP_UNRESOLVED
SOURCING_UNRESOLVED
RESIDUAL_NOT_ESTABLISHED
MATERIALIZATION_NOT_AUTHORIZED
```

Reversible prototypes may exist only as non-authoritative evidence when explicitly classified as such.

## 22. Dual output

Every run produces:

### A — project-position evidence

What was learned about the analyzed proposal.

### B — protocol/tool evidence

What was learned about the protocol itself.

For every material correction:

```text
OBSERVATION
   ↓
RESULT DELTA
   ↓
MISSING / WRONG RULE
   ↓
PROTOCOL CHANGE
   ↓
IMPLEMENTATION REQUIREMENT
```

## 23. Reproducibility record

```yaml
assessment_id:
protocol_version:
date:
subject_version:
phase:
evidence_snapshot:
search_queries:
sources:
source_verification_states:
factorization_before:
factorization_after:
prior_art_collisions: []
rules_added_or_changed: []
implementation_requirements: []
```

## 24. Current empirical limitations

Still unvalidated:

- systematic search saturation criterion;
- calibrated research coverage metric;
- evidence-maturity grading;
- operational `ΔD` distance functions;
- threshold `ε`;
- inter-rater agreement targets;
- validity of XC/XA/XE as independent constructs;
- usefulness of the neutral position profile;
- generalization beyond self-dogfood;
- pre-consultancy utility;
- longitudinal stability.

## 25. Next canonical step

The prior-art run is useful but out of order.

The next canonical execution remains:

```text
Phase 01 independent interviews
        ↓
multiple investigator reports
        ↓
consolidation of divergence
        ↓
originator homologation
        ↓
Pre-analysis Investigative Understanding Record
```

After that, the viability/prior-art analysis is rerun against the homologated idea statement.

The foreign Run 006 then becomes a comparator: we can measure how much the result changes when the investigation starts from a rigorously understood idea rather than from an analyst-created representation.
