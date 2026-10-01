# MyTrues Organization Migration Manifest

Date: 2026-10-01

Status: **STAGED — repository-admin operations pending target-org access/tooling**

Frozen FlowED migration source SHA:

`d67d3e18ec0ac1f8bb363b25a9081b5239162ec4`

The canonical subtree import MUST use this SHA, not a later moving branch head.

## Rename map

No repository is deleted.

Exact required renames:

- `MyTrues` -> `MyTrues_arquived_261001`;
- `MyTrues_p` -> `MyTrues_p_arquived_261001`;
- `cli` -> `cli_arquived_261001`;
- `kernel` -> `kernel_arquived_261001`;
- `paper` -> `paper_arquived_261001`;
- `replication` -> `replication_arquived_261001`;
- `site` -> `site_arquived_261001`;
- `spec` -> `spec_arquived_261001`.

## New canonical repositories

### `MyTrues/mytrues`

Purpose: generic decision protocol.

Initial code/content source:

- `appLaboware/FlowED/Tools/MYTRUES`;
- protocol schemas;
- OpenAPI;
- reference `provider_server.py`;
- conformance `test_protocol.py`;
- `docs/ALGORITHM-BOUNDARY.md`;
- seed/conformance material that remains correctly classified.

Historical documentary source:

- `InitProj-260119/MyTrues`;
- inspected source head:
  `dc891f1d354b85c6f11666d62cb1e59dde839b2e`;
- CCP/EDT material is imported as documentary lineage, not as runtime authority.

License: MIT.

### `MyTrues/ideos`

Purpose: DevOps intent CLI.

Initial source:

- `appLaboware/FlowED/Tools/IDEOS`;
- `spec/syscall-table.md`;
- `spec/capability-ports.md`;
- `spec/form-factors.md`;
- `spec/positioning.md`.

License: MIT.

## History-preserving import

Preferred method for the FlowED subtrees:

```text
git subtree split --prefix=Tools/MYTRUES d67d3e18ec0ac1f8bb363b25a9081b5239162ec4 -b import/mytrues
git subtree split --prefix=Tools/IDEOS d67d3e18ec0ac1f8bb363b25a9081b5239162ec4 -b import/ideos
```

The resulting filtered branches preserve relevant FlowED commit history and are
used to seed the new canonical repositories.

Historical CCP/EDT lineage should be imported as a history-preserving
documentation subtree. A valid approach is:

1. fetch `InitProj-260119/MyTrues` at the recorded historical commit;
2. filter/move that history under `docs/legacy-ccp/`;
3. merge the filtered history into `MyTrues/mytrues`;
4. preserve the original commit identities/provenance in the merge history.

Do not use a copy-and-paste-only import when a history-preserving import is
available.

## Original-source rule

After migration:

- MyTrues behavior changes only in `MyTrues/mytrues`;
- IDEOS behavior changes only in `MyTrues/ideos`;
- FlowED retains migration/evidence material only;
- IDEOS consumes MyTrues by immutable SHA through `DecisionMemory`;
- no implementation code is copied from MyTrues into IDEOS.

## Completion evidence

The migration is complete only when the record contains:

- API/UI evidence for all eight renames;
- URLs for both new canonical repositories;
- initial canonical commit SHA for each;
- evidence that history survived the import;
- MIT license in both repositories;
- real IDEOS -> MyTrues lock SHA;
- adapter compatibility run URL.

## Migration-only files

The history-preserving split starts from the frozen FlowED SHA above, but the
canonical product repositories must not retain FlowED reorganization machinery.

Before the first canonical push, remove from the MyTrues import branch:

- `ORG-INVENTORY.md`;
- `MIGRATION-MANIFEST.md`;
- `migration/`.

These remain in FlowED as migration evidence.

The canonical IDEOS import similarly does not receive FlowED-level
`Tools/EVOLUTION/` documents; only the IDEOS subtree is imported.

## Google Drive archaeology

The frozen source above includes the Drive archaeology consolidation:

- pre-repository CCW/CCC/OMGDiary/TRUE lineage;
- concrete decision/cognition pair fixtures;
- Drive inventory;
- recovered 2026 Science Frontier discovery contract;
- `research/SCIENCE-FRONTIER-DISCOVERY-GATE.md`.

These are documentary/research inputs unless separately promoted by versioned
protocol work.

## Additional research intake

The frozen source also includes the 2026-10-01 supplied research artifacts:

- canonical staging copy of `MTR-METAOBJECTIVE-001 — MYTRUES APPLIED TO MYTRUES`;
- `MYTRUES-META-PROPOSAL-001` intake/governance record;
- independent qualification record for
  `GROK-MYTRUES-COGNITIVE-DISCOVERY-001`;
- corresponding updates to the archaeology synthesis and Science Frontier gate.

These are research/governance inputs only. They do not authorize Microbrain
execution or promote the Grok run to qualified Discovery.

