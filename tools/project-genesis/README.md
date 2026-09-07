# Project Genesis Tool

Status: `INCUBATION / DOGFOODING`

## Purpose

Orchestrate the zero-stage from a raw idea until the proposal has an evidence-informed position and, only when warranted by the human decision, can continue toward identity, repository materialization and POC work.

Project Genesis is not an idea judge. It is an evidence-positioning and project-birth system.

> **Not a verdict. A position.**

> **The AI does not decide for the human. It lets the idea confront available evidence before the human decides.**

The tool is intentionally decomposed into promotion-ready subtools. Each subtool may remain internal forever or later become an independent repository/subrepository without changing its architectural position.

## Pipeline

```text
RAW IDEA
  ↓
viability-gate / evidence positioning
  ↓
PROJECT EVIDENCE DOSSIER
  ↓
HUMAN DECISION
  ├─ stop / reformulate / investigate / adopt existing
  └─ continue
        ↓
semantic-naming
        ↓
repository-design
        ↓
repository-seed
        ↓
early POC / later durable project structure
```

The downstream path is not mandatory. A valuable run may end by showing that adoption is sufficient, that more research is required, or that the human prefers another direction.

## Founding rules

1. An idea does not authorize project creation.
2. Discovery precedes naming.
3. Adoption is attempted before proprietary construction.
4. The protocol does not collapse evidence into a magic idea score.
5. Pertinence, existing coverage, conceptual exclusivity, architectural exclusivity, execution exclusivity, residual factorization and evidence strength remain independent dimensions.
6. Every metric must be explainable through evidence, counterevidence, uncertainty and provenance.
7. The proposal may evolve during investigation; idea evolution is a first-class artifact.
8. Naming receives a sufficiently stabilized model; it does not re-run the evidence-positioning stage.
9. Repository design receives an approved identity and boundary.
10. Repository seed materializes only what the current stage actually needs.
11. External AIs receive only the context necessary for their current task; internal future tools are not mentioned unless operationally necessary.
12. Every child tool owns its contract and can be promoted independently.
13. Human decision, responsibility and value judgment remain human.

## Pre-consultation projection

Project Genesis may be used as a pre-consultation instrument by consultancies, incubators, universities, accelerators and entrepreneurship-support institutions.

The objective is to compress searchable/repetitive investigation before a human session so that specialist time can focus on interpretation, tacit experience, trade-offs, values and responsibility.

See:

- `docs/PRE-CONSULTATION-AND-HUMAN-DECISION-BOUNDARY-v0.1.md`
- `docs/PROJECT-EVIDENCE-DOSSIER-CONTRACT-v0.1.md`

## Subtools

- `tools/viability-gate/` — evidence positioning, adversarial discovery, adoption-first analysis and residual factorization determination.
- `tools/semantic-naming/` — naming after sufficient model/boundary stabilization.
- `tools/repository-design/` — domain, organization, repository decomposition, descriptions and topics.
- `tools/repository-seed/` — minimal repository materialization and generic AI handoff/bootstrap artifacts.

## Dogfood

The tool must be tested against itself before proprietary implementation grows.

Current dogfood seeds:

- `dogfood/PROJECT-GENESIS-SELF-DOGFOOD-v0.1.md`
- `dogfood/INITPROJ-SEED-DOGFOOD-v0.1.md`

Dogfood is successful even when it proves that an internal capability should be removed, delegated, adopted or composed from existing solutions.

## Authority

The governing zero-stage blueprint is documented under `docs/pt-br/protocols/project-genesis/`.
The repository bootstrap authority remains the Repository Bootstrap Protocol.
The PMFN research hypothesis is documented under `docs/pt-br/research/proposals/`.

This directory is an implementation/incubation surface, not a replacement for those protocols or research authorities.
