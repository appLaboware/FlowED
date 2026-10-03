# MyTrues Capability / Prior-Art Inventory

Date: 2026-10-01

Status: **living design inventory — ADOPT FIRST**

Legend:

- **ADOPT** — established standard/project/method should be used or adapted first;
- **COMPOSE** — combine existing pieces; no novelty claim;
- **RESEARCH** — candidate scientific question requiring experiments;
- **PRODUCT** — useful product surface without scientific novelty;
- **OPEN** — open interoperability surface;
- **PRIVATE-OK** — implementation/data may be private behind an open port.

| Capability | MyTrues role | Prior art / upstream family | Current stance |
|---|---|---|---|
| Decision request/response | protocol | XACML PDP model; DMN services; OPA API | **ADOPT/COMPOSE** |
| Decision model/rules | engine adapter | OMG DMN, decision tables, rule engines | **ADOPT** |
| Policy evaluation | engine adapter | OPA/Rego, XACML, ODRL | **ADOPT** |
| Multi-criteria decision | engine adapter | MCDA/MCDM | **ADOPT** |
| Preference learning | profile/engine adapter | PL/MCPL literature | **ADOPT/RESEARCH** |
| Conditional preferences | profile/engine adapter | CP-nets and related formalisms | **ADOPT** |
| Personalized reasoning | profile/engine benchmark | PrefDisco and personalized-agent research | **ADOPT baseline** |
| Case reuse | engine/retrieval adapter | Case-Based Reasoning | **ADOPT** |
| Argumentation | engine/evidence adapter | Dung/structured argumentation/AIF | **ADOPT** |
| Belief revision | engine adapter | AGM/TMS/ATMS | **ADOPT** |
| Provenance | provenance port | W3C PROV; OMG PPMN | **ADOPT** |
| RDF graph validation | validator adapter | SHACL | **ADOPT when RDF** |
| JSON validation | protocol/schema | JSON Schema | **ADOPT** |
| Temporal context graph | memory adapter | Graphiti/Zep family | **ADOPT/COMPARE** |
| SQLite decision memory | reference adapter | SQLite | **CURRENT REFERENCE** |
| Vector retrieval | retrieval adapter | established vector search | **ADOPT optional** |
| Graph retrieval | retrieval adapter | KG/graph traversal | **ADOPT optional** |
| Hybrid retrieval | retrieval adapter | agent memory / IR systems | **ADOPT optional** |
| Cognition extraction from conversation | CognitionProposal port | agent-memory extraction + LLM IE | **PRODUCT + RESEARCH S4** |
| Decision policy/profile | DecisionProfile port | PPX + MCDA/PL + personalized agents + ODRL constraints | **ADOPT/RESEARCH S1/S3** |
| Portable preference/profile exchange | profile/interchange | PPX 0.1 draft; historical W3C CC/PP | **ADOPT/COMPARE** |
| Replayable personalized decision | protocol/audit | provenance + decision models exist separately | **RESEARCH S2** |
| No Retroactive Cognition | temporal profile/CCP semantics | temporal memory/provenance partly overlap | **RESEARCH S3** |
| Candidate vs canonical memory | authority port | HITL/governance patterns; memory systems vary | **RESEARCH S6 / PRODUCT** |
| Abstain / ask / escalate | engine lifecycle | selective prediction/HITL/policy patterns | **ADOPT + protocol semantics** |
| Outcome feedback | outcome port | learning/CBR/decision analysis | **ADOPT/COMPOSE** |
| MyTrues experiment selection | research tooling | AutoML, AC, SMAC, Bayesian optimization | **ADOPT; no novelty** |
| MCP integration | inbound/outbound adapter | MCP 2026-07-28 | **ADOPT** |
| Plugin manifest | ecosystem | MCP Registry, OTel components, K8s extension patterns | **PRODUCT/COMPOSE** |
| Registry/marketplace | distribution | MCP Registry and software marketplaces | **PRODUCT** |
| Conformance suite | protocol | standards ecosystems + MCP/SHACL practices | **OPEN PRODUCT FOUNDATION** |
| ADR/MADR view | export/view | ADR/MADR | **ADOPT** |
| NORM/WHY/TRACE views | view contracts | derived-doc pattern; PROV/ADR pieces | **COMPOSE/RESEARCH UX** |
| Commercial decision engine | DecisionEngine adapter | proprietary implementations behind open protocols | **PRIVATE-OK** |
| Commercial plugin | any port adapter | normal extension-market pattern | **PRIVATE-OK** |
| Provider memory/data | instance data | privacy/security concern | **PRIVATE-OK** |
| Protocol / ports / manifests | interoperability | standards pattern | **OPEN** |

