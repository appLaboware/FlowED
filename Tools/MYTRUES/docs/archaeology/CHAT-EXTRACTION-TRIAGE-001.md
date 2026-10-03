# Chat Extraction Triage — Batch 001

Date: 2026-10-01

Status: **ARCHAEOLOGY / SOURCE-PROVENANCE INDEX — NOT NORMATIVE**

## Purpose

This batch contains Markdown reports generated in different ChatGPT conversations
after asking each chat what it contained about MyTrues / EDT / CCP / decision
memory.

The reports are **secondary sources**.

They are not equivalent evidence:

- some explicitly restrict themselves to the chat in which they were generated;
- some explicitly incorporate other conversations, branches, memory or prior
  extracts;
- some are broad consolidations useful as search indexes but weak for proving
  where a concept originated.

Therefore this document records **what each chat can plausibly prove**, what is
only a lead, and which ideas are worth carrying forward.

## Source-confidence classes

### A — chat-local extraction

The report explicitly says it is restricted to that conversation and does not
import other conversations/memory.

Useful for attributing that a concept existed in that chat, subject to later
forensic verification of literal speaker/turn.

### B — mixed reconstruction

The report says it used recoverable history, branches, prior extracts or related
conversations.

Useful for discovering concepts and candidate lineages.

Not sufficient by itself to prove origin in the titled chat.

### C — consolidation/index

The report is mainly a synthesis over already-recovered material.

Useful as a navigation aid, not as origin evidence.

## Files reviewed

### A — strongest chat-local sources

#### 1. `Diário de Decisões Criativo.MD`

Value: **foundational genealogy**.

Unique/high-value material:

- two complementary memory tracks:
  - OMGDiary = temporal/episodic cognition;
  - MyTrues = semantic/decision-oriented "truths";
- a True/decision may link back to cognition UUIDs;
- original `CCC — Caminho Cognitivo do Criador` naming;
- POO analogy:
  - verticalization = specialization/refinement;
  - horizontalization = contextual variants;
  - specific experience may generalize upward;
- `OMG` = epiphany that can change a higher-level conceptual truth;
- historical four-layer proposal:
  1. Episodes — OMGDiary;
  2. Truths — MyTrues;
  3. Inference — TrueEngine;
  4. Epiphanies — OMG.

Important boundary:

`TrueEngine` is preserved only as a **historical name/hypothesis**. It was not
shown to survive as current architecture.

This source is especially valuable for documenting **how MyTrues began**, not how
the current protocol works.

#### 2. `Escolha Plataforma IA Agentes.MD`

Value: **early operational semantics**.

The report explicitly says it is restricted to that conversation.

High-value material:

- MyTrues was explicitly called a **"banco de verdades"**;
- project-local decisions were treated as contextual authority, e.g. NPM vs PNPM;
- the local decision base should be consulted before relying on generic LLM
  knowledge;
- decisions should carry the **why**, not merely the selected value;
- MyTrues should be consulted by agents, including during the production of new
  agents;
- MyTrues was framed as a first fictitious client/case of a larger agent-based
  software-production platform;
- strong dogfooding loop:
  `platform builds MyTrues -> platform uses MyTrues -> MyTrues helps future builds`.

Important nomenclature ambiguity:

- the transcript/report also contains `MyTools`;
- no chat-local evidence proves whether this was an intentional earlier name,
  transcription error or informal variant;
- do not encode `MyTools -> MyTrues` as a formal rename without primary turn
  evidence.

This source is especially important because it predates the later language of
"decision memory" while already expressing the functional semantics.

#### 3. `[transit] PO01-001-isol=ccp-mkdoc-Branch · FLOWED2-001-LBWARE-POi-001_001 — ChatGPT Operating Architecture..MD`

Value: **independent CCP technical evidence**.

The report explicitly says MyTrues itself was not developed there.

That negative evidence is useful: it shows CCP has an architecture independent
of MyTrues.

Strong material:

```text
preserved source/log
-> non-destructive marking/annotation
-> structured CCP
-> projection contract
-> adapter
-> projection
```

Explicit rule:

`Raw log is not CCP.`

The POC reportedly implemented:

