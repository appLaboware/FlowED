# Canonical References

Snapshot reviewed: 2026-10-01.

This list is not exhaustive. It is the starting set that every dossier may extend.

## Packaging / lifecycle

### CNAB

- https://cnab.io/
- https://cnab.io/community-projects

CNAB defines a cloud-agnostic package format for distributed applications.
The CNAB community lists Porter as an active tool in the ecosystem.

### Porter

- https://github.com/getporter/porter

Relevant upstream areas to exhaust:

- mixins;
- credential sets;
- parameter sets;
- dependencies/wiring;
- storage/secrets/signing plugins;
- OCI bundle handling;
- lint/inspect.

## Decision / process standards

### DMN

- Formal DMN 1.5:
  https://www.omg.org/spec/DMN/1.5
- OMG catalog:
  https://www.omg.org/spec/

As of this snapshot, DMN 1.5 is formal and DMN 1.7 is listed as beta.
Use 1.5 as normative baseline until a later formal version is adopted.

### BPMN

- BPMN 2.0.2:
  https://www.omg.org/spec/BPMN/2.0.2

## HTTP / APIs

### OpenAPI

- Current specification index:
  https://spec.openapis.org/oas/
- OpenAPI 3.2.1:
  https://spec.openapis.org/oas/v3.2.1.html

OpenAPI 3.2.1 was published 2026-09-10 and is the current target for protocol migration.

### RFC 9457

- https://www.rfc-editor.org/rfc/rfc9457.html

Use Problem Details instead of inventing MyTrues-specific error envelopes.

## Events

### CloudEvents

- https://github.com/cloudevents/spec

Use the stable CloudEvents release/tag as the event envelope baseline.

### AsyncAPI

- Specification:
  https://www.asyncapi.com/docs/reference/specification/
- AsyncAPI 3.1 release:
  https://www.asyncapi.com/blog/release-notes-3.1.0

AsyncAPI 3.1.0 is the target for MyTrues event contract work.

## Tracing

### W3C Trace Context

- https://www.w3.org/TR/trace-context/

Use `traceparent` / `tracestate` for distributed correlation.

## Provenance

### W3C PROV

- Overview:
  https://www.w3.org/TR/prov-overview/
- Primer:
  https://www.w3.org/TR/prov-primer/
- Access/query:
  https://www.w3.org/TR/prov-aq/

Use PROV concepts as the public baseline for decision provenance.

## Decision science

### Case-Based Reasoning

Canonical family:

`retrieve -> reuse -> revise -> retain`

The project must study the foundational Aamodt & Plaza model and modern CBR work
before inventing case retrieval/adaptation algorithms.

Example modern applied source:

- https://link.springer.com/article/10.1007/s10844-024-00861-0

### MCDA / MCDM

Recent broad review:

- Greco, Słowiński, Wallenius — Fifty years of multiple criteria decision analysis
  https://doi.org/10.1016/j.ejor.2024.07.038

Important dimensions:

- preference elicitation;
- criteria aggregation;
- recommendation;
- robust ordinal regression;
- multi-actor decision support.

### Data-driven decision methods

Review of ML-supported multi-criterion decision making:

- https://doi.org/10.1016/j.inffus.2023.101970

These methods remain OPEN baselines.

## AI / human oversight

### NIST AI RMF

- https://www.nist.gov/itl/ai-risk-management-framework
- GenAI profile:
  https://doi.org/10.6028/NIST.AI.600-1

Use for risk-management and evaluation discipline where LLM/AI assistance is introduced.

## Memory / graph

### Neo4j

- Operations manual:
  https://neo4j.com/docs/operations-manual/current/introduction/
- Deprecations:
  https://neo4j.com/docs/operations-manual/current/deprecations/

As of the current docs, vector indexes are available in Community Edition and
older vector query procedures are being replaced by Cypher `SEARCH` in Cypher 25.

## Identity / execution

### GitHub OIDC -> Azure

- GitHub:
  https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/configuring-openid-connect-in-azure

Prefer workload identity federation over long-lived Azure secrets.

### Azure Container Instances

- https://learn.microsoft.com/en-us/azure/container-instances/
- Multi-container YAML:
  https://learn.microsoft.com/en-us/azure/container-instances/container-instances-multi-container-yaml

ACI is currently a laboratory target, not the definition of production architecture.
