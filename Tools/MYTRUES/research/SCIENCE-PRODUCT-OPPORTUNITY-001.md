# MyTrues Science and Product Opportunity Study — 001

Date: 2026-10-01

Status: **PRIOR-ART / FRONTIER MAP — NO NOVELTY CLAIM**

## Research question

Given the target model:

- open decision/memory protocol;
- open ports through a replaceable `DecisionEngine` contract;
- independently developed OSS or proprietary adapters/plugins;
- portable decision-policy/profile concept;
- optional LLM cognition extractors that propose new memories from conversations;
- marketplace/registry of compatible extensions;

what is already solved by science/standards/products, and what residual may remain
scientifically or commercially interesting?

## Executive finding

The individual ingredients are **not novel**.

Science and engineering already contain mature work for:

- decision modeling/execution;
- policy decision points;
- preference representation and learning;
- personalized agents;
- temporal agent memory;
- provenance;
- argumentation;
- algorithm configuration;
- plugin architectures and registries.

No source found in this pass, however, defines the exact full combination:

```text
temporal provider-owned decision memory
+ portable/versioned decision preference profile
+ replaceable decision engine protocol
+ explicit abstention/authority promotion
+ reproducible decision provenance
+ outcome feedback
+ open extension registry
```

This is **not evidence of novelty**. It is a candidate residual requiring a
systematic literature/patent/standards search and experiments.

The strongest scientific opportunity appears to be in the semantics and
evaluation of **portable, reproducible personalized decision behavior across
heterogeneous engines**, not in plugins, graphs, LLMs or marketplaces themselves.

The strongest product opportunity appears to be an **open decision interoperability
platform + conformance-tested extension ecosystem**.

---

# 1. ADOPT — decision models and engines

## OMG DMN

Decision Model and Notation is a mature OMG standard for precise business
decisions/rules, designed to be understandable and executable. DMN provides
machine-readable schemas/meta-models and libraries of reusable decision
components.

Current relevant status observed:

- DMN 1.6 formal — September 2026;
- DMN 1.7 beta — September 2026.

Sources:

- https://www.omg.org/dmn/
- https://www.omg.org/spec/DMN/1.6
- https://www.omg.org/spec/DMN

**MyTrues implication:**

Do not invent a generic decision-table/rule notation.

A DMN adapter/reference engine is an obvious adoption candidate behind
`DecisionEngine`.

Potential MyTrues residual is lifecycle/memory/profile/provenance around engines,
not basic decision-table execution.

## OPA / Rego

Open Policy Agent provides a policy decision engine, REST API, custom built-ins
and runtime plugins.

Sources:

- https://www.openpolicyagent.org/docs/rest-api
- https://www.openpolicyagent.org/docs/extensions

**Implication:**

Policy evaluation and extensible policy engines already exist.

OPA can be an adapter/engine where the decision class maps naturally to policy.

MyTrues should not rebuild Rego or a generic policy evaluator.

## XACML

OASIS XACML already formalizes a Policy Decision Point request/response model for
authorization decisions.

Source:

- https://docs.oasis-open.org/xacml/3.0/xacml-3.0-core-spec-cos01-en.html

**Implication:**

The abstract idea "client asks replaceable decision point and receives structured
decision" is established prior art.

MyTrues needs a different contribution than merely naming a decision-engine port.

## ODRL

W3C ODRL defines interoperable policies with permissions, prohibitions, duties,
constraints, parties, profiles and conflict strategies.

Source:

- https://www.w3.org/TR/odrl-model/

**Implication:**

Some DecisionPolicyProfile semantics — especially hard permissions,
prohibitions, duties and constraints — should be mapped/adopted where applicable
instead of privately reinvented.

ODRL does not by itself express the whole notion of personal multi-criteria
decision preference.

---

# 2. ADOPT — provenance and structured knowledge

## W3C PROV

PROV defines interoperable provenance around Entities, Activities and Agents,
including derivation and responsibility.

Sources:

- https://www.w3.org/TR/prov-o/
- https://www.w3.org/TR/prov-overview/

**Implication:**

Use/provide PROV mappings for DecisionRecord/CCP provenance before inventing a
new generic provenance model.

## OMG PPMN

OMG Pedigree and Provenance Model and Notation 1.0 became formal in September
2026.

