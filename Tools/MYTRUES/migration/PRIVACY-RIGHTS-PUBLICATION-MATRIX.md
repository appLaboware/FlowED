# Canonical Repositories — Privacy, Rights and Publication Matrix

Date: 2026-10-01

Status: **PRIVATE-FIRST POLICY**

All canonical repositories start PRIVATE.

A future public target is a plan, not a present license grant.

| Repo | Now | Future target | Private rights model | Planned public licensing |
|---|---|---|---|---|
| mytrues | private | public | restricted pre-release | original code/protocol reference: MIT candidate |
| ccp | private | public | restricted pre-release | authored conceptual/spec prose: CC BY 4.0 candidate; schemas/tools: MIT candidate |
| edt | private | selective publication only | unpublished doctoral material; all rights reserved unless stated | per published artifact; no blanket repo license |
| research | private | public | restricted pre-release | harness/code: MIT candidate; authored research docs: CC BY 4.0 candidate; datasets retain upstream terms |
| registry | private | public | restricted pre-release | tooling/schema: MIT candidate; metadata policy explicit at release |
| ideos | private | public | restricted pre-release | original code: MIT candidate |
| site | private | public | restricted pre-release | site code and authored content licensed separately |
| mytrues-enterprise | private | private | proprietary/restricted | no public license by default |

## Non-negotiable rule

Private status does not erase third-party or previously granted licenses.

No migration may:

- revoke an existing open-source grant;
- relicense third-party material without permission;
- treat repository privacy as ownership of imported third-party work.

## Planned-public labels

Topics such as:

- `private-pre-release`;
- `planned-public`;

mean only that a future publication is intended.

They are not a license.

## Publication gate

Each planned-public repository must pass:

- secret/private-data review;
- provenance review;
- license compatibility review;
- research embargo review;
- security review;
- conformance/tests;
- README/boundary review;
- public metadata review;
- explicit PO authorization.

See:

`migration/bootstrap/COMMON/PUBLICATION-GATE.md`.
