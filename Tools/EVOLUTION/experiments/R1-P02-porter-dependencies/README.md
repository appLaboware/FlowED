# R1-P02 — Porter direct dependencies

Purpose: reproduce Porter's dependency capabilities before deciding whether a higher-level
composition engine is required.

The experiment publishes two compatible versions of the same dependency:

- `r1-child:v1.0.0`;
- `r1-child:v1.0.1`.

The root bundle declares:

- pinned default reference `v1.0.0`;
- semver range `>=1.0.0 <2.0.0`.

It then proves:

1. default/exact strategy uses the pinned version;
2. `max-patch` chooses `v1.0.1`;
3. a dependency parameter can be overridden from the root CLI using
   `child#child_value=value`;
4. child output is available to the root through
   `bundle.dependencies.child.outputs.child_result`;
5. `porter inspect --show-dependencies` resolves the dependency graph.

This is deliberately a direct-dependency experiment. Shared dependencies v2 and transitive
execution are separate gates.
