# IDEA TO POC — ZERO STAGE

ID: FLOWED-PROJECT-ZERO-STAGE
Version: 0.1-draft
Status: BLUEPRINT / ASPIRATIONAL
Owner domain: FlowED

## 1. Purpose

Define the mandatory zero-stage that occurs before a project receives its durable local engineering structure.

The zero-stage starts from a raw idea and must determine, with adversarial evidence, whether the idea deserves to become a project at all.

The purpose is to prevent naming, repository creation, implementation, local session structure or product identity from granting premature legitimacy to an idea that should instead be adopted, composed, customized, adapted, reduced or abandoned.

## 2. Founding law

```text
IDEA DOES NOT AUTHORIZE PROJECT CREATION.
DISCOVERY PRECEDES IDENTITY.
IDENTITY PRECEDES REPOSITORY MATERIALIZATION.
IMPLEMENTATION EXISTS ONLY FOR THE RESIDUAL THAT SURVIVES ADOPTION.
```

## 3. Zero-stage pipeline

```text
RAW IDEA
   ↓
IDEA BOUNDARY DISCOVERY
   ↓
ADVERSARIAL PRIOR-ART / MARKET / ENGINEERING / ACADEMIC SEARCH
   ↓
ADOPT WHOLE?
 ├─ YES → GO BY ADOPTION / NO PROPRIETARY BUILD
 └─ NO
      ↓
CUSTOMIZE EXISTING?
 ├─ YES → ADOPT + CUSTOMIZE
 └─ NO
      ↓
ADAPT / COMPOSE EXISTING PARTS?
 ├─ YES → ADOPT + COMPOSE + ADAPT
 └─ NO
      ↓
BUILD MINIMUM RESIDUAL
      ↓
PRODUCT / RESEARCH RELEVANCE ASSESSMENT
      ↓
GO / NO-GO / GO-BY-ADOPTION
      ↓
ONLY AFTER GO:
NAMING
      ↓
DOMAIN / ORGANIZATION / REPOSITORY DESIGN
      ↓
MINIMUM CONCEPTUAL DOCUMENTATION
      ↓
POC
      ↓
DURABLE LOCAL PROJECT STRUCTURE
```

## 4. Search intent

The first research question is not:

> How should we build this?

It is:

> What is the smallest admissible amount of proprietary work required to realize the intent?

The zero-stage must actively attempt to eliminate proprietary implementation.

The preferred path is:

```text
ADOPT
→ CUSTOMIZE
→ COMPOSE
→ ADAPT
→ BUILD MINIMUM RESIDUAL
```

The distinction between CUSTOMIZE and ADAPT must be made explicit by each domain. As a working rule, customize means using an existing product's supported extension/configuration mechanisms; adapt means introducing an external translation/wrapper/integration layer or modifying a replaceable boundary.

## 5. Existing FlowED discovery authority

This zero-stage does not replace the existing `ADVERSARIAL-DISCOVERY-AND-DECISION-CHALLENGE` protocol. It makes that protocol mandatory at project birth.

Required discovery dimensions include, when relevant:

- technical feasibility;
- existing complete products;
- existing partial capabilities;
- composition alternatives;
- open-source and commercial solutions;
- standards and specifications;
- package and repository ecosystems;
- market evidence;
- maintenance and one-human-company cost;
- academic prior art;
- research frontier;
- legal/licensing constraints;
- operational risk;
- residual proprietary work.

Discovery must seek saturation rather than pretend to prove non-existence.

## 6. Decision outcomes

The zero-stage may conclude:

### GO BY ADOPTION
The intent is worth pursuing, but proprietary software is unnecessary or materially inferior to adopting an existing solution/composition.

### GO — CUSTOMIZE / COMPOSE / ADAPT
The intent survives, with proprietary work limited to supported customization, composition or adaptation.

### GO — BUILD MINIMUM RESIDUAL
A defensible residual remains after exhaustive admissible adoption attempts.

