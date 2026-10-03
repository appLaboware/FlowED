# IDEOS Form Factors

Status: migration baseline.

## Canonical product surface

The canonical product identity for the new repository is a **DevOps intent CLI**.

## Packaging form

The existing laboratory also proves a containerized controller form in which:

`host Docker Engine -> IDEOS controller container -> Porter -> invocation container -> materialized workload`

This container packaging is an execution form of the CLI/controller, not a
different product and not a requirement that target applications run in Docker.

## Independence rule

A materialized application should remain independent of the IDEOS controller
whenever the adopted lifecycle tool supports that topology.

## Non-canonical forms

The reorganization does not yet declare as canonical:

- a long-running IDEOS SaaS;
- a desktop GUI;
- a web control plane;
- an IDEOS-specific cloud runtime;
- InFabric.

Those forms require their own evidence and adoption analysis.

## Relationship to adopted tools

Form factor must not leak into capability ownership. A CLI or controller container
may invoke Porter, Docker, cloud CLIs, Kubernetes, Helm, Terraform/OpenTofu,
Ansible or other adopted tools without turning those implementations into IDEOS code.
