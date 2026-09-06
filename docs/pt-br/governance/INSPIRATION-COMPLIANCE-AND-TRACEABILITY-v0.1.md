# FlowED — Inspiration, Compliance and Traceability Protocol v0.1

- ID: `FLOWED-INSPIRATION-COMPLIANCE-TRACEABILITY`
- Version: `0.1-draft`
- Status: `DOGFOODING`
- Owner domain: `FlowED`

## 1. Purpose

Make inspiration, adoption, composition, compliance and transitive provenance first-class, queryable properties of every FlowED-governed product or project.

This protocol requires every product/project created under FlowED to materialize two distinct sections:

1. `INSPIRATIONS`
2. `COMPLIANCE_AND_ORIGINS`

The first explains intellectual/engineering lineage and influence. The second reports measurable direct and transitive implementation provenance and conformance.

## 2. Core distinction

```text
INSPIRATION != DIRECT ADOPTION
INSPIRATION != IMPLEMENTATION DEPENDENCY
INSPIRATION != CERTIFIED CONFORMITY
```

A technology, method, standard or product may influence a product without being directly embedded in it.

Conversely, a product may use another product transitively and therefore inherit part of its engineering lineage without directly importing or invoking the original source.

## 3. Mandatory template sections

Every FlowED repository bootstrap/template MUST include placeholders for:

```text
## Inspirations

## Compliance and Origins
```

A project is structurally incomplete when these sections are missing or unresolved.

## 4. Inspirations section

`INSPIRATIONS` records declared references that shaped the product's thinking, architecture, methods, constraints, values, or target outcomes.

Each inspiration SHOULD record:

- `name`
- `type` (`standard`, `method`, `framework`, `product`, `paper`, `practice`, `other`)
- `canonical_url`
- `why_it_matters`
- `admired_aspects[]`
- `criticized_aspects[]`
- `adopted_aspects[]`
- `divergences[]`
- `evidence_refs[]`
- `status`

FlowED itself SHOULD list, when supported by its current decision graph and product rationale, inspirations such as:

- Domain-Driven Design (DDD)
- Test-Driven Development (TDD)
- Clean Code
- Hexagonal Architecture / Ports and Adapters
- Agile
- Scrum
- ISO/IEC 29110 family, where applicable as an external standard/reference

This list is not frozen. Additions and removals are governed by the decision graph.

## 5. Compliance and Origins section

This section reports what the product actually depends on, incorporates, conforms to, or inherits transitively.

It MUST distinguish:

- `DIRECT_EXTERNAL_COMPONENT`
- `DIRECT_INTERNAL_PRODUCT`
- `TRANSITIVE_INTERNAL_PRODUCT`
- `TRANSITIVE_EXTERNAL_ORIGIN`
- `STANDARD_CONFORMANCE`
- `METHOD_CONFORMANCE`
- `INSPIRATION_ONLY`

Each record SHOULD include:

- `name`
- `canonical_url`
- `relation_type`
- `version_or_revision`
- `license_or_terms`
- `used_capabilities[]`
- `provenance_source`
- `monitor_id`
- `compliance_status`
- `compliance_score` when a defensible scoring model exists
- `evidence_refs[]`

## 6. Direct vs transitive relation

A product can inherit lineage through products it adopts.

Example:

```text
Product A
  ↓ adopts
FlowED
  ↓ incorporates/inspires from
DDD
```

Then Product A may answer:

```text
DIRECT_DDD_USE = NO
TRANSITIVE_DDD_LINEAGE = YES
PATH = Product A -> FlowED -> DDD
```

FlowED MUST preserve these paths as graph edges rather than flattening them into an ambiguous claim such as "Product A uses DDD directly".

## 7. Reverse-traceability query

Every governed product SHOULD be able to answer deterministically:

```text
WHAT EXTERNAL TECHNOLOGIES / STANDARDS / METHODS
CONTRIBUTE TO THIS PRODUCT, DIRECTLY OR TRANSITIVELY?
```

The answer is produced by reverse traversal of the adoption/composition/inspiration graph.

The traversal MUST preserve path semantics and relation types.

## 8. Compliance claims

FlowED MUST NOT fabricate certification or standards compliance.

The following statuses SHOULD be used:

- `NOT_ASSESSED`
- `PARTIALLY_ASSESSED`
- `SELF_ASSESSED`
- `EVIDENCE_BASED_INTERNAL_CONFORMANCE`
- `THIRD_PARTY_CERTIFIED`
- `NOT_APPLICABLE`
- `NON_CONFORMANT`
- `UNPROVEN`

A badge, logo, percentage or marketing statement MUST be backed by an explicit assessment model and evidence.

Official certification logos or marks MUST NOT be used unless their usage conditions are satisfied.

## 9. Compliance percentage

A percentage MAY be shown only when all of the following exist:

1. explicit assessment scope;
2. finite and published checklist/rule universe;
3. weighting model;
4. evidence for each evaluated item;
5. documented treatment of `NOT_APPLICABLE` and `UNKNOWN`;
6. reproducible calculation.