- preserved P2.3 source;
- 14 exact non-destructive markings;
- typed CCP in JSON;
- explicit projection contract;
- adapter;
- REDUCT-MAX / BASE / DEFESA;
- Git/blob/SHA provenance;
- tests for tampering, invented citation, bad spans, bad IDs, unknown refs and
  projection invariants.

Projection family:

```text
REDUCT-MAX <- ... <- BASELINE -> ... -> EXPAND-MAX
                         |
                         v
                       DEFESA
```

Key conceptual separation:

- editorial-density axis and argumentation axis are not the same;
- DEFESA is not merely "more text";
- monotonic expansion/reduction is different from broader semantic invariance.

This material belongs primarily to **CCP/EDT architecture**, not automatically
to the MyTrues decision protocol.

## B — mixed reconstructions with unique leads

### 4. `Branch · Branch · Branch · OCONSOANTE_ORACLE_FREETIER_CLOUDFLARE.MD`

Value: **temporal/epistemic model lead**.

Unique candidate model:

- `event_time`;
- `known_time`;
- repeated `considered_time`;
- `decision_time / promoted_time`;
- `recorded_time`;
- `valid_from`;
- `valid_until`.

Important rationale:

an event may occur before it is known; it may be known before it is considered;
it may be considered multiple times before becoming a decision.

Also distinguishes:

- chronological graph;
- causal-cognitive graph.

Explicit rule:

`chronological precedence does not prove causation`.

This is a strong candidate for the Science Frontier inventory around temporal
epistemology and No Retroactive Cognition.

It is **not yet a normative MyTrues time model**.

### 5. `Branch · Branch · Branch · Branch · OCONSOANTE_ORACLE_FREETIER_CLOUDFLARE_2.MD`

Value: **recent epistemic/reuse hypothesis**.

High-value material:

- SQL tic-tac-toe analogy;
- phrase `Trocar inteligência por memória`;
- failed/defeated paths as reusable knowledge;
- candidate epistemic states:
  - `KNOWN`;
  - `DEFEATED`;
  - `PARTIALLY_KNOWN`;
  - `UNKNOWN`;
  - `CONFLICTING`;
- `UNKNOWN` as a legitimate answer;
- separation:
  - `MyTrues = KNOWING / What may I claim?`;
  - `LLM = SAYING / How should I explain it?`;
- rule:
  `LLM may transform representation, never epistemic state`.

This source strengthens the SQLDAVELHA/metaobjective line already preserved in
research.

The state vocabulary remains a **candidate research model**, not frozen protocol
schema.

### 6. `Branch · VRAMPP-002 - 043b - D2b_3_full.MD`

Value: **MyTrues Discovery branch lead**.

The report itself says it mixes the older decision-memory lineage with a newer
branch extracted from VRAMPP Project Miner work.

Important branch:

`MyTrues Discovery / MyTrues Discovery & Mining Engine`

Problem space:

- inspect project/corpus;
- determine what exists;
- current vs historical;
- authority;
- conflict;
- duplication;
- gaps;
- opportunities;
- candidates;
- evidence.

Important architecture invariant recovered there:

`MCP is adapter, not core.`

This branch is already preserved separately in:

`research/product-branches/MYTRUES-DISCOVERY-HISTORICAL.md`

It MUST remain distinct from the core decision protocol until a future decision
explicitly merges product boundaries.

Commercial tier/pricing/TAM material from this lineage remains research/hypothesis
unless primary PO approval is found.

## B/C — useful corroboration, not priority origin sources

### 7. `Agentes no VSCode Codex_2.MD`

Contains many strong concepts:

- MyTrues as "Minhas Verdades";
- memory of why decisions were made;
- CCP;
- brain/decision-network metaphor;
- dynamic documentation;
- MyTrues as EDT evidence;
- dogfooding;
- No Retroactive Cognition;
- protocol/engine separation.

However, the report explicitly reconstructs across prior material.

Use it as a high-value index, not as sole origin evidence.

### 8. `Branch · OCONSOANTE_ORACLE_FREETIER_CLOUDFLARE.MD`

Strong operational consolidation:

