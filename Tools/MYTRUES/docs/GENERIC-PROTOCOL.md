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


## Target engine-extension boundary

The target open design extends through a versioned port used to attach a
`DecisionEngine`.

MyTrues does not define one mandatory decision algorithm.

Conceptually:

`client -> MyTrues protocol/lifecycle -> DecisionEngine port -> selected engine`

The selected engine may be:

- a reference/public algorithm;
- DMN/rule based;
- policy based;
- MCDA/CBR/preference based;
- LLM-assisted/hybrid;
- human/team backed;
- provider-specific OSS;
- provider-specific commercial/proprietary.

The interoperability contract remains open even when an engine implementation is
private.

Other candidate open ports include decision memory, decision profile, evidence,
provenance, authority, cognition proposal, retrieval, observed outcome, views and
source connectors.

The detailed target taxonomy is maintained in:

`OPEN-EXTENSION-ECOSYSTEM.md`

This section is a target design north. It does not silently modify the v0.2 wire
profile.

## Extension ecosystem

Ports and adapters are intended to permit an independently developed ecosystem.

A distributable plugin may implement one or more adapters.

Examples include:

- decision engines;
- DecisionPolicyProfile providers/learners;
- conversation/document cognition extractors;
- storage/retrieval adapters;
- evidence/provenance adapters;
- authority/escalation workflows;
- view/export adapters;
- MCP/CLI/SDK/integration adapters.

An LLM-based cognition extractor produces **candidate** cognition/decision
artifacts. It does not obtain canonical authority merely by being an adapter.

A future registry/marketplace is an ecosystem/distribution concern, not part of
the semantic definition of a decision.


## Preference-profile prior art boundary

MyTrues does not own the concept of a portable user/provider preference profile.

The target `DecisionProfile` capability should first interoperate with PPX
(Preference Profile Exchange) and evaluate older profile prior art such as
W3C CC/PP.

A MyTrues-specific portable profile schema is not authorized merely because the
protocol has a `DecisionProfile` port.

The likely integration direction is:

`portable profile (for example PPX) -> DecisionProfile adapter -> selected
DecisionEngine mapping`

The decision protocol may standardize how an engine/profile/version participates
in a DecisionRecord without standardizing a new preference vocabulary.
