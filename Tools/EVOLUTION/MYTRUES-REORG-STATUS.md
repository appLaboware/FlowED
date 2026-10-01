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

`121c63642c4cc552c46a7cf3ff70ab57924cb2be`

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

`121c63642c4cc552c46a7cf3ff70ab57924cb2be`

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

## Chat extraction archaeology batch 001

Twelve conversation-derived MyTrues reports were triaged by evidentiary
strength.

Added:

- `Tools/MYTRUES/docs/archaeology/CHAT-EXTRACTION-TRIAGE-001.md`;
- source-confidence distinction between chat-local extraction, mixed
  reconstruction and consolidation/index;
- corresponding additions to `ARCHAEOLOGY-SYNTHESIS.md`.

No additional original-chat interrogation is required before continuing with
the next archaeology batch.

The authoritative frozen SHA above includes this batch.

## Chat extraction archaeology batch 002

Nine additional conversation-derived reports were reviewed.

Added:

- `docs/archaeology/CHAT-EXTRACTION-TRIAGE-002.md`;
- `docs/archaeology/EARLY-TECHNICAL-LINEAGE.md`;
- `research/branches/EXPERIENCE-FIRST-MYTRUES.md`;
- Experience-first Science Frontier gate.

The previously unresolved Experience-first item is now **resolved** by a
chat-local forensic audit:

- Experience-first was not explicitly PO-approved as the MyTrues identity;
- Memory Mesh/Systematic Agent was approved only as an experimental
  metaobjective;
- current v0.2 decision-protocol identity remains unchanged.

The authoritative frozen SHA above includes this batch.

## Experience-first forensic result

Added:

- `Tools/MYTRUES/docs/archaeology/forensics/EXPERIENCE-FIRST-CHAT-FORENSIC-001.md`.

Conclusion:

- `Experience is the primary unit` = assistant formulation;
- `MyTrues = SQL of experience` = assistant formulation;
- Decision Cell / Cognitive Pre-flight / Cartridge / Amortization / Compiled
  Cognition = research proposals, not PO-approved protocol entities;
- Memory Mesh + deterministic Systematic Agent + LLM-assisted candidate linking
  = PO-approved **metaobjective/experiment**;
- provider-scoped v0.2 memory remains the executable baseline;
- PAUSE/SANITIZE/RESOLVE remains unrepealed.

No further forensic follow-up from batch 002 is currently required.

## Chat extraction archaeology batch 003

The final uploaded batch has been triaged and indexed.

Added:

- `Tools/MYTRUES/docs/archaeology/CHAT-EXTRACTION-TRIAGE-003.md`;
- Cognit.me/MyTrues boundary in the extension-ecosystem documentation;
- CCP de Partida / versioned epistemic starting-point discipline in the Science
  Frontier gate;
- batch-003 additions in `ARCHAEOLOGY-SYNTHESIS.md`;
- new evidence annotation in the Experience-first research branch.

Current unresolved historical items:

1. whether `VRMP-MYTRUES 260901 01` contains explicit human-PO promotion of
   Experience as the canonical primary MyTrues unit;
2. who/what authority authored the `MyTrues = epistemic history of the subject`
   boundary in `VRMP-EDT 260901 01`;
3. whether `Education-Driven Things` was explicitly human-PO approved there.

These are genealogy/naming questions only.

They do not modify the current MyTrues Open Decision Protocol v0.2 executable
baseline.

The authoritative frozen SHA above includes the final uploaded batch.

## EDT / CCP research boundary

Current researcher clarification and historical source pack have been integrated.

Authoritative current orientation:

```text
EDT
= Education-Driven Thinking
= conceptual/philosophical doctoral thesis

CCP
= Caminho Cognitivo do Criador / Creator Cognitive Path
= central concept under study

MyTrues
= technical instrument/reference implementation
= operationalizes/tests CCP
= may yield independent technical publications/product opportunities
```

Consequences:

- do not make EDT a MyTrues runtime/product layer;
- do not require MyTrues technical novelty as a precondition for EDT novelty;
- do not use current MyTrues implementation choices to rewrite historical EDT;
- Education-Driven Things is non-canonical under current researcher orientation.

Historical source pack:

`Tools/MYTRUES/docs/archaeology/EDT-HISTORICAL-SOURCES-001.md`.

Current boundary:

`Tools/MYTRUES/docs/EDT-CCP-MYTRUES-BOUNDARY.md`.

Only the separate global MyTrues `Experience as primary unit` forensic question
remains if product ontology needs to be frozen.

## Final VRMP forensic closure

The two remaining batch-003 original-chat audits are complete.

Resolved:

- EDT current canonical name: Education-Driven Thinking;
- Education-Driven Things: temporary historical human naming branch;
- Experience: important but not established as canonical primary MyTrues unit;
- subject-history vs Thing-history: PM/PO working boundary, not direct human
  thesis wording;
- MyTrues = Minhas Verdades: direct human naming evidence;
- white-box/upstream-first product direction: direct human decision.

No remaining batch-003 forensic question blocks the current genealogy.

The authoritative frozen SHA above includes this closure.


## Real MyTrues organization access restored

The GitHub App installation now includes the actual `MyTrues` organization.

Installation id:

`166957143`

Repository selection:

`all`.

All eight expected legacy repositories are readable and report admin repository
permission.

`Tools/MYTRUES/ORG-INVENTORY.md` is now COMPLETE with:

- pushed_at;
- size;
- default branch;
- exact head SHA;
- content summary;
- URL.

The previous target-org access blocker is closed.

## Definitive organization topology

Added:

`Tools/MYTRUES/ORG-TOPOLOGY-2026-10-01.md`

Definitive repository set:

### public/open

- `MyTrues/mytrues`;
- `MyTrues/ccp`;
- `MyTrues/research`;
- `MyTrues/registry`;
- `MyTrues/ideos`;
- `MyTrues/site`.

### private

- `MyTrues/edt`;
- `MyTrues/mytrues-enterprise`.

The topology explicitly separates:

- EDT thesis;
- CCP concept/spec;
- reproducible science;
- open product/common protocol;
- extension registry;
- reference client;
- closed commercial extensions.

## Frontier reference suite

Added:

`Tools/MYTRUES/research/FRONTIER-REFERENCE-SUITE-2026.md`.

The suite includes current reference benchmarks/systems such as:

- LongMemEval-V2;
- MemoryArena;
- AMemGym;
- LoCoMo-Plus;
- GroupMemBench;
- RHELM;
- MemGym;
- Microsoft Memora;
- Microsoft human-inspired memory architecture;
- Microsoft MAGE;
- Google ReasoningBank;
- Google MARS;
- Google agent-system scaling work;
- provenance/design-rationale/human-authority references.

These are baselines/reference tests, not evidence of MyTrues novelty.

## Current remaining blocker

The current GitHub connector exposes repository content/branch/issue/PR writes
and reports admin permission, but does **not** expose repository-level:

- rename;
- create;
- visibility/settings mutation.

The local runtime also has no `gh` CLI.

Therefore the only remaining blocker to actual organization mutation is the lack
of a repository-admin mutation surface in this session.

The exact executable runbook is staged at:

`Tools/MYTRUES/migration/reorganize-org.sh`.

It now performs:

- all eight legacy renames;
- creation of the eight definitive repositories;
- visibility split;
- history seeding for CCP/EDT/research/site;
- filtered product import for MyTrues;
- IDEOS import;
- registry/enterprise boundary seeding;
- final archive/read-only lock;
- migration evidence generation.
