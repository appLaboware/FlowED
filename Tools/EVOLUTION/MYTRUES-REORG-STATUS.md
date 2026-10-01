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

`65ea6ab7e81d0b4f8d664a6c4dfe663f2570777a`

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

## Runbook consistency note

The migration manifest and `reorganize-org.sh` now both point to the same
authoritative frozen source SHA:

`65ea6ab7e81d0b4f8d664a6c4dfe663f2570777a`

No known SHA drift remains between those two migration records.


## Google Drive archaeology

Google Drive archaeology was also completed for the current accessible Drive
surface.

Added:

- `Tools/MYTRUES/docs/archaeology/DRIVE-INVENTORY.md`;
- selected pre-repository source copies under
  `Tools/MYTRUES/docs/archaeology/drive/`;
- Drive-derived additions to `ARCHAEOLOGY-SYNTHESIS.md`;
- `Tools/MYTRUES/research/SCIENCE-FRONTIER-DISCOVERY-GATE.md`.

Literal `MyTools` search produced no distinct relevant project lineage.

The authoritative frozen product SHA above includes these additions.

## Additional uploaded research

The current staging also preserves and classifies:

- `MTR-METAOBJECTIVE-001 — MYTRUES APPLIED TO MYTRUES` as RECORD ONLY;
- `MYTRUES-META-PROPOSAL-001` as proposal awaiting explicit PO decision;
- `GROK-MYTRUES-COGNITIVE-DISCOVERY-001` as external candidate research with
  an independent qualification record.

No Microbrain implementation is authorized by these artifacts.

The Grok package is not promoted to qualified Discovery because its received
payload contains required JSON parse failures and manifest/payload count
inconsistencies.

The authoritative frozen product SHA above includes these additions.

## Conversation-reconstruction archaeology

Four additional historical reconstructions were reviewed and indexed:

- `Agentes no VSCode Codex.MD`;
- `VRAMPP-001.MD`;
- `VRAMPP-002 - 043b - D2b.MD`;
- `Branch · Agentes no VSCode Codex.MD`.

Promoted documentary invariants:

- No Retroactive Cognition;
- explicit canonical-promotion boundary.

Preserved but not promoted as core:

- AKU/digital-neuron hypothesis;
- MyTrues Discovery product branch;
- proposed family Discovery/Cognition/Verify;
- old commercial/licensing/org layouts.

The authoritative frozen product SHA above includes these additions.

## Open extension / engine ecosystem north

The current staging now records:

- OPEN protocol boundary through `DecisionEngine`;
- provisional ports for DecisionMemory, DecisionProfile, Evidence, Provenance,
  Authority, CognitionProposal, Retrieval, Outcome, View and Source;
- independently distributable adapters/plugins;
- MCP as adapter, not core;
- LLM cognition harvester as candidate producer behind explicit authority;
- conformance-aware registry/marketplace as a product direction;
- PPX as direct prior art/adoption candidate for portable preference profiles;
- science/product opportunity map and capability/prior-art inventory.

Current Science Frontier status:

- GO for continued prior-art and open interoperability design;
- GO for open port/adapter/plugin/conformance work;
- DONT_GO for claiming preference-profile portability as novel;
- DONT_GO for claiming plugin/marketplace architecture as novel;
- DONT_GO for inventing a proprietary DecisionEngine yet;
- possible research residual remains cross-engine decision semantic preservation,
  temporal replay/provenance, authority gating and memory-reuse behavior.

The authoritative frozen product SHA above includes these additions.
