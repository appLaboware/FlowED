# Project Genesis Tool

Status: `INCUBATION / DOGFOODING`

## Purpose

Orchestrate the zero-stage from a raw idea until a project is admissible for repository materialization and POC work.

This tool is intentionally decomposed into promotion-ready subtools. Each subtool may remain internal forever or later become an independent repository/subrepository without changing its architectural position.

## Pipeline

```text
RAW IDEA
  ↓
viability-gate
  ↓
GO / GO-BY-ADOPTION / NO-GO
  ↓ only if project identity is justified
semantic-naming
  ↓
repository-design
  ↓
repository-seed
  ↓
early POC / later durable project structure
```

## Founding rules

1. An idea does not authorize project creation.
2. Discovery precedes naming.
3. Adoption is attempted before proprietary construction.
4. Naming receives a validated model; it does not re-run viability.
5. Repository design receives an approved identity and boundary.
6. Repository seed materializes only what the current stage actually needs.
7. External AIs receive only the context necessary for their current task; internal future tools are not mentioned unless operationally necessary.
8. Every child tool owns its contract and can be promoted independently.

## Subtools

- `tools/viability-gate/` — adversarial viability, adoption-first and residual determination.
- `tools/semantic-naming/` — naming after viability and boundary stabilization.
- `tools/repository-design/` — domain, organization, repository decomposition, descriptions and topics.
- `tools/repository-seed/` — minimal repository materialization and generic AI handoff/bootstrap artifacts.

## Authority

The governing zero-stage blueprint is documented under `docs/pt-br/protocols/project-genesis/`.
The repository bootstrap authority remains the Repository Bootstrap Protocol.

This directory is an implementation/incubation surface, not a replacement for those protocols.
