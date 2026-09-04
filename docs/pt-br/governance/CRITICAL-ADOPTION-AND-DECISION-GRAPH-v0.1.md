# FlowED — Critical Adoption and Decision Graph Protocol v0.1

- ID: `FLOWED-CRITICAL-ADOPTION`
- Version: `0.1-draft`
- Status: `DOGFOODING`
- Owner domain: `FlowED`

## 1. Purpose

This protocol prevents adopted rules from becoming passive compliance and prevents consumers from silently diverging from adopted domains.

FlowED requires a consumer to do two things at the same time:

1. obey the adopted domain faithfully;
2. continuously challenge whether that adopted rule remains the best known solution for the current subdomain.

The consumer may not locally override the adopted rule.

If the consumer cannot honestly defend the adopted rule as the best known applicable choice after reviewing the domain knowledge, the consumer must stop and escalate.

## 2. Core law

```text
ADOPTED DOMAIN:
USE FAITHFULLY.
CRITIQUE CONTINUOUSLY.
DIVERGE NEVER.
ESCALATE WHEN NOT CONVINCED.
```

Obedience is not passive submission.

Obedience preserves the integrity of the experiment so that criticism produces reusable domain knowledge instead of local fragmentation.

```text
LOCAL DISAGREEMENT
MUST BECOME
DOMAIN KNOWLEDGE
NOT LOCAL DIVERGENCE
```

## 3. Consumer obligation

Before continuing a work unit governed by an adopted domain, the responsible actor MUST establish all of the following:

- the applicable adopted rule is identified;
- the rule covers the current case;
- the actor has reviewed the rule's rationale and known criticisms when relevant;
- materially plausible alternatives have been considered when the decision warrants it;
- no known alternative is better for the exact subdomain under consideration;
- any new criticism has been checked against prior domain decisions, experiments, rejected alternatives and evidence;
- the actor can honestly defend continuation under the adopted rule.

If any item cannot be established, execution MUST stop.

## 4. Mandatory decision path

```text
WORK UNIT
    ↓
IDENTIFY APPLICABLE ADOPTED DOMAIN
    ↓
IDENTIFY APPLICABLE RULE / DECISION
    ↓
LOAD DECISION GRAPH CONTEXT
    ↓
CHECK PRIOR CRITICISMS / ALTERNATIVES / EXPERIMENTS
    ↓
IS THE CURRENT RULE STILL THE BEST KNOWN CHOICE
FOR THIS EXACT SUBDOMAIN?
    ├─ YES
    │    ↓
    │  USE FAITHFULLY
    │    ↓
    │  EXECUTE
    │
    └─ NO / UNKNOWN / NOT CONVINCED
         ↓
       STOP
         ↓
       MATERIALIZE CRITICISM OR GAP
         ↓
       ESCALATE TO DOMAIN AUTHORITY
         ↓
       DOMAIN REVIEWS / TESTS / DECIDES
         ↓
       UPDATE DECISION GRAPH
         ↓
       CONSUMER RE-EVALUATES
```

## 5. Decision Graph

FlowED requires important decisions to accumulate as a graph rather than disconnected prose.

Each decision node SHOULD be able to reference:

- `decision_id`
- `domain`
- `scope`
- `question`
- `current_decision`
- `rationale`
- `alternatives_considered[]`
- `criticisms[]`
- `experiments[]`
- `evidence[]`
- `outcomes[]`
- `rejected_options[]`
- `supersedes[]`
- `superseded_by[]`
- `related_decisions[]`
- `applicable_rules[]`
- `status`
- `owner`
- `last_reviewed_at`

A criticism is not discarded after resolution. It becomes a node or edge in the decision graph.

The objective is that a later actor asking the same question can traverse the previous reasoning before consuming new human time, model tokens, experiments or development effort.

## 6. Criticism protocol

When an actor disagrees with an adopted decision, the actor MUST NOT immediately create a new proposal.

The actor first searches the decision graph for the same or equivalent criticism.

### Case A — criticism already exists and actor accepts the existing resolution

Continue under the adopted rule.

### Case B — criticism already exists but actor does not accept the resolution

The actor MUST critique the resolution itself and identify what new premise, evidence, counterexample or reasoning makes reconsideration justified.

Then STOP and escalate.

### Case C — criticism is new

Materialize it as a new criticism linked to the governing decision and STOP for domain review.

