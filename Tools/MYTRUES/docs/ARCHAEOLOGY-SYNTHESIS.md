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


## Drive archaeology additions

The Google Drive archaeology added earlier conceptual artifacts and working
decision examples that were not preserved as clearly in Git history.

### 11. Cognitive keyframes instead of exhaustive thought capture

The February 2025 CCW material proposed **cognitive keyframes**: selected
decision/reflection moments along a creator path.

This is better aligned with the current MyTrues boundary than an attempt to
capture every internal thought.

Candidate invariant:

- CCP SHOULD preserve explicit, intentionally recorded decision-relevant
  milestones;
- CCP MUST NOT require hidden chain-of-thought;
- a current decision remains independently consumable without traversing its
  full provenance path.

This reinforces the current-decision-first rule already promoted to
`CCP-RECORD.md`.

### 12. Case criteria are not decision-profile preferences

The August 2025 Drive pair:

- current decision: `framework-choice-decision`;
- cognition path: `framework-choice-cognition`;

shows explicit criteria such as performance, package size, DOM control, state
management and complexity.

Those criteria explain **that decision case**.

They are not yet a reusable model of the chooser's recurring preferences.

This distinction should remain explicit in future design:

```text
DecisionContext / DecisionRecord
  -> criteria relevant to this case

DecisionPolicyProfile
  -> reusable preferences/trade-offs of a provider/authority
```

A future decision engine may combine both, but the protocol should not silently
infer a durable preference from one case.

### 13. Intent / decision / execution-state provenance

The March 2025 FlowED Line Interface material separated:

- cognitive backlog / intent before implementation;
- cognitive changelog / actual attempts and decision evolution;
- environment/state changes.

The exact FlowED representation is not a MyTrues protocol requirement.

The reusable lesson is that **intent, decision and observed outcome/state are
different provenance objects** and should not be collapsed into a single
DecisionRecord field.

### 14. Science Frontier design-space method predates the current gate

The September 2026 `MYTRUES-DISCOVERY-001` Drive artifact already formalized
the methodological core of the current Science Frontier Gate:

- high-recall discovery before architecture selection;
- historical and contemporary coverage;
- evidence-class separation;
- primary-source preference;
- contradiction preservation;
- no winner selection during discovery;
- variables/parameters as machine-readable experiment dimensions;
- explicit compatibilities/incompatibilities;
- benchmark and open-question registries;
- GO/DONT_GO gates;
- provenance and numeric-range honesty.

This should be retained as a **research-method ancestor** and reused when
evaluating any proposed proprietary/original MyTrues Decision Engine.

It is not evidence that a new algorithm is scientifically novel; it defines how
we must investigate that question.

## Drive legacy corpus

Concrete TRUEs recovered from Drive (routing, rendering, naming, framework
choice and related examples) should be treated as a **legacy decision corpus
candidate**, not protocol specification.

Potential future uses:

- old-TRUE -> DecisionRecord migration tests;
- CCP extraction/conversion fixtures;
- preference-profile elicitation experiments;
- re-decision tests using changed context/evidence;
- comparison of current decision versus recorded cognitive path.

Do not use this corpus as a scientific benchmark until it has a frozen sampling
protocol, labels, task definition and scoring methodology.


## Uploaded research additions — SQLDAVELHA / Microbrain

Three additional user-supplied artifacts were inspected on 2026-10-01:

- `MTR-METAOBJECTIVE-001 — MYTRUES APPLIED TO MYTRUES`;
- `MYTRUES-META-PROPOSAL-001`;
- `GROK-MYTRUES-COGNITIVE-DISCOVERY-001`.

They add research direction and external-discovery evidence but do not change
the current v0.2 protocol baseline.

### 15. Exchange repeated intelligence for accumulated experience

The metaobjective gives a compact recurring principle, illustrated by
`SQLDAVELHA`:

> Do not repeatedly solve what accumulated experience has already made
> queryable.

The reusable MyTrues form is:

```text
context
+ action/configuration
-> observed consequence
```

This is a research hypothesis about materializing useful experience, not a claim
that every decision domain is finite or enumerable.

It is compatible with the existing decision-memory direction because MyTrues
already preserves provider-scoped decisions and abstains on unknown cases.

### 16. Separate semantic assistance from epistemic authority

The metaobjective sharpens a boundary already implicit in the current staging:

```text
LLM
-> interpretation
-> candidate association
-> language rendering

registered memory + systematic mechanism
-> what may be claimed
```

Candidate relations proposed by an LLM must not silently become canonical
relations.

Likewise, an LLM renderer must not add factual/causal claims not authorized by
the structured result.