Source:

- https://www.omg.org/spec/PPMN/1.0

**Implication:**

PPMN must enter the Science Frontier prior-art inventory before MyTrues claims
novel provenance/pedigree notation.

## SHACL

SHACL validates RDF graphs; the active SHACL 1.2 work also includes inference
rules, profiling and UI-related specifications.

Sources:

- https://www.w3.org/TR/shacl-core/all/
- https://www.w3.org/TR/shacl12-rules/
- https://www.w3.org/TR/shacl-profiling/

**Implication:**

If MyTrues supports RDF/JSON-LD graph representations, SHACL is a strong adoption
candidate for validation/profile conformance instead of building graph
validators from scratch.

---

# 3. ADOPT — preference models and "decision personality"

## MCDA + Preference Learning

A 2024 invited two-part survey by Hüllermeier and Słowiński explicitly frames
MCDA and preference learning as established but complementary fields.

It notes that both build decision models for choosing, sorting or ranking
alternatives and that combinations of MCDA models with machine learning remain
an active area of research.

Sources:

- https://doi.org/10.1007/s10288-023-00560-6
- https://doi.org/10.1007/s10288-023-00561-5

**Implication:**

"My preferences influence my decision" is not new.

A DecisionPolicyProfile must be grounded in existing preference representation,
elicitation and learning literature.

Candidate adopted representations may include:

- value/utility models;
- outranking relations;
- decision rules;
- conditional preference formalisms such as CP-nets;
- learned preference models.

## PPX — Preference Profile Exchange

A major prior-art correction was found after the initial pass.

PPX 0.1.0-draft (2026-04-23) defines a portable, user-owned preference/context
profile exchange format and interaction model across applications and agents.

It already provides:

- preference/aversion/tendency/constraint claims;
- provenance kinds including user-stated, observed, imported, inferred and
  derived aggregate;
- confidence and stability;
- context modifiers;
- evidence references;
- lifecycle/expiry/decay metadata;
- explicit review states;
- first-class consent grants;
- domain extensions;
- derived views;
- JSON Schema;
- bindings for MCP, A2A, AG-UI, A2UI and HTTP;
- conformance levels.

PPX is explicitly a draft, pre-standardization and pre-stable. It is strong
prior art, not yet a mature international standard.

Sources:

- https://ppx.dev/spec/
- https://ppx.dev/
- https://ppx.dev/bindings/

Historical profile prior art also includes W3C CC/PP, an RDF framework for
describing capabilities and user preferences.

Sources:

- https://www.w3.org/TR/CCPP-struct-vocab/
- https://www.w3.org/TR/CCPP-vocab/

**MyTrues implication:**

Do not invent `DecisionPolicyProfile` as a new portable preference-profile
format.

First attempt to adopt:

`PPX Profile -> DecisionProfile adapter -> engine-specific semantic mapping`

and define a MyTrues/decision extension only if a real residual is demonstrated.

The candidate scientific question is no longer profile portability itself. It is
whether decision semantics can be preserved/replayed when one portable profile
is interpreted by heterogeneous decision engines.

## Personalized reasoning — PrefDisco

ICLR 2026 introduces PrefDisco for proactive personalized reasoning: the system
must identify unknown user preferences, elicit them, then adapt its reasoning.

Source:

- https://proceedings.iclr.cc/paper_files/paper/2026/hash/82d50077a0e140b524a18f380c95d55a-Abstract-Conference.html

**Implication:**

Preference elicitation and preference-dependent reasoning are current scientific
frontiers already being benchmarked.

MyTrues must compare against this line of work.

## PersonaAgent / preference-aware memory

ACL 2026 includes:

- PersonaAgent: personalized episodic + semantic memory controlling action;
- Preference-Aware Memory Update: dynamically refining preference memory;
- Me-Agent: hierarchical preference memory and personalized action;
- temporal semantic memory for evolving personalized agents.

Sources:

- https://aclanthology.org/2026.findings-acl.1315/
- https://aclanthology.org/2026.findings-acl.38/
- https://aclanthology.org/2026.findings-acl.1211/
- https://aclanthology.org/2026.findings-acl.1496/

**Implication:**

"agent learns user preferences over time" is not novel.

