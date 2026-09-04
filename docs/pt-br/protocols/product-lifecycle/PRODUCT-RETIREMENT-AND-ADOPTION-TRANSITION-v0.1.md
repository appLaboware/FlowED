# FlowED — Product Retirement and Adoption Transition Protocol v0.1

- ID: `FLOWED-PRODUCT-RETIREMENT-ADOPTION-TRANSITION`
- Version: `0.1-draft`
- Status: `DOGFOODING`
- Owner domain: `FlowED`

## 1. Purpose

Define how a FlowED-governed product, internal implementation or capability is retired, replaced, or migrated when a better external or internal solution becomes available.

A product is not entitled to continue existing merely because it already exists.

A local implementation is not entitled to remain local merely because it was once necessary.

The governing objective is always the best known solution for the declared domain and constraints.

## 2. Core laws

```text
PRODUCT SURVIVAL IS NOT A SUCCESS CRITERION.
BEST-KNOWN SOLUTION IS.
```

```text
WHEN AN ADOPTABLE SOLUTION ELIMINATES THE RESIDUAL,
RE-EVALUATE OWNERSHIP.
```

```text
WHEN A PRODUCT LOSES ITS JUSTIFYING RESIDUAL,
RETIRE, REDUCE OR TRANSITION IT.
DO NOT KEEP IT ALIVE FOR SENTIMENT, SUNK COST OR IDENTITY.
```

## 3. Trigger conditions

A transition or retirement review MUST be opened when any of the following occurs:

- a continuous validation probe invalidates a product premise;
- a newly discovered external solution covers the residual previously owned by the product;
- an adopted dependency evolves and absorbs the product's unique value;
- a better composition of existing solutions supersedes the current implementation;
- maintenance cost materially exceeds remaining unique value;
- a product capability becomes redundant with another authoritative domain;
- a PO or consumer produces evidence that direct adoption is now superior.

## 4. Transition types

### `RETIRE_PRODUCT`

The product no longer has a material residual worth owning.

Example:

```text
Git did not solve need X
        ↓
NGit existed to solve X
        ↓
Git later solves X better
        ↓
NGit residual = 0 or negligible
        ↓
RETIRE NGit
        ↓
consumers migrate to Git
```

### `REPLACE_IMPLEMENTATION_WITH_ADOPTION`

The product/domain still exists, but an internally implemented capability is replaced by an adopted external implementation behind the same public contract.

### `REDUCE_TO_ADAPTER_OR_ORCHESTRATOR`

The product keeps only the residual contract/orchestration that remains uniquely valuable while delegating implementation to adopted components.

### `MERGE_DOMAIN`

The independent product/domain ceases to be justified and its remaining responsibilities are absorbed by another authoritative domain.

### `SUPERSEDE_WITH_NEW_PRODUCT`

A materially different product becomes the authoritative solution and migration is required.

## 5. Mandatory retirement review

Before retirement or major transition, record:

- `product_id`;
- `current_mission`;
- `original_residual`;
- `current_residual`;
- `trigger`;
- `new_solution_or_composition`;
- `evidence`;
- `affected_decisions[]`;
- `affected_consumers[]`;
- `affected_documents[]`;
- `affected_contracts[]`;
- `migration_plan`;
- `rollback_plan` when relevant;
- `final_disposition`;
- `owner_approval`;
- `effective_revision_or_date`.

## 6. Consumer impact propagation

A product/domain being retired or materially changed MUST identify all known consumers and dependents.

The owner must propagate a change event containing at least:

- what changed;
- why it changed;
- authoritative evidence;
- what replaces the old capability;
- compatibility status;
- required consumer action;
- migration deadline when applicable;
- affected versions;
- retirement/supersession relationship.

Communication transport is delegated to the adopted communication domain. FlowED owns the requirement that the impact is identified, scheduled, executed and verified.

## 7. Document and decision propagation

Retirement or transition MUST update or supersede all authoritative artifacts whose truth depends on the retired decision.

Do not silently rewrite history.

Use stable identity and revision/supersession relationships so that historical rationale remains inspectable.

At minimum, affected artifacts should be classified as:

- still valid;
- valid with revised dependency;
- superseded;
- retired;
- migration-only historical evidence.

## 8. Reverse adoption path

FlowED explicitly supports the inverse of product genesis:

```text
OWN IMPLEMENTATION
      ↓
NEW EXTERNAL / INTERNAL CAPABILITY DISCOVERED
      ↓
ADVERSARIAL DISCOVERY + COMPOSITION REVIEW
      ↓
IS ADOPTION NOW BETTER?
   ├─ NO → keep current implementation
   └─ YES
        ↓
      STOP NEW LOCAL EVOLUTION
        ↓
      MIGRATE BEHIND STABLE CONTRACT
        ↓
      VALIDATE EQUIVALENCE / IMPROVEMENT
        ↓
      RETIRE REPLACED IMPLEMENTATION
```

This path is mandatory to consider whenever a Late Discovery Defect or external evolution reveals that the organization is maintaining code that no longer needs to be owned.

## 9. No sunk-cost protection

The following are NOT valid arguments for preserving a product or implementation:

- "we already spent too much on it";
- "it is ours";
- "the repository already exists";
- "the team is used to it";
- "changing would make previous work look wasted";
- "we prefer controlling everything".

Past investment is evidence and learning, not authority over future architecture.

## 10. Exit quality gate

A retirement/transition closes only when:

```text
JUSTIFICATION_REVIEWED = YES
REPLACEMENT_IDENTIFIED = YES|NOT_APPLICABLE
CONSUMER_GRAPH_RESOLVED = YES
DOCUMENT_IMPACT_RESOLVED = YES
DECISION_GRAPH_UPDATED = YES
MIGRATION_EXECUTED = YES|NOT_APPLICABLE
COMPATIBILITY_VALIDATED = YES|NOT_APPLICABLE
OLD_IMPLEMENTATION_FROZEN = YES
RETIREMENT_STATUS_MATERIALIZED = YES
```

Any unresolved critical item keeps the transition open.

## 11. Final law

```text
CREATE ONLY WHEN RESIDUAL JUSTIFIES OWNERSHIP.
KEEP ONLY WHILE RESIDUAL STILL JUSTIFIES OWNERSHIP.
RETIRE WHEN ADOPTION BECOMES BETTER.
PRESERVE HISTORY, NOT OBSOLETE IMPLEMENTATION.
```