### NO-GO
The idea lacks sufficient technical, commercial, strategic, scientific or organizational justification under the declared objectives.

A NO-GO is a successful prevention of unjustified work.

## 7. Research-frontier assessment

When the idea contains a possible academic contribution, the zero-stage must separately classify it.

Suggested classes:

- `KNOWN`;
- `KNOWN_COMBINATION`;
- `EXTENSION_CANDIDATE`;
- `ANTITHESIS_CANDIDATE`;
- `POTENTIALLY_NOVEL_PROPERTY`;
- `INSUFFICIENT_EVIDENCE`;
- `NOT_DEFENSIBLE`.

No commercial GO automatically authorizes a novelty claim.
No academic novelty automatically establishes product viability.

Engineering, research and business verdicts must remain separate before reconciliation.

## 8. Relevance scoring

A proprietary residual should receive an explicit relevance assessment before product identity is created.

The exact scoring model is not yet normative. It should eventually measure, with doctorate-level rigor where research claims are involved:

- uniqueness of residual;
- engineering value;
- user value;
- market evidence;
- strategic fit;
- maintainability;
- replaceability;
- research depth;
- evidence quality;
- cost/risk of ownership.

Status: OPEN DESIGN QUESTION.

## 9. Naming is downstream of viability

Naming must not precede zero-stage GO.

The naming step receives the validated model, boundaries, residual, technical category and intended scope as inputs.

The naming actor must not be forced to rediscover project viability.

Principle:

> THE NAME IS A CONSEQUENCE OF THE MODEL, AND THE MODEL MUST FIRST SURVIVE DISCOVERY.

## 10. Repository and organization design is downstream of naming

Only after the identity is provisionally selected should the process design:

- domain ownership;
- organization placement;
- repository decomposition;
- repository names;
- About/description text;
- tags/topics;
- dependencies on preceding projects/capabilities;
- minimum conceptual documentation;
- first POC boundary.

Repository creation must not be used as an early brainstorming artifact unless explicitly marked disposable.

## 11. Pre-local-session execution

The zero-stage through early POC may run without a durable local session system.

During this phase, multiple AIs may collaborate through a generic communication protocol and materialized handoffs.

Generic prompts must request only information required to continue the work. They must not mention future internal products, migration targets or implementation mechanisms unless that knowledge is actually necessary to perform the current task.

This avoids causing an external AI to spend context asking what an irrelevant internal product is.

## 12. Generic seed principle

A seed created before the durable project structure must be self-describing and generic.

It should contain only what a future actor needs to know, such as:

- idea / mission;
- validated boundaries;
- decision status;
- evidence references;
- known facts;
- unknowns;
- current demand;
- decisions already established;
- pending work;
- stop conditions;
- required outputs;
- provenance.

It must not leak the name of a future tool merely because that tool may later adopt the project.

## 13. Tool decomposition candidate

The zero-stage should be decomposable into replaceable tools/capabilities rather than one monolith.

Candidate chain:

```text
IdeaDiscovery / Viability
        ↓
Naming
        ↓
Domain & Repository Design
        ↓
Repository Seed
        ↓
POC Bootstrap
        ↓
Durable Project Adoption
```

Each element has no right to exist as proprietary software if an admissible superior solution already exists.

## 14. Dogfooding requirement

The creation of each zero-stage tool must itself pass the zero-stage.

Example:

```text
Need a naming tool?
        ↓
Search for existing naming / brand / domain / trademark / repository-design tools
        ↓
Adopt or compose if sufficient
        ↓
Only build the missing residual
```

Therefore this protocol is recursively applicable to the tools that implement it.

## 15. Relationship to FlowED mission

This is a candidate FlowED genesis capability because it governs the path from intent to admissible project creation.

Its long-term execution surface may be exposed through FlowED while preserving the sovereignty of every underlying tool, provider and resulting artifact.

This document defines target behavior only. It does not assert that the complete zero-stage is implemented today.