### Case D — rule is missing or ambiguous

Materialize a GAP and STOP.

## 7. No local fixes

The following are prohibited while an adopted domain governs the matter:

- local exception;
- local substitute policy;
- hidden workaround that changes semantics;
- forked interpretation inside the consumer;
- continuing under a rule the actor believes is inferior;
- silently ignoring the adopted rule;
- modifying the adopted domain from the consumer's repository.

The consumer may create only the artifacts necessary to describe, evidence and escalate the criticism or gap.

## 8. Domain sovereignty

```text
OWN DOMAIN:
DECIDE.

ADOPTED DOMAIN:
OBEY + CRITIQUE.

DISAGREEMENT:
STOP + ESCALATE.

MISSING CAPABILITY:
STOP + GAP.
```

No product is globally superior to another.

Authority is bounded by domain.

A product adopting another product transfers decision authority for that adopted concern to the adopted domain while preserving the right and obligation to challenge it through the formal feedback path.

## 9. AI enforcement

A prompt alone is insufficient.

FlowED SHOULD progressively enforce this protocol using the following ladder:

```text
RULE
  ↓
PROMPT CONTRACT
  ↓
STRUCTURED DECISION RECORD
  ↓
DECISION GRAPH
  ↓
VALIDATOR
  ↓
GATE
  ↓
AUTOMATED EXECUTION BLOCK
```

The target behavior is fail-closed.

If required evidence of compliance, criticism review or domain resolution is absent, the agent MUST NOT infer permission to continue.

## 10. Machine-checkable gate

Before execution, the actor or automation SHOULD produce:

```text
ADOPTED_DOMAIN = <domain>
APPLICABLE_DECISION_ID = <id>
DECISION_GRAPH_REVIEWED = YES|NO
KNOWN_CRITICISM_MATCH = NONE|<id>
BETTER_KNOWN_ALTERNATIVE = NO|YES|UNKNOWN
ACTOR_CONVINCED = YES|NO
NEW_CRITICISM = NONE|<id or description>
GAP = NONE|<id or description>
EXECUTION_ALLOWED = YES|NO
NEXT_ACTION = <single action>
```

`EXECUTION_ALLOWED = YES` only when:

```text
APPLICABLE_DECISION_ID != UNKNOWN
AND DECISION_GRAPH_REVIEWED = YES
AND BETTER_KNOWN_ALTERNATIVE = NO
AND ACTOR_CONVINCED = YES
AND NEW_CRITICISM = NONE
AND GAP = NONE
```

Otherwise:

```text
EXECUTION_ALLOWED = NO
```

and the actor must STOP.

## 11. Anti-sycophancy requirement

Actors, especially LLM-based actors, MUST NOT treat agreement with the current PO, project or domain as a success criterion.

The actor is obligated to search for counterexamples, existing superior solutions, prior art and unresolved weaknesses whenever the decision warrants it.

Acceptance without challenge is not evidence of correctness.

The goal is not to oppose for its own sake. The goal is to make continuation require a defensible belief that the adopted decision is still the best known applicable choice.

## 12. Historical review

When old projects, chats, repositories or decisions are reviewed, FlowED SHOULD extract prior attempts into the decision graph.

For each recovered attempt, record where possible:

- what was tried;
- why it was tried;
- what result occurred;
- what was learned;
- whether the attempt was accepted, rejected, superseded or remains unresolved;
- what future criticism it answers.

This converts historical discussion into reusable decision memory.

## 13. Efficiency objective

The graph exists to reduce repeated cognition.

A criticism already answered should be answerable by traversal before new discussion begins.

A criticism not adequately answered should improve the domain rather than create a consumer-specific fork.

The desired trend is:

```text
FIRST CASE:
long discussion + experiments + decision

SECOND SIMILAR CASE:
graph traversal + validation

MATURE CASE:
automatic gate + deterministic execution
```

## 14. Final rule

```text
USE WHAT THE DOMAIN DECIDED.
CHALLENGE WHETHER IT IS STILL THE BEST.
SEARCH THE HISTORY BEFORE REPEATING THE ARGUMENT.
IF YOU CANNOT HONESTLY DEFEND IT, STOP.
IMPROVE THE DOMAIN, NOT THE CONSUMER-SPECIFIC VARIANT.
RECORD THE RESULT SO THE NEXT ACTOR PAYS LESS.
```