This is a strong research invariant for later experiments and should be tested,
not merely asserted.

### 17. MyTrues-applied-to-MyTrues dogfooding

The metaobjective proposes that each architecture/configuration experiment itself
become a MyTrues-style experience:

```text
dataset/context
+ cognitive configuration
+ question set
-> observed performance
```

That would allow the research process to distinguish, under recorded context:

- unknown configuration;
- known-defeated configuration;
- best-observed-so-far configuration;
- context-dependent result.

This is a useful long-range research loop because it makes architecture
selection evidence-bearing rather than opinion-bearing.

It remains **RECORD ONLY** until explicitly promoted by the PO.

### 18. Proposed Microbrain is an instrument, not the product

`MYTRUES-META-PROPOSAL-001` proposes a future bounded
`MYTRUES-MICROBRAIN-V0` experiment with:

- controlled fixtures;
- deterministic systematic answer path;
- deterministic gold evaluation;
- explicit context/temporal/supersession/defeater switches;
- repeatable reset/replay;
- machine-readable configuration -> consequence evidence.

The package contains no PO acceptance.

Therefore this synthesis preserves the proposal but does not convert it into an
active demand.

### 19. External discovery runs require independent qualification

The supplied Grok Discovery run is valuable but demonstrates why a producing
model must not self-certify its own package.

As received:

- package hashes are internally consistent;
- overall self-declared status is already `DONT_GO`;
- three required JSON files do not parse;
- its manifest declares 42 mechanisms / 68 variables while the delivered
  parseable payload contains 20 / 23 and its own executive map says 20 / 23;
- it self-declares G7 machine readability as GO despite the parse failures.

Therefore:

**external Discovery output is candidate research input until independently
qualified.**

Checksums prove byte integrity, not scientific or schema correctness.

Preserved qualification:

`research/external-runs/GROK-MYTRUES-COGNITIVE-DISCOVERY-001-QUALIFICATION.md`


## Conversation reconstruction additions

Four user-supplied reconstructions of earlier conversations were reviewed on
2026-10-01.

They are secondary archaeology sources, not primary specifications.

Exact uploaded-byte identities are recorded under:

`docs/archaeology/conversation-reconstructions/`

### 20. No Retroactive Cognition

One reconstruction recovers the explicit phrase:

`NO RETROACTIVE COGNITION`

This is consistent with the temporal/provenance direction and has now been
promoted into `CCP-RECORD.md` as a documentary invariant:

- preserve what was known/considered at the time;
- later evidence creates reevaluation/supersession;
- do not rewrite historical cognition as if later knowledge had existed earlier.

### 21. CCP-as-source -> Views-as-build

The reconstructions recover a strong documentation model:

`CCP-as-source -> Views-as-build`

with candidate views such as:

- NORM — current normative/consolidated view;
- WHY — rationale;
- TRACE — provenance/history;
- ADR — interoperability view;
- onboarding/risk/policy/timeline/graph views.

They also distinguish:

- Tier 0 — deterministic;
- Tier 1 — deterministic template;
- Tier 2 — LLM-assisted narrative.

This is a useful candidate model for derived documentation because it avoids
calling unconstrained generation a deterministic compilation.

It remains a design candidate until view contracts are specified and tested.

### 22. AKU / Digital Neuron is a historical representation hypothesis

The VRAMPP reconstruction links:

`Atomic Knowledge Unit -> Digital Neuron -> connected cognition -> MyTrues`

but explicitly records that AKU was never frozen as the native MyTrues unit.

It also separates MyTrues from the learning/pedagogical layer.

Therefore:

- preserve AKU/digital-neuron terminology as historical/research input;
- do not make it a current protocol schema;
- do not make MyTrues itself an education platform.

### 23. MyTrues Discovery is a separate historical product branch

The D2/Project Miner reconstruction records a substantial branch named:

`MyTrues Discovery`

focused on project/corpus discovery, authority mapping, conflicts, duplicates,
gaps, opportunities, candidates and evidence packages.

That branch is preserved separately at:

`research/product-branches/MYTRUES-DISCOVERY-HISTORICAL.md`

It must not silently broaden the current decision protocol.

A particularly reusable invariant from that branch is:

`MCP = adapter, not core`

which is compatible with the current port/adapter architecture.

### 24. Canonical promotion is explicit

The reconstructions repeatedly distinguish agent/LLM output, OUTBOX or proposal
from canonical MyTrues memory.

That rule has now been promoted into `CCP-RECORD.md`:

`proposal/staging -> authority decision -> canonical retention`

rather than automatic promotion.

