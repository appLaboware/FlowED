# RESULTS — R1-P03 Porter Dependencies v2 / shared dependencies

Status: **ATTEMPTED, NOT PROVEN**.

Evidence class: **EVIDENCE-B (failed integration runs)**.

## Actions runs

Audited runs include:

- `36820091768` — failure;
- `36820416064` — failure;
- `36820579778` — failure.

The latest audited run reached these successful steps:

1. clone;
2. local OCI registry;
3. Porter 1.6.1 installation;
4. `exec` mixin installation;
5. build and publish of the `infra`, `app`, and `root` fixture bundles.

It then failed at:

`Install independent shared infra`

## Observed boundary

The command using the experimental Dependencies v2 environment and the
`sh.porter.SharingGroup` label returned non-zero:

`INSTALL_RC=1`

Porter created an installation record carrying the sharing-group label, but no
successful action/run state was established.

The captured Porter log showed JIT parameter/credential resolution and then returned
failure without an explicit underlying error message in the CLI output captured by
the workflow.

Therefore this audit does **not** assign a root cause that the logs do not prove.

## Diagnostic defect in the test

The workflow also attempted:

`porter installations runs list --installation shared-infra`

and Porter reported:

`unknown flag: --installation`

This is a defect in the diagnostic command, but it occurred after the install command
had already returned `INSTALL_RC=1`; it is not evidence of the install failure's
root cause.

## Claims not proved

The following R1-P03 acceptance claims remain open:

- reuse of a pre-existing shared dependency;
- sibling dependency output -> parameter wiring;
- shared dependency graph/wiring runtime behavior;
- root uninstall preserving independently installed shared infrastructure.

## What is proved

Only the following is accepted:

- Dependencies v2 fixtures can be authored/built/published under the experimental
  feature environment in this Actions laboratory;
- the tested independent shared-infra installation path currently fails before the
  shared-dependency behavior can be exercised.

## Next action

Before any local workaround:

1. minimize the failing independent install;
2. correct the diagnostic CLI command;
3. compare with upstream examples/tests;
4. inspect current Porter issue/proposal state;
5. report upstream if the minimized case still fails.

No IDEOS abstraction should be introduced to hide this boundary.
