# ADVERSARIAL DISCOVERY AND DECISION CHALLENGE

ID: FLOWED-ADVERSARIAL-DISCOVERY
Version: 0.1-draft
Status: DOGFOODING
Owner domain: FlowED

## 1. Purpose

Prevent LaboWare from spending engineering time, human attention, tokens, money, compute and energy building what already exists adequately, or preserving a weaker decision merely because it is already institutionalized.

This protocol establishes two mandatory mechanisms:

1. **Adversarial Discovery** — multiple independent search lanes must try to discover every potentially useful existing solution before proprietary construction is authorized.
2. **Decision Challenge** — every adopted decision remains executable law, but every consumer is also obligated to test whether a materially better alternative exists and to escalate honest disagreement instead of diverging locally.

The purpose is not to create debate for its own sake. The purpose is to make every discovered failure permanently improve the system.

---

## 2. Core laws

```text
SEARCH BROADLY BEFORE SELECTING.
COMPOSE BEFORE BUILDING.
BUILD ONLY THE RESIDUAL OF THE BEST KNOWN COMPOSITION.
```

```text
USE THE ADOPTED LAW.
CHALLENGE WHETHER IT IS STILL THE BEST.
IF YOU CANNOT HONESTLY DEFEND IT, STOP AND ESCALATE.
NEVER DIVERGE LOCALLY.
```

```text
EVERY FAILURE MUST IMPROVE THE NEXT SEARCH.
EVERY REPEATED ARGUMENT MUST BECOME CHEAPER.
EVERY LATE-DISCOVERED EXISTING SOLUTION IS A PROCESS DEFECT.
```

---

## 3. Discovery is a tournament, not a single search

No single model, search engine, researcher or query strategy is assumed sufficient.

A discovery cycle must use independent lanes whose results are unioned before ranking or elimination.

Minimum lanes should include, when applicable:

- general web search;
- GitHub / public source-code repositories;
- package registries and dependency ecosystems;
- official product/vendor documentation;
- academic literature and technical papers;
- standards and specifications;
- software catalogs / marketplaces / extension ecosystems;
- community discussions, issue trackers and comparison discussions;
- multiple LLMs or agentic research systems with different models and search strategies;
- at least one adversarial researcher explicitly tasked with finding candidates missed by the others.

Domain-specific sources may be added as mandatory lanes.

No candidate may be rejected merely because another candidate already appears good.

---

## 4. Two-stage discovery

### Stage A — exhaustive candidate capture

Goal: maximize recall.

Researchers must search for every solution with a plausible chance of contributing partially or totally.

During this stage:

- do not optimize for one winner;
- do not stop at the first adequate solution;
- do not prefer fewer dependencies merely for convenience;
- do not build architecture around an early favorite;
- do not remove candidates before recording why they were considered.

Output: `CANDIDATE_UNIVERSE`.

### Stage B — free composition search

Goal: determine the best known composition of existing capabilities.

The question is not:

> Which single product should be adopted?

The question is:

> Which combination of available capabilities produces the strongest implementation of the desired domain?

One component may win. Two may win. Seventy may win.

Component count is secondary to engineering quality. Fewer components are preferred only when quality is equal or when the reduced composition materially improves maintainability, security, operability, supply-chain risk or another explicit criterion.

Only after this composition is known may a residual proprietary build be calculated.

---

## 5. Mandatory discovery artifacts

Each discovery cycle must materialize at least:

- `DEMAND` / target problem;
- capability inventory;
- mandatory source lanes;
- researchers/models/search systems used;
- queries or search strategies used;
- candidate universe;
- candidate × capability matrix;
- license / provenance notes when relevant;
- composition alternatives;
- selected best-known composition;
- residual gap;
- uncertainty and blind spots;
- stop condition evidence;
- cost and effort metrics.

If a proprietary build is authorized, its authorization must point to this evidence.

---

## 6. Search saturation gate

Discovery cannot prove mathematically that no solution exists. Therefore the system uses evidence of saturation rather than false certainty.

A discovery cycle may close only after:

1. mandatory source lanes were completed or explicitly marked inaccessible;
2. multiple independent researchers were executed;
3. at least one adversarial pass attempted to find missed candidates;
4. candidate discovery rate materially decayed;
5. repeated new searches produced no material new candidate for a configured saturation window;
6. known high-probability synonyms, adjacent domains and alternate terminology were explored;
7. unresolved blind spots are recorded.

