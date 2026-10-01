# RESULTS — EXP-005B Porter one command to Azure

> Historical note: the repository contains two experiments carrying the EXP-005
> number. This file calls this one **EXP-005B** to distinguish it from the GRyCAP
> Infrastructure Manager experiment (**EXP-005A**).

Status: **PASS**.

## Evidence A — real Azure materialization

Successful runs:

- `36796448509`
- `36804765898`

Primary acceptance run: `36796448509`.

The Actions job passed:

1. Azure identifiers resolved;
2. GitHub OIDC token obtained;
3. Porter installed;
4. official Porter `az` mixin installed;
5. Porter credential set applied;
6. one user-facing `porter install` command executed;
7. Azure Container Instance created;
8. Azure FQDN discovered;
9. HTTP endpoint verified.

Evidence class: **EVIDENCE-A**.

## User-facing operation proved

After bootstrap, the tested operation was:

`porter install site -c azure-oidc --param site_name=<name>`

The user did not issue an ARM/Bicep/Terraform deployment command.

## Important implementation observation

The official `az` mixin path required a custom Porter Dockerfile pinned to Debian
bookworm because the generated image path encountered an Azure CLI repository
compatibility problem when Debian stable resolved to trixie.

This is ecosystem friction, not a new IDEOS capability.

## Limits

This experiment did **not** prove:

- target selection from generic intent;
- the same bundle working unchanged on Docker and Azure;
- PHP+MySQL;
- custom DNS;
- persistence;
- production security/hardening.

The bundle remained Azure-specific and used a minimal public HTTP workload.

## Honest conclusion

Porter alone, using its existing lifecycle and Azure mixin, materially reduced the
recurring operation to one Porter command and returned a live Azure URL. It did not
solve target inference or generic application modeling.
