# FlowDisP Protocol — POC 0.1

## 1. Mission

FlowDisP is a decision-support discovery protocol. It determines what antecedents materially overlap a bounded claim, how strong that overlap is, what remains uncovered, and what the evidence allows the decision owner to say.

It prevents two symmetrical errors:

- **under-searching:** “I do not know anything equal, therefore it is new”;
- **over-decomposing:** “every primitive already exists, therefore nothing can be distinctive”.

The protocol seeks the smallest research scope and comparison granularity sufficient for the decision at hand.

## 2. Research the claim, not the whole project

Every case MUST define:

```text
RESEARCH_OBJECT
CLAIM
DIMENSION
COMPARISON_UNIT
DECISION_CONTEXT
EXPECTED_RIGOR
REFUTATION_CONDITION
EXPLICIT_NON_GOALS
```

Candidate dimensions:

```text
CAPABILITY
CONCEPT
METHOD
ARCHITECTURE
IMPLEMENTATION
COMPOSITION
PRODUCTIZATION
COMMERCIAL_OFFERING
```

Different dimensions may produce different results for the same object. A public prototype can refute a claim that a capability has never existed while saying little about production readiness or commercial viability.

## 3. Separate four questions

1. **EXISTENCE** — is there an antecedent?
2. **EQUIVALENCE** — how much of the bounded claim does it cover?
3. **FITNESS** — would it satisfy the present need?
4. **DISPOSITION** — what should the project do about it?

The ABR primarily researches 1 and 2 and may collect evidence relevant to 3. The Discovery Owner decides 4.

## 4. Match classes

```text
EXACT
SUBSTANTIAL
PARTIAL
ADJACENT
ANALOGOUS
NO_SUFFICIENT_MATCH_FOUND
```

`NO_SUFFICIENT_MATCH_FOUND` MUST always be scoped by the search performed. It is never equivalent to “does not exist”.

## 5. Mode-sensitive evidence

See `PROFILES.md`.

For product/capability claims, a public repository, prototype, plugin or archived implementation may refute capability novelty if the capability is actually present. That does not establish fitness, supportability or commercial equivalence.

For academic/conceptual claims, semantic equivalence matters more than identical terminology.

## 6. Code is evidence, not the researcher's product

The ABR MAY inspect source code only when necessary to establish whether a claimed capability or mechanism exists.

The ABR MUST NOT turn the case into code review unless code quality is itself the claim.

Forbidden drift includes:

```text
"this function should be refactored"
"use framework X instead"
"this violates SOLID"
```

when the real question is whether an antecedent exists.

## 7. Preserve raw material

Research can start from saved HTML pages, Markdown transcripts, TXT notes, conversation exports or downloaded evidence files.

The original file is immutable evidence. A normalized view may be derived but never replaces raw.

```text
RAW
→ NORMALIZED VIEW
→ SOURCE MAP / HASH
→ RESEARCH INTERPRETATION
→ OWNER INTERPRETATION
→ DECISION
```

## 8. Iterative research

A Research Case remains open across rounds:

```text
FRAMING
→ ABR ROUND
→ OWNER AUDIT
→ FOLLOW-UP / SAME ABR
→ OPTIONAL INDEPENDENT REPLICATION
→ CONVERGENCE REVIEW
→ EVIDENCE FREEZE
→ DOWNSTREAM DECISION
```

Use the same ABR for continuity when useful. Use another ABR when independence matters, the result is surprising, a strong negative claim is involved, or search-path bias is suspected.

Agreement is not mandatory.

## 9. Closure states

```text
CONVERGED
CONTESTED
UNRESOLVED
INSUFFICIENT
```

- `CONVERGED`: sufficiently stable for the stated decision;
- `CONTESTED`: legitimate material interpretations remain in conflict;
- `UNRESOLVED`: available evidence cannot decide;
- `INSUFFICIENT`: work performed does not meet required rigor.

Closure means operational saturation, not proof that all world knowledge was exhausted.

## 10. Operational saturation

The owner may freeze evidence when:

- the claim is stable and bounded;
- main synonyms/neighboring terms were explored;
- relevant source classes for the profile were searched;
- closest antecedents were explicitly compared;
- strong negative claims were qualified;
- caveats from raw traces are preserved;
- follow-up rounds stop changing the boundary materially, OR remaining uncertainty is explicitly classified;
- evidence is sufficient for the decision context.

Academic novelty claims normally require higher rigor than internal product decisions.

## 11. Per-round outputs

Each round preserves:

```text
RESEARCHER-PROMPT.md
SEARCH-TRACE.md
EVIDENCE-LEDGER.md
ROUND-REPORT.md
raw chat export(s), when available
```

The report is a projection, not the source of truth. The owner MUST inspect the raw trace before accepting it.

## 12. Owner forensic audit

The owner checks:

1. actual bounded question answered?
2. scope drift?
3. implementation/code-review/product-design drift?
4. sufficient synonyms and adjacent domains?
5. important source classes missed?
6. primary sources skipped?
7. source interpreted too strongly?
8. near-matches dismissed too quickly?
9. caveats present in raw chat omitted from report?
10. absence-of-evidence converted into novelty?
11. granularity manipulated to create/erase residual?
12. another round or independent ABR justified?

## 13. Downstream disposition

After evidence freeze, candidate project dispositions are:

```text
ADOPT
CONFIGURE / PERSONALIZE
EXTEND / OVERLAY
COMPOSE
FORK / MODIFY
DERIVE / INSPIRE
BUILD_RESIDUAL
UNRESOLVED
```

ABR may recommend; Discovery Owner decides.

## 14. Ethical lineage

A residual may be distinctive without being ex nihilo. Even when the end result is materially new, the Evidence Pack preserves what was inherited, transformed, composed, extended or reacted against.

“Invented” does not mean “without ancestry”.

## 15. Downstream gate

Only after owner review/evidence freeze should implementation/editorial actors receive a prepared Evidence Pack with claim, antecedents, references, match classes, inherited elements, residual, uncertainty/limits, allowed wording strength, and disposition if decided.