Potential residual must involve stronger interoperability/reproducibility or a
different experimentally supported property.

---

# 4. ADOPT — memory and temporal knowledge

## Graphiti

Graphiti is an OSS temporal context-graph framework for agents.

Its current model supports:

- evolving facts;
- temporal validity;
- episodes/provenance;
- hybrid semantic/keyword/graph retrieval;
- prescribed/learned ontology;
- an MCP adapter.

Sources:

- https://github.com/getzep/graphiti
- https://github.com/getzep/graphiti/blob/main/mcp_server/README.md

**Implication:**

Temporal graphs, superseded facts, provenance-to-episode and LLM-assisted memory
extraction already exist.

Graphiti is a candidate adapter/upstream, not a reason to build a MyTrues graph
database.

MyTrues' separate authority/promotion semantics may still differ and should be
experimentally compared rather than assumed superior.

## Agent-memory science

A 2026 survey describes a progression from Storage to Reflection to Experience
in agent memory and treats experience abstraction/continual learning as current
frontier work.

Source:

- arXiv:2605.06716 — From Storage to Experience: A Survey on the Evolution of
  LLM Agent Memory Mechanisms.

**Implication:**

"turn conversation history into reusable experience" is an active research
field. MyTrues cognition extractors must be compared against agent-memory
baselines.

---

# 5. ADOPT — plugin / extension architecture

## MCP

MCP 2026-07-28 has a stateless core, extension framework and an official
community registry. Servers expose tools/resources/prompts and the ecosystem
already supports independent publication/discovery.

Sources:

- https://blog.modelcontextprotocol.io/posts/2026-07-28/
- https://registry.modelcontextprotocol.io/
- https://registry.modelcontextprotocol.io/docs

**Implication:**

MCP should be an adapter/transport ecosystem, not MyTrues' internal architecture.

MyTrues can expose an MCP adapter and can consume MCP adapters, but should not
invent another general agent-tool protocol.

## OpenTelemetry Collector

OpenTelemetry demonstrates a mature component taxonomy:

- receivers;
- processors;
- exporters;
- connectors;
- extensions;

and explicitly supports custom/community components.

Sources:

- https://opentelemetry.io/docs/collector/components/
- https://opentelemetry.io/docs/collector/extend/

**Implication:**

This is strong architectural prior art for a typed MyTrues plugin taxonomy.

## Kubernetes

Kubernetes dynamically extends its API through Custom Resources and custom
controllers/operators.

Source:

- https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/

**Implication:**

Extensibility, registration, schemas, discovery and versioned extension APIs are
mature engineering patterns.

A MyTrues plugin manifest/registry is product engineering, not research novelty.

---

# 6. ADOPT — MyTrues-applied-to-MyTrues experiment selection

The SQLDAVELHA metaobjective proposes accumulating:

`configuration -> observed consequence`

and using this experience to avoid repeating defeated architecture experiments.

This idea overlaps strongly with:

- automated algorithm configuration;
- hyperparameter optimization;
- AutoML;
- Bayesian optimization;
- meta-learning.

Sources:

- https://doi.org/10.1007/s10462-025-11397-2
- https://www.automl.org/hpo-overview/hpo-tools/smac/
- DOI 10.1613/jair.1.13676 — Survey of Automated Algorithm Configuration.

**Implication:**

Do not claim novelty for experiment/configuration selection itself.

If Microbrain is later authorized, compare at least:

- random search;
- grid/factorial designs where feasible;
- SMAC/algorithm configuration;
- Bayesian optimization;
- simple accumulated best-observed lookup.

Potential research contribution would need to arise from the peculiar structure
of MyTrues' decision/memory problem, not from rediscovering AutoML.

---

# 7. Candidate scientific residual

## S1 — Cross-engine semantic preservation of portable preference profiles

Question:

> Can a portable profile such as PPX be mapped into heterogeneous decision
> engines while preserving measurable decision semantics and making information
> loss/divergence explicit?

Portable preference exchange itself is prior art. The residual is semantic
execution/interoperability across unlike decision models, not inventing a new
profile container.

Potential experiment:

- one profile;
- several engines: rule/DMN, MCDA, CBR, learned/LLM-assisted;
- common decision corpus;
- compare consistency with declared preferences;
- measure where engines cannot preserve semantics;
- retain engine/profile/version/evidence provenance.

