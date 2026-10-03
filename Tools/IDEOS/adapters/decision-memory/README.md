# DecisionMemory adapter boundary

This directory is the physical IDEOS adapter boundary for decision-memory
providers.

IDEOS code outside this directory depends on the consumer-owned
`DecisionMemory` capability contract defined in:

`../../spec/capability-ports.md`

## First adapter: MyTrues

The first adopted provider is `MyTrues/mytrues`.

Rules:

- no MyTrues implementation code is vendored here;
- no direct SQLite/Neo4j/storage access is allowed;
- the adapter talks only to the public MyTrues protocol;
- the adapter is activated only when
  `../../upstreams/mytrues.lock.json` contains a real immutable canonical SHA;
- the example lock is not an accepted dependency pin;
- compatibility evidence is required before a new pin is accepted.

The current v0.2 mapping is:

- request decision -> `POST /v1/decisions/resolve.failure`;
- decided -> HTTP 200;
- pending -> HTTP 202 and decision request locator;
- poll pending request -> `GET /v1/decision-requests/{id}`.

Provider-side resolution is not an IDEOS operator capability.
