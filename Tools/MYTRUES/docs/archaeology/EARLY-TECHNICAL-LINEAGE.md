# Early Technical Lineage — Logic/Rules MyTrues

Date: 2026-10-01

Status: **HISTORICAL ARCHITECTURE — SUPERSEDED BY CURRENT PROTOCOL-FIRST STAGING**

## Purpose

A batch-002 reconstruction preserves a 2025 technical direction that predates the
current Open Decision Protocol.

It is useful for genealogy because it shows that MyTrues originally explored a
logic/rule-engine architecture before becoming protocol-first.

It is **not** a proposal to revive that architecture.

## Historical branch

The reconstructed 2025 proposal described a `mytrues-core` with:

- Datalog/Prolog style logic;
- facts;
- rules;
- queries;
- explanations.

Candidate API surface:

```text
/assert
/retract
/query
/why
```

Additional ideas recorded:

- append-only / event-sourcing style history;
- semantic versioning;
- JSON Schema and/or Protobuf;
- HTTP/gRPC;
- adapters for JavaScript/Node, Python, Java and Rust;
- CozoDB as candidate engine/storage.

A TICA-adjacent pipeline was also associated historically:

`capture -> normalize -> distill -> store`.

These items are genealogy, not present-day requirements.

## Why the branch was superseded

The later architecture moves semantics away from one embedded inference/storage
technology and toward:

```text
open protocol
+ schemas
+ lifecycle
+ conformance
+ ports/adapters
+ replaceable engines
+ reference persistence
```

The current staging uses SQLite as a reference provider-memory implementation,
not as protocol identity.

A graph, logic engine or rule engine may return later as a DecisionEngine,
retrieval adapter or storage adapter if justified.

## Current executable evidence

Repository evidence on 2026-10-01 confirms:

`Tools/MYTRUES/protocol/openapi.yaml`

with:

- title: `MyTrues Open Decision Protocol`;
- OpenAPI: `3.1.0`;
- info version: **0.2.0**.

Current operations include:

- `POST /v1/decisions/resolve.failure`;
- `GET /v1/decision-requests/{decisionRequestId}`;
- provider resolution submission.

Current conformance code:

`Tools/MYTRUES/conformance/test_protocol.py`

validates:

- JSON Schema draft 2020-12 definitions;
- schema identities under `/protocol/0.2/`;
- request identifier `mytrues.decision/v1`;
- different provider decisions for the same known case;
- 202 `awaiting-provider-decision` for unknown cases;
- sanitized case packet;
- explicit provider resolution;
- resume;
- persistence across restart;
- no cross-provider learning leakage.

## Version clarification

A conversation reconstruction contains an older reference to:

`OpenAPI version 0.1.0`.

That reference is historical.

Current staging evidence says:

`info.version = 0.2.0`.

The request protocol identifier remains:

`mytrues.decision/v1`.

Do not conflate:

- OpenAPI document version;
- protocol identifier;
- product/runtime version;
- schema version.

## Genealogical significance

The transition can be summarized as:

```text
2025
logic/rules engine
Datalog/Prolog + facts/rules/query
        ↓
2026
protocol-first
DecisionMemory + provider lifecycle + conformance
        ↓
target north
open ports/adapters through DecisionEngine
```

The historical branch shows a real change of architecture, not merely a rename.
