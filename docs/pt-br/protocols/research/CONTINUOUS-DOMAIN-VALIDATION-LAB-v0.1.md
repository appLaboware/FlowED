# FlowED — Continuous Domain Validation Laboratory v0.1

- ID: `FLOWED-CONTINUOUS-DOMAIN-LAB`
- Version: `0.1-draft`
- Status: `DOGFOODING`
- Owner domain: `FlowED`

## 1. Purpose

Require each product/domain PO to maintain an ongoing research and validation laboratory for the assumptions that justify the product's continued existence, architecture and major decisions.

A product is not considered permanently justified because it was once correct.

Its important premises must remain challengeable, testable and, whenever possible, continuously revalidated.

## 2. Core law

```text
A DECISION THAT JUSTIFIES THE PRODUCT
MUST REMAIN TESTABLE.

WHEN A DETERMINISTIC TEST CAN REPLACE DEBATE,
AUTOMATE THE TEST.

WHEN THE TEST CHANGES RESULT,
REOPEN THE DECISION.
```

## 3. Research laboratory as a PO duty

The PO must maintain a portfolio of microdomains / microquestions that materially support:

- product existence;
- major architecture;
- adopted dependencies;
- controversial decisions;
- known external limitations;
- assumptions about competing solutions;
- assumptions about platform/runtime behavior.

Each microquestion should be as narrow as possible.

Example for NGit:

```text
QUESTION:
Can a parent Git repository safely and naturally version a nested independent Git repository in the exact way NGit requires without NGit-specific alignment?

CURRENT EXPECTED RESULT:
FAIL

IF RESULT BECOMES PASS:
NGit justification must be re-evaluated.
```

## 4. Deterministic probes first

When a microquestion can be expressed as a reproducible experiment, it SHOULD become a deterministic probe rather than repeated LLM reasoning.

A probe records at least:

- `probe_id`;
- `domain`;
- `question`;
- `setup`;
- `command_or_test`;
- `expected_result`;
- `actual_result`;
- `environment`;
- `tool_versions`;
- `evidence`;
- `last_run_at`;
- `next_run_policy`;
- `decision_ids_affected[]`.

## 5. Continuous execution

Probes may run:

- on a schedule;
- when an external dependency changes version;
- when a relevant standard/specification changes;
- when a new competitor/candidate appears;
- when a consumer raises a criticism;
- before a major release;
- on demand by the PO.

The cheapest deterministic mechanism that produces adequate evidence SHOULD be preferred.

LLMs are used where interpretation, discovery or hypothesis generation is required, not where a stable executable test already exists.

## 6. Result states

```text
PASS_STILL_SUPPORTS_DECISION
FAIL_STILL_SUPPORTS_DECISION
RESULT_CHANGED
INCONCLUSIVE
TEST_INVALID
ENVIRONMENT_CHANGED
```

The semantic meaning of PASS/FAIL must be defined per probe. A raw technical PASS is not automatically a product success.

## 7. Result change is a governance event

When a probe result changes in a way that undermines a governing premise:

```text
PROBE RESULT CHANGED
      ↓
FREEZE AFFECTED DECISION / ADOPTION
      ↓
MATERIALIZE EVIDENCE
      ↓
OPEN DECISION-GRAPH CHALLENGE
      ↓
PO RE-EVALUATES
      ↓
DECISION CONFIRMED / SUPERSEDED / RETIRED
      ↓
PROPAGATE IMPACT
```

The product must not hide or downgrade a result because it threatens its own relevance.

## 8. Product self-obsolescence is success

A product that becomes unnecessary because an external platform, standard or adopted dependency evolves must be allowed to retire.

```text
PRODUCT VALUE != PRODUCT SURVIVAL
PRODUCT VALUE = BEST CURRENT SOLUTION
```

If Git eventually solves the exact residual that justifies NGit better than NGit itself, the correct outcome may be to retire NGit and return to Git directly.

Keeping a product alive after its residual disappears is process failure.

## 9. Dependency and consumer graph

Every material decision SHOULD identify affected consumers.

When a decision is superseded or retired, the domain must be able to determine:

- which products adopt it;
- which procedures reference it;
- which documents cite or depend on it;
- which tests validate it;
- which repositories/configurations instantiate it;
- which owners/followers must be notified.

The notification/relationship model is delegated to the adopted documentation and communication domains.

FlowED owns the orchestration requirement: impact must propagate; the mechanism may be supplied by ISO29110-Lite and InterMembers.

## 10. Research agent

Each mature domain SHOULD have one or more research agents with bounded missions.

Examples:

- monitor one external limitation;
- rerun one deterministic compatibility test;
- search periodically for new competing solutions;
- inspect release notes affecting a known gap;
- challenge one controversial decision;
- report only meaningful state changes.

The agent must not modify the governing decision directly.

It produces evidence and challenge events for the PO.

## 11. Microdomain registry

Suggested fields:

```text
microdomain_id
name
owner_domain
question
current_claim
decision_ids[]
probe_ids[]
external_dependencies[]
search_profile
criticality
review_frequency
last_validated_at
status
```

## 12. Metrics

Track at least:

- `ACTIVE_MICRODOMAIN_COUNT`
- `AUTOMATED_PROBE_RATIO`
- `PROBE_EXECUTION_COUNT`
- `RESULT_CHANGE_COUNT`
- `TIME_FROM_RESULT_CHANGE_TO_PO_REVIEW`
- `DECISIONS_REOPENED_BY_EVIDENCE`
- `PRODUCT_ASSUMPTIONS_WITHOUT_TEST`
- `EXTERNAL_CHANGE_DETECTION_LATENCY`
- `RETIREMENT_OR_SIMPLIFICATION_EVENTS`

The objective is not to maximize changes. It is to minimize the time a product continues under a premise that has stopped being true.

## 13. Interaction with Critical Adoption

Continuous validation does not authorize local divergence.

A consumer or research agent that discovers a better alternative must:

1. record evidence;
2. STOP affected execution where required;
3. challenge/escalate through the owning domain;
4. wait for authoritative resolution;
5. resume only under the new or confirmed decision.

## 14. Interaction with Adversarial Discovery

The initial Discovery Arena asks:

> What already exists?

The Continuous Domain Lab asks forever after:

> Has the world changed enough that our decision should change?

Both feed the same decision graph.

## 15. Final law

```text
DO NOT DEFEND A PRODUCT'S EXISTENCE.
DEFEND THE BEST KNOWN SOLUTION.

TURN IMPORTANT ASSUMPTIONS INTO TESTS.
RUN CHEAP TESTS CONTINUOUSLY.
TREAT RESULT CHANGES AS GOVERNANCE EVENTS.
ALLOW EVIDENCE TO RETIRE THE PRODUCT THAT CREATED THE TEST.
```
