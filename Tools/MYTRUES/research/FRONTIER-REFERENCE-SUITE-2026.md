# MyTrues / CCP / EDT — Frontier Reference & Benchmark Suite (2026-10)

Status: **CURRENT RESEARCH REFERENCE SUITE — NOT A NOVELTY CLAIM**

Purpose:

define the external frontier against which MyTrues technical claims and
CCP/EDT operationalization experiments should be compared.

This file intentionally separates:

- **EDT/CCP conceptual research**;
- **MyTrues technical/product research**;
- **reference benchmarks**;
- **frontier systems/mechanisms**;
- **human-governance/provenance work**.

"Top-tier/A1-style" here means internationally strong reference venues/labs
(ICML, ICLR, ACL, Microsoft Research, Google Research/DeepMind, etc.). It does
not assert a specific Brazilian Qualis classification without a separate venue
check.

---

## A. MUST-RUN memory / cognition benchmarks

### A1. LongMemEval-V2 (2026)

Use for:

- long-term agent memory;
- multimodal/web-agent trajectory histories;
- compact evidence retrieval;
- latency + answer accuracy;
- experience accumulation.

Official repo:

https://github.com/xiaowu0162/LongMemEval-V2

Why relevant:

closer to "experienced colleague" behavior than static conversational recall.

### A2. MemoryArena — ICML 2026

Use for:

- multi-session agentic tasks;
- memory affecting future decisions/actions;
- preference-constrained planning;
- progressive information search;
- sequential reasoning;
- experience distilled from earlier actions/feedback.

Reference:

https://proceedings.mlr.press/v306/he26am.html

This is one of the strongest baselines for testing whether MyTrues memory
actually improves future action, not just recall.

### A3. AMemGym — ICLR 2026

Use for:

- interactive/on-policy memory;
- evolving user profiles/states;
- personalization;
- state-dependent questions;
- memory-management selection.

Reference:

https://proceedings.iclr.cc/paper_files/paper/2026/hash/0856bc553d3e3b9827e5140d0ad3bf8d-Abstract-Conference.html

### A4. LoCoMo-Plus — ACL 2026

Use for:

- "cognitive memory" beyond factual recall;
- latent goals/values/constraints;
- cue-trigger semantic disconnect;
- constraint consistency.

Reference:

https://aclanthology.org/2026.acl-long.1150/

Especially relevant to future DecisionProfile / preference-aware MyTrues work.

### A5. GroupMemBench — Microsoft Research 2026

Use for:

- multi-party/group memory;
- speaker-grounded belief tracking;
- user-specific knowledge;
- temporal reasoning;
- ambiguity;
- abstention.

Reference:

https://www.microsoft.com/en-us/research/publication/groupmembench-benchmarking-llm-agent-memory-in-multi-party-conversations/

Especially relevant to provider/person/authority separation.

### A6. RHELM — Microsoft / EMNLP Findings 2026

Use for:

- realistic evolving long-term memory;
- heterogeneous sources:
  - dialogue;
  - email;
  - files;
- temporal event trajectories;
- multi-source aggregation.

Reference:

https://microsoft.github.io/RHELM/

Highly relevant to MyTrues Source adapters and future cross-source cognition
harvesting.

### A7. MemGym — 2026

Use for:

- long-horizon memory pressure;
- multi-hop dependency;
- memory compression/reward models.

Reference:

https://wujiangxu.github.io/memgym-site/

---

## B. Frontier systems / mechanisms to reproduce or compare

### B1. Memora — Microsoft Research / ICML 2026

Key idea:

separate rich stored memory from lightweight retrieval abstractions/cue anchors,
balancing specificity and abstraction.

Reference:

https://www.microsoft.com/en-us/research/blog/memora-a-harmonic-memory-representation-balancing-abstraction-and-specificity/

MyTrues relevance:

- CCP cognitive keyframes;
- projection versus source;
- compression without losing decisive detail.

### B2. Human-Inspired Memory Architecture — Microsoft Research 2026

Mechanisms:

- consolidation;
- interference-based forgetting;
- maturation;
- reconsolidation;
- entity knowledge graphs;
- hybrid retrieval.

Reference:

https://www.microsoft.com/en-us/research/publication/human-inspired-memory-architecture-for-llm-agents/

MyTrues relevance:

baseline for any claim involving consolidation/forgetting/reconsolidation.

### B3. MAGE — Microsoft Research 2026

Key idea:

memory as execution-state management, preserving active trajectories and
revisable branches rather than only semantic similarity.

Reference:

https://www.microsoft.com/en-us/research/publication/beyond-semantic-organization-memory-as-execution-state-management-for-long-horizon-agents/

MyTrues relevance:

- decision/cognitive path;
- branch/revision;
- state reconstruction;
- avoiding contamination by failed traces.

### B4. ReasoningBank — Google Research 2026

Key idea:

distill generalizable reasoning strategies from **successful and failed
experiences**.

Reference:

https://research.google/blog/reasoningbank-enabling-agents-to-learn-from-experience/

MyTrues relevance:

direct prior art for:

- defeated-path value;
- SQLDAVELHA;
- experience reuse;
- avoiding repeated strategic errors.

This MUST be a baseline before claiming novelty around failed-path memory.

### B5. MARS — Google Research 2026

Key idea:

- budget-aware planning;
- modular research;
- comparative reflective memory;
- cross-branch transfer of lessons.

Reference:

https://research.google/pubs/mars-modular-agent-with-reflective-search-for-automated-ai-research/

MyTrues relevance:

- research-agent learning;
- branch comparison;
- experiment-memory reuse;
- Microbrain/meta-experiment design.

### B6. Scaling agent systems — Google Research 2026

Controlled study:

180 agent configurations; quantitative principles for when multi-agent
architectures help/hurt.

Reference:

https://research.google/blog/towards-a-science-of-scaling-agent-systems-when-and-why-agent-systems-work/

MyTrues relevance:

strong methodological baseline for:

`test architectures/configurations instead of choosing by plausibility`.

### B7. Titans + MIRAS — Google Research 2025

Reference:

https://research.google/blog/titans-miras-helping-ai-have-long-term-memory/

Use only as model-memory prior art.

Do not confuse model-internal memory with MyTrues' external protocol/memory
semantics.

---

## C. CCP / Design Rationale / provenance reference line

### C1. W3C PROV

Use for provenance mapping before inventing a private provenance ontology.

https://www.w3.org/TR/prov-overview/

### C2. ADR / MADR

Use as derived decision views, not as the whole CCP.

### C3. IBIS / QOC

Use as classical design-rationale baselines for issue/options/criteria/argument
structure.

### C4. LLM-generated design rationale — 2025

"Using LLMs in Generating Design Rationale for Software Architecture Decisions"

Reference:

https://arxiv.org/abs/2504.20781

Reported results show that generated design-rationale recall can be useful while
precision remains limited.

MyTrues/CCP relevance:

supports the need for:

`LLM candidate extraction -> validation/authority -> canonical retention`

instead of direct auto-canonization.

### C5. Architectural decision extraction from commits — 2026

"Can LLMs Extract Architectural Design Decisions from Source Code Commits?"

Reference:

https://arxiv.org/abs/2609.03721

MyTrues/CCP relevance:

candidate baseline for cognition harvesters over Git/commit sources.

---

## D. Human authority / bounded delegation / provenance

### D1. To Copilot and Beyond — Microsoft Research 2026

Large developer study identifies demand for AI systems with explicit authority
scoping, provenance, uncertainty signaling and least privilege.

Reference:

https://www.microsoft.com/en-us/research/publication/to-copilot-and-beyond-22-ai-systems-developers-want-built/

MyTrues relevance:

supports experimentation around explicit Authority ports and candidate/canonical
boundaries.

### D2. You Shall Not Pass! — Microsoft Research 2026

Mixed-methods study of 448 professional developers on acceptable AI autonomy.

Reference:

https://www.microsoft.com/en-us/research/publication/you-shall-not-pass-where-and-why-developers-draw-the-line-on-ai-autonomy/

MyTrues relevance:

human authority is task/context dependent.

Do not assume one global autonomy policy.

### D3. Project Provenance — Microsoft Research

Reference:

https://www.microsoft.com/en-us/research/project/project-provenance/

Relevant as human-centered provenance prior art.

### D4. Google / DeepMind validation bottleneck — 2026

"Conjecture Machines: AI agents and the new validation bottleneck in science"

Reference:

https://deepmind.google/public-policy/conjecture-machines-ai-agents-and-the-new-validation-bottleneck-in-science/

MyTrues/EDT research relevance:

AI-generated hypotheses increase the need for explicit validation/provenance
rather than reducing it.

---

## E. Product-facing personalization / preference references

### E1. PersonaAgent — ACL Findings 2026

Personalized agent architecture with episodic + semantic memory linked to action.

Reference:

https://aclanthology.org/2026.findings-acl.1315/

### E2. PPX — Preference Profile Exchange

Direct prior art for portable user preference/context profiles.

Use PPX before inventing a MyTrues preference-profile format.

https://ppx.dev/spec/

---

# Reference test matrix

## Tier 0 — protocol/conformance (mandatory on every MyTrues release)

Existing MyTrues tests:

- known decision;
- unknown -> 202/pending;
- sanitize;
- resolve;
- retain;
- resume;
- provider isolation;
- restart persistence;
- no cross-provider leakage.

These test **protocol correctness**, not memory intelligence.

## Tier 1 — baseline memory competence

Run:

- LongMemEval / LongMemEval-V2;
- LoCoMo / LoCoMo-Plus;
- RHELM.

Questions:

- recall;
- temporal consistency;
- evidence retrieval;
- evolving facts/preferences;
- heterogeneous sources.

## Tier 2 — memory changes future action

Run:

- MemoryArena;
- AMemGym;
- MemGym.

Questions:

- does retained experience improve future action?
- false reuse?
- context mismatch?
- appropriate abstention?
- memory cost/latency?

## Tier 3 — MyTrues-specific epistemic behavior

Create qualified benchmark extensions for:

- AS-KNOWN-THEN;
- known vs considered;
- current vs historical position;
- source -> candidate -> canonical;
- supersession without retroactive cognition;
- provider/authority isolation;
- provenance completeness;
- defeated-path reuse;
- explicit UNKNOWN;
- conflicting authority/provider state;
- decision replay under profile/engine versions.

Do not call these benchmark dimensions novel until compared against existing
benchmarks.

## Tier 4 — CCP/EDT instrument tests

Measure whether preserving CCP material changes human/project outcomes.

Candidate tests:

1. decision reconstruction:
   - raw final artifact only;
   - artifact + ADR;
   - artifact + CCP projection/source links.

2. rationale recovery:
   - time to answer "why?";
   - correctness;
   - source-grounding;
   - confidence calibration.

3. rejected-path value:
   - repeated investigation rate;
   - time lost revisiting defeated alternatives;
   - false suppression when context changed.

4. change/review:
   - ability to identify what evidence/assumption invalidated the old decision;
   - ability to distinguish historical from current position.

5. onboarding/learning:
   - comprehension transfer;
   - ability to adapt rather than merely reproduce;
   - retention after delay.

These belong to EDT/CCP research, not ordinary MyTrues conformance.

---

# Highest-value current writing opportunities

## W1 — EDT / CCP conceptual thesis paper

Core:

`SOURCE -> CCP -> PROJECTION`

Questions:

- consolidation loss;
- cognitive keyframes;
- rejected-path value;
- provenance vs rationale;
- epistemic primacy without display primacy.

Primary repo:

`edt` + public operational concepts in `ccp`.

## W2 — Grounded CCP operationalization

Focus:

`raw source != extracted != inferred != confirmed != evidenced != projection`.

Compare with:

- W3C PROV;
- design rationale;
- ADR;
- LLM design-rationale extraction.

Primary repo:

`ccp` + experiments in `research`.

## W3 — MyTrues open decision-memory protocol

Focus:

- provider-scoped memory;
- explicit pending/resolution;
- sanitization;
- retain/resume;
- open DecisionEngine boundary;
- conformance.

Primary repo:

`mytrues`.

## W4 — Cognition harvester with authority gate

Focus:

LLM/source extraction produces candidates, never canonical truth automatically.

Compare against:

- design-rationale generation/extraction;
- memory ingestion systems;
- source-grounding methods.

Primary repo:

`research`, plugin may later live under `mytrues` or external repo.

## W5 — Defeated-path memory / SQLDAVELHA

Focus:

when should known failed experiences reduce future deliberation?

Mandatory comparison:

- ReasoningBank;
- CBR;
- MemoryArena;
- MARS;
- algorithm configuration/search memory.

Primary repo:

`research`.

## W6 — Historical decision replay / No Retroactive Cognition

Focus:

- event time;
- known time;
- considered time;
- decision/promoted time;
- recorded time;
- valid time;
- historical replay.

Compare with:

- bitemporal databases;
- temporal KG;
- provenance;
- belief revision;
- RHELM/LongMemEval-V2 temporal tests.

Primary repo:

`research` + protocol candidates in `mytrues`.

## W7 — Portable preference semantics across decision engines

Focus:

PPX/profile -> multiple DecisionEngine families.

Metrics:

- semantic coverage;
- mapping loss;
- preference/constraint adherence;
- explainable divergence.

Primary repo:

`research`.

---

# Research admission rule

A paper opportunity enters active experimental work only when:

1. prior-art map is current;
2. strongest available open baselines are runnable;
3. benchmark/task is frozen;
4. metrics are defined before seeing results;
5. negative results are retained;
6. any claimed residual survives direct comparison.

Use Microsoft/Google/frontier systems as baselines, not branding.

The goal is not to "beat Microsoft/Google" as a slogan.

The goal is to expose the smallest reproducible residual that current systems do
not already solve.
