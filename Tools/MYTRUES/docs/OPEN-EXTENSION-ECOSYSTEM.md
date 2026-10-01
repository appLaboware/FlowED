# MyTrues Open Extension Ecosystem

Date: 2026-10-01

Status: **TARGET DESIGN NORTH — NOT v0.2 WIRE-PROTOCOL CHANGE**

## Core boundary

The intended open boundary extends through the contract used to attach a decision
engine.

MyTrues MUST NOT require one canonical decision algorithm.

Conceptually:

```text
                    OPEN MYTRUES
┌─────────────────────────────────────────────────────────────┐
│ protocol / schemas / lifecycle / conformance               │
│                                                             │
│                Application / Domain Core                    │
│                         │                                   │
│       ┌─────────────────┼──────────────────┐                │
│       │                 │                  │                │
│   DecisionMemory    DecisionProfile    DecisionEngine       │
│       Port              Port               Port             │
│       │                 │                  │                │
│   Evidence / Provenance / Authority / Cognition / Views    │
│                         Ports                               │
└───────────────┬───────────────────────┬─────────────────────┘
                │                       │
          OPEN adapters          third-party adapters
                │                       │
        SQLite / DMN / OPA       custom engine / storage
        PROV / MCP / CLI         proprietary or OSS plugin
```

An implementation behind `DecisionEngine` may be:

- public/open source;
- scientific/reference;
- provider-specific;
- commercial/proprietary;
- deterministic;
- probabilistic;
- hybrid;
- human-backed;
- a composition of several engines.

Interoperability belongs to the open protocol. Algorithm ownership does not.

## Hexagonal interpretation

The terms **port** and **adapter** are used in the hexagonal-architecture sense.

A port is an application-facing capability contract.

An adapter implements or exposes that capability using a specific technology,
provider or protocol.

A plugin is a distributable package that supplies one or more adapters and a
machine-readable manifest.

A marketplace/registry indexes compatible plugin packages. It is not part of the
decision semantics.

## Candidate ports

These names are provisional. Each port requires its own versioned contract before
becoming normative.

### DecisionEngine

Purpose:

evaluate a decision request using an implementation-selected algorithm.

Candidate input envelope:

- decision context;
- alternatives, when known;
- criteria, when known;
- evidence references;
- selected provider/authority;
- DecisionPolicyProfile reference/version, when applicable;
- relevant memory/case references;
- protocol version;
- correlation/provenance identifiers.

Candidate result classes:

- `DECIDED`;
- `ABSTAIN`;
- `NEEDS_INPUT`;
- `ESCALATE`;
- `ERROR`.

A result SHOULD identify:

- engine implementation + version;
- profile version actually applied;
- evidence/provenance references used;
- structured reason/result codes where the engine can provide them.

An engine MUST NOT be required to reveal private implementation internals merely
to satisfy the open protocol.

### DecisionMemory

Stores and retrieves approved provider-scoped decision memory.

Current SQLite v0.2 reference behavior is one implementation.

### DecisionProfile

Loads and versions portable decision-policy/preference profiles.

This port intentionally separates reusable provider/person preferences from
criteria that belong only to one decision case.

**ADOPT-FIRST correction:** PPX (Preference Profile Exchange) 0.1-draft is
direct prior art for portable user-owned preference/context profiles, including
provenance, confidence, consent, context modifiers, lifecycle, extensions and
MCP/A2A/HTTP bindings.

Therefore the preferred exploration path is:

`PPX -> DecisionProfile adapter -> engine-specific semantic mapping`

rather than inventing a competing MyTrues preference-profile format.

A MyTrues-specific PPX extension/namespace should exist only if the decision
semantics cannot be represented by PPX core/domain extensions plus adopted
decision models.

Historical W3C CC/PP is additional evidence that extensible user preference
profiles are longstanding prior art.

### Profile semantic mapper

This is a candidate adapter responsibility, not necessarily a new normative
port.

It translates portable preference/profile claims into the representation a
specific DecisionEngine can consume, for example:

- PPX -> MCDA weights/constraints;
- PPX -> DMN input/context;
- PPX -> OPA input/policy context;
- PPX -> CBR retrieval/selection features;
- PPX -> learned/hybrid engine prompt/features.

The mapper SHOULD make unsupported/unmapped semantics explicit rather than
silently dropping them.

Cross-engine semantic preservation is a research target.

### Evidence

Obtains or resolves evidence referenced by a decision process.

Evidence transport is not automatically evidence authority.

### Provenance

Persists or exports provenance links.

W3C PROV should be evaluated before inventing a private provenance vocabulary.

### Authority

