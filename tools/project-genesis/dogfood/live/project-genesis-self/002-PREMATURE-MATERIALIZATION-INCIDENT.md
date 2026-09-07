# Run 002 — Premature Materialization Incident

**Status:** LIVE DOGFOOD / PROCESS EVIDENCE
**Date:** 2026-09-07

## Event

Before the Project Genesis / PMFN protocol had stabilized, another team independently created a `project-discovery` POC inside `InitProjHQ/InitProj` and opened draft PR #2.

The work includes useful research and conceptual artifacts, but its placement occurred before domain ownership and the discovery protocol were complete.

## Why this matters

This is not only a repository-placement accident. It is direct evidence of a failure mode that Project Genesis must prevent:

```text
IDEA
  ↓
ENTHUSIASM / PARTIAL UNDERSTANDING
  ↓
PREMATURE DOMAIN ASSIGNMENT
  ↓
REPOSITORY MATERIALIZATION
  ↓
IMPLEMENTATION PRESSURE
```

The desired controlled path is:

```text
IDEA
  ↓
POSITIONING / DISCOVERY
  ↓
MINIMUM NECESSARY FACTORIZATION
  ↓
SOURCING / OWNERSHIP / DOMAIN EVIDENCE
  ↓
MATERIALIZATION AUTHORIZATION
  ↓
IMPLEMENTATION
```

## Protocol requirement derived from the incident

A project/tool creation flow must contain an explicit pre-materialization gate.

Candidate blocking conditions:

```text
DISCOVERY_INCOMPLETE
DOMAIN_OWNERSHIP_UNRESOLVED
SOURCING_UNRESOLVED
RESIDUAL_NOT_ESTABLISHED
MATERIALIZATION_NOT_AUTHORIZED
```

A downstream tool must not infer authorization merely because a concept, folder name, prompt or preliminary architecture exists.

## Evidence source

External dogfood branch:

```text
repository: InitProjHQ/InitProj
branch: docs/project-discovery-dogfood
PR: #2
```

A governance hotfix was added there to quarantine the material and preserve it as evidence rather than merge it as an InitProj-owned capability.

## Useful contributions observed in the external prototype

The prototype contains material worth reconciling into the sovereign live study, including:

- a strong neutral-positioning stance: `Not a verdict. A position.`;
- explicit evidence provenance/coverage/confidence;
- a preliminary PMFN stopping rule using decisional gain;
- separation of conceptual, architectural and execution exclusivity;
- a qualitative realization/reuse profile;
- pre-consultancy handoff concepts;
- an initial self-dogfood factorization;
- explicit admission that `COMPOSE` may be transversal rather than ordinal.

These are candidate contributions, not authoritative definitions. Each must be re-evaluated by the live dogfood protocol before adoption.

## Requirement generated

**IR-008 — Pre-materialization authorization gate**

Project Genesis must be capable of returning a state that explicitly prevents downstream identity/repository/tool materialization while discovery, domain ownership, sourcing or residual definition remain unresolved.

**IR-009 — Foreign-prototype ingestion**

The protocol must support importing an independently created prototype as evidence without granting it architectural authority. Imported artifacts must retain provenance and be classified as candidate findings until reconciled.

## Dogfood interpretation

The accident strengthens the case for the protocol only as evidence of a process problem. It does not prove that the proposed solution is unique or correct.

The correct response is to use the accident against the protocol itself: if the final protocol would not have prevented or clearly blocked this premature materialization, the protocol is incomplete.
