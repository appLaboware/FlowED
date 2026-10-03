# RESULTS — R1-P02

Status: **PASS WITH ONE UNRESOLVED LEGACY OUTPUT-WIRING OBSERVATION**

GitHub Actions:

- run: `36819797057`
- Porter: `v1.6.1`

## Proven

### Direct dependency execution

The root bundle installed its `child` dependency before executing the root action.

### Dependency parameter override

Root install used:

`--param child#child_value=exact-value`

The child output was:

`v1.0.0:exact-value`

For max-patch:

`--param child#child_value=maxpatch-value`

The child output was:

`v1.0.1:maxpatch-value`

### Version strategy

With the dependency declaration pinned to `v1.0.0` plus range
`>=1.0.0 <2.0.0`:

- `exact` selected `v1.0.0`;
- `max-patch` selected `v1.0.1`.

### Dependency graph inspection

`porter inspect --show-dependencies --dependencies-version-strategy max-patch`
resolved and displayed `r1-child:v1.0.1`.

### Lifecycle

Uninstalling each root installation also executed the managed direct dependency
uninstall lifecycle.

## Unresolved observation: legacy root action interpolation

The root action contained the documented template:

`${ bundle.dependencies.child.outputs.child_result }`

The child output was successfully persisted in the child installation, but the value
resolved as empty inside the root action in both exact and max-patch runs.

Observed:

- child output: present and correct;
- root action interpolation: empty.

The public Porter documentation shows dependency outputs as valid action templates, so
this is not yet classified as intended behavior.

Next action:

1. reproduce with the smallest upstream-style bundle;
2. compare legacy dependency mode against Dependencies v2;
3. check latest/canary;
4. search/report upstream before any local workaround.

Evidence class: **EVIDENCE-B**.