**Status:** promising research question, NOT novelty claim.

## S2 — Reproducible personalized decisions

Candidate identity:

```text
Decision =
  f(
    context snapshot,
    evidence snapshot,
    memory snapshot/ref,
    DecisionPolicyProfile@version,
    DecisionEngine@version
  )
```

Question:

> How much of a personalized decision can be replayed, audited and
> counterfactually re-evaluated when these components are explicit?

Potential metrics:

- exact/semantic replay rate;
- explanation/provenance completeness;
- historical-state query accuracy;
- decision drift;
- cross-engine portability;
- user/provider preference adherence.

Existing personalized-agent work must be the baseline.

## S3 — Preference evolution without retroactive cognition

Question:

> Does explicit profile versioning + temporal decision history outperform
> overwrite-style preference memory for longitudinal audit and re-decision?

Compare:

- mutable "current user profile" memory;
- append-only/versioned profile;
- temporal event/preference memory;
- MyTrues-style profile + DecisionRecord + CCP/provenance.

This connects the project's No Retroactive Cognition rule to a testable
scientific question.

## S4 — Candidate cognition extraction with canonical-authority gate

A lightweight LLM conversation adapter is product-feasible and scientifically
testable.

Question:

> Can a cognition extractor achieve useful recall while keeping false canonical
> promotion near zero through explicit candidate/authority separation?

Candidate tasks:

- detect decision moments;
- extract issue/options/criteria/evidence;
- link to existing DecisionRecords;
- propose profile updates;
- identify supersession/reconsideration.

Metrics:

- candidate precision/recall;
- human acceptance rate;
- false-canonicalization rate;
- provenance correctness;
- temporal attribution correctness;
- missed-decision rate.

This must compare to current agent-memory extraction systems.

## S5 — Decision-memory reuse versus repeated probabilistic deliberation

Question:

> For previously resolved contexts, when does structured decision-memory reuse
> improve consistency/cost/latency without harming correctness or context
> sensitivity compared with fresh probabilistic reasoning?

This is the scientifically defensible form of the SQLDAVELHA intuition.

Need distinct classes:

- exact-known;
- similar-but-context-changed;
- superseded;
- unknown;
- conflicting-provider policy.

Metrics may include:

- correctness/utility;
- preference adherence;
- unnecessary re-deliberation;
- false reuse;
- appropriate abstention;
- latency/cost;
- historical explainability.

## S6 — Explicit authority/promotion semantics for agent memory

Many memory systems extract and update facts/preferences.

Candidate question:

> Does separating CandidateCognition from CanonicalDecision and requiring an
> explicit authority policy reduce memory contamination while preserving useful
> learning?

This may be scientifically useful, especially in longitudinal personalized-agent
settings, but needs a literature review on memory governance before any novelty
claim.

---

# 8. What is probably NOT a scientific opportunity

Do not frame the following alone as research novelty:

- hexagonal ports/adapters;
- plugin architecture;
- marketplace/registry;
- MCP adapter;
- graph memory;
- vector retrieval;
- temporal facts;
- provenance;
- decision tables;
- policy engines;
- preference learning;
- personas;
- human approval;
- algorithm configuration;
- multiple decision algorithms;
- open-source extension ecosystem.

They are engineering composition/product strategy unless a new formal or
empirically demonstrated property is introduced.

---

# 9. Product opportunity

## P1 — Open Decision Interoperability Layer

A stable open protocol + SDK + conformance suite through `DecisionEngine`.

Value:

- consumers do not couple to one algorithm;
- providers can swap engines;
- OSS/community engines coexist with private engines;
- decision records remain inspectable across implementations.

This resembles the value MCP created for tool/context integration, but in the
narrower decision domain.

## P2 — PPX-backed Decision Profile interoperability

A portable, versioned profile remains a valuable product surface, but MyTrues
should first adopt/interoperate with PPX rather than define a competing profile
format.

Possible decision-oriented claims include:

- "prefer LTS in production";
- risk tolerance;
- evidence thresholds;
- reversibility preference;
- cost/performance trade-offs;
- abstention/escalation policy.

Product differentiation requires:

