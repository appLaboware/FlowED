# MyTrues Organization — Definitive Repository Topology

Date: 2026-10-01

Status: **APPROVED PRIVATE-FIRST MIGRATION TARGET / PUBLICATION REQUIRES EXPLICIT RELEASE GATE**

## Design principles

The organization must separate four concerns that historically became mixed:

1. conceptual doctoral research (EDT);
2. the central conceptual object/specification (CCP);
3. technical/product implementation owned by MyTrues;
4. external adopted products/clients owned by their own organizations;
5. reproducible frontier research/benchmarks.

It must also make the open/closed boundary explicit.

## Existing repositories

All eight current repositories are historical and must be renamed with the
authorized suffix `_arquived_261001`.

They are not deleted.

## Definitive repositories

### SCIENCE / THESIS

#### `MyTrues/edt` — PRIVATE initially

Purpose:

- canonical working repository for **Education-Driven Thinking**;
- doctoral thesis manuscript;
- conceptual claims;
- systematic/scoping reviews;
- methodology;
- thesis CCP;
- unpublished article drafts;
- reviewer/bank material;
- historical research genealogy.

Why private initially:

- active doctoral manuscript and unpublished claims;
- publication/embargo/reviewer workflow;
- permits later release of selected published materials without exposing every
  working note.

Current canonical relationship:

```text
EDT
= conceptual/philosophical engineering thesis

CCP
= central concept/object under investigation

MyTrues
= technical instrument/reference implementation
```

License:

- no blanket OSS license while private thesis work is unpublished;
- published text can later receive an explicit scholarly license per artifact.

Historical ancestor:

- `paper_arquived_261001`.

#### `MyTrues/ccp` — PRIVATE PRE-RELEASE / PLANNED PUBLIC

Purpose:

- canonical open home of **CCP — Creator Cognitive Path / Caminho Cognitivo do
  Criador**;
- conceptual model;
- terminology;
- SOURCE -> CCP -> PROJECTION;
- cognitive keyframes;
- raw source != CCP;
- provenance vs rationale;
- current/historical position concepts when qualified;
- projection contracts/views;
- examples and fixtures;
- mappings to W3C PROV, ADR/MADR, IBIS/QOC and other adopted prior art;
- CCP de Partida / versioned epistemic starting-point research.

Why public:

- CCP is the conceptual interface the thesis intends to discuss/test;
- public specification/examples improve citation, critique and replication;
- it should remain independent of one MyTrues implementation.

Licensing north:

- prose/specification: CC BY 4.0 candidate;
- executable schemas/examples/code: MIT candidate;
- final license choice should be explicit per file family.

Historical ancestor:

- `spec_arquived_261001`.

#### `MyTrues/research` — PRIVATE PRE-RELEASE / PLANNED PUBLIC

Purpose:

- frontier map;
- baselines;
- benchmark harnesses;
- experiments;
- replication packages;
- negative results;
- qualified external runs;
- Microbrain work only if explicitly authorized;
- paper opportunities that are not the EDT thesis itself;
- reproducibility evidence.

Top-level target:

```text
frontier/
baselines/
benchmarks/
experiments/
replication/
paper-candidates/
external-runs/
negative-results/
```

Open-by-default because scientific claims must be reproducible.

Do not place private user/customer data here.

Historical ancestor:

- `replication_arquived_261001`;
- qualified `Tools/MYTRUES/research` staging.

### PRODUCT — OPEN COMMON LAYER

#### `MyTrues/mytrues` — PRIVATE PRE-RELEASE / PLANNED PUBLIC

Purpose:

open technical product and interoperability layer.

Contains only product/common material:

```text
protocol/
schemas/
ports/
conformance/
reference/
memory/
integrations/
sdk/
open/
seeds/
docs/
```

The open boundary reaches the replaceable `DecisionEngine` contract.

Must remain open:

- wire protocol;
- lifecycle semantics;
- schemas;
- port contracts;
- plugin manifest contract;
- conformance suite;
- reference implementation;
- reference storage;
- open adapters;
- canonical-promotion/authority rules;
- security/data-handling declarations required for interoperability.

Must NOT contain by default:

- EDT thesis manuscript;
- broad archaeology;
- speculative research branches;
- proprietary engines;
- enterprise control plane;
- customer/provider private memory.

License: MIT for code/protocol reference implementation unless a specific
adopted dependency imposes another compatible requirement.

#### `MyTrues/registry` — PRIVATE PRE-RELEASE / PLANNED PUBLIC

Purpose:

open extension registry and manifest/conformance surface.

Contains:

- plugin manifest schema;
- port/capability taxonomy;
- compatibility declarations;
- license declarations;
- data-access/network/LLM-use declarations;
- signatures/provenance;
- conformance result schema;
- public registry index;
- rules distinguishing published / conformant / security-reviewed / benchmarked
  / scientifically reproduced.

Marketplace payment/commercial UX is **not** required for the registry.

The open registry prevents closed commercial extensions from forcing a closed
interoperability protocol.

License: MIT for tooling/schema; registry metadata under an explicit open data
policy.

#### `MyTrues/site` — PRIVATE PRE-RELEASE / PLANNED PUBLIC

Purpose:

- public documentation/landing;
- published EDT/CCP material only;
- MyTrues protocol/docs;
- registry browsing/docs;
- links to papers/DOIs/benchmarks.

Site build code can be MIT; authored prose/media should carry explicit content
licensing.

Historical ancestor:

- `site_arquived_261001`.

### PRODUCT — CLOSED / COMMERCIAL LAYER

#### `MyTrues/mytrues-enterprise` — PRIVATE

Purpose:

a clearly separated place for material that may legitimately remain closed.

Possible contents:

- proprietary DecisionEngine implementations;
- enterprise-only adapters;
- hosted control-plane code;
- private registry/organization management;
- enterprise policy/workflow integrations;
- commercial scaling/operations;
- proprietary optimization/tuning;
- customer-specific deployment automation;
- private learned models/profiles where legally/contractually permitted.

MUST NOT redefine:

- open wire protocol;
- open port contracts;
- required conformance semantics;
- CCP;
- EDT;
- public registry manifest compatibility.

Commercial closed extensions implement open contracts.

No OSS license by default.

## Why there is no separate `cli`, `kernel` or `spec` canonical repo now

Those old repositories reflected an architecture phase before the current
boundaries were clear.

Current rule:

- CLI/SDK belong in `mytrues` unless independently reusable enough to split;
- generic agent kernel is not MyTrues core and should not be resurrected without
  a new justified bounded context;
- the old `spec` becomes conceptual ancestry for `ccp`, while the actual
  MyTrues protocol spec lives inside `mytrues`.

Avoid premature repository fragmentation.

## Why there is no canonical `paper` repo

Writing has two destinations:

- EDT/thesis work -> `edt`;
- independent MyTrues/CCP technical paper opportunities and replication ->
  `research`.

Published papers can later receive dedicated archival/DOI repositories if needed.

## Open / closed boundary in one diagram

```text
                   SCIENCE
        ┌───────────────────────────┐
        │ edt (private while draft) │
        │ ccp (public)              │
        │ research (public)         │
        └─────────────┬─────────────┘
                      │ evidence / concepts
                      ▼
             OPEN PRODUCT COMMON
        ┌───────────────────────────┐
        │ mytrues                   │
        │ registry                  │
        │ site                      │
        └─────────────┬─────────────┘
                      │ open contracts
                      ▼
              CLOSED EXTENSIONS
        ┌───────────────────────────┐
        │ mytrues-enterprise        │
        │ third-party closed engine │
        │ third-party paid plugin   │
        └───────────────────────────┘
```

A third party may distribute a proprietary plugin/engine without entering
`mytrues-enterprise`; the open registry only needs enough manifest/conformance
metadata to interoperate safely.

## Migration mapping from current repositories

