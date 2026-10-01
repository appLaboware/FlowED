# MyTrues

MyTrues is an experiment in **provider-owned operational decision memory**.

A MyTrues belongs to a technician, team, or solution provider.

The client chooses which provider's MyTrues to consult. Different providers can
legitimately resolve the same incident in different ways because each has its own
approved knowledge and experience.

## Current rule

Known case:

`request -> provider MyTrues -> approved decision -> resume`

Unknown case:

`request -> PAUSE -> anonymize -> provider senior -> synthetic sandbox -> explicit resolution -> retain in that provider's memory -> resume`

MyTrues does **not** invent a new operational truth just to avoid stopping.

## Open-first boundary

Everything already known publicly stays open:

- standards;
- public algorithms;
- protocols;
- reference memory models;
- reference implementations;
- conformance tests;
- baseline heuristics.

`core/` is intentionally empty of proprietary logic today.

Only additional behavior that later proves genuinely ours and measurably better
than the open baseline should move into MyTrues Core.

## What works now

The reference implementation already proves:

- two independent provider MyTrues;
- same protocol, different known decisions;
- unknown case returns `202 awaiting-provider-decision`;
- case packet removes real customer identifiers;
- a provider can resolve the synthetic case;
- only that provider learns the resolution;
- the paused request becomes resumable;
- provider memory survives service restart.

## Structure

- `protocol/` — open interoperability contract;
- `reference/` — open reference service;
- `memory/` — open reference memory adapters;
- `conformance/` — protocol/behavior tests;
- `open/` — statement of the open surface;
- `core/` — reserved for future demonstrably proprietary added value.