- user ownership/export;
- explicit profile versions;
- transparent updates;
- provider isolation;
- adapter/engine portability.

Do not market this as scientifically new until S1/S3 are tested.

## P3 — Cognition Harvester plugins

Examples:

- conversation -> candidate decisions/CCP keyframes;
- meetings -> decisions/actions/evidence;
- GitHub issues/PRs -> decision candidates;
- Slack/email/docs -> cognition candidates.

A small/local LLM implementation is particularly useful where privacy matters.

The canonical-promotion gate becomes a product safety feature.

## P4 — Engine ecosystem

Community/commercial engines behind the same port:

- DMN;
- OPA;
- MCDA;
- CBR;
- preference engines;
- domain-specific engines;
- LLM/hybrid engines;
- human/team engines.

A provider can publish an engine without forking MyTrues.

## P5 — Conformance-aware registry / marketplace

The product opportunity is not merely "an app store".

A useful MyTrues registry can expose:

- implemented ports;
- protocol compatibility;
- license;
- data permissions;
- local/cloud behavior;
- external model calls;
- conformance evidence;
- benchmark evidence;
- deterministic/probabilistic classification;
- signature/provenance;
- known incompatibilities.

Possible commercial layers later:

- verified publisher;
- hosted adapters;
- paid plugins;
- organization/private registry;
- compliance/security review;
- enterprise support.

## P6 — Audit/replay tooling

Because records can contain:

- engine version;
- profile version;
- evidence snapshot/ref;
- context;
- provenance;
- outcome;

a strong product can answer:

- why did we decide this?
- what engine/profile produced it?
- what was true then?
- what changed?
- would the current profile decide differently?
- can we replay the decision?
- which plugin contributed each artifact?

This is more distinctive than a generic memory store.

---

# 10. Recommended architecture north

```text
                         CLIENTS
          CLI / SDK / HTTP / MCP / UI / Agents
                           │
                    inbound adapters
                           │
                           ▼
┌───────────────────────────────────────────────────────────────┐
│                    MYTRUES OPEN CORE                          │
│                                                               │
│ Decision lifecycle / identity / authority / provenance       │
│                                                               │
│  ┌──────────┐  ┌─────────────┐  ┌──────────────────────┐     │
│  │ Memory   │  │ Profile     │  │ DecisionEngine       │     │
│  │ Port     │  │ Port        │  │ Port                 │     │
│  └────┬─────┘  └──────┬──────┘  └──────────┬───────────┘     │
│       │               │                     │                 │
│ Evidence / Provenance / Cognition / Retrieval / Authority    │
│ Outcome / View / Source ports                                │
└───────┼───────────────┼─────────────────────┼─────────────────┘
        │               │                     │
     adapters        adapters              engines
        │               │                     │
   SQLite/RDF       profile store     DMN / OPA / MCDA / CBR
   Graphiti/etc     elicitation       custom OSS / commercial
        │
   cognition adapters
        │
 conversation LLM / Git / docs / meeting / MCP
```

The protocol reaches the `DecisionEngine` port.

It does not dictate the engine.

## Product packaging

```text
MyTrues Protocol
MyTrues Reference
MyTrues Conformance
MyTrues SDK

MyTrues Registry
   ├── Engines
   ├── Profiles
   ├── Cognition Extractors
   ├── Memory/Storage
   ├── Retrieval
   ├── Evidence/Provenance
   ├── Authority/Governance
   ├── Views/Exports
   └── Integrations
```

"Marketplace" may be a later commercial UX over the Registry.

Start with registry + manifest + conformance rather than payment infrastructure.

---

# 11. Next Science Frontier Gate

Before inventing a MyTrues Decision Engine, the next focused discovery should
not ask "what decision algorithm can we invent?"

Ask:

> **Is there already a standard/protocol for a portable, versioned decision
> preference profile that can be applied across heterogeneous decision engines,
> while preserving temporal provenance, abstention and replay?**

and:

> **Has anyone standardized an interoperable lifecycle connecting personalized
> decision memory -> engine invocation -> evidence/provenance -> outcome ->
> profile/decision revision?**

If prior art already closes those gaps, adopt it.

If not, formalize only the smallest residual and test S1–S6.

---

# 12. Source register — first focused pass

Standards / official engineering:

