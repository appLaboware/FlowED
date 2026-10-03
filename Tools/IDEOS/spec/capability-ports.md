# IDEOS Capability Ports

Status: migration baseline.

Only ports required by currently accepted architecture are normative here.
Future ports must be added from observed integration boundaries, not imagined
product features.

## DecisionMemory

`DecisionMemory` isolates IDEOS from any concrete decision-memory implementation.

### Responsibility

The port allows IDEOS to:

1. submit a decision request;
2. receive an immediate approved decision or a pending state;
3. retain the request locator/correlation identity while execution is paused;
4. query the pending request until a decision is available;
5. resume the original IDEOS execution using the returned decision.

Provider-side authoring/resolution is outside the IDEOS port. It belongs to the
selected decision provider implementation.

### MyTrues adapter

The first adapter targets `MyTrues/mytrues` and maps the port to the MyTrues
v0.2 reference protocol:

- `POST /v1/decisions/resolve.failure`;
- `200` -> decided;
- `202` + `Location` -> awaiting provider decision;
- `GET /v1/decision-requests/{decisionRequestId}` -> pending or decided.

The provider operation
`POST /v1/provider/decision-requests/{decisionRequestId}/resolution`
is not exposed as an IDEOS operator capability merely because the upstream
protocol supports it.

### Dependency rule

The adapter MUST record:

- upstream repository: `https://github.com/MyTrues/mytrues`;
- immutable upstream commit SHA;
- protocol/schema version;
- adapter compatibility evidence.

The adapter MUST NOT:

- vendor/copy the MyTrues implementation;
- read private MyTrues storage directly;
- depend on SQLite internals;
- depend on Neo4j material;
- assume a provider's decisions are global truth.

### Replacement rule

IDEOS code outside the adapter depends on the `DecisionMemory` port, not the
MyTrues implementation. Replacing MyTrues therefore changes the adapter/pin,
not the IDEOS intent or execution model.

## Other capabilities

Porter/CNAB, provider CLIs and materializers are still being exhausted in R1/R2.
No additional IDEOS-owned capability port is declared normative by this migration.