## Current open-port universe

Target candidate ports:

- `DecisionEngine`;
- `DecisionMemory`;
- `DecisionProfile`;
- `Evidence`;
- `Provenance`;
- `Authority`;
- `CognitionProposal`;
- `Retrieval`;
- `Outcome`;
- `View`;
- `Source`.

This list is a design inventory, not a frozen normative API.

## Adapter examples

### Driving / inbound

- HTTP/OpenAPI;
- MCP server;
- CLI;
- language SDK;
- batch/file;
- events;
- UI.

### Driven / outbound

- DMN;
- OPA/Rego;
- MCDA;
- CBR;
- preference engine;
- custom engine;
- SQLite;
- Graphiti;
- RDF/SHACL;
- vector/graph retrieval;
- PROV;
- human approval workflow;
- LLM cognition extractor;
- Git/Drive/chat/source connectors;
- ADR/NORM/WHY/TRACE exporters.

## Marketplace categories

A future registry can classify plugins as:

- engine;
- profile;
- cognition;
- memory/storage;
- retrieval;
- evidence/provenance;
- authority/governance;
- view/export;
- integration/source.

Registry publication must not imply scientific quality.

Recommended separate badges/status:

- published;
- signed/provenanced;
- protocol-compatible;
- conformance-passed;
- security-reviewed;
- benchmarked;
- scientifically reproduced.

## Residual to investigate first

Highest-priority unresolved questions:

1. Can **PPX or an existing profile vocabulary** cover the portable preference layer without a MyTrues-specific competing format?
2. Is there an existing protocol that joins **decision memory + profile + engine
   invocation + evidence/provenance + outcome/revision**?
3. How should PPX/profile claims map into ODRL/DMN/MCDA/CP-nets and other engines, and how should mapping loss/divergence be represented?
4. Can profile behavior be replayed consistently across multiple engine families?
5. Can candidate cognition extraction be useful without contaminating canonical
   memory?
6. What is the smallest open port set that supports an ecosystem without turning
   MyTrues into a generic integration bus?

See:

- `../docs/OPEN-EXTENSION-ECOSYSTEM.md`;
- `SCIENCE-PRODUCT-OPPORTUNITY-001.md`;
- `SCIENCE-FRONTIER-DISCOVERY-GATE.md`.


## Prior-art correction — PPX

PPX (Preference Profile Exchange) 0.1.0-draft, dated 2026-04-23, is direct
prior art for portable, user-owned preference profiles.

It includes provenance, confidence, context modifiers, consent, lifecycle,
extensions, derived views, JSON Schema and bindings including MCP/A2A/HTTP.

Therefore:

- do not define a competing MyTrues portable profile format by default;
- prefer a `DecisionProfile` adapter backed by PPX;
- consider a decision-specific PPX namespace/extension only after proving that
  core/domain extensions cannot express the required semantics;
- distinguish PPX conformance from MyTrues decision-engine conformance.

Historical W3C CC/PP further proves that portable/extensible user preference
profiles are longstanding prior art.

The remaining candidate gap is cross-engine **decision semantic preservation**,
not preference-profile interchange itself.
