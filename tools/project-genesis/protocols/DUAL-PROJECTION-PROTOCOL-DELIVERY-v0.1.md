# Dual Projection Protocol Delivery v0.1

Status: `EXPERIMENTAL / GENERIC / UNVALIDATED`

## Purpose

Every Project Genesis protocol must be deliverable through two synchronized projections of the same canonical intent:

1. `HUMAN-GUIDE` — conceptual, explanatory, value-oriented and example-driven.
2. `AGENT-CONTRACT` — operational, deterministic where possible, explicit about gates, schemas, states, validation and machine-readable structures.

The two projections may live in one document for small protocols or in separate files for larger ones. For protocols with substantial rules, references, datasets, examples, schemas or execution constraints, separate files are preferred.

## Core law

`ONE PROTOCOL INTENT -> TWO AUDIENCES -> TWO PROJECTIONS -> NO SEMANTIC DIVERGENCE`

Neither projection is a simplified substitute for the other.

The human projection explains meaning, values, risks and desired behavior.
The agent projection constrains execution.

An AI agent should normally receive both projections when executing the protocol.
A human may normally read only the human projection unless auditing implementation details.

## Human Guide projection

The `HUMAN-GUIDE` must prioritize:

- why the protocol exists;
- what values it protects;
- what outcomes it seeks;
- what the human should pay attention to;
- examples of good behavior;
- examples of prohibited or dangerous behavior;
- conceptual explanation of gates;
- interpretation of outputs;
- important limitations;
- how the human can challenge, correct or homologate the result.

It should avoid unnecessary implementation noise such as large JSON schemas, machine-only identifiers or repetitive exhaustive rule matrices unless they materially help human understanding.

## Agent Contract projection

The `AGENT-CONTRACT` must prioritize executable compliance.

Where applicable it should include:

- MUST / MUST NOT / SHOULD / MAY rules;
- GO / DON'T-GO gates;
- explicit preconditions;
- allowed and forbidden transitions;
- exact output states;
- required fields;
- JSON / YAML / other structured fragments;
- validation rules;
- evidence requirements;
- provenance requirements;
- uncertainty representation;
- stop conditions;
- escalation conditions;
- failure conditions;
- reference-context inputs;
- examples of compliant and non-compliant outputs;
- large reference/context payload pointers where necessary.

## GO / DON'T-GO pattern

Every material execution gate should be representable in an agent-consumable form similar to:

```yaml
gate_id: UNDERSTANDING_SUFFICIENCY
required:
  - WHOLE_MODEL_HOMOLOGATION
  - ORIGINATOR_HOMOLOGATION
forbidden_if:
  - unresolved_material_misinterpretation
  - evaluation_leakage_detected
on_go: START_PHASE_02
on_dont_go: RETURN_TO_CLARIFICATION
```

The human projection should explain the same gate conceptually rather than merely reproducing this structure.

## Reference data and large context

Large research bases, reference corpora, evidence registers, taxonomies and examples should not be duplicated blindly inside both projections.

Preferred pattern:

```text
PROTOCOL INTENT
├── HUMAN-GUIDE.md
├── AGENT-CONTRACT.md
└── references/
    ├── REFERENCE-CONTEXT-BASE.md
    ├── schemas/
    ├── examples/
    └── evidence/
```

The agent contract may require these resources.
The human guide explains why they exist and how they affect the process.

## Synchronization requirement

Every protocol family must declare:

```yaml
protocol_family_id:
protocol_version:
human_guide_path:
agent_contract_path:
shared_reference_paths: []
semantic_sync_status: VERIFIED | UNVERIFIED | DRIFT_DETECTED
```

A change that alters protocol behavior must update both projections or explicitly record why one projection is unaffected.

## Anti-drift check

Before release of a protocol version, verify:

1. every human-stated mandatory rule exists operationally in the agent contract;
2. every agent-enforced consequential rule has a human-understandable explanation;
3. gate meanings are equivalent;
4. terminology is aligned;
5. examples do not contradict rules;
6. reference-context assumptions are visible to both audiences at the appropriate level.

If any fails:

`DONT_GO_PROTOCOL_RELEASE`

## Audience rule

Default delivery behavior:

```text
HUMAN USER
    -> HUMAN-GUIDE

AI / EXECUTION AGENT
    -> HUMAN-GUIDE
    + AGENT-CONTRACT
    + REQUIRED REFERENCE CONTEXT
```

The agent receives the human guide because values and conceptual intent can be lost when execution is reduced to machine rules alone.

## Scope

This is a cross-cutting protocol-authoring rule and should apply to the Project Genesis protocol family unless a specific protocol documents a justified exception.