The saturation threshold is configurable by risk/cost of the prospective build.

Higher expected implementation cost requires stronger discovery evidence.

---

## 7. Adversarial researcher roles

A discovery arena should separate roles to reduce correlated failure.

Suggested roles:

- **Scout** — broad candidate discovery;
- **Repository Scout** — source-code ecosystems;
- **Standards Scout** — standards/specifications/prior art;
- **Commercial Scout** — existing products/SaaS/tools;
- **Academic Scout** — papers/research prototypes;
- **Composition Analyst** — finds useful partial combinations;
- **Red Scout** — attempts to find what all previous scouts missed;
- **Reconciler** — unions, deduplicates and preserves provenance without prematurely eliminating candidates.

Different LLM families, search engines and query formulations should be used where economically reasonable.

The same model repeated with nearly identical prompts is not considered strong independence.

---

## 8. Discovery failure as first-class defect

A **Late Discovery Defect (LDD)** occurs when, after meaningful proprietary effort has begun, an existing solution is found that would materially have reduced or eliminated that effort and should reasonably have been discoverable during the original discovery cycle.

An LDD is not merely recorded as historical regret. It triggers process correction.

Required postmortem:

- what product/solution was missed;
- when it became discoverable;
- which search lane should have found it;
- which terminology would have revealed it;
- which researcher/model missed it;
- why reconciliation did not expose it;
- monetary/token/human-time/compute cost incurred after the miss;
- what permanent rule/query/source/profile/test must be added;
- which prior and future projects are affected.

The corrected discovery protocol becomes the new baseline.

---

## 9. Decision Challenge

Every consumer of an adopted domain has two simultaneous obligations:

1. **execution fidelity** — obey the current authoritative decision;
2. **productive challenge** — seek evidence that a better decision exists.

Obedience is not passive submission.

It preserves the integrity of the adopted experiment while channeling criticism to the domain where everyone can benefit from it.

A consumer may not modify, bypass or locally replace an adopted decision.

If the consumer finds a superior alternative or cannot honestly defend the current decision, execution must stop and the challenge must be escalated to the sovereign domain.

---

## 10. Challenge sequence

```text
CURRENT DECISION
      ↓
READ RATIONALE
      ↓
READ PRIOR CRITICISMS
      ↓
READ PRIOR ALTERNATIVES / EXPERIMENTS
      ↓
ATTEMPT TO REFUTE CURRENT DECISION
      ↓
CAN CURRENT DECISION STILL BE HONESTLY DEFENDED?
   ├─ YES → CONTINUE EXECUTION
   └─ NO  → STOP + ESCALATE
```

A challenge must distinguish:

- preference;
- familiarity;
- training bias;
- aesthetic disagreement;
- measurable superiority;
- contextual superiority;
- new evidence;
- previously tested argument;
- previously rejected argument with unchanged premises;
- genuinely novel argument.

The challenge is not "Would I personally choose something else?"

It is:

> Can I demonstrate that another decision is materially superior under the domain's declared objectives and constraints?

---

## 11. Decision graph

Every significant decision should be represented as a graph rather than an isolated conclusion.

Suggested node types:

- QUESTION
- ASSUMPTION
- CANDIDATE
- DECISION
- RATIONALE
- CRITICISM
- COUNTERARGUMENT
- EXPERIMENT
- EVIDENCE
- RESULT
- FAILURE
- SUPERSEDED_DECISION
- OPEN_GAP

Suggested relationships:

- challenges
- supports
- contradicts
- tested_by
- produced
- supersedes
- depends_on
- rejected_because
- accepted_because
- discovered_after
- equivalent_to
- refines

Before raising a new criticism, the consumer must search this graph for semantically equivalent prior challenges.

If equivalent material exists, the consumer must inspect the prior reasoning before reopening the question.

A previously decided issue may be reopened when premises, evidence, constraints or domain objectives have materially changed, or when the prior reasoning is itself successfully challenged.

---

## 12. Productive change-of-mind objective

A product should not optimize for defending its existing decisions.

It should optimize for retaining the best defensible decision.

Therefore:

```text
WIN ≠ KEEP THE OLD DECISION
WIN = KEEP THE BEST KNOWN DECISION
```

A successful challenge that causes a better decision is a product improvement, not a governance failure.

Conversely, an unsuccessful challenge is still valuable when its rationale is recorded, because future actors do not need to pay again for the same argument.

