# MyTrues Generic Decision Protocol

Status: canonical identity baseline for migration to `MyTrues/mytrues`.

## Identity

MyTrues is a **domain-generic decision protocol**.

It defines how a client asks a selected decision provider for a decision, how the
provider may abstain/pause when it has no approved answer, how an explicit
resolution is supplied, how that provider may retain the resolution, and how the
client resumes.

MyTrues is not DevOps-specific. IDEOS is one client.

## Generic interaction

Known decision:

`client -> selected MyTrues provider -> approved decision -> client resumes`

Unknown decision:

`client -> pending -> sanitized decision context -> authorized provider/human -> explicit resolution -> provider retains -> client resumes`

Different providers may legitimately return different decisions for the same
context because provider memory, policy and authority are scoped.

## v0.2 compatibility

The current executable v0.2 reference was born from operational failure
resolution and exposes the profile:

`POST /v1/decisions/resolve.failure`

with `failure_code`-oriented schemas.

This profile is retained as working conformance evidence. It is **not** a claim
that the generic protocol is limited to failures or to DevOps.

A future protocol revision may generalize the request vocabulary only through a
versioned compatibility process. The migration itself does not silently rewrite
v0.2 schemas.

## Domain-neutral concepts

- decision request;
- decision context;
- selected provider/authority;
- decided response;
- pending/abstained response;
- explicit provider resolution;
- provider-scoped retention;
- correlation/provenance;
- resume.

## CCP Record

A persisted decision may carry a documentary provenance layer called a
**CCP Record**, defined in `CCP-RECORD.md`.

CCP means **Caminho Cognitivo do Criador**.

The CCP layer preserves how a decision was created or revised. It is not required
to make the wire protocol DevOps-specific and it does not itself define a
decision algorithm.

## Open/core boundary

Protocols, schemas, reference implementations, published algorithms, baselines
and conformance remain open.

Provider data may be private.

No proprietary MyTrues Core is authorized by this reorganization.