## Conversation-reconstruction archaeology

The frozen source also includes four 2026-10-01 uploaded reconstructions of
earlier MyTrues/EDT/CCP conversations.

They contributed:

- No Retroactive Cognition;
- CCP-as-source -> Views-as-build;
- NORM/WHY/TRACE/ADR view taxonomy;
- AKU/digital-neuron historical hypothesis;
- MyTrues Discovery historical product branch;
- MCP-as-adapter rule;
- secondary claims requiring primary verification, including EDT expansion and
  a reported CCP DOI.

These are archaeology/research inputs unless separately promoted.

## Open extension ecosystem / DecisionEngine boundary

The frozen source also includes the 2026-10-01 architecture/research update that:

- extends the OPEN MyTrues boundary through a replaceable `DecisionEngine` port;
- defines a provisional hexagonal port/adapter/plugin taxonomy;
- permits OSS, commercial, private, human and hybrid decision engines behind
  the same open interoperability boundary;
- treats MCP as an adapter/transport, not internal architecture;
- treats LLM cognition extraction as candidate/staging generation, not automatic
  canonical authority;
- introduces a conformance-aware registry/marketplace direction;
- adds focused science/product prior-art research;
- adopts a PPX-first direction for portable preference/profile interchange;
- narrows the scientific residual to decision-semantic preservation, replay,
  provenance and authority across heterogeneous engines.

These are target-design/research inputs. They do not silently modify the
executable v0.2 failure profile and do not authorize a proprietary engine.

## Chat extraction archaeology batch 001

The frozen source also includes the first chat-extraction provenance triage:

- source-confidence classification for 12 conversation-derived reports;
- OMGDiary/MyTrues two-axis historical origin;
- historical TrueEngine nomenclature;
- early local-decision-before-generic-LLM semantics;
- independent CCP technical evidence including `Raw log is not CCP`;
- candidate multi-time epistemic model;
- chronology/causality separation;
- defeated-path memory hypothesis;
- KNOWING versus SAYING boundary;
- reinforcement that MyTrues Discovery remains a separate historical branch.

These findings are archaeology/research inputs. They do not modify v0.2
conformance or authorize new runtime behavior.

## Chat extraction archaeology batch 002

The frozen source also includes:

- source-confidence triage for nine additional chat-derived reports;
- exact SHA-256 identities of the reviewed uploads;
- strict negative evidence from a FlowDisP-only chat;
- explicit `MyTools`/MyTrues ambiguity handling;
- preservation of the historical Datalog/Prolog/Cozo logic/rules branch;
- correction that current OpenAPI staging is 0.2.0;
- the Experience-first MyTrues research branch;
- a Science Frontier gate requiring forensic PO-intent verification before any
  Experience-first domain promotion.

The Experience-first branch is research only and does not redefine v0.2.

## Experience-first forensic resolution

The frozen source includes the primary-chat forensic follow-up that resolves the
batch-002 Experience-first ambiguity.

Result:

- Experience-first is **not** a PO-approved MyTrues identity pivot;
- `MyTrues = SQL of experience` is not PO-approved;
- Memory Mesh/Systematic Agent is preserved only as an approved experimental
  metaobjective;
- provider-scoped v0.2 memory remains unrepealed;
- PAUSE/SANITIZE/RESOLVE remains current executable behavior.

No v0.2 schema or runtime change follows from this forensic result.

## Chat extraction archaeology batch 003

The frozen source includes the final uploaded chat-extraction batch:

- exact-byte SHA-256 inventory for nine additional reports;
- Cognit.me / InitProj extraction kept upstream of MyTrues ingestion;
- RAG characterization retained only as ungrounded incidental history;
- CCP de Partida / Fundação Epistêmica as a research-governance candidate;
- subject-history versus Thing-history EDT/MyTrues boundary candidate;
- global Experience-first question reopened by a different source without
  changing the v0.2 baseline;
- unresolved EDT expansion conflict:
  Education-Driven Thinking vs Education-Driven Things.

Two original-chat forensic follow-ups remain before global genealogy is fully
frozen:

- VRMP-MYTRUES 260901 01;
- VRMP-EDT 260901 01.

These unresolved historical questions do not alter current v0.2 behavior.

## EDT / CCP research boundary clarification

The frozen source includes a current researcher clarification plus historical
January/February-2025 EDT/CCP source pack.

Current boundary:

- EDT = Education-Driven Thinking;
- EDT = conceptual/philosophical doctoral research thesis in engineering;
- CCP = Caminho Cognitivo do Criador / Creator Cognitive Path, central concept;
- MyTrues = technical instrument/reference implementation used to
  operationalize/test CCP and potentially generate independent technical papers
  or product opportunities.

MyTrues technical novelty is not a prerequisite for EDT conceptual novelty.

Education-Driven Things is non-canonical under current researcher orientation.

The historical source pack is indexed without rewriting its earlier academic
stage.
