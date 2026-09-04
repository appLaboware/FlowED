# FlowED — External Adoption and Product Identity Law v0.1

- ID: `FLOWED-EXTERNAL-ADOPTION`
- Version: `0.1-draft`
- Status: `DOGFOODING`
- Owner domain: `FlowED`

## 1. Purpose

Define how a FlowED-governed product must research, adopt, compose, challenge, replace, derive from and attribute external software, frameworks, standards and methods.

This law complements internal critical adoption.

Internal and external adoption share the same execution principle: while a concern is adopted, the consumer must preserve its semantic integrity and may not silently diverge locally.

The difference is the escalation destination and the path to evolution.

## 2. Core laws

```text
DO NOT BUILD WHAT DESERVES TO BE ADOPTED.
DO NOT ADOPT WHAT DESERVES TO BE REJECTED.
SEARCH UNTIL YOU CAN DEFEND THE DIFFERENCE.
```

```text
DISCOVER BEFORE SELECTING.
COMPOSE BEFORE BUILDING.
BUILD ONLY THE RESIDUAL OF THE BEST KNOWN COMPOSITION.
```

```text
ADOPTED CONCERN:
USE FAITHFULLY.
CRITIQUE CONTINUOUSLY.
DO NOT DIVERGE LOCALLY.
```

## 3. External adoption is not passive obedience

Adoption means the product has decided that an external concern is currently the best known authoritative implementation for that concern.

The consumer must:

- use it faithfully;
- expose the adoption explicitly where architecturally relevant;
- preserve required legal notices and provenance;
- continuously challenge whether it remains the best known choice;
- stop when a legitimate uncovered need or superior alternative invalidates the adoption.

A consumer must not keep saying it adopts an external product while implementing incompatible local semantics behind it.

## 4. External gap path

When an externally adopted concern no longer satisfies the need:

```text
EXTERNAL ADOPTION
      ↓
LEGITIMATE GAP OR SUPERIOR ALTERNATIVE
      ↓
STOP
      ↓
MATERIALIZE GAP / EVIDENCE
      ↓
RESEARCH ALL EXISTING OPTIONS AGAIN
      ↓
SELECT BEST PATH
```

Possible paths include:

- continue unchanged when challenge is refuted;
- configure;
- compose with additional external capabilities;
- extend through a supported extension mechanism;
- replace;
- contribute upstream when economically and strategically justified;
- fork when legally permitted and strategically justified;
- derive a new product;
- build only the remaining residual.

Contributing upstream is optional for external products. It is not a prerequisite for LaboWare to continue.

## 5. Product genesis from external insufficiency

A LaboWare product must not be created merely because LaboWare wants its own version of something.

Product genesis is justified only after evidence shows that the best known composition of existing solutions still leaves a material residual worth owning.

Typical path:

```text
EXTERNAL INSPIRATION / SOLUTION
        ↓
EXHAUSTIVE DISCOVERY
        ↓
BEST KNOWN COMPOSITION
        ↓
MATERIAL RESIDUAL GAP
        ↓
OWNERSHIP JUSTIFIED?
   ├─ NO → keep external composition
   └─ YES → PROJECT GENESIS
```

## 6. No arbitrary component-count threshold

Product identity is not determined by a fixed number of adopted components.

One external component may dominate the resulting system. Seventy external components may together form only ingredients of a new architecture.

Component count is therefore not a legal or architectural identity test.

## 7. Dominant Origin Test

FlowED uses an architectural dominance test to decide how strongly an external origin must be represented in the product identity.

For each major external candidate, ask:

1. If this component were removed, would the resulting product stop being recognizably the same product?
2. Does the main architecture come substantially from this component?
3. Does the main execution flow come substantially from this component?
4. Does this component provide most of the relevant domain capability?
5. Would a reasonable engineer describe the result as "that product plus orchestration/modifications"?

Predominantly positive answers indicate `DOMINANT_ADOPTION`.

Predominantly negative answers, together with genuinely independent architecture and composition, indicate `COMPOSITE_OWN_PRODUCT`.

This test is descriptive, not a substitute for license analysis.

## 8. Identity and attribution are separate

```text
PRODUCT_IDENTITY != LICENSE_PROVENANCE
```

A product may have independent LaboWare identity while incorporating many third-party components.

Independent identity does not erase:

- copyright notices;
- license obligations;
- NOTICE requirements;
- source-disclosure obligations when applicable;
- attribution requirements;
- patent/license conditions;
- dependency provenance;
- SBOM responsibilities.

Every incorporated component must preserve the obligations of its actual license.

The legal gate is evaluated per component and relationship, never inferred from product branding.

## 9. Composition classes

### `DOMINANT_ADOPTION`

One external product materially defines architecture, behavior or identity.

The product description SHOULD clearly state the relationship, for example "built on", "based on", "orchestrates" or equivalent truthful wording.

### `COMPOSITE_PRODUCT`

Several external components contribute materially, but none alone sufficiently defines the resulting product.

The resulting product may have independent identity while retaining full component provenance and license compliance.

### `HIGHLY_COMPOSED_PRODUCT`

A large set of independently sourced components, algorithms, patterns and libraries forms ingredients of an architecture whose defining decisions and integration are independent.

The "ultraprocessed food" analogy may be used internally as an explanatory metaphor: the final product may no longer be sensibly described by a single ingredient, but its ingredients and provenance remain traceable.

The analogy is not a legal criterion.

## 10. Mandatory provenance artifacts

A FlowED product that incorporates third-party software SHOULD progressively materialize:

- component name;
- source;
- version / commit;
- license;
- original copyright notice where required;
- modification status;
- relationship to the product;
- adopted capabilities;
- files/modules incorporated when applicable;
- required notices;
- SBOM identifier when available;
- rationale for adoption;
- dominant-origin classification.

## 11. Critical external adoption

An externally adopted concern is still subject to the Critical Adoption protocol.

The consumer must ask:

> Is this still the best known solution for this exact concern?

If YES, continue faithfully.

If NO or honestly UNKNOWN, STOP and re-enter Discovery.

The consumer may not silently create a local alternative merely to keep execution moving.

## 12. Final law

```text
SEARCH EVERYTHING PLAUSIBLE.
ADOPT WHAT IS BEST.
COMPOSE WITHOUT ARTIFICIAL LIMITS.
BUILD ONLY THE RESIDUAL.
PRESERVE THE INTEGRITY OF WHAT YOU ADOPT.
WHEN IT STOPS BEING BEST, STOP.
CHANGE THE AUTHORITATIVE SOLUTION, NOT A HIDDEN LOCAL VARIANT.
KEEP PRODUCT IDENTITY AND LEGAL PROVENANCE AS SEPARATE QUESTIONS.
```
