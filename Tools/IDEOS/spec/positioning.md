# IDEOS Positioning

Status: migration baseline for canonical `MyTrues/ideos`.

## Identity

IDEOS is a **DevOps intent CLI**.

Its job is to accept an operator intent, resolve the capabilities required to
fulfil that intent, and compose adopted tools that perform the actual work.

IDEOS is not:

- a replacement for Porter/CNAB;
- a replacement for Docker, Kubernetes, Terraform/OpenTofu, Ansible or cloud CLIs;
- a general-purpose decision protocol;
- the owner of MyTrues decision logic or storage;
- InFabric.

## Relationship to MyTrues

`MyTrues/mytrues` is an independent, domain-generic decision protocol.

IDEOS may consume MyTrues as one adopted upstream through the `DecisionMemory`
capability port. MyTrues is optional from the IDEOS architecture perspective:
another implementation that satisfies the same port may be substituted.

No MyTrues source code is copied into IDEOS.

## Open-first rule

IDEOS follows:

`DISCOVER -> ADOPT -> EXHAUST CONFIGURATION -> COMPOSE/PERSONALIZE -> FORK -> REPRODUCE STATE OF THE ART -> SCIENCE FRONTIER GATE -> INVENT`

Therefore IDEOS owns orchestration/intent-specific composition only where a
real residual gap survives the adoption protocol.

## Canonical repository boundary

After migration:

- original IDEOS changes happen only in `MyTrues/ideos`;
- the FlowED copy becomes migration/history evidence, not a second original;
- adopted upstreams are recorded by immutable version/SHA;
- adapters remain behind named capability ports.

## Current evidence boundary

The current laboratory has evidence for Docker and Azure materialization paths
through adopted tools. It does not yet prove a complete generic natural-language
intent resolver, nor every target listed in the evolution roadmap.

Claims must continue to follow the A/B/C/D evidence discipline.
