# Chat Extraction Triage — Batch 002

Date: 2026-10-01

Status: **ARCHAEOLOGY / SOURCE-PROVENANCE INDEX — NOT NORMATIVE**

## Purpose

This batch contains nine additional Markdown reports generated in different
ChatGPT conversations after asking what each conversation contained about
MyTrues / EDT / CCP / decision memory.

As in batch 001, the reports are secondary sources.

The main goals of this pass are:

- identify genuinely new lineage;
- distinguish chat-local evidence from mixed reconstruction;
- preserve negative evidence where a chat did **not** discuss MyTrues;
- record divergences without harmonizing them;
- avoid promoting assistant extrapolation into PO decisions.

## Source-confidence classes

- **A — chat-local:** explicitly restricted to that conversation.
- **B — mixed reconstruction:** includes branches, recoverable history, prior
  extracts or project-wide reconstruction.
- **C — consolidation/index:** useful navigation, weak origin evidence.

---

## Files reviewed

### A — chat-local / negative sources

#### 1. `FLWD002(n)-- FLWD001.MD`

Classification: **A — strong negative evidence**.

This report explicitly states that MyTrues / EDT / CCP were not substantively
developed in that chat.

Relevant FlowDisP statements include:

- `Chat executes. Files remember. Validators decide.`
- `Repository state canonical; chat memory never canonical.`

But the report explicitly warns that those principles were **not connected to
MyTrues in that conversation**.

Therefore this chat MUST NOT be used to claim that FlowDisP architecture was
already MyTrues architecture.

Value: provenance discipline / negative evidence.

#### 2. `LBWARE-POi-001_001 — ChatGPT Operating Architecture..MD`

Classification: **A — chat-local, narrow**.

This chat contains one useful organizational-memory theme, but also an important
naming warning.

The user wrote:

`MyTools`

in a statement about materializing organizational autoeducation, company pillars
and metaphilosophy into executable/material artifacts.

The assistant then interpreted that as:

`MyTrues`

without explicit confirmation.

Therefore:

- **MyTools MUST NOT be silently normalized to MyTrues**;
- this chat does not prove a rename or synonym;
- the association of MyTrues with organizational technical-culture memory was
  primarily an assistant interpretation in this chat.

The useful conceptual lead is:

```text
organizational autoeducation
-> principles / decisions / restrictions / configuration changes / learning
-> structured historical memory
```

This may be compatible with MyTrues, but this chat alone does not authorize that
mapping.

---

## B — mixed reconstructions / major leads

### 3. `FLOWED2-001LBWARE-POi-001_001 — ChatGPT Operating Architecture..MD`

Classification: **B/C — broad reconstruction**.

Useful additions:

- current FlowED-manifest refinement:
  cognition worth preserving is not accumulated conversation, but the rationale
  that makes a decision understandable, resumable and revisable;
- consolidated document can be normatively authoritative while CCP remains the
  richer epistemic source;
- stated project-sequencing intent:
  build MyTrues before the definitive FlowED rebuild so the new FlowED can record
  its own cognitive path from the beginning.

This is useful project-history evidence, but the file mixes multiple periods.

### 4. `INB-C3_001.MD`

Classification: **B — mixed reconstruction**.

Mostly corroborates already-preserved material:

- decision memory;
- Protocol != Decision Engine;
- DecisionMemory port;
- provider isolation;
- pause/sanitize/resolve/resume;
- SQLite reference;
- DecisionProfile hypotheses.

No unique core concept requiring promotion was found in this pass.

### 5. `linguagens a apreder e mytrues - tica_01.MD`

Classification: **B — broad conversation extraction**.

Useful corroboration:

- explicit `core, ports e adapters` direction;
- algorithm must remain separate from protocol;
- third parties may provide their own algorithm/policy/profile/storage/adapter;
- DecisionProfile / "personalidade decisória";
- provider independence;
- Decision current first, CCP on demand.

Despite the title, this extraction does not provide enough unique TICA-specific
MyTrues material to justify a new TICA/MyTrues dependency.

### 6. `MAN-001-Branch · Branch · FLOWED2-001-LBWARE-POi-001_001 — ChatGPT Operating Architecture..MD`

Classification: **B/C — large reconstruction, valuable technical index**.

