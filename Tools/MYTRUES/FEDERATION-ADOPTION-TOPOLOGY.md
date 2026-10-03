# MyTrues Federation / Adoption Topology

Date: 2026-10-01

Status: **CURRENT ORGANIZATIONAL NORTH**

## Principle

A project should live in the organization that owns its identity and lifecycle.

Other projects should consume it by **adoption/reference**, not by copying it
into their own organization.

This applies equally to product and academic artifacts.

## Current canonical ownership

### IDEOS

Canonical organization:

`IDEOS-DEV`

Canonical repository observed on 2026-10-01:

`IDEOS-DEV/IDeOS-core`

- visibility: private;
- default branch: `main`;
- head: `5b43b1bda1f9ab3c91424dc5c05346827a031ffd`;
- URL: `https://github.com/IDEOS-DEV/IDeOS-core`.

Therefore:

`MyTrues/ideos` is **not** a canonical target.

IDEOS is an independent product/client.

MyTrues may record IDEOS as a downstream/reference adoption, but must not own a
duplicate IDEOS implementation.

### MyTrues

Canonical organization:

`MyTrues`

Canonical technical product target:

`MyTrues/mytrues`.

### FlowED

FlowED remains an independent orchestrating/project environment.

Its relationship is:

```text
FlowED
├─ pinned reference/submodule -> MyTrues
└─ pinned reference/submodule -> IDEOS
```

Neither product should be copied into FlowED as a second canonical source.

## Academic incubation

### CCP

Current temporary/incubation repository:

`MyTrues/ccp`.

Long-term north:

- CCP should eventually have an academic organization/repository of its own;
- the history should be transferred/preserved, not recopied;
- MyTrues then records a pinned adoption/reference to the external canonical CCP
  source.

### EDT

Current temporary/incubation repository:

`MyTrues/edt`.

Long-term north:

- EDT should eventually have an academic organization/repository of its own;
- thesis/research history should be transferred/preserved;
- MyTrues should reference/adopt published or operationally relevant EDT/CCP
  artifacts rather than own the thesis.

## Transfer pattern for future academic separation

When an academic project receives its own organization:

1. freeze current incubation SHA;
2. create/verify the target organization;
3. transfer or history-preserving migrate the canonical repository;
4. verify issues/history/tags/branches;
5. record the new canonical URL and immutable SHA;
6. update downstream adoption locks;
7. leave no second writable canonical copy.

Preferred GitHub operation:

`repository transfer`

when feasible, because it preserves repository identity/history better than a
copy.

## Adoption record pattern

A downstream repository may keep an explicit adoption record such as:

```text
upstreams/
  mytrues.lock.json
  ccp.lock.json
  ideos.lock.json
```

Each record should contain at least:

- canonical repository URL;
- immutable commit SHA;
- semantic/protocol version when relevant;
- role: upstream / downstream / research-reference;
- compatibility/evidence URL where relevant;
- date accepted.

A Git submodule may be used when the downstream project needs the upstream tree
physically.

A lock/reference file is better when only provenance/compatibility is needed.

## Direction matters

Do not describe all relationships as "adoption" in the same direction.

Examples:

- **IDEOS adopts MyTrues** as a decision-memory capability/client dependency.
- **FlowED adopts/references IDEOS** and **FlowED adopts/references MyTrues**.
- **MyTrues does not adopt IDEOS as a runtime dependency**; IDEOS is a downstream
  reference client.
- **EDT uses MyTrues as an experimental instrument**.
- **MyTrues may reference/adopt CCP semantics** once CCP is externalized.

## Current MyTrues organization target

Permanent product/technical repos:

- `mytrues`;
- `registry`;
- `research` — MyTrues technical/reproducible research;
- `site`;
- `mytrues-enterprise`.

Temporary academic incubation:

- `ccp`;
- `edt`.

Not canonical in MyTrues:

- `ideos`.

## Misplaced MyTrues/ideos staging repo

The repository `MyTrues/ideos` was created empty during organization
reorganization before this ownership correction.

It should not receive IDEOS content.

Safe disposition:

- make private immediately;
- rename to `ideos_misplaced_arquived_261001`;
- archive/read-only;
- description must point to canonical `IDEOS-DEV/IDeOS-core`.

Do not delete it during migration; preserve the mistake as provenance.
