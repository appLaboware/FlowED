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
| Decision policy/profile | DecisionProfile port | MCDA/PL + personalized agents + ODRL constraints | **RESEARCH S1/S3** |
| Portable profile across engines | protocol/profile | no complete match identified in current pass | **RESEARCH S1** |
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

1. Is there an existing general standard for a **portable versioned decision
   preference/profile** across heterogeneous engines?
2. Is there an existing protocol that joins **decision memory + profile + engine
   invocation + evidence/provenance + outcome/revision**?
3. How should profile semantics be divided among existing standards such as
   ODRL/DMN/MCDA/CP-nets rather than encoded in a proprietary schema?
4. Can profile behavior be replayed consistently across multiple engine families?
5. Can candidate cognition extraction be useful without contaminating canonical
   memory?
6. What is the smallest open port set that supports an ecosystem without turning
   MyTrues into a generic integration bus?

See:

- `../docs/OPEN-EXTENSION-ECOSYSTEM.md`;
- `SCIENCE-PRODUCT-OPPORTUNITY-001.md`;
- `SCIENCE-FRONTIER-DISCOVERY-GATE.md`.
