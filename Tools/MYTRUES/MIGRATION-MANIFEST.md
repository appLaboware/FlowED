# MyTrues Organization Migration Manifest

Date: 2026-10-01

Status: **STAGED — repository-admin operations pending target-org access/tooling**

Frozen FlowED migration source SHA:

`0c8098169123b7d0f48105f1f249c3a8681e3ec6`

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
git subtree split --prefix=Tools/MYTRUES 0c8098169123b7d0f48105f1f249c3a8681e3ec6 -b import/mytrues
git subtree split --prefix=Tools/IDEOS 0c8098169123b7d0f48105f1f249c3a8681e3ec6 -b import/ideos
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