This report preserves two technically important periods.

#### Historical 2025 branch

A proposed `mytrues-core` based on:

- Datalog/Prolog;
- facts;
- rules;
- queries;
- explanations;
- `/assert`;
- `/retract`;
- `/query`;
- `/why`;
- append-only/event-sourcing ideas;
- JSON Schema / Protobuf;
- gRPC/HTTP;
- JS/Python/Java/Rust adapters;
- CozoDB;
- TICA-like `capture -> normalize -> distill -> store`.

This is **historical architecture**, not current direction.

#### Executable protocol branch

The report identifies concrete staging artifacts under `Tools/MYTRUES`.

Current repository evidence independently confirms:

- `protocol/openapi.yaml`;
- title: `MyTrues Open Decision Protocol`;
- current OpenAPI info version: **0.2.0**;
- endpoint: `POST /v1/decisions/resolve.failure`;
- `GET /v1/decision-requests/{decisionRequestId}`;
- provider resolution endpoint;
- `mytrues.decision/v1` in current conformance requests;
- schema identifiers under `/protocol/0.2/`;
- provider isolation;
- 202 pending behavior;
- sanitization;
- provider-scoped durable memory after restart.

The report's reference to OpenAPI `0.1.0` is therefore historical, not current.

### 7. `MSOMCP_POC_001.MD`

Classification: **B — mixed reconstruction**.

Mostly corroborates:

- protocol-first;
- DecisionEngine separation;
- ports/adapters;
- SQLite;
- MCP as adapter;
- provider isolation;
- No Retroactive Cognition.

No unique MSOMCP-specific MyTrues core dependency was established.

### 8. `OCONSOANTE_ORACLE_FREETIER_CLOUDFLARE.MD`

Classification: **B/C — broad project reconstruction**.

Useful corroboration and operational history:

- POC/conformance lineage;
- Seed-004 as failure-case corpus;
- provider-scoped decision memory;
- domains `mytrues.dev` and `mytrues.io`;
- IDEOS client relationship;
- open-first direction;
- MyTrues Discovery/product hypotheses.

Most substantive architecture is already better supported by executable evidence
and earlier archaeology.

---

## Critical mixed source

### 9. `mytrues- INTERMEMBERS.DEV_001-VRMP-DEMO-POO-01-DV4-02.MD`

Classification: **B — major research reconstruction**.

This is the most important new file in batch 002.

It contains a substantial branch that moves MyTrues beyond the narrower
"decision memory" definition.

### Claimed promoted direction inside that reconstruction

The report says the conversation promoted:

`Experience` as the primary conceptual unit.

Candidate flow:

```text
Experience
-> considered/interpreted
-> Belief / Argument
-> under Values + Context
-> Position
-> Decision
```

It also explicitly records a semantic pivot:

```text
decision memory
-> broader experiential / epistemic memory
```

with the phrase:

`MyTrues is the SQL of experience.`

This is a **material product/domain divergence** from the current staging, which
is still named and implemented as an Open Decision Protocol.

Because this report is a reconstruction rather than turn-level primary evidence,
this pivot MUST NOT be promoted as the current product definition until the
original chat confirms whether it was an explicit PO decision or an assistant
synthesis.

### Strong research invariants / candidates from this branch

The report additionally preserves:

- time is semantic, not a single timestamp;
- `KNOWN != CONSIDERED != INFLUENCED`;
- `NO INFERRED CAUSALITY AS FACT`;
- `NO COGNITION WITHOUT PROVENANCE`;
- Raw Source != Derived Cognition;
- defeated paths should be retained;
- context is part of applicability;
- `BEST_OBSERVED != SUCCESS`;
- `UNKNOWN` must remain unknown;
- LLM is not epistemic authority;
- provider/model should be replaceable;
- memory should belong to the user/authorized organization;
- vector/embedding is a derived index, not epistemic authority;
- runtime may be disposable while durable cognitive state survives.

Several of these strengthen rules already present in the project.

### New research vocabulary

Candidate research concepts include:

- `Experience Base`;
- `Defeater Base`;
- `Successful Path Base`;
- `Unknown Frontier`;
- `Cognitive Pre-flight`;
- `Cognitive Cartridge`;
- `Cognitive Amortization`;
- `Compiled Cognition`;
- `Current Position`;
- `Historical Position / AS-KNOWN-THEN`;
- `Decision Cell`;
- `CognitiveLink`;
- `Memory Mesh`;
- `Semantic Registrar`;
- `Systematic Agent`;
- `Language Renderer`;
- `Claim Checker`;
- `Experiment Engine`;
- `Gold Evaluator`;
- `CandidateRelation`.

These are not current protocol entities merely because this branch names them.

### Research mechanisms surveyed in the branch

The branch explores or inventories:

- Case-Based Reasoning;
- spreading activation;
- TMS / ATMS;
- AGM belief revision;
- structured argumentation;
- graph cognition;
- vectors;
- episodic/semantic/working memory;
- active inference;
- attention/forgetting/consolidation/replay;
- ACT-R / SOAR / CLARION / LIDA;
- Graphiti / FalkorDB / Qdrant;
- agent-memory systems.

No final stack was selected.

### Important architecture boundaries in this branch

#### Vector is not epistemic authority

```text
VECTOR
= associative retrieval

GRAPH
= explicit relationship structure

EVIDENCE / PROVENANCE
= epistemic support
```

Embeddings are treated as derived/rebuildable.

#### Activation is not truth

```text
activation score
!= truth score
```

Candidate separation:

- Epistemic Graph = persistent justified relations;
- Activation Graph = transient attention/retrieval state.

#### Candidate relation is not canonical relation

An LLM/Semantic Registrar may propose links.

It does not gain authority to canonize them.

#### Decision Cell

A decision is hypothesized as a structured cognitive subgraph containing:

- trigger/problem;
- goal;
- context;
- assumptions;
- known/considered at the time;
- alternatives;
- arguments;
- evidence;
- criteria/values;
- decision;
- action;
- observed outcome;
- revision/supersession.

Status: hypothesis, not schema.

### Microbrain pivot

This branch records a major research-method correction:

```text
Graphiti-first
-> Microbrain-first
```

Instead of selecting graph/vector infrastructure first:

```text
Python + SQLite + controlled schema + controlled fixtures
+ gold questions + deterministic systematic agent
+ deterministic evaluator + experiment runner
```

would test cognitive-organization mechanisms before product architecture is
selected.

This is consistent with the already-preserved Microbrain meta-proposal, which
remains **not authorized for execution**.

### Provider-scoped memory versus user-owned memory

The branch surfaces another unresolved tension.

Earlier operational model:

`memory scoped by provider`

Later branch:

`user-owned memory + provider replaceable`

These can potentially coexist through user-owned memory with provider-scoped
partitions/provenance, but **that reconciliation is not yet formalized**.

### PAUSE/SANITIZE/RESOLVE centrality

The branch reports that the decision-protocol lifecycle became less central in
the SQLDAVELHA/Microbrain line.

Possible newer research flow:

```text
query
-> structured epistemic state
-> experiment if needed
```

This does not repeal v0.2 behavior.

It is another sign that the Experience branch may represent a broader research
domain than the executable decision protocol.

---

## Promoted findings from batch 002

The following are safe to preserve without changing current protocol semantics.

### H9. Do not treat `MyTools` as a MyTrues alias

There is now direct chat-local evidence that an assistant changed `MyTools` to
`MyTrues` without explicit confirmation.

Therefore any archaeology search should include `MyTools` as a lead but must not
claim a formal rename/synonym unless primary evidence confirms it.

### H10. Early MyTrues had a logic/rules branch

The 2025 lineage includes a Datalog/Prolog/facts/rules/query/explanation model.

Preserve it historically.

Do not revive it as current architecture without a new reason/gate.

### H11. Current executable protocol evidence supersedes historical report version labels

Current repository evidence is authoritative for the staging runtime:

- OpenAPI info version `0.2.0`;
- schema/conformance version `0.2`;
- protocol request identifier `mytrues.decision/v1`.

Historical `0.1.0` references remain lineage only.

### H12. Organizational autoeducation is a possible consumer/use case, not proven MyTrues identity

The FlowED manifesto line suggests value in retaining organizational learning,
principles, decisions and reasons for configuration changes.

But the strongest chat-local occurrence was triggered by `MyTools` and then
mapped to MyTrues by the assistant.

