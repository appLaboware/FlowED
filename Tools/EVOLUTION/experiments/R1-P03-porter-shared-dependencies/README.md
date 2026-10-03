# R1-P03 — Porter Dependencies v2 / shared dependencies

Purpose: test the experimental Dependencies v2 path before inventing a service-composition
or dependency-sharing layer.

The experiment proves or falsifies:

- pre-existing dependency reuse by sharing group;
- sibling dependency output -> parameter wiring;
- graph inspection of shared dependencies;
- root uninstall behavior when a dependency pre-existed independently.

Topology:

```
existing shared infra
       |
       | output connstr
       v
root ---------> app dependency
                 parameter connstr
```

Expected app assertion:

`CONNSTR == mysql://r1-shared-infra`

Dependencies v2 is explicitly experimental in Porter 1.6.1. Any success here is evidence
of capability, not a production recommendation.