### 25. EDT expansion and CCP DOI require primary verification

One reconstruction explicitly names EDT as:

`Education-Driven Thinking`

and says the user described CCP as an authored concept with a DOI.

Other reconstructions note that the literal EDT expansion was not consistently
recoverable.

Therefore:

- `Education-Driven Thinking` is a strong historical candidate expansion;
- the CCP DOI/authorship statement is preserved as a claim;
- neither should be presented as bibliographically verified until the primary
  DOI/source record is located.

### 26. Historical licensing/org plans are superseded by current explicit north

The reconstructions preserve older plans such as:

- Apache-2.0 preference for incorporated modules;
- a larger MyTrues org with `cli/kernel/paper/replication/site/spec`;
- possible open-core/commercial decision-engine boundaries.

The current authorized reorganization explicitly selects:

- `MyTrues/mytrues`;
- `MyTrues/ideos`;
- MIT for both initial canonical repositories.

Therefore the older organization/licensing plans remain archaeology, not current
execution authority.

### 27. Working reconciliation: CCP central to EDT, optional to basic decision use

The reconstructions expose a real tension:

- historically CCP is central to EDT/MyTrues identity;
- operationally a consumer often needs only the current DecisionRecord;
- some later technical sketches treat CCP linkage as optional.

A useful working reconciliation is:

```text
generic decision interoperability
  -> DecisionRecord can be consumed directly

deep audit / learning / reevaluation / EDT research
  -> linked CCP Record
```

Thus CCP can remain scientifically central to EDT without forcing every routine
decision lookup to transport the complete cognitive history.

This is a synthesis/reconciliation, not yet a normative protocol amendment.


## Chat-extraction batch 001 additions

A new batch of chat-local and mixed conversation extractions was reviewed on
2026-10-01.

Source-confidence and per-chat provenance are recorded at:

`docs/archaeology/CHAT-EXTRACTION-TRIAGE-001.md`

### 28. Original two-axis memory lineage

The strongest early chat-local source distinguishes:

```text
OMGDiary
-> temporal / episodic cognition

MyTrues
-> semantic / decision-oriented "truths"
```

This is useful genealogy.

It should not replace the current DecisionRecord/CCP separation, but it explains
why the project repeatedly distinguishes chronology from decision semantics.

### 29. TrueEngine is historical nomenclature only

An early four-layer proposal contained:

1. OMGDiary — episodes;
2. MyTrues — truths;
3. TrueEngine — inference;
4. OMG — epiphany.

`TrueEngine` is not current architecture.

Preserve it as lineage only.

Do not present current `DecisionEngine` as a proven direct rename unless a
primary historical source establishes continuity.

### 30. Local contextual authority predates the formal protocol

A chat-local extraction records an early rule equivalent to:

`project-local decision + why -> consult before generic LLM knowledge`

This predates the later names `DecisionMemory`, `Authority` and
candidate/canonical promotion.

It is a useful historical precursor of the current epistemic-authority boundary.

### 31. Raw source is not CCP

A FlowED/CCP chat-local POC independently established:

`raw source/log != annotation != structured CCP != projection`

This is an important EDT/CCP invariant.

A conversation transcript or session log is therefore not automatically a CCP
Record merely because it contains cognition.

### 32. Candidate multi-time epistemic model

A later mixed reconstruction proposes distinct times:

- `event_time`;
- `known_time`;
- repeatable `considered_time`;
- `decision_time / promoted_time`;
- `recorded_time`;
- `valid_from / valid_until`.

The rationale is strong: occurrence, awareness, consideration, promotion,
recording and validity need not coincide.

This remains a **research/schema candidate**, not protocol law.

It should be compared with temporal database, bitemporal, provenance and belief
revision prior art before promotion.

### 33. Chronology is not causality

The same lineage distinguishes a chronological graph from a causal-cognitive
graph.

Reusable invariant:

`A before B` MUST NOT be silently promoted to `A caused B`.

Causal relations require explicit evidence/authority.

### 34. Defeated paths are candidate reusable experience

The SQLDAVELHA lineage sharpens the memory hypothesis:

`failed / defeated path != useless history`

Under equivalent context, a defeated path may reduce future search.

This remains a research hypothesis and must be compared against established
case-based reasoning, negative experience, planning/search memory and automated
algorithm-configuration literature.

### 35. Epistemic state and linguistic rendering are separate

A recovered formulation states:

```text
MyTrues = KNOWING
"What may I claim?"

LLM = SAYING
"How should I explain it?"
```

This is consistent with the current authority boundary.

