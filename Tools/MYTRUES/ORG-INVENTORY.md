# ORG-INVENTORY — MyTrues reorganization 2026-10-01

Status: **TARGET ORG NOT READABLE BY CURRENT GITHUB CONNECTION**

This inventory intentionally does not substitute another organization for the
user-declared target `MyTrues`.

## Target repositories declared for reorganization

The declared current set is:

| Repository | Required archival name | Last push | GitHub size | Content inventory | Current evidence |
|---|---|---:|---:|---|---|
| `MyTrues/MyTrues` | `MyTrues_arquived_261001` | unavailable | unavailable | unavailable | current connection returns 404 |
| `MyTrues/MyTrues_p` | `MyTrues_p_arquived_261001` | unavailable | unavailable | unavailable | current connection returns 404 |
| `MyTrues/cli` | `cli_arquived_261001` | unavailable | unavailable | unavailable | current connection returns 404 |
| `MyTrues/kernel` | `kernel_arquived_261001` | unavailable | unavailable | unavailable | current connection returns 404 |
| `MyTrues/paper` | `paper_arquived_261001` | unavailable | unavailable | unavailable | current connection returns 404 |
| `MyTrues/replication` | `replication_arquived_261001` | unavailable | unavailable | unavailable | current connection returns 404 |
| `MyTrues/site` | `site_arquived_261001` | unavailable | unavailable | unavailable | current connection returns 404 |
| `MyTrues/spec` | `spec_arquived_261001` | unavailable | unavailable | unavailable | current connection returns 404 |

Required suffix from the authorized north is exactly:

`_arquived_261001`

Exact execution rename map:

- `MyTrues` -> `MyTrues_arquived_261001`
- `MyTrues_p` -> `MyTrues_p_arquived_261001`
- `cli` -> `cli_arquived_261001`
- `kernel` -> `kernel_arquived_261001`
- `paper` -> `paper_arquived_261001`
- `replication` -> `replication_arquived_261001`
- `site` -> `site_arquived_261001`
- `spec` -> `spec_arquived_261001`

## Why metadata is unavailable

The GitHub App installations visible to this session do not include an account
named `MyTrues`.

Direct repository reads for all eight declared names returned HTTP 404 through
the authenticated GitHub connector.

Therefore:

- no last-push timestamp is inferred;
- no repository size is inferred;
- no file tree is inferred;
- no rename is claimed;
- no repository creation is claimed.

This is an access boundary, not evidence that the repositories do not exist.

## Accessible historical lineage — source material only

These are **not substitutes for the target-org inventory**. They are recorded
only because they contain material useful for the canonical import.

### `InitProj-260119/MyTrues`

- last push: `2025-10-05T02:58:32Z`;
- GitHub size: `152`;
- default branch: `main`;
- observed head used during inspection:
  `dc891f1d354b85c6f11666d62cb1e59dde839b2e`;
- license: MIT;
- relevant content:
  - `README.md`;
  - `INDEX.md`;
  - `TEMPLATE.md`;
  - `MyTrues.sh`;
  - `CORE/mytrues-evolution/README.md`;
  - `CORE/mytrues-evolution/REFINED.md`;
  - `docs/pt-br/README.md`;
  - `docs/pt-br/edt-filosofia-mytrues-mecanismo.md`;
  - `docs/pt-br/estado-da-arte-ia-experiencial.md`.

This is the strongest currently readable CCP/EDT lineage source.

### `InitProj-260119/MyTrues_p`

- last push: `2025-10-05T16:32:35Z`;
- GitHub size: `7`;
- head:
  `89d2175403f7be97a8e6f53b31fb088a53bc9d16`;
- relevant content:
  - `README.md`;
  - `README_IA.md`;
  - `NESTED-GIT-WORKFLOW.md`;
  - `PROD/NESTED-GIT.md`.

### `detcss/detcss_p` historical copy

The current connector also exposes a historical raw copy under:

`DEV/ia-sessions/MPO-SEED/raw/POC_MyTrues/`

It contains the same MyTrues/CCP material family, including the EDT/MyTrues
document and MyTrues evolution records.

This copy is useful for provenance comparison only; it is not selected as the
canonical source while `InitProj-260119/MyTrues` remains readable.

## Inventory completion gate

This file becomes **COMPLETE** only after the GitHub connection can read the
actual `MyTrues` organization and the eight rows above are replaced with:

- exact `pushed_at`;
- exact GitHub `size`;
- default branch/head SHA;
- concise file-tree/content summary;
- repository URL.

No archival rename may be reported as DONE before that verification.
