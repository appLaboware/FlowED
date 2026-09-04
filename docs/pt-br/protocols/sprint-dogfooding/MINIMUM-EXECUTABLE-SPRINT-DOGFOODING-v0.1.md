# Minimum Executable Sprint Dogfooding v0.1

**ID:** `FLOWED-MINIMUM-EXECUTABLE-SPRINT-DOGFOODING`
**Version:** `0.1-draft`
**Status:** `DOGFOODING`
**Owner domain:** FlowED

## 1. Objective

Define the minimum executable sprint flow required to test FlowED governance in real work without depending on implicit agent memory or unverified assumptions.

The flow MUST make execution measurable, traceable, criticizable, reproducible when applicable, and capable of improving its own templates and rules cycle by cycle.

## 2. Minimum flow

```text
REQUESTER
  -> DEMAND
  -> REFERENCE VALIDATION
  -> VIEWPOINT ANALYSIS
  -> PO RECONCILIATION
  -> SPRINT CONTRACT
  -> CONTEXT MANIFEST
  -> ROLE-SPECIFIC RULE COMPILATION
  -> EXECUTION
  -> EXECUTION RECORD + EVIDENCE
  -> QUALITY CHECK
  -> DELIVERY
  -> REQUESTER FEEDBACK
  -> MULTI-VIEWPOINT CLOSEOUT
  -> METRICS
  -> DECISION / LEARNING
  -> TEMPLATE / POLICY / TOOL UPDATE
  -> NEXT CYCLE
```

## 3. Mandatory artifacts

Each relevant artifact MUST have identity and version.

```text
SPRINT
├── DEMAND
├── VIEWPOINT-INPUTS
├── PO-RECONCILIATION
├── SPRINT-CONTRACT
├── CONTEXT-MANIFEST
├── ROLE-COMPILED-RULES
├── EXECUTION-RECORD
├── EVIDENCE
├── REQUESTER-FEEDBACK
├── MULTI-VIEWPOINT-CLOSEOUT
├── METRICS
└── DECISION / LEARNING RECORD
```

## 4. Context Manifest

The executor MUST NOT depend on implicit LLM memory as operational authority.

Minimum structure:

```yaml
context_id:
context_version:
mission:
scope:
authoritative_sources: []
applicable_rules: []
adopted_affinities: []
known_decisions: []
input_artifacts: []
output_contract:
acceptance_tests: []
forbidden_actions: []
stop_conditions: []
escalation_path:
unresolved_references: []
```

## 5. Verify Before Propagate

Names, products, protocols, files, commands, versions, roles, identifiers, rules and operational facts MUST be resolved before propagation when they materially affect execution.

```text
VERIFY BEFORE PROPAGATE.
ASK BEFORE INVENT.
MARK UNKNOWN BEFORE GUESS.
```

Unresolved critical references MUST trigger `UNKNOWN`, clarification or STOP according to their impact.

## 6. Versioned templates

Recurring questions and operational forms SHOULD come from versioned templates so their efficiency can be compared across cycles.

Minimum candidates:

```text
DEMAND-TEMPLATE
VIEWPOINT-TEMPLATE
RESEARCH-TEMPLATE
SPRINT-CONTRACT-TEMPLATE
PO-RECONCILIATION-TEMPLATE
EXECUTION-TEMPLATE
FEEDBACK-TEMPLATE
CLOSEOUT-TEMPLATE
```

Each use SHOULD record:

```yaml
template_id:
template_version:
actor:
sprint_id:
execution_id:
answers:
```

## 7. Role-specific compilation

Applicable authority MUST be reconciled before execution and projected to the target role.

```text
AUTHORITATIVE POLICIES
+ SPRINT CONTRACT
+ CONTEXT MANIFEST
+ ROLE
+ TARGET
        -> RULE COMPILATION
        -> ROLE-SPECIFIC EXECUTION CONTEXT
```

The executor MUST receive at least:

```text
MISSION
INPUT CONTRACT
OUTPUT CONTRACT
CONSTRAINTS
ACCEPTANCE TESTS
FORBIDDEN ACTIONS
STOP CONDITIONS
ESCALATION PATH
REQUIRED EVIDENCE
```

## 8. Research viewpoint

Research MUST operate in two directions.

### 8.1 Forward research

