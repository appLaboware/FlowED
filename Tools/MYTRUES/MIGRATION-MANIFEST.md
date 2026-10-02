# MyTrues Organization Migration Manifest

Date: 2026-10-01

Status: **READY FOR REPOSITORY-ADMIN EXECUTION**

Frozen FlowED staging source:

`121c63642c4cc552c46a7cf3ff70ab57924cb2be`

This SHA contains the current qualified archaeology, EDT/CCP/MyTrues boundaries,
open extension architecture, org topology and 2026 frontier reference suite.

Later migration-only commits are not required as product/science source.

## 1. Verified target organization

Organization:

`MyTrues`

GitHub App installation:

`166957143`

The installation can read/write repository contents and reports admin repository
permission on all eight existing repositories.

Repository-level create/rename actions are not exposed by the current connector,
so execution requires a GitHub repository-admin UI/API/CLI surface.

## 2. Preserve all current repositories

No deletion.

Rename exactly:

- `MyTrues` -> `MyTrues_arquived_261001`;
- `MyTrues_p` -> `MyTrues_p_arquived_261001`;
- `cli` -> `cli_arquived_261001`;
- `kernel` -> `kernel_arquived_261001`;
- `paper` -> `paper_arquived_261001`;
- `replication` -> `replication_arquived_261001`;
- `site` -> `site_arquived_261001`;
- `spec` -> `spec_arquived_261001`.

After successful canonical imports and verification, set the eight renamed legacy
repositories to GitHub archived/read-only state.

## 3. Definitive repositories

| Repository | Visibility | Purpose |
|---|---|---|
| `mytrues` | private pre-release | open decision-memory protocol, ports, conformance, reference implementation |
| `ccp` | private pre-release | Creator Cognitive Path conceptual model/specification, provenance and projections |
| `edt` | private initially | Education-Driven Thinking doctoral research workspace |
| `research` | private pre-release | frontier map, benchmarks, experiments, replication, paper opportunities |
| `registry` | private pre-release | open plugin/engine/adapter manifest registry and conformance metadata |
| `site` | private pre-release | public docs/site |
| `mytrues-enterprise` | private | closed commercial extensions implementing open MyTrues contracts |

Canonical topology rationale:

`ORG-TOPOLOGY-2026-10-01.md`.

## 4. Science versus product boundary

### EDT

`EDT = Education-Driven Thinking`.

Conceptual/philosophical doctoral thesis.

CCP is the central concept/object under investigation.

The thesis does not depend on MyTrues inventing technically novel components.

### CCP

Open conceptual object/specification.

Must remain independent of one MyTrues runtime.

### MyTrues

Technical product/instrument.

Open common layer reaches the replaceable `DecisionEngine` contract.

### Research

Scientific/technical experiments and reproducibility.

Uses current frontier baselines recorded in:

`research/FRONTIER-REFERENCE-SUITE-2026.md`.

## 5. Open versus closed boundary

### Must remain open/common

In `mytrues` / `registry`:

- wire protocol;
- schemas;
- lifecycle semantics;
- port contracts;
- plugin manifest contract;
- conformance;
- reference implementation;
- reference storage;
- required security/data-handling declarations;
- public registry compatibility metadata.

### May remain closed

In `mytrues-enterprise` or third-party private repositories:

- proprietary DecisionEngine implementations;
- enterprise-only adapters;
- hosted control plane;
- scaling/operations optimizations;
- customer-specific deployment automation;
- private learned models/profiles subject to law/contracts;
- commercial integrations.

Closed extensions implement open contracts; they do not redefine the contracts.

## 6. History mapping

### `ccp`

Historical ancestor:

`spec_arquived_261001`.

Preserve its history as the starting history of the new `ccp`.

Then import qualified current CCP material from FlowED.

### `edt`

Historical ancestor:

`paper_arquived_261001`.

Preserve its history as the starting history of the private `edt`.

Then import current EDT/CCP boundary and historical-source indexes.

### `research`

Historical ancestor:

`replication_arquived_261001`.

Preserve its history and then import qualified `Tools/MYTRUES/research`.

### `site`

Historical ancestor:

`site_arquived_261001`.

### `mytrues`

Do not reuse the old `MyTrues` root as current architecture.

Build from qualified FlowED product paths only:

- `LICENSE`;
- `README.md`;
- `docker-compose.yml`;
- `protocol/`;
- `conformance/`;
- `core/`;
- `memory/`;
- `reference/`;
- `integrations/`;
- `open/`;
- `seeds/`;
- `docs/ALGORITHM-BOUNDARY.md`;
- `docs/GENERIC-PROTOCOL.md`;
- `docs/OPEN-EXTENSION-ECOSYSTEM.md`.

The old `MyTrues_arquived_261001` remains the historical evidence for the
pre-canonical implementation family.

### IDEOS — external canonical owner

Do **not** create/import IDEOS under the MyTrues organization.

Canonical IDEOS repository:

`IDEOS-DEV/IDeOS-core`

IDEOS adopts MyTrues through the open protocol/ports. FlowED references both as
independent upstreams. The mistakenly created empty `MyTrues/ideos` repo must be
preserved privately as `ideos_misplaced_arquived_261001` and archived, not used
as a canonical source.

## 7. Private-first release and licensing policy

All definitive repositories stay PRIVATE during migration, qualification and content preparation.

Repositories intended for later public release are marked `planned-public`, but that label grants no public license.

Before public release:
- audit secrets/private data;
- audit third-party licenses;
- decide exact code/content/data licenses;
- add publication/release notice;
- explicitly change GitHub visibility.

For original unpublished material, a restricted pre-release notice may be used. It must not revoke rights already granted under earlier licenses or alter third-party licenses.

## 8. Licensing north

### Product/open code

`mytrues`, registry tooling:

MIT, unless a specific imported component requires a compatible distinct
license.

### CCP

Candidate split:

- authored prose/specification: CC BY 4.0;
- executable schemas/examples/code: MIT.

Do not apply a blanket license to third-party material.

### EDT

Private/unpublished thesis workspace initially.

Published artifacts get explicit scholarly licensing individually.

### Research

- code/harness: MIT candidate;
- authored docs: CC BY 4.0 candidate;
- datasets: preserve each upstream dataset license; never blanket-relicense.

### Enterprise

Private/proprietary by default.

## 9. Frontier/reference gate

Before claiming technical/scientific novelty, compare as applicable against the
current suite including:

- LongMemEval-V2;
- MemoryArena (ICML 2026);
- AMemGym (ICLR 2026);
- LoCoMo-Plus (ACL 2026);
- GroupMemBench;
- RHELM;
- MemGym;
- Microsoft Memora;
- Microsoft human-inspired memory architecture;
- Microsoft MAGE;
- Google ReasoningBank;
- Google MARS;
- Google controlled agent-architecture scaling work;
- W3C PROV;
- ADR/MADR;
- IBIS/QOC;
- current design-rationale extraction/generation work.

See the frozen frontier file for exact references and intended test use.

## 10. Completion evidence

The reorganization is complete only after recording:

### Legacy

- API/UI evidence for all eight renames;
- all eight archived URLs;
- archive/read-only status after import.

### New repos

For all eight definitive repositories:

- canonical URL;
- visibility;
- initial/default branch SHA;
- description;
- license/boundary README.

### Imports

- proof that `ccp`, `edt`, `research`, `site` retained historical ancestor
  history;
- proof that `mytrues` contains only qualified product/common material;
- proof that `research` contains the frontier suite;
- proof that `edt` remains private initially.

### Product

- canonical MyTrues conformance run URL;
- IDEOS-DEV/IDeOS-core -> MyTrues compatibility run;
- real immutable MyTrues SHA in the canonical external IDEOS upstream lock.

## 11. Execution runbook

Use:

`migration/reorganize-org.sh`

The runbook is idempotency-aware and never deletes a repository.

Current blocker:

**repository-level rename/create/visibility operations are not exposed by the
GitHub connector actions in this session, and the local runtime has no `gh`
binary/authentication surface.**

Do not report execution until real GitHub mutation evidence exists.


## Academic incubation / future transfer

`MyTrues/ccp` and `MyTrues/edt` are deliberately temporary incubation repos.

When dedicated academic organizations exist:

1. freeze accepted SHA;
2. transfer/migrate each canonical repo preserving history;
3. verify branches/tags/issues/history;
4. update MyTrues/FlowED references to the new canonical URL/SHA;
5. remove the second writable canonical copy.

Prefer GitHub repository transfer when feasible.

After separation:

- MyTrues references/adopts CCP as an external conceptual upstream;
- EDT uses MyTrues as an experimental instrument;
- MyTrues does not become the permanent owner of EDT/CCP academic identity.

See `FEDERATION-ADOPTION-TOPOLOGY.md`.
