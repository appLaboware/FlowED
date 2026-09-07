# FlowED — Stable Contract and Adapter Boundary Law v0.1

- ID: `FLOWED-STABLE-CONTRACT-ADAPTER-BOUNDARY`
- Version: `0.1-draft`
- Status: `DOGFOODING`
- Owner domain: `FlowED`

## 1. Purpose

Require product capabilities to be consumed through stable product-owned contracts rather than raw implementation details, external APIs, repositories, files, commands or vendor-specific mechanisms.

The objective is to make adoption, replacement, composition and retirement cheap for consumers.

## 2. Core law

```text
CONSUMERS DEPEND ON PRODUCT CONTRACTS.
PRODUCT CONTRACTS DO NOT DEPEND ON ONE IMPLEMENTATION.
IMPLEMENTATIONS MAY CHANGE BEHIND THE CONTRACT.
```

## 3. Port, not bypass

When a product owns a capability, consumers SHOULD call a product-owned port such as:

- CLI command;
- API endpoint;
- library function/interface;
- schema/contract;
- event/message contract;
- declarative manifest.

Consumers SHOULD NOT directly depend on the raw implementation when a product-owned port exists.

Examples of prohibited bypass when an authoritative port exists:

- calling GitHub raw APIs directly instead of the owning product command;
- reading implementation-specific files as if they were public contract;
- invoking a third-party CLI directly from consumers when an adopted domain wraps that concern;
- duplicating provider-specific logic in multiple projects;
- binding workflows to repository layout that is not part of the declared contract.

## 4. Hexagonal interpretation

FlowED adopts the architectural idea of ports and adapters as a strong default for substitutable capabilities.

```text
CONSUMER
   ↓
STABLE PORT / CONTRACT
   ↓
DOMAIN CORE / ORCHESTRATION
   ↓
ADAPTER
   ↓
CURRENT IMPLEMENTATION
```

The current implementation may be:

- proprietary code;
- one adopted product;
- a composition of products;
- a SaaS/API;
- a local executable;
- a future replacement.

The consumer should not need to know which one is currently behind the port unless that knowledge is itself part of the contract.

## 5. Stable does not mean frozen forever

A stable contract may evolve through explicit versioning.

The rule is not "never change the interface".

The rule is:

```text
DO NOT FORCE CONSUMERS TO CHANGE
BECAUSE AN INTERNAL IMPLEMENTATION CHANGED.
```

Contract changes require their own semantic reason, versioning and migration path.

## 6. CLI as operational public port

For FlowED-governed products, a CLI SHOULD exist when the capability has repeatable operational behavior that humans, AIs, automation or other products need to invoke.

A CLI command SHOULD represent domain intent, not provider mechanics.

Prefer:

```text
flowed project init
```

over:

```text
gh api ...
cp ...
mkdir ...
python vendor_script.py ...
```

inside consumer procedures.

The first form preserves product intent. The second leaks implementation details.

## 7. Domain-owned commands

Each bounded context SHOULD expose its own commands for capabilities it owns.

Examples:

```text
flowed ...        # project/work orchestration
iso29110 ...      # document lifecycle/validation
intermembers ...  # interaction/communication
ngit ...          # NGit-specific Git alignment capability
```

The exact command names are product decisions. FlowED may orchestrate other CLIs but must not reimplement their domain semantics.

## 8. Orchestration without semantic theft

A parent/orchestrator may call another domain's public contract.

It may not bypass that contract and directly manipulate the adopted domain's internals merely for convenience.

```text
FLOWED
  ↓ calls
INTERMEMBERS PORT
  ↓
InterMembers implementation
```

not:

```text
FLOWED
  ↓ directly edits InterMembers internal transport/state
```

unless that direct mechanism is explicitly part of InterMembers' public contract.

## 9. Replaceability requirement

A capability intended to support future adoption changes SHOULD be designed so that the implementation can be replaced without changing consumer intent.

Before introducing a direct dependency, ask:

1. Is this external/raw mechanism part of our public domain contract?
2. Could this implementation reasonably be replaced later?
3. Would replacing it force changes in multiple consumers?
4. Can a stable port absorb that variation now?

If the likely replacement cost is cross-cutting, introduce or use the owning domain port.

## 10. Reverse-adoption migration

The stable-port rule enables migration from owned implementation to adopted implementation:

```text
CONSUMER
   ↓ unchanged
PRODUCT PORT
   ↓
OLD OWN IMPLEMENTATION
```

becomes:

```text
CONSUMER
   ↓ unchanged
PRODUCT PORT
   ↓
NEW ADAPTER
   ↓
ADOPTED IMPLEMENTATION
```

The same model supports the inverse migration if an adopted implementation later becomes insufficient.

## 11. Contract-first development

For capabilities likely to be consumed by multiple actors/products, define the public contract before committing consumers to implementation details.

Suggested order:

```text
DOMAIN INTENT
   ↓
PUBLIC CONTRACT / PORT
   ↓
ACCEPTANCE TEST
   ↓
ADAPTER(S)
   ↓
CURRENT IMPLEMENTATION
```

## 12. Compatibility evidence

Replacing an implementation behind a stable contract requires evidence that the new implementation preserves or intentionally revises the contract.

Use:

- contract tests;
- golden cases;
- integration tests;
- behavior fixtures;
- compatibility matrices;
- migration tests.

If behavior changes materially, the contract version must reflect it rather than pretending compatibility.

## 13. No raw-dependency default

Raw dependency is allowed only when one of the following is true:

- the raw mechanism itself is deliberately the public contract;
- no product-owned boundary exists yet and a bootstrap exception is explicitly recorded;
- the dependency is purely internal to the owning adapter;
- the cost of a boundary is demonstrably greater than the replacement risk and the decision is recorded.

Bootstrap exceptions are technical debt with an owner and exit condition.

## 14. MyTruth-class implication

Products that expose durable institutional or personal knowledge, memory, truth, decision or provenance capabilities SHOULD expose stable product contracts from inception.

Consumers must not depend directly on whichever storage engine, website, database, LLM provider, vector store or repository happens to implement that capability today.

This allows the implementation to evolve while preserving the consumer command/API semantics.

## 15. Final law

```text
DEPEND ON INTENT, NOT IMPLEMENTATION.
CALL THE DOMAIN, NOT ITS CURRENT TOOL.
PUT CHANGE BEHIND PORTS.
KEEP CONSUMERS STABLE WHILE IMPLEMENTATIONS EVOLVE.
```
