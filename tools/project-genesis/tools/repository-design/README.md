# Repository Design

Status: `INCUBATION / DOGFOODING`

## Purpose

Translate an approved project identity and boundary into a domain, organization and repository topology before physical repository creation.

## Inputs

- viability verdict;
- naming decision record;
- domain boundaries;
- preceding/adopted projects and capabilities;
- expected ownership and sovereignty;
- distribution/versioning needs.

## Required outputs

For every proposed repository:

- repository name;
- owning domain;
- organization/owner placement;
- purpose;
- relationship to parent/preceding projects;
- dependency direction;
- visibility recommendation;
- description/About text with target maximum of 350 characters;
- topics/tags;
- minimum conceptual documentation needed at birth;
- whether it is initially internal, promotion-ready, or independently justified.

## Rules

- Do not split repositories merely for aesthetic modularity.
- Do not collapse sovereign domains merely for convenience.
- A prospective independent component should be born at the path where it could later become a repository/subrepository.
- Repository decomposition must preserve immediate-domain dependency boundaries.
- Unknown placement remains `UNKNOWN`; do not invent an organization or domain.

## Completion

Output is a repository plan. It does not create repositories. Physical materialization belongs to the repository-seed stage.
