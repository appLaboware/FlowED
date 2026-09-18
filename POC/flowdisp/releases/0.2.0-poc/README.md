# FlowDisP Seed 0.2.0 POC

**Status:** experimental seed snapshot

This release freezes the portable FlowDisP seed used to plant structured discovery into an existing project after a free exploratory chat has been preserved as a raw ROLL.

Lifecycle:

```text
free exploratory chat
→ save complete chat as ROLL
→ plant FlowDisP seed
→ reconstruct claims without strengthening them
→ split into bounded Research Cases (FDP-RC-xxx)
→ ABR research rounds + owner forensic audit
→ optional independent replication
→ operational saturation / evidence freeze
→ approved Evidence Pack
→ downstream MAN / WRK / architecture / product decisions
```

Key additions over POC 0.1:

- immutable `CLAIM_ORIGINAL` plus claim lineage;
- `REFUTATION_CONDITION` and `WEAKENING_CONDITION`;
- pre-search `SEARCH-PLAN.md`;
- durable Research Case IDs (`FDP-RC-xxx`) separated from ABR actors/rounds;
- separate match, evidence strength, source authority and verification status;
- raw-private → normalized → optional shareable evidence pipeline with SHA-256 provenance;
- first-class disagreement ledger;
- supported / qualified / prohibited / unresolved claim gates;
- audit vs downstream package scopes;
- `plant` command for freezing a ROLL into a project;
- Portuguese and English seed prompts.

Validation: 5/5 stdlib-only Python tests passed.

Archive SHA-256:

`ccdbf9d813af5d235df87565ce5ba80aa86f3b294ae63c7433b08f3f3900e340`

This snapshot does not claim FlowDisP itself is novel and is not yet a canonical product release.
