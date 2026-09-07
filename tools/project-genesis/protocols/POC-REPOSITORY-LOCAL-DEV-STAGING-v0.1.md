# POC Repository-Local `_DEV` Staging Protocol v0.1

Status: `EXPERIMENTAL / PRE-INITPROJ / GENERIC`

## Purpose

Define how a pre-InitProj POC preserves development-only artifacts next to each repository-shaped unit without forcing the POC to adopt the full InitProj DEV/PROD topology prematurely.

## Core rule

For every directory in a POC that represents a repository boundary, whether it is already an actual Git repository or is intended to become one, the repository root MAY contain a reserved `_DEV/` directory.

`_DEV/` is the local staging area for artifacts that belong to the future development environment of that repository but do not belong to the repository's canonical/product surface.

The directory containing `_DEV/` is the repository root candidate.

## Semantics

```text
<repo-root>/
├── _DEV/        # development-only staging; future migration target
├── ...          # canonical repository content
```

A present but empty `_DEV/` means:

> this repository boundary permits a development environment, but no development-only artifacts have yet been materialized here.

An absent `_DEV/` means only that no local development-staging area has been declared for that repository boundary.

It MUST NOT be interpreted as proof that the repository has no development concerns.

## What belongs in `_DEV/`

Examples:

- planning notes tied specifically to this repository;
- temporary analysis artifacts;
- implementation experiments not yet promoted;
- rejected spikes and their evidence;
- migration notes;
- repository-local research notes;
- draft prompts or agent instructions specific to this repository;
- temporary tooling artifacts;
- reconciliation notes for future InitProj ingestion;
- evidence that should survive migration but should not be published as canonical repository content.

## What does not belong in `_DEV/`

- canonical product/specification documentation;
- source code that is already accepted repository content;
- public README material;
- release artifacts;
- files required for normal operation of the repository;
- data that should remain outside version control for security/privacy reasons;
- organization-wide development rules that belong to a higher sovereign domain.

## Repository-root law

`_DEV/` is always interpreted relative to the repository boundary that contains it.

Therefore:

```text
A/
├── _DEV/
└── B/
    └── _DEV/
```

means that `A` and `A/B` are two distinct repository candidates/boundaries, each with its own development-staging scope.

Artifacts MUST NOT be moved upward merely because a parent `_DEV/` exists.

## Pre-InitProj role

This protocol is intentionally lighter than InitProj.

It does not create sessions, INBOX/OUTBOX, DEV/PROD separation, role hierarchy, or NGit topology.

It only preserves a deterministic place for repository-local development artifacts before those mechanisms exist.

## InitProj migration rule

When a POC is ingested by InitProj, every `_DEV/` directory MUST be inventoried before normal project work begins.

For each `_DEV/` artifact, the ingestion process MUST classify one destination:

```text
MOVE_TO_INITPROJ_DEV
MAP_TO_SESSION
MAP_TO_PLAN
MAP_TO_MEMORY
MAP_TO_EVIDENCE
MAP_TO_DECISION_OR_EXCEPTION
KEEP_REPOSITORY_LOCAL
PROMOTE_TO_CANONICAL_REPOSITORY
REJECT_AS_OBSOLETE
HUMAN_REVIEW_REQUIRED
```

No artifact may disappear silently.

The migration MUST preserve provenance from original POC path to final InitProj destination.

## Relationship to NGit

NGit currently defines a different concern: separate granular DEV history and semantic PROD repository history. Its documented topology places canonical product worktrees under `PROD/` while the outer project repository captures granular snapshots.

This `_DEV/` protocol does not replace or modify NGit semantics.

Instead:

```text
PRE-INITPROJ POC
repository-local _DEV staging
        ↓ ingestion
INITPROJ DEV environment
        ↓ where applicable
NGit-managed DEV/PROD repository topology
```

The POC must not fabricate NGit metadata before InitProj/NGit adoption merely to resemble the future topology.

## GO criteria

Use `_DEV/` when:

- the enclosing directory is a real or intended repository boundary;
- there are development-only artifacts that should survive future ingestion;
- keeping them in canonical repository content would contaminate the repository surface; or
- an empty marker is useful to declare that a repository-local development scope is allowed.

## DON'T-GO criteria

Do not use `_DEV/`:

- as a generic dumping ground;
- for organization-wide planning that has no repository-local ownership;
- to duplicate canonical content;
- to hide unresolved ownership decisions indefinitely;
- as a substitute for proper InitProj sessions after InitProj has been adopted;
- to model NGit DEV/PROD history before that topology actually exists.

## Ingestion invariant

`POC_STRUCTURE != INITPROJ_STRUCTURE`

but:

`POC_INFORMATION -> INITPROJ_DESTINATION` MUST be complete, auditable, and provenance-preserving.

## Human interpretation

The human meaning is simple:

> `_DEV/` marks material that belongs to the making of that repository, not necessarily to what the repository ultimately publishes or operates as its canonical surface.

The folder can be empty. Its presence declares a possible development space for that repository boundary.