| Current | Archive | Definitive successor/use |
|---|---|---|
| `MyTrues` | `MyTrues_arquived_261001` | history source only; qualified product pieces already reconstructed in FlowED -> `mytrues` |
| `MyTrues_p` | `MyTrues_p_arquived_261001` | development archaeology only |
| `cli` | `cli_arquived_261001` | CLI functionality moves into `mytrues` |
| `kernel` | `kernel_arquived_261001` | no automatic successor |
| `paper` | `paper_arquived_261001` | history seed for `edt` |
| `replication` | `replication_arquived_261001` | history seed for `research` |
| `site` | `site_arquived_261001` | history seed for new `site` |
| `spec` | `spec_arquived_261001` | history seed for `ccp` |

## Creation order

1. rename all eight legacy repos;
2. create `ccp`, `edt`, `research`;
3. create `mytrues`, `registry`, `site`;
4. create private `mytrues-enterprise`;
5. keep `ccp` and `edt` as temporary academic incubation repos;
6. import qualified history/content;
7. run conformance/benchmark smoke tests;
8. only then archive the eight renamed legacy repos at GitHub repository-setting level.

## Visibility target

All definitive repositories remain PRIVATE until an explicit release review.

| Repository | Current visibility | Intended release posture |
|---|---|---|
| `mytrues` | private | planned public after release gate |
| `ccp` | private | planned public after publication/review gate |
| `edt` | private | private working thesis; selective publication only |
| `research` | private | planned public after reproducibility/licensing review |
| `registry` | private | planned public after schema/conformance review |
| `site` | private | planned public when public content is ready |
| `mytrues-enterprise` | private | remains private/commercial |

Private-first means no future open-source or scholarly license is implied merely by planned-public status.

Before publication, each planned-public repo must pass:
- secret/privacy scan;
- third-party license review;
- content/IP review;
- reproducibility/conformance checks where applicable;
- explicit license selection;
- explicit visibility change approved by the owner.

## Pre-publication licensing

For private pre-release material, use a restricted/all-rights-reserved notice for original unpublished content.

Do not overwrite or revoke:
- third-party licenses;
- rights previously granted under an earlier open license;
- licenses on imported upstream components.

At the public-release gate, replace the pre-release notice with the intended repository/file-family licenses (for example MIT for eligible code and CC BY 4.0 for eligible authored research prose).

## Gate before adding another canonical repo

Create a new repo only when at least one applies:

- independent release/version lifecycle;
- independent external contributor surface;
- independent citation/DOI/replication object;
- independent security/visibility boundary;
- independent product/business boundary.

Otherwise keep it as a directory/module.


## Federated ownership correction

IDEOS does **not** belong in the MyTrues organization.

Canonical IDEOS ownership is external:

`IDEOS-DEV/IDeOS-core`.

Observed on 2026-10-01:

- visibility: private;
- default branch: `main`;
- head: `5b43b1bda1f9ab3c91424dc5c05346827a031ffd`.

Relationship:

```text
IDEOS-DEV/IDeOS-core
    -> adopts MyTrues through open protocol/ports

FlowED
    -> references/pins IDEOS
    -> references/pins MyTrues
```

The empty `MyTrues/ideos` repository created during migration is a misplaced
staging artifact. It must not receive IDEOS content. Preserve it privately as
`ideos_misplaced_arquived_261001` and archive it after the correction.

See:

`FEDERATION-ADOPTION-TOPOLOGY.md`.

## Academic incubation is temporary

`MyTrues/ccp` and `MyTrues/edt` are current incubation locations only.

Long-term:

- CCP gets a dedicated academic organization/repository;
- EDT gets a dedicated academic organization/repository;
- history is transferred/preserved;
- MyTrues keeps pinned references/adoption records rather than writable copies.

This prevents the MyTrues product organization from becoming the permanent owner
of independent academic identities.

`MyTrues/research` remains valid because it is specifically **MyTrues technical
and reproducibility research**, not the canonical home of the EDT thesis.
