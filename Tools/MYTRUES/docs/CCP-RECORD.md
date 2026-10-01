# CCP Record

Status: documentary/provenance layer for MyTrues.

## Definition

A **CCP Record** is a decision record enriched with the **Caminho Cognitivo do
Criador (CCP)** that led to the recorded decision.

The protocol decision and the CCP record are related but distinct:

- the decision answers what was decided;
- the CCP record preserves how and why that decision emerged.

## Minimum documentary semantics

A CCP Record SHOULD be able to preserve, when available:

- decision identity;
- creator/authority identity or pseudonymous authority reference;
- problem/context understood at decision time;
- alternatives considered;
- assumptions and constraints;
- evidence consulted;
- rationale;
- rejected alternatives and reasons;
- selected decision;
- expected consequences;
- observed outcome;
- later revisions/re-evaluations;
- provenance links to source material.

## Boundary

CCP is not:

- a requirement that every client expose private reasoning;
- a chain-of-thought capture mandate;
- a decision algorithm;
- a DevOps-specific concept;
- authority by itself.

The recorded documentary layer may be partial, sanitized or access-controlled.

## Relationship to MyTrues

MyTrues provides the generic decision interoperability contract.

A provider MAY attach or link a CCP Record to a decision according to deployment
policy.

The reference wire protocol may evolve to carry standardized provenance links,
but the current v0.2 executable profile remains unchanged by this migration.

## Historical lineage

The documentary concept comes from the earlier EDT/CCP MyTrues lineage.

For provenance, the migration baseline references:

- `InitProj-260119/MyTrues`;
- inspected historical head:
  `dc891f1d354b85c6f11666d62cb1e59dde839b2e`;
- MIT-licensed historical material under `docs/pt-br/` and
  `CORE/mytrues-evolution/`.

The historical texts are preserved as documentary lineage, not as normative
runtime behavior.