---

## 13. Metrics

Minimum metrics should include:

### Discovery quality

- `CANDIDATE_COUNT`
- `SOURCE_LANE_COVERAGE`
- `INDEPENDENT_RESEARCHER_COUNT`
- `NEW_CANDIDATES_PER_PASS`
- `SEARCH_SATURATION_RATE`
- `CANDIDATE_OVERLAP_RATE`
- `RED_SCOUT_NOVEL_CANDIDATE_COUNT`
- `LATE_DISCOVERY_DEFECT_COUNT`
- `LATE_DISCOVERY_DEFECT_RATE`

### Cost

- `TOKENS_TO_DISCOVERY`
- `HUMAN_MINUTES_TO_DISCOVERY`
- `MODEL_COST_TO_DISCOVERY`
- `COMPUTE_COST_TO_DISCOVERY`
- `TIME_TO_FIRST_VALID_CANDIDATE`
- `TIME_TO_SATURATION`
- `COST_AFTER_MISSED_DISCOVERY`

### Decision reuse

- `PRIOR_ARGUMENT_REUSE_RATE`
- `REPEATED_ARGUMENT_RATE`
- `TIME_TO_FIND_PRIOR_RATIONALE`
- `FALSE_NOVELTY_RATE`
- `DECISION_GRAPH_HIT_RATE`

### Challenge quality

- `CHALLENGE_COUNT`
- `NOVEL_CHALLENGE_RATE`
- `CHALLENGE_WITH_EVIDENCE_RATE`
- `DECISION_CHANGE_RATE`
- `DECISION_CONFIRMED_RATE`
- `UNRESOLVED_CHALLENGE_RATE`
- `LOCAL_DIVERGENCE_COUNT`

No metric should reward changing decisions merely to increase change rate.

---

## 14. Retrospective benchmark

Historical LaboWare failures where a suitable external solution was found only after significant internal effort must become benchmark cases.

For each known case:

1. hide the known solution from the researchers;
2. run the current discovery protocol;
3. measure whether the protocol rediscovers it;
4. record which lane/model/query found it;
5. measure cost and time;
6. if it still fails, improve the protocol and rerun.

The protocol is not considered mature because it sounds reasonable. It becomes mature by demonstrating increasing recall on known historical failures and future live cases.

---

## 15. Aviation-style learning principle

The operating analogy is safety-critical learning: anomalies, misses, near-misses and failures receive disproportionate analytical attention because they reveal how the system can improve.

For LaboWare:

```text
SUCCESS CONFIRMS.
FAILURE TEACHES.
A REPEATED FAILURE WITHOUT PROCESS CHANGE IS UNACCEPTABLE.
```

Blame is not the objective. Process learning is.

The valuable question is not:

> Who failed to find it?

It is:

> What property of our search system allowed a discoverable solution to remain invisible, and what permanent mechanism will prevent recurrence?

---

## 16. Execution gate

Before proprietary implementation begins, the responsible actor must be able to produce:

```text
DISCOVERY_COMPLETE = YES
MANDATORY_SOURCE_LANES_COMPLETE = YES
INDEPENDENT_RESEARCH_COMPLETE = YES
ADVERSARIAL_SEARCH_COMPLETE = YES
SATURATION_GATE = PASS
BEST_KNOWN_COMPOSITION_IDENTIFIED = YES
RESIDUAL_GAP_IDENTIFIED = YES
KNOWN_EXISTING_SOLUTION_THAT_DOMINATES = NO
BUILD_AUTHORIZATION = YES
```

Any required `NO`, `UNKNOWN` or unresolved blocker results in:

```text
EXECUTION_ALLOWED = NO
STOP
```

---

## 17. Dogfooding sequence

First intended controlled proving ground:

1. InterMembers communication path becomes operational;
2. NGit receives its own repository/domain/PO;
3. known controversial NGit decisions are materialized into the decision graph;
4. independent consumers challenge those decisions;
5. InterMembers transports STOP/escalation/response cycles;
6. the domain records criticisms, prior attempts, evidence and decisions;
7. repeated equivalent challenges are measured for interaction-cost reduction;
8. discovery/search mechanisms are tested against known alternatives;
9. results refine this protocol.

The objective is not to prove NGit right.

The objective is to prove that the system can discover when NGit is right, discover when it is wrong, change it when justified, and preserve enough history that the next actor pays less for the same question.
