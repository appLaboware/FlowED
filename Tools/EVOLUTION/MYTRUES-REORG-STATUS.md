# MyTrues organization reorganization — execution status

Date: 2026-10-01

North: reorganize MyTrues as the generic decision protocol and IDEOS as an
independent DevOps intent client.

## DONE in FlowED staging

- [x] R0/R1 exact pause point recorded in `Tools/EVOLUTION/NEXT.md`.
- [x] MyTrues repositioned as a domain-generic decision protocol.
- [x] Existing executable v0.2 preserved without silently changing its schemas.
- [x] CCP formalized as a documentary/provenance layer through `CCP Record`.
- [x] Historical EDT/CCP material preserved with provenance.
- [x] MIT license staged for canonical MyTrues.
- [x] IDEOS positioned as DevOps intent CLI.
- [x] IDEOS specs staged:
  - `spec/syscall-table.md`;
  - `spec/capability-ports.md`;
  - `spec/form-factors.md`;
  - `spec/positioning.md`.
- [x] MIT license staged for canonical IDEOS.
- [x] `DecisionMemory` consumer port defined.
- [x] Thin MyTrues v0.2 adapter boundary materialized under IDEOS.
- [x] Adapter does not copy MyTrues implementation or access storage internals.
- [x] Immutable upstream lock format staged.
- [x] `ADOPTION-PROTOCOL` defined.
- [x] IDEOS -> MyTrues recorded as the first internal adoption case.
- [x] History-preserving organization migration script staged.
- [x] FlowED -> canonical MyTrues alignment designed as a pinned Git submodule.
- [x] Submodule transition script staged.
- [x] InFabric intentionally not created.

## BLOCKED only by target-org access / repository-admin operations

- [ ] Read the actual eight `MyTrues/*` repositories and replace unavailable
  inventory fields with exact:
  - `pushed_at`;
  - size;
  - content/tree summary;
  - head/default branch;
  - URL.
- [ ] Rename:
  - `MyTrues` -> `MyTrues_arquived_261001`;
  - `MyTrues_p` -> `MyTrues_p_arquived_261001`;
  - `cli` -> `cli_arquived_261001`;
  - `kernel` -> `kernel_arquived_261001`;
  - `paper` -> `paper_arquived_261001`;
  - `replication` -> `replication_arquived_261001`;
  - `site` -> `site_arquived_261001`;
  - `spec` -> `spec_arquived_261001`.
- [ ] Create `MyTrues/mytrues`.
- [ ] Create `MyTrues/ideos`.
- [ ] Execute history-preserving subtree/import process.
- [ ] Verify MIT license at both canonical roots.
- [ ] Record canonical initial commit SHAs and repository URLs.
- [ ] Run IDEOS adapter compatibility against the real canonical MyTrues SHA.
- [ ] Create real `upstreams/mytrues.lock.json` in IDEOS with:
  - canonical repo;
  - 40-hex commit SHA;
  - protocol version;
  - compatibility run URL.
- [ ] Replace FlowED `Tools/MYTRUES` with a git submodule pinned to the accepted
  canonical `MyTrues/mytrues` SHA.
- [ ] Verify a fresh FlowED clone with `--recurse-submodules`.
- [ ] Capture API response/URL evidence for every rename/create operation.

## Frozen product staging source

History-preserving canonical subtree import uses FlowED commit:

`0982911b09dc7738686db2f1ff953a7ce0c1fb8b`

This commit contains the complete product staging surface including the physical
IDEOS `DecisionMemory` adapter boundary.

Later commits only refine migration machinery/state and are not required as
product subtree source.

## After completion

Resume SESSION-006 at the exact R0 -> R1 point recorded in `NEXT.md`.

Do not create InFabric in this session.

## Archaeology consolidation

A complete accessible-repository scan was performed before canonical migration.

Canonical references:

- `Tools/MYTRUES/docs/archaeology/ECOSYSTEM-INVENTORY.md`;
- `Tools/MYTRUES/docs/ARCHAEOLOGY-SYNTHESIS.md`;
- preserved source copies under `Tools/MYTRUES/docs/archaeology/`;
- executable historical candidates under
  `Tools/MYTRUES/research/legacy-candidates/`.

The frozen migration SHA above includes this recovered material.
