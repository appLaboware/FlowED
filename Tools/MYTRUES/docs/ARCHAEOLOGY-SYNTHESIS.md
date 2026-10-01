# MyTrues Archaeology Synthesis

Date: 2026-10-01

Status: **design input, not v0.2 normative specification**

This document consolidates reusable ideas recovered from the accessible MyTrues
lineage and compares them against the current generic v0.2 staging.

## Current baseline wins

The current FlowED staging remains the strongest executable baseline because it
already proves:

- provider-scoped decision memory;
- different providers may legitimately decide differently;
- explicit abstention/pause for unknown cases;
- sanitized case packet;
- explicit human/provider resolution;
- resume after resolution;
- SQLite persistence across restart;
- open/core boundary;
- conformance evidence.

Older material must not replace these properties.

## Promote as future protocol requirements

### 1. Stable record identity

Recovered from the MultiUni embedded MyTrues.

The protocol should eventually require a stable identifier for a persistent
decision record independent of content revisions.

The legacy implementation used UUID v4 as `truth_id`.

**Promote the invariant, not the exact UUID choice yet:**

- identity MUST remain stable across revisions;
- revisions MUST NOT silently create a new logical record;
- requests/executions and persistent decisions are distinct identities.

### 2. Design-rationale structure

Recovered strongly from InitProjHQ scientific planning and the MultiUni world scan.

Future CCP/decision records should be able to represent:

- Issue / question;
- Options / alternatives;
- Criteria;
- Decision;
- Rationale / arguments;
- Evidence.

This aligns with IBIS/QOC/ADR prior art and should be mapped to those models
rather than invented as a private ontology.

### 3. Formal provenance interoperability

Recovered from InitProjHQ.

W3C PROV should be evaluated as an **optional interoperability/export mapping**
for actors, activities, entities and source provenance.

Do not build a proprietary provenance model before exhausting PROV.

### 4. Decision lifecycle semantics

Recovered from PLAN-MYTRUES-THESIS-0001.

Candidate semantics:

- `reopen`;
- `supersede`;
- `deprecate`;
- `valid_from`;
- `valid_to`;
- explicit trigger/condition for re-evaluation.

These are more precise than the old generic notion of "truth evolution" and fit
a domain-generic decision protocol.

They require versioned protocol design and conformance before becoming normative.

### 5. Human-reviewed merge/sync

Recovered from MultiUni.

Useful invariants:

- compare by stable record identity;
- detect divergent content/metadata/relations;
- never overwrite silently;
- produce a deterministic conflict report;
- require explicit human/authority resolution;
- preserve author/provenance of resolution.

This aligns well with the current MyTrues rule that unknown/conflicting authority
must not be auto-promoted to truth.

### 6. Portable export

Recovered implementation already exports historical records to JSONL.

Portable export is valuable for:

- backup;
- research/replication;
- migration;
- audit;
- interoperability.

The legacy JSONL schema is only a POC. A future export format must derive from
the canonical protocol schema.

### 7. Compiled views

Recovered from InitProjHQ.

A canonical decision record may generate read-only views such as:

- ADR;
- onboarding;
- policy/rule;
- risk;
- change timeline.

This is stronger than manually maintaining parallel documentation because views
remain derived from one source of truth.

### 8. Static publication

Recovered from MultiUni.

The old static renderer proves the idea with a very small implementation.

Future design should prefer established publication tooling (MkDocs/Docusaurus,
Log4brains where suitable) over growing a custom renderer, unless a minimal
generated view is needed for conformance.

### 9. Separate cognitive provenance from normative decision

Recovered from the earliest FremUX EDT/CCC lineage and now reflected by
`CCP-RECORD.md`.

The valuable part of the early two-track model is:

- chronological/episodic source material;
- normative/current decision;
- explicit links between them.

Do **not** preserve the old brain/neural-network metaphor as architecture.

CCP should remain a provenance/documentary layer over decisions.

### 10. Scoped specialization without OOP metaphors

Early MyTrues/NGit material proposed global/local truth inheritance and overrides.

The useful requirement is narrower:

- provider/project/domain policy may specialize a broader decision/policy;
- the relationship must be explicit and auditable.

Do not normatively model this as class inheritance/polymorphism unless later
research proves that representation is useful.

## Preserve as research candidates, not runtime

The recovered MultiUni scripts are preserved under:

`research/legacy-candidates/`

Classification:

- `mytrues_uuid.py` — useful POC for stable identity;
- `mytrues_export.py` — useful POC for portable export;
- `mytrues_merge.py` — useful POC for deterministic conflict detection;
- `mytrues_static.py` — useful proof of compiled/static views;
- `mytrues_vector.py` — **historical baseline only**.

The vector POC uses a hashing/bag-of-words embedding into SQLite. It must not be
represented as a serious vector-search implementation or promoted over adopted
retrieval engines.

## Preserve historically but do not promote

The following older concepts remain useful as intellectual lineage but are not
current architecture:

- "Truth Neural Network" as literal system architecture;
- emotional synaptic weights as decision authority;
- automatic global federation/marketplace claims;
- MyTrues as a social operating system;
- automatic generation of operational truth from LLM output;
- MyTrues as a replacement for agent-memory products;
- MyTrues as a custom vector database;
- MyTrues as a generic PKM/notetaking application.

## Research gate

Several recovered claims explicitly describe scientific novelty or superiority.

They remain **claims/hypotheses**, not accepted facts.

Before promotion they must pass the existing evolution/science gates, including
reproduction/comparison against:

- ADR/MADR;
- IBIS/QOC;
- W3C PROV;
- Case-Based Reasoning;
- decision tables / DMN;
- relevant agent-memory systems;
- retrieval baselines;
- empirical evaluation methodology.

## Recommended next generic protocol shape

Without changing v0.2, the next design exploration should consider:

```text
DecisionRequest
  -> selected provider/authority
  -> Decision | Pending

Persistent DecisionRecord
  - stable record identity
  - domain/context
  - issue
  - options
  - criteria
  - rationale
  - evidence
  - provenance links
  - lifecycle state
  - validity window
  - supersession/reopen relations
  - optional CCP Record link

Derived views
  - ADR
  - policy
  - onboarding
  - risk
  - timeline

Interoperability
  - canonical JSON schema
  - portable export
  - optional W3C PROV mapping
```

This shape is a research/design candidate only. v0.2 conformance remains the
executable protocol baseline until a versioned successor is specified and proved.
