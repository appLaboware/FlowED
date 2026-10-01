# ADOPTION-001 — IDEOS -> MyTrues

Status: **MIGRATION CONTRACT — canonical repositories pending creation**

This is the first application of `ADOPTION-PROTOCOL` between products maintained
by the same organization/ecosystem.

Being maintained by the same people does not relax the decoupling rule.

## Upstream

- canonical target repository: `https://github.com/MyTrues/mytrues`;
- role: generic decision protocol and reference implementation;
- license: MIT;
- current migration source: `appLaboware/FlowED/Tools/MYTRUES`;
- current reference protocol: v0.2;
- canonical upstream SHA: **PENDING until the new repository is created/imported**.

## Consumer

- canonical target repository: `https://github.com/MyTrues/ideos`;
- role: DevOps intent CLI;
- license: MIT;
- current migration source: `appLaboware/FlowED/Tools/IDEOS`.

## Capability adopted

IDEOS adopts decision memory/decision resolution through the consumer-owned
`DecisionMemory` port.

The first adapter maps that port to MyTrues v0.2 public HTTP/schema behavior.

## Hard boundary

IDEOS MUST NOT:

- copy `provider_server.py` or other MyTrues implementation code;
- open/read the MyTrues SQLite database directly;
- depend on MyTrues storage schema;
- depend on historical Neo4j material;
- treat MyTrues provider decisions as globally authoritative;
- modify MyTrues behavior inside the IDEOS repository.

MyTrues changes happen in `MyTrues/mytrues` only.

## Pin

After canonical import, IDEOS MUST contain one explicit upstream lock record with:

- repository URL;
- exact MyTrues commit SHA;
- protocol/schema version;
- date of adoption;
- evidence URL proving adapter compatibility.

The initial lock cannot be truthfully written before `MyTrues/mytrues` exists.

## Update flow

1. MyTrues changes are committed/released in `MyTrues/mytrues`.
2. IDEOS selects a candidate MyTrues commit SHA.
3. IDEOS runs adapter conformance/integration against that exact SHA.
4. If accepted, IDEOS updates only its pin/adapter compatibility record.
5. If rejected, IDEOS remains on the previous accepted SHA.

No synchronized release is required.

## Replacement

IDEOS code outside the adapter sees only `DecisionMemory`.

A different decision service may replace MyTrues if it satisfies the port and
passes the same compatibility evidence.

## CCP relationship

MyTrues is now domain-generic.

A recorded decision may be documented as a **CCP Record**: a decision record that
preserves the creator's cognitive path/provenance layer.

CCP is documentation/provenance semantics over decision records; it does not make
IDEOS the owner of MyTrues and does not make MyTrues DevOps-specific.

## Evidence gate

This adoption becomes `ACTIVE` only when both canonical repositories exist and
the IDEOS pin contains a real immutable MyTrues SHA plus a reproducible run URL.
