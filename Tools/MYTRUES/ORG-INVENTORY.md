# ORG-INVENTORY — MyTrues reorganization 2026-10-01

Status: **TARGET ORG READABLE — INVENTORY COMPLETE / REPO-ADMIN MUTATIONS NOT EXPOSED BY CURRENT TOOLING**

GitHub App installation:

- organization: `MyTrues`;
- installation id: `166957143`;
- repository selection: `all`;
- observed repository permissions: admin/maintain/push/pull/triage on all eight
  current repositories.

## Current repositories

| Repository | Visibility | Last push | GitHub size | Default branch | Head SHA | Content summary | URL |
|---|---|---|---:|---|---|---|---|
| `MyTrues/MyTrues` | private | 2026-01-27T14:55:05Z | 346 | main | `cbe55aab5b4f0f2cd72977e5b49c757241e2bc8b` | historical umbrella/runtime: shell implementation, MyTrues evolution, vector DB, UUID/export/merge/static/vector tools, adoption/world-scan docs | https://github.com/MyTrues/MyTrues |
| `MyTrues/MyTrues_p` | private | 2026-01-23T06:56:42Z | 376 | main | `d78e9c3f6e4a07de1f59e1aa008f75a80f20c166` | large DEV/InitProj planning surface, IA prompts/sessions, project process material | https://github.com/MyTrues/MyTrues_p |
| `MyTrues/cli` | private | 2026-01-23T04:49:26Z | 5 | main | `9f48c68a76d9a5cb03337c8813af8fd99f77a10d` | Typer/JSONSchema CLI skeleton for CCP registration/validation/export | https://github.com/MyTrues/cli |
| `MyTrues/kernel` | private | 2026-01-23T04:49:28Z | 9 | main | `817d400e377e3fe5ec9db0c073aedf98122281b9` | agent loop/kernel, cartridges, adapter instructions, approval/message schemas | https://github.com/MyTrues/kernel |
| `MyTrues/paper` | private | 2026-01-23T04:49:32Z | 7 | main | `0775f4ca682f9349a3bb375770df7d641cb7d5f7` | EDT paper/thesis skeleton: outline, related work, claims, evaluation, bibliography | https://github.com/MyTrues/paper |
| `MyTrues/replication` | private | 2026-01-23T04:49:34Z | 5 | main | `999c62ebac6dbeedafc3aadc9a424739544352bd` | replication skeleton: experiment design and scripts | https://github.com/MyTrues/replication |
| `MyTrues/site` | private | 2026-01-23T04:49:36Z | 4 | main | `8ff324b27c43f9a4ea9486ddbab009baa39ece7d` | Hugo/Docsy site skeleton for mytrues.dev | https://github.com/MyTrues/site |
| `MyTrues/spec` | private | 2026-01-23T04:49:38Z | 6 | main | `8d532a981f7ded3b1406c378a4a1c10be1f7be36` | CCP spec: schema/example, terminology, W3C PROV mapping | https://github.com/MyTrues/spec |

Observed metadata source: authenticated GitHub connector against the real
`MyTrues` installation on 2026-10-01.

## Existing repository trees — notable content

### `MyTrues/MyTrues`

39 files observed, including:

- `.mytrues`;
- `.mytrues-data/vector.db`;
- `CORE/mytrues-evolution/*`;
- `MyTrues.sh` and modular shell scripts;
- `docs/PROMPT-ADOPTION.md`;
- `docs/oss-adoption.md`;
- `docs/pt-br/edt-filosofia-mytrues-mecanismo.md`;
- `docs/pt-br/estado-da-arte-ia-experiencial.md`;
- `docs/pt-br/integracao-initproj.md`;
- `docs/pt-br/merge-sync.md`;
- `docs/pt-br/schema-uuid.md`;
- `docs/pt-br/vector-store.md`;
- `docs/world-scan.md`;
- `tools/mytrues_export.py`;
- `tools/mytrues_merge.py`;
- `tools/mytrues_static.py`;
- `tools/mytrues_uuid.py`;
- `tools/mytrues_vector.py`.

This repository is historically important and should be archived intact.

### `MyTrues/MyTrues_p`

301 files observed.

It is primarily a planning/IA-session/InitProj development surface, not a clean
canonical product repository.

Archive intact; selectively migrate only qualified material.

### `MyTrues/spec`

8 files observed:

- `mapping-prov.md`;
- `schemas/ccp-record.example.yaml`;
- `schemas/ccp-record.schema.json`;
- `terminology.md`.

This is an important direct ancestor of the future `ccp` repository.

### `MyTrues/paper`

9 files observed:

- `ARTICLE-OUTLINE.md`;
- `RELATED-WORK.md`;
- `claims.md`;
- `evaluation.md`;
- `references.bib`.

This is an important ancestor of the future EDT/thesis research surface.

## Authorized archive rename map

Required suffix:

`_arquived_261001`

Exact rename map:

- `MyTrues/MyTrues` -> `MyTrues/MyTrues_arquived_261001`;
- `MyTrues/MyTrues_p` -> `MyTrues/MyTrues_p_arquived_261001`;
- `MyTrues/cli` -> `MyTrues/cli_arquived_261001`;
- `MyTrues/kernel` -> `MyTrues/kernel_arquived_261001`;
- `MyTrues/paper` -> `MyTrues/paper_arquived_261001`;
- `MyTrues/replication` -> `MyTrues/replication_arquived_261001`;
- `MyTrues/site` -> `MyTrues/site_arquived_261001`;
- `MyTrues/spec` -> `MyTrues/spec_arquived_261001`.

## Tooling boundary discovered after access was restored

The current GitHub connector now exposes full repository content access and
admin-level repository permissions, but its available mutation actions do **not**
include:

- create organization repository;
- rename repository;
- archive/unarchive repository;
- edit repository visibility/settings.

The connector does support content/branch/PR/issue writes inside existing
repositories.

The local runtime does not currently provide the `gh` CLI.

Therefore this session can verify and stage the reorganization completely, but
cannot truthfully report repository-level rename/create operations as executed
through the currently exposed actions.

The exact admin runbook is maintained under `migration/` for execution as soon
as a repository-admin API/UI/CLI surface is available.

## Completion gate

Inventory: **COMPLETE**.

Reorganization: **PENDING repository-admin mutation surface**.

No rename/create may be reported DONE without GitHub URL/API evidence.