A language model may interpret or render a structured answer, but it must not
silently alter the epistemic state returned by the authoritative memory/decision
process.

### 36. MyTrues Discovery remains a separate branch

The new batch reinforces that `MyTrues Discovery` emerged from a separate
Project Miner / Truth Engine lineage.

It remains preserved as a historical/research product branch and must not be
silently merged into the generic decision protocol.


## Chat-extraction batch 002 additions

Nine additional conversation-derived reports were reviewed on 2026-10-01.

Per-chat source confidence and findings are recorded at:

`docs/archaeology/CHAT-EXTRACTION-TRIAGE-002.md`

### 37. `MyTools` is not a proven alias of MyTrues

A strict chat-local source records the user writing `MyTools` and the assistant
then normalizing it to `MyTrues` without confirmation.

Therefore:

- include `MyTools` in archaeology searches;
- do not claim `MyTools -> MyTrues` rename/synonym without primary proof;
- do not use assistant normalization as evidence of user intent.

### 38. Organizational autoeducation is a candidate use case

A FlowED-manifest chat discusses materializing organizational learning, company
principles, technical culture, configuration changes and reasons for change.

The strongest local occurrence uses `MyTools`, while MyTrues is introduced by
the assistant afterward.

Therefore this is useful as a **possible MyTrues consumer/use case**, not a
proven core requirement.

### 39. Early technical lineage used logic/rules

A mixed reconstruction preserves a 2025 MyTrues technical branch based on:

- Datalog/Prolog;
- facts/rules/queries/explanations;
- `/assert`, `/retract`, `/query`, `/why`;
- append-only/event-sourcing ideas;
- JSON Schema / Protobuf;
- HTTP/gRPC;
- CozoDB.

This is historical architecture.

The current staging is protocol-first and independently verifies OpenAPI 0.2.0,
JSON Schema v0.2, provider isolation, pending/resolve/resume and durable SQLite
provider memory.

See:

`docs/archaeology/EARLY-TECHNICAL-LINEAGE.md`

### 40. Current protocol version evidence supersedes historical report labels

A report mentions OpenAPI `0.1.0`.

The current repository artifact says:

`MyTrues Open Decision Protocol / info.version 0.2.0`.

Current conformance code also requires schema IDs under `/protocol/0.2/`.

The request identifier `mytrues.decision/v1` is a different versioning surface
and remains present.

Do not collapse document version, protocol identifier, schema version and product
version.

### 41. Experience-first MyTrues is a major unresolved domain branch

The InterMembers/VRMP reconstruction records a substantial pivot from:

`decision memory`

toward:

`Experience as primary conceptual unit`

and the phrase:

`MyTrues is the SQL of experience.`

This is too consequential to merge silently with the current Open Decision
Protocol.

It is preserved at:

`research/branches/EXPERIENCE-FIRST-MYTRUES.md`

Until forensic confirmation from the original chat:

- current executable baseline remains decision-protocol v0.2;
- Experience-first remains a research/domain branch.

### 42. Defeated paths are candidate first-class reusable experience

The Experience branch strengthens the SQLDAVELHA hypothesis by treating known
failures as assets rather than disposable history.

Candidate concepts:

- Experience Base;
- Defeater Base;
- Successful Path Base;
- Unknown Frontier;
- Cognitive Pre-flight;
- Cognitive Amortization;
- Compiled Cognition.

These require prior-art comparison before protocol promotion.

### 43. Retrieval attention must not become epistemic authority

The Experience branch makes several useful separations:

```text
vector similarity != truth
activation score != truth score
candidate relation != canonical relation
chronology != causality
```

These are compatible with the existing authority/provenance boundaries and
should be retained as experiment invariants.

### 44. Decision Cell is a representation hypothesis

A decision is explored as a structured cognitive subgraph containing trigger,
goal, context, assumptions, known/considered-at-the-time, alternatives,
arguments, evidence, criteria, decision, action, observed outcome and revision.

This is not a normative schema.

### 45. Provider-scoped versus user-owned memory remains unresolved

Two desirable properties now coexist in the archaeology:

```text
provider-scoped operational memory
```

for isolation, and:

```text
user-owned memory + replaceable provider
```

for portability/control.

A possible user-owned store with provider-scoped partitions is only a candidate
reconciliation.

No protocol amendment is authorized.

### 46. FlowDisP negative evidence must remain negative

One strict chat-local report explicitly says MyTrues was not developed in that
FlowDisP conversation.

Principles such as repository-canonical state, externalized memory and
deterministic validators may be relevant analogies, but that conversation did
not establish them as MyTrues requirements.

Do not retroactively merge the domains.
