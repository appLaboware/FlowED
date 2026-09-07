# FlowED — Contract-First Automatable Interaction v0.1

- ID: `FLOWED-CONTRACT-FIRST-INTERACTION`
- Version: `0.1-draft`
- Status: `DOGFOODING`
- Owner domain: `FlowED`

## 1. Purpose

Define the architectural rule that all interactions between humans, software components, projects and external tools must cross explicit, documentable, automatable and testable contracts.

FlowED adopts DDD and Hexagonal Architecture as inspirations for bounded ownership, ports/adapters and protection of domain intent from implementation details.

## 2. Core law

```text
DEPEND ON DOMAIN INTENT.
DO NOT DEPEND ON IMPLEMENTATION DETAILS.

INTERACT THROUGH A CONTRACT.
MAKE THE CONTRACT SCRIPTABLE.
MAKE THE CONTRACT TESTABLE.
MAKE THE CONTRACT DOCUMENTABLE.
```

## 3. Stable port, replaceable adapter

Consumers depend on a stable domain port.

```text
CONSUMER
   ↓
DOMAIN CONTRACT / PORT
   ↓
ADAPTER
   ↓
CURRENT IMPLEMENTATION
```

The implementation behind the adapter may change without forcing every consumer to change its behavior.

The implementation may be internal code, an external library, a SaaS, an operating-system primitive, a GitHub API, another CLI, another product or a future implementation not yet known.

## 4. Allowed interaction surfaces

A product capability exposed to another actor or system MUST have at least one canonical non-graphical interaction surface suitable for automation.

Preferred forms include:

- CLI;
- HTTP/API;
- RPC;
- message/event contract;
- file/data contract with explicit schema;
- function/library API when the boundary is in-process;
- other deterministic machine-addressable interface.

The exact transport may vary. The invariant is explicit contract + automation + testability.

## 5. GUI law

A GUI MUST NOT be the only authoritative control surface of a capability.

A GUI is an adapter that constructs and invokes domain commands/contracts.

```text
HUMAN
  ↓
GUI
  ↓
DOMAIN COMMAND / API CONTRACT
  ↓
APPLICATION
```

Not:

```text
HUMAN
  ↓
GUI-SPECIFIC HIDDEN BEHAVIOR
  ↓
APPLICATION INTERNALS
```

A capability that exists only as an opaque graphical interaction is not considered sufficiently automatable for FlowED-controlled operation.

## 6. Batchability and automation gate

For every externally usable operation, the product SHOULD be able to answer YES to:

```text
CAN_INVOKE_WITHOUT_GUI = YES
CAN_EXECUTE_IN_BATCH = YES
CAN_AUTOMATE = YES
CAN_TEST_AUTOMATICALLY = YES
CONTRACT_DOCUMENTED = YES
INPUTS_EXPLICIT = YES
OUTPUTS_EXPLICIT = YES
ERRORS_EXPLICIT = YES
```

A NO/UNKNOWN requires either an explicit exception or a gap/change request.

## 7. Human-software symmetry

Human interaction and machine interaction SHOULD converge on the same domain contract whenever practical.

Example:

```text
GUI BUTTON
   ↓
flowed project init ...

HUMAN TERMINAL
   ↓
flowed project init ...

AUTOMATION
   ↓
flowed project init ...
```

Equivalent API/message forms may exist, but they should preserve the same domain semantics.

## 8. No raw bypass

Consumers MUST NOT normally depend directly on implementation internals when a domain-owned contract exists.

Examples of prohibited bypass when a product contract exists:

- editing internal persistence files directly;
- invoking vendor internals instead of the domain CLI/API;
- depending on undocumented command output;
- calling a third-party implementation directly from multiple consumers when a domain adapter is meant to own that dependency;
- embedding GUI-only procedures into operational law.

Raw access may exist for debugging, migration, recovery or adapter implementation, but it is not the normal consumer contract.