- SQLite;
- provider isolation;
- DecisionMemory;
- v0.2 lifecycle;
- Science Frontier;
- local-first;
- IDEOS as client.

Most of this is already better supported by executable staging and other
archaeology.

### 9. `Branch · Branch · Branch · Branch · OCONSOANTE_ORACLE_FREETIER_CLOUDFLARE.MD`

Useful for product/org/licensing chronology and large-scale consolidation.

Weak as an origin source because it reconstructs prior conversations.

### 10. `0001 - TICA_PHY_001.001.MD`

Useful mainly as corroboration that MyTrues concepts intersected TICA-era work.

No uniquely necessary MyTrues core finding was identified in this pass.

### 11. `Avaliação abordagem FremUX.MD`

Useful corroboration across a different project context.

No uniquely necessary current MyTrues core finding was identified in this pass.

### 12. `#2-PO001-001b- [transit] PO01-001-isol=ccp-mkdoc Branch · FLOWED2-001-LBWARE-POi-001_001 — ChatGPT Operating Architect.MD`

Large consolidation/index.

Useful for navigation.

The sibling `[transit] ... Operating Architecture..` report is stronger for
chat-local CCP evidence.

## Promoted historical findings from this batch

These findings deserve explicit preservation in the project inventory.

### H1. The original architecture had two memory axes

```text
OMGDiary
-> episodic / temporal cognition

MyTrues
-> semantic / decision-oriented state
```

This is historical lineage, not current runtime architecture.

### H2. TrueEngine predates DecisionEngine as an idea

`TrueEngine` was an early proposed inference layer.

It should be preserved as nomenclature/genealogy only.

The current `DecisionEngine` port must not be presented as a mere rename unless
primary historical evidence proves continuity.

### H3. Local decision memory predates the formal protocol

Before "DecisionMemory" terminology, the project already expressed:

`project-local decision + rationale -> consult before generic LLM knowledge`

This is an important precursor of the current canonical-authority boundary.

### H4. CCP is not raw conversation/history

The FlowED CCP POC gives a strong independent invariant:

```text
raw source
!= annotation
!= structured CCP
!= projection
```

This should remain visible in any future EDT/CCP specification.

### H5. Time should probably be multi-dimensional

The recovered time model suggests that one timestamp is insufficient to describe
epistemic history.

Candidate distinctions:

`event / known / considered / decided-promoted / recorded / valid`.

This deserves focused prior-art/science review before schema promotion.

### H6. Chronology is not causality

A chronological graph and causal-cognitive graph must not be conflated.

Causal links require explicit evidence/authority.

### H7. Defeated experience is useful memory

The SQLDAVELHA line suggests preserving not only successful decisions but also
contextually defeated paths because they can reduce future search.

This remains a research hypothesis requiring comparison with CBR, negative
experience replay, algorithm configuration, planning/search memory and agent
memory literature.

### H8. Epistemic answer and linguistic rendering are separate

Candidate invariant:

```text
MyTrues
-> epistemically authorized structured answer

LLM
-> interpretation/rendering
```

A renderer must not silently change epistemic state.

This is compatible with the existing candidate->authority->canonical boundary.

## What this batch does NOT authorize

This batch does not authorize:

- resurrecting TrueEngine as current architecture;
- changing the v0.2 wire protocol;
- making the candidate epistemic-state enum normative;
- adopting the multi-time schema without prior-art work;
- merging MyTrues Discovery into MyTrues core;
- treating MyTools as a proven former product name;
- treating mixed reconstruction files as primary evidence.

## Forensic follow-up policy

No additional chat interrogation is required to preserve the useful material in
this batch.

If future academic/history work requires **exact authorship/origin** rather than
conceptual lineage, the highest-value chats to re-open are:

1. `Diário de Decisões Criativo`;
2. `Escolha Plataforma IA Agentes`;
3. `[transit] ... Operating Architecture..`;
4. the temporal `Branch · Branch · Branch · OCONSOANTE...`;
5. the SQLDAVELHA `...OCONSOANTE..._2`;
6. `Branch · VRAMPP-002 - 043b - D2b_3_full`.

Until that level of attribution is needed, continue ingesting new archaeology
files rather than interrupting the batch.