Evaluate whether the sprint can generate generalizable knowledge, including hypothesis, experiment, benchmark, dataset, comparison, replication, case study, systematic review/mapping opportunity, paper, dissertation or thesis opportunity.

### 8.2 Foundational research

Search for theories, theses, standards, methods and prior art that support, contradict, refine or eliminate the need for proprietary work.

Research does not decide adoption. It produces evidence for the competent authority.

## 9. Inspiration and affinity

`INSPIRATION` does not create a conformity obligation.

A formally adopted `AFFINITY` creates an internal obligation of coherence within its declared scope.

Before declaring affinity:

```text
REFERENCE DISCOVERED
  -> AFFINITY PROPOSED
  -> APPLICABLE PRINCIPLES EXTRACTED
  -> SCOPE DEFINED
  -> IMPACT / CONFLICT REVIEW
  -> PO DECISION
  -> AFFINITY ADOPTED
  -> CONTINUOUS CONFORMANCE CHECK
```

Review results:

```text
READY
READY_WITH_SCOPE_LIMIT
REQUIRES_REMEDIATION
INCOMPATIBLE
```

## 10. Execution Record

The execution log MUST be structured rather than only free text.

```yaml
execution_id:
sprint_id:
demand_id:
actor_id:
role:
runtime:
model:
template_versions: {}
contract_version:
context_manifest_version:
start_time:
end_time:
inputs: []
outputs: []
tools_used: []
deterministic_steps: []
agentic_steps: []
human_interventions: []
questions_asked: []
stops: []
retries:
tests_run: []
tests_passed: []
tests_failed: []
evidence_refs: []
result:
requester_feedback_ref:
cost:
tokens:
duration:
```

## 11. Requester feedback

Every delivery MUST receive requester feedback, immediately or correlated with a later demand.

Minimum structure:

```yaml
execution_id:
accepted:
quality_score:
requirement_fit:
rework_required:
unexpected_value:
failure_reason:
requester_comment:
```

Without requester feedback, the system can measure execution but not perceived value.

## 12. Metrics

The sprint SHOULD collect comparable metrics in at least these dimensions:

- delivery: lead time, cycle time, completion, rework, failure;
- process: questions, STOPs, retries, human interventions, contract violations;
- cognition: context size, tokens, model/runtime, agentic calls;
- quality: tests, defects, acceptance, conformance violations;
- economics: execution cost, accepted-outcome cost, rework cost;
- research: hypotheses, experiments, reproducibility, benchmarks, datasets, publication opportunities.

Metrics MUST distinguish real observations from simulated or estimated data.

## 13. Self-observation

An observability/logging tool SHOULD be capable of observing its own operation without special-case semantic bypass.

Self-observation MUST avoid infinite recursion through a generic mechanism such as non-recursive sinks, reentrancy guards, idempotent event handling, or equivalent architecture.

```text
instrumented operation
  -> event emission
  -> non-recursive event sink
  -> storage
```

The architecture MUST NOT rely on a domain exception equivalent to:

```text
if tool == "log":
    bypass normal architecture
```

## 14. Multi-viewpoint closeout

Sprint closeout MUST allow independent analysis before authoritative reconciliation. Typical viewpoints include Product, Engineering, Quality, Marketing and Research; other viewpoints may be added when the domain requires them.

Viewpoints MAY disagree. Conflict MUST be recorded before PO reconciliation rather than silently collapsed.

## 15. Process improvement as an experimental outcome

The process itself is part of the experiment.

A cycle SHOULD make it possible to compare template, policy, tool, context and model-allocation versions using measurable outcomes.

```text
same or comparable demand
+ changed template/policy/tool version
        -> measurable outcome delta
```

Potential improvements include less context, fewer questions, fewer retries, less human intervention, lower cost, better acceptance, less rework, higher deterministic coverage and stronger traceability.

## 16. Evolution rule

No new abstraction should enter the executable flow merely because it appears elegant.

```text
OBSERVED DEFECT / GAP / EVIDENCE
  -> ANALYSIS
  -> OWNING DOMAIN
  -> CHANGE REQUEST
  -> DECISION
  -> IMPLEMENTATION
  -> NEXT MEASURED CYCLE
```

This document is intentionally minimal and subject to revision through dogfooding evidence.