## 9. Atomic capability rule

Domain operations SHOULD be independently meaningful, narrowly scoped and composable.

A higher-level operation orchestrates lower-level operations through their contracts instead of reimplementing them.

```text
ATOMIC COMMAND / CAPABILITY
      ↓
COMPOSITE COMMAND / WORKFLOW
      ↓
HIGHER-LEVEL PROCESS
```

This mirrors atomic POP composition in the documentation domain.

## 10. Contract properties

A domain contract SHOULD define:

- stable operation identifier/name;
- intent;
- inputs and types;
- defaults;
- preconditions;
- outputs/results;
- side effects;
- errors and exit/status semantics;
- idempotency characteristics;
- authorization requirements;
- version/compatibility policy;
- evidence/logging behavior;
- machine-readable form where feasible.

## 11. CLI as first-class port

Where a product has operational commands, a CLI SHOULD be treated as a first-class domain port rather than a convenience wrapper.

Examples:

```text
flowed ...
iso29110 ...
decb ...
intermembers ...
```

Each product owns its own domain CLI. FlowED may orchestrate them but SHOULD NOT erase their domain ownership.

## 12. Replaceability test

An architecture satisfies this principle only if a current implementation can be replaced while preserving consumer intent with bounded adapter changes.

```text
IMPLEMENTATION A
      ↓ replaced by
IMPLEMENTATION B

CONSUMER CONTRACT
      = unchanged or explicitly version-migrated
```

If replacement requires changing unrelated consumers, the boundary is considered insufficiently decoupled.

## 13. Internal-use viability

A generic adapter/tool MAY be worth creating even when no external market exists.

The viability question is not only market size.

A tool is justified when, after discovery and composition, it materially reduces internal duplication, risk, coupling, human effort, token cost or repeated cognition.

If external users later exist, productization may follow; external demand is not a prerequisite for architectural correctness.

## 14. MyTrues-class implication

Products such as `MyTrues` (`MyTrues.io`) SHOULD expose their own stable domain contracts rather than requiring clients to know whether the current implementation uses Git, a database, a vector store, a website, a specific LLM or another persistence/search mechanism.

The domain owns the intent; adapters own implementation substitution.

## 15. DDD + Hexagonal inspiration

FlowED explicitly records the following inspirations:

### Domain-Driven Design

Used as inspiration for:

- bounded contexts;
- domain ownership;
- explicit domain language;
- keeping implementation concerns subordinate to domain intent.

### Hexagonal Architecture / Ports and Adapters

Used as inspiration for:

- stable ports/contracts;
- replaceable adapters;
- external systems as implementation details behind domain boundaries;
- automated testing against ports independently from infrastructure.

These inspirations do not imply unqualified compliance with every interpretation or practice associated with DDD or Hexagonal Architecture. Compliance claims require explicit criteria and evidence under the FlowED compliance protocol.

## 16. Architecture gate

A new capability is not considered architecturally complete until it can show:

```text
DOMAIN_OWNER = KNOWN
CONTRACT = DEFINED
NON_GRAPHICAL_PORT = PRESENT
AUTOMATABLE = YES
BATCHABLE_WHERE_APPLICABLE = YES
TESTABLE_WITHOUT_GUI = YES
IMPLEMENTATION_BEHIND_ADAPTER = YES
DOCUMENTATION_SOURCE = KNOWN
RAW_BYPASS_REQUIRED_FOR_NORMAL_USE = NO
```

## 17. Final law

```text
THE GUI IS AN ADAPTER, NOT THE APPLICATION CONTRACT.
THE VENDOR IS AN ADAPTER, NOT THE DOMAIN.
THE CURRENT IMPLEMENTATION IS REPLACEABLE.
THE DOMAIN INTENT IS STABLE.

IF A HUMAN CAN DO IT,
AN AUTOMATION SHOULD BE ABLE TO DO IT THROUGH THE SAME SEMANTICS.
```