Therefore this should be treated as a **possible application/use case**, not a
core MyTrues requirement.

### H13. Experience-first is a major unresolved branch

The Experience branch is too consequential to silently merge with the current
Decision Protocol.

For now preserve both:

```text
CURRENT EXECUTABLE BASELINE
MyTrues Open Decision Protocol v0.2
-> DecisionRequest / decision memory / provider lifecycle

RESEARCH BRANCH
Experience-first MyTrues
-> experiential / epistemic memory
-> decision as one derived state/object
```

A future PO decision or primary-chat forensic extraction must establish whether:

- Experience-first supersedes decision-memory identity;
- Experience is only a research-layer substrate beneath DecisionRecord;
- or the two should become separate bounded contexts/products.

### H14. Current memory ownership model needs reconciliation

Preserve the tension:

```text
provider-scoped operational memory
vs
user-owned memory with replaceable provider
```

Do not silently pick one.

### H15. Retrieval/attention mechanisms must remain separate from epistemic authority

The Experience branch gives a strong reusable design constraint:

- similarity is not truth;
- activation is not truth;
- candidate relation is not canonical relation.

This is consistent with the existing authority/provenance boundary and deserves
retention in future experiments.

---

## What batch 002 does NOT authorize

This batch does not authorize:

- changing MyTrues from Decision Protocol to Experience Protocol;
- making `Experience` a normative protocol entity;
- adopting Decision Cell;
- adopting Memory Mesh;
- adopting Graphiti/FalkorDB/Qdrant;
- starting Microbrain;
- making spreading activation/TMS/CBR the engine;
- replacing provider isolation;
- equating MyTools and MyTrues;
- changing v0.2 wire behavior.

## Forensic follow-up required

One original chat is important enough to revisit before any v0.3/domain
redefinition:

`mytrues- INTERMEMBERS.DEV_001-VRMP-DEMO-POO-01-DV4-02`

Goal:

determine whether the Experience-first pivot was an explicit PO decision or an
assistant/research synthesis.

Other chats in this batch do not need interrogation before the next archaeology
batch.


## Uploaded-byte identities

The exact uploaded byte streams reviewed in this batch were:

| File | Bytes | SHA-256 |
|---|---:|---|
| `FLOWED2-001LBWARE-POi-001_001 — ChatGPT Operating Architecture..MD` | 33322 | `e879b5ccf04c57db19f561ef03e87721f269b30c07d69deb05f2c382b14e7807` |
| `FLWD002(n)-- FLWD001.MD` | 12794 | `b60c2c9da9e13968233cefafc7f7cb13f6d43863dd16a9ff368711f6b7cf05f7` |
| `INB-C3_001.MD` | 21711 | `14e55a4e3ea053dcdcccfe1ed5561a527e83af97f9f71e4ffb78e2886df54d62` |
| `LBWARE-POi-001_001 — ChatGPT Operating Architecture..MD` | 9920 | `a2c67ce2aa433113cdf9a0dd1ee24c996ebcb2918eafe26e07d79f4836513cae` |
| `linguagens a apreder e mytrues - tica_01.MD` | 24862 | `0ad6f01fc8961af75ea4728eb7d22cb9a068bbe6edd75fad28651485f86320bc` |
| `MAN-001-Branch · Branch · FLOWED2-001-LBWARE-POi-001_001 — ChatGPT Operating Architecture..MD` | 35263 | `3c91ef65e9c5f360d96aff9937b4556ddf847a234dae25a39f3c4ff60ea788bf` |
| `MSOMCP_POC_001.MD` | 23086 | `7cbe330d2a547822c9fddb849120ad15c590aba8e21880b1af9b696bb786ac8f` |
| `mytrues- INTERMEMBERS.DEV_001-VRMP-DEMO-POO-01-DV4-02.MD` | 41984 | `43c26f6eb98c1f22247f2ef3cfa00ffd2938631ec3130a77f93df6b57127aea3` |
| `OCONSOANTE_ORACLE_FREETIER_CLOUDFLARE.MD` | 32161 | `7e0766ca75137d626e98c6d6d5de693ad6082d62e99f84d92c464b6e00fc0739` |

The hashes identify the exact secondary reports reviewed. They do not convert the
reports into primary turn-level evidence.