- OMG DMN — https://www.omg.org/dmn/
- OMG DMN 1.6 — https://www.omg.org/spec/DMN/1.6
- W3C PROV-O — https://www.w3.org/TR/prov-o/
- OMG PPMN 1.0 — https://www.omg.org/spec/PPMN/1.0
- W3C ODRL — https://www.w3.org/TR/odrl-model/
- OASIS XACML 3.0 —
  https://docs.oasis-open.org/xacml/3.0/xacml-3.0-core-spec-cos01-en.html
- OPA REST/Extensions — https://www.openpolicyagent.org/docs/
- MCP 2026-07-28 —
  https://blog.modelcontextprotocol.io/posts/2026-07-28/
- Official MCP Registry — https://registry.modelcontextprotocol.io/
- OpenTelemetry Collector components —
  https://opentelemetry.io/docs/collector/components/
- Kubernetes API extensions —
  https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/
- JSON Schema 2020-12 — https://json-schema.org/draft/2020-12
- SHACL 1.2 Core — https://www.w3.org/TR/shacl-core/all/

Scientific / peer-reviewed:

- Hüllermeier & Słowiński 2024, Preference Learning + MCDA I:
  DOI 10.1007/s10288-023-00560-6
- Hüllermeier & Słowiński 2024, Preference Learning + MCDA II:
  DOI 10.1007/s10288-023-00561-5
- PrefDisco, ICLR 2026:
  https://proceedings.iclr.cc/paper_files/paper/2026/hash/82d50077a0e140b524a18f380c95d55a-Abstract-Conference.html
- PersonaAgent, ACL Findings 2026:
  DOI 10.18653/v1/2026.findings-acl.1315
- Preference-Aware Memory Update, ACL Findings 2026:
  DOI 10.18653/v1/2026.findings-acl.38
- Me-Agent, ACL Findings 2026:
  DOI 10.18653/v1/2026.findings-acl.1211
- Automated Algorithm Configuration survey:
  DOI 10.1613/jair.1.13676
- AutoML literature review:
  DOI 10.1007/s10462-025-11397-2

Engineering prior art:

- Graphiti — https://github.com/getzep/graphiti
- SMAC3 — https://www.automl.org/hpo-overview/hpo-tools/smac/

## Current conclusion

**GO for continued prior-art/design work.**

**DONT_GO for any scientific novelty claim yet.**

**DONT_GO for inventing a proprietary engine yet.**

**GO for defining the open extension/port taxonomy and conformance model**, because
that is useful product architecture even if it produces no novel science.


### Revised residual after PPX

PPX materially narrows the candidate frontier.

The working decomposition is now:

```text
PPX / profile prior art
  -> portable preferences, context, consent, provenance

MyTrues candidate residual
  -> decision lifecycle
  -> decision-memory history
  -> engine invocation
  -> semantic mapping from profile to engine
  -> abstention / authority
  -> evidence + outcome
  -> replay / re-decision
```

The key research problem is therefore not:

`how do we serialize a person's preferences?`

It is closer to:

`how do we preserve, measure and audit decision behavior when the same portable
preference evidence is interpreted by heterogeneous decision engines over time?`

This remains a research question, not a novelty claim.


## Interoperability research correction

A further literature pass confirms that semantic/profile interoperability itself
is also longstanding research.

Relevant examples include:

- W3C CC/PP for extensible user preference/capability profiles;
- research on sharing/reusing heterogeneous user models through semantic
  alignment;
- federated interoperability frameworks for heterogeneous Systems of Systems,
  emphasizing autonomy, semantic mediation, composable/interchangeable
  components and open evolution.

Therefore none of the following is an adequate standalone novelty claim:

- a portable profile;
- profile exchange across applications;
- semantic mediation between heterogeneous systems;
- a federated plugin architecture;
- independently replaceable interoperability components.

The candidate scientific residual must remain specifically tied to **decision
behavior**:

```text
same portable preference evidence
+ same decision context/evidence snapshot
+ different DecisionEngine families
        ↓
measure:
  semantic coverage
  mapping loss
  behavioral preservation/divergence
  constraint violations
  abstention behavior
  replayability
  provenance completeness
```

Even this is only a research question until a systematic review demonstrates
that it is not already adequately addressed.