Example:

```text
FLOWED_CONFORMANCE = 87%
SCOPE = repository-governance-v0.3
ASSESSED_RULES = 46
PASS = 40
FAIL = 4
NOT_APPLICABLE = 2
METHOD = weighted-rule-coverage-v0.1
EVIDENCE = <refs>
```

Without such a model, FlowED MUST report a qualitative status rather than invent a percentage.

## 10. Continuous micro-adoption monitoring

Every non-trivial adopted capability SHOULD be decomposed into monitorable micro-adoptions.

A micro-adoption monitor SHOULD record:

- `monitor_id`
- `consumer_domain`
- `adopted_domain_or_component`
- `capability`
- `current_reason_for_adoption`
- `current_test_or_evidence`
- `replacement_candidates[]`
- `last_checked_at`
- `next_check_policy`
- `status`

The monitoring agent asks repeatedly:

```text
IS THIS STILL THE BEST KNOWN WAY TO SATISFY THIS CAPABILITY?
```

When deterministic verification exists, prefer deterministic tests over LLM judgment.

Example:

```text
TEST capability X
RESULT = FAIL
→ current residual still exists

LATER:
RESULT = PASS
→ current residual may have disappeared
→ STOP + domain review + migration/retirement analysis
```

## 11. Marketing transparency as production by-product

Because provenance and compliance are already required for engineering control, FlowED SHOULD project a public transparency view from the same authoritative graph instead of maintaining separate marketing claims.

Examples of generated views:

- inspirations;
- technologies used;
- direct and transitive origins;
- standards/framework conformance;
- compliance evidence summary;
- active external dependencies;
- retired dependencies;
- replaced internal implementations.

Public presentation is a projection. The graph is the source.

## 12. Dynamic documentation pipeline

FlowED adopts the requirement that documentation be generated from authoritative atomic sources rather than maintained primarily as disconnected static prose.

The intended deterministic pipeline is:

```text
SOURCE CODE
  ↓
SOURCE-LEVEL SEMANTIC COMMENTS
  + language-native API docs (e.g. Javadoc equivalent)
  ↓
AI-FIRST METADATA / FUNCTION INTENT
  ↓
ATOMIC TECHNICAL DOCUMENTS
  ↓
DEVELOPER DOCUMENTATION
  ↓
USER DOCUMENTATION
  ↓
PROJECT / PRODUCT AGGREGATED DOCUMENTATION
```

The exact syntax belongs to the documentation/tooling domain, not to FlowED.

FlowED owns the orchestration requirement and consumer-facing query semantics.

## 13. AI-first source annotations

Source-level annotations SHOULD enable an AI agent to understand intent, contract, side effects, invariants and dependencies without first re-reading the full implementation.

Suggested semantic fields:

- `purpose`
- `inputs`
- `outputs`
- `side_effects`
- `invariants`
- `preconditions`
- `postconditions`
- `errors`
- `dependencies`
- `domain_terms`
- `decision_refs`
- `doc_atom_refs`

These annotations MUST NOT become a second contradictory source of truth. They must be validated against code/tests or generated from authoritative contracts where possible.

## 14. Documentation query agent

A documentation agent SHOULD answer graph-backed questions such as:

```text
Which external technologies contribute to this product?
Which are direct versus transitive?
Why is component X still adopted?
What would happen if X were removed?
What is this product's conformance with FlowED?
What is its direct conformance with DDD?
What DDD lineage exists transitively?
Which standards influence this product?
Which compliance claims are evidence-backed?
```

The agent MUST traverse authoritative relations and cite their path/evidence.

## 15. Separation of ownership

FlowED owns:

- requirement for inspiration/compliance/origin sections;
- orchestration of traceability queries;
- adoption-monitor lifecycle;
- conformance gate behavior;
- transitive graph traversal semantics.

ISO29110-Lite/documentation domain owns, when adopted:

- generic document atom model;
- document metadata schemas;
- document composition/versioning rules;
- follower/editor/executor/owner semantics for controlled documents;
- dynamic documentation materialization contracts.

Individual product domains own:

- their actual inspiration list;
- adoption decisions;
- compliance evidence;
- domain-specific monitor tests;
- whether a challenge changes the product.

## 16. Template rule

Every FlowED bootstrap template MUST include machine-readable slots equivalent to:

```yaml
inspirations: []
origins: []
compliance: []
adoptions: []
transitive_relations: []
monitors: []
documentation_sources: []
```

A human-readable projection SHOULD be generated from the same data.

## 17. Final law

```text
DECLARE WHAT INSPIRED YOU.
TRACE WHAT YOU ACTUALLY USE.
DISTINGUISH DIRECT FROM TRANSITIVE.
PROVE COMPLIANCE BEFORE CLAIMING IT.
MONITOR EVERY MATERIAL ADOPTION.
GENERATE DOCUMENTATION FROM ATOMIC AUTHORITATIVE SOURCES.
LET PUBLIC TRANSPARENCY BE A PROJECTION OF ENGINEERING TRUTH.
```
