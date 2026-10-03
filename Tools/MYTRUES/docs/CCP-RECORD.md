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

## Consumption rule

The default consumer path is:

`current decision -> use it`

A consumer SHOULD traverse the linked CCP Record when it needs to:

- understand why the current decision exists;
- challenge or propose a different decision;
- re-evaluate after context/evidence changes;
- audit provenance;
- avoid repeating an already tested/rejected path.

Therefore CCP is **available context, not mandatory payload for every decision
request**.

This rule is recovered from the earliest operational CCC flow: consult the
current decision first, then traverse its cognitive path only when deeper
context is necessary.

A client must not require hidden chain-of-thought. The CCP Record contains
explicitly recorded rationale/evidence/provenance chosen for preservation.

## No Retroactive Cognition

A CCP Record MUST preserve the decision-relevant state that existed when the
recorded cognition/decision occurred.

Later knowledge MUST NOT silently rewrite an earlier cognitive state as if that
knowledge had already been available.

When later evidence changes the position, the preferred representation is:

`old recorded state -> new evidence/cognition -> reevaluation -> superseding/new state`

rather than destructive reinterpretation of the historical record.

This does not prohibit correcting transcription or metadata errors. Such
corrections should themselves remain attributable when they materially affect
meaning.

The purpose is temporal epistemic honesty: a future reader must be able to ask
both "what is believed/decided now?" and "what was believed/decided then, using
the evidence available then?"

## Canonical promotion boundary

A generated proposal, agent OUTBOX, candidate relation, draft decision or
external-model output is not canonical merely because it exists.

Promotion into canonical decision memory requires the authority/process defined
by the selected provider or deployment policy.

For an unknown operational case in the current reference behavior, that means an
explicit provider resolution before retention.

The generic invariant is:

`proposal/staging -> authority decision -> canonical retention`

not:

`proposal/staging -> automatic truth`