Resolves semantic/canonical promotion when automated mechanisms abstain or when
deployment policy requires approval.

### CognitionProposal

Produces **candidate** cognition/decision-memory material from unstructured input.

Example adapter:

a small LLM reads a conversation and proposes:

- candidate issue;
- candidate alternatives;
- candidate criteria;
- candidate evidence links;
- candidate DecisionRecord;
- candidate CCP keyframes.

Its output is staging, not canonical memory.

```text
conversation
    ↓
LLM cognition extractor
    ↓
CandidateCognition / CandidateDecision
    ↓
validation / authority
    ↓
canonical retention
```

This preserves the established rule:

`proposal -> authority -> canonical retention`

### Retrieval

Supplies lexical, case-based, graph, vector or hybrid retrieval without making
retrieval similarity itself semantic authority.

### Outcome / Observation

Records observed consequences after a decision/action so later evaluation or
reconsideration can use actual outcomes.

### View / Export

Produces ADR, NORM, WHY, TRACE, policy, timeline, JSON/JSON-LD, PROV or other
derived views.

### Source / Connector

Connects Git, files, conversation exports, external APIs, knowledge stores or
other source systems.

## Inbound adapters

Possible driving adapters include:

- HTTP/OpenAPI;
- MCP server;
- CLI;
- language SDK;
- batch/file interface;
- event-driven adapter;
- UI.

MCP is therefore **an adapter**, not the MyTrues core.

The same MCP technology may also appear on the outbound side when a MyTrues
adapter consumes another MCP server for evidence/tools. Role depends on direction.

## Plugin classes

A future ecosystem may support independently distributed implementations such as:

1. **decision-engine plugins**
   - DMN engines;
   - MCDA;
   - CBR;
   - CP-net/preference engines;
   - OPA/policy engines;
   - custom research engines;
   - provider proprietary engines.

2. **profile plugins**
   - static profile;
   - elicitation;
   - preference learning;
   - profile migration/normalization.

3. **cognition plugins**
   - conversation cognition extraction;
   - meeting/document decision extraction;
   - code/commit/issue cognition extraction;
   - multi-model candidate generation.

4. **memory/storage plugins**
   - SQLite;
   - document/files;
   - RDF;
   - temporal/context graph;
   - graph/vector stores where justified.

5. **retrieval plugins**
   - lexical;
   - graph;
   - vector;
   - CBR;
   - hybrid.

6. **evidence/provenance plugins**
   - W3C PROV mapping;
   - source verification;
   - citation resolution;
   - audit/signature adapters.

7. **authority/governance plugins**
   - local human approval;
   - team workflow;
   - enterprise policy;
   - escalation queue.

8. **view/export plugins**
   - ADR/MADR;
   - static docs;
   - NORM/WHY/TRACE;
   - dashboards;
   - JSON/JSON-LD/RDF.

9. **integration adapters**
   - MCP;
   - CLI;
   - IDE/editor;
   - Git platforms;
   - chat/collaboration systems;
   - workflow engines.

## Plugin manifest candidate

Before building a marketplace, define a portable manifest.

Candidate metadata:

- plugin identity;
- semantic version;
- supported MyTrues protocol versions;
- implemented port(s);
- capability declarations;
- license;
- source/binary location;
- configuration schema;
- required permissions;
- network access;
- external-provider/data-sharing declaration;
- secret requirements;
- local/offline capability;
- deterministic/probabilistic classification;
- data-retention declaration;
- conformance suite + result URL;
- signature/provenance;
- optional benchmark evidence;
- compatibility constraints.

The registry must distinguish:

`published` from `conformant` from `scientifically benchmarked`.

## Registry / marketplace

A future MyTrues registry may list open and commercial plugins.

Do not equate registry with scientific contribution.

Existing ecosystems already demonstrate the pattern:

- MCP has an official community registry;
- OpenTelemetry Collector has receivers/processors/exporters/connectors/extensions;
- Kubernetes supports dynamically registered custom resources/controllers;
- OPA supports plugins/custom built-ins.

The product opportunity is a **decision-specific, conformance-aware ecosystem**,
not the generic idea of plugins.

## Security and epistemic boundary

A plugin may have access to highly sensitive decision history and preferences.

Therefore marketplace metadata must make data-handling explicit.

A cognition or retrieval plugin cannot promote its own output to canonical truth
unless the active authority policy explicitly grants that capability.

A DecisionEngine may decide according to its contract but must report enough
identity/version information for the DecisionRecord to remain replayable and
auditable.

## v0.2 compatibility

None of this silently changes the executable v0.2 failure profile.

v0.2 remains the proved reference baseline.

These ports/adapters define the target design space for versioned protocol work.
