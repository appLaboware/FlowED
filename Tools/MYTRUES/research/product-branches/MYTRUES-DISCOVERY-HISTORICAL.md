# Historical Product Branch — MyTrues Discovery

Date: 2026-10-01

Status: **HISTORICAL / RESEARCH BRANCH — NOT CANONICAL PRODUCT APPROVAL**

Source family:

- `VRAMPP-002 - 043b - D2b.MD`;
- related D2 / Project Miner discussions summarized in that reconstruction.

## Why preserve this branch

The reconstruction records a substantial productization direction that is
distinct from the current MyTrues decision protocol:

`MyTrues Discovery`

Its goal was to point at a project/corpus and discover:

- sources;
- current versus historical material;
- authorities;
- conflicts;
- duplicates;
- gaps;
- opportunities;
- candidate formations;
- evidence/review packages.

This is not the same problem as provider-scoped decision memory.

## Reconstructed architecture proposal

The historical branch proposed approximately:

```text
MyTrues Discovery
    ↓
Generic Core
    ↓
Contracts
    ↓
Adapters
    ├── CLI
    ├── Python API
    ├── MCP
    └── domain/project profiles
```

A strong invariant from this branch is:

> **MCP is an adapter, not the internal architecture.**

That invariant is compatible with the current protocol/port/adapter philosophy
and may be reused if Discovery is ever revived.

## Candidate inputs

The reconstruction mentions:

- project folders;
- source trees;
- Git repositories;
- ZIP/tar archives;
- documentation corpora;
- AI-session exports;
- cognition packages;
- planning artifacts;
- evidence packages;
- authority snapshots.

## Candidate outputs

The reconstruction mentions:

- source inventory;
- observations and claims;
- authority map;
- decision graph;
- opportunity map;
- candidates;
- candidate-formation packages;
- evidence bundles;
- review queues;
- machine-readable reports;
- human-readable reports.

## Candidate adapters

Historical proposals include:

Input:

- FilesystemAdapter;
- GitAdapter;
- ArchiveAdapter;
- ConversationExportAdapter;
- CognitionPackageAdapter;
- EvidencePackageAdapter;
- project/workspace-specific adapters.

Provider:

- LLMProviderAdapter;
- EmbeddingProviderAdapter;
- StorageAdapter;
- SearchAdapter;
- GraphAdapter.

Output:

- JSONBundleExporter;
- MarkdownExporter;
- EvidencePackageExporter;
- ReviewQueueExporter.

## CLI / MCP proposals

Examples preserved by the reconstruction:

```text
mytrues scan .
mytrues inventory .
mytrues discover .
mytrues authorities .
mytrues opportunities .
mytrues candidates .
mytrues validate package.zip
mytrues serve --mcp
```

and MCP operations in a `discovery.*` namespace.

These names are historical proposals, not current contracts.

## Commercial branch

The D2 reconstruction also contains proposed Community / Pro / Enterprise tiers
and the phrase:

`Git for Reasoning & Ground Truth`

Those were proposals from the D2/productization branch, not approved current
business policy.

## Relationship to current MyTrues

Do not merge this historical branch into the current generic decision protocol
by default.

Current separation should remain:

```text
MyTrues protocol
  -> decision/memory interoperability

possible future MyTrues Discovery
  -> corpus/project discovery and authority reconciliation
```

If revived, Discovery should consume the same open contracts where appropriate,
but must justify its own product boundary, evidence, name and lifecycle.

## Family hypothesis

A later reconstruction suggested a possible family such as:

- MyTrues Discovery;
- MyTrues Cognition;
- MyTrues Verify;
- MyTrues Graph;
- MyTrues Platform.

This family is explicitly preserved as **hypothesis**, not architecture.
