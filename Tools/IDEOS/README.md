# IDEOS

> Migration target: `MyTrues/ideos`

IDEOS is a **DevOps intent CLI** built by composing adopted open tools before
creating new behavior.

It is not a replacement for Porter/CNAB, Docker, Kubernetes, Terraform/OpenTofu,
Ansible, cloud CLIs, or MyTrues.

## Core rule

Before writing new code:

1. discover existing tools/protocols;
2. adopt and execute them as designed;
3. exhaust native configuration/extensions;
4. compose through replaceable ports/adapters;
5. fork only after the fork gate;
6. invent only after the Science Frontier Gate.

## MyTrues relationship

MyTrues is an independent generic decision protocol.

IDEOS consumes MyTrues only through its consumer-owned `DecisionMemory` port.
The implementation is pinned by immutable upstream SHA and may be replaced by
another compatible provider.

IDEOS does not copy MyTrues implementation code or read MyTrues storage
internals.

See:

- `spec/capability-ports.md`;
- `upstreams/mytrues.lock.json.example`;
- `../EVOLUTION/ADOPTIONS/001-IDEOS-MYTRUES.md` while staging remains in FlowED.

## Current adopted stack

The laboratory has used, among others:

1. Cloud Native Buildpacks where applicable;
2. Porter/CNAB for packaging/lifecycle;
3. Porter mixins/adapters;
4. Docker/Compose and provider tooling for materialization.

## Current evidence

A Docker reference flow has been proved:

`Docker Engine -> IDEOS controller container -> Porter -> CNAB invocation -> Docker Compose -> workload`

Evidence:

https://github.com/appLaboware/FlowED/actions/runs/36769533522

Azure materialization has also been proved in separate experiments. A single
generic contract across every target remains open and must not be claimed yet.

## Structure

- `docs/` — architecture/decisions;
- `spec/` — positioning, capability ports, syscalls and form factors;
- `runtime/` — controller/CLI laboratory packaging;
- `experiments/` — reproducible proofs;
- `upstreams/` — immutable adoption locks/templates.
