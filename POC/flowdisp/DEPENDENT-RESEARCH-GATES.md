# FlowDisP — Dependent Research Gates

Status: proposal from PIT2ME dogfood  
Origin evidence: PIT2ME/PIT2ME_p, K0002 and research session 0010-VD

## Problem

A discovery cognition may expose a research obligation that is real now but should not be executed until another research line has produced its Consolidate C0. Leaving that obligation only in conversation creates cognitive debt; executing it immediately can duplicate work or start without required evidence.

PIT2ME exposed this with UCP: a broad ecosystem/protocol study already exists, while a UCP-specific drill-down is also required. The drill-down should be commissioned now but must consume the broad study before execution.

## Protocol increment

FlowDisP SHOULD support a first-class **Dependent Research Gate (DRG)**.

A derived research session may be created immediately with status `PENDING` and one or more explicit upstream dependencies. Commissioning removes the future-task debt; it does not authorize premature execution.

Each dependent session records at minimum:

- stable session/research ID;
- originating session and cognition;
- exact research scope;
- required upstream session IDs;
- optional upstream inputs;
- current project context/PITCH;
- exact PROMPT;
- status;
- resulting cognitive line when executed.

## Start gate

A dependent research session MUST NOT transition from `PENDING` to execution until every required dependency has produced the required accepted/materialized input, normally its Consolidate C0 or the FlowDisP artifact explicitly named by the dependency.

At start time the executor MUST:

1. resolve every required dependency;
2. attach/provide those outputs as research inputs;
3. record the exact input identity/version/hash where available;
4. stop closed if any required input is absent, unresolved or not in the required state;
5. instruct the dependent research not to repeat work already established upstream, but to validate/reference it and deepen only its own scope.

Optional dependencies may be consumed when available but do not block start.

## Dependency graph

Dependencies form a directed graph of research sessions. FlowDisP MUST reject:

- self-dependency;
- cycles;
- missing required dependency IDs;
- execution with unresolved required dependencies.

A parent research session is not automatically a chronological predecessor in the original RAW. Research dependency and cognitive chronology are separate relations and both retain provenance.

## Completion and propagation

A dependent session produces its own independent cognitive line and Consolidate C0. It does not mutate the parent result. Its result returns through normal Cross-Line Reconciliation.

If the dependent study discovers another necessary future investigation, that investigation is commissioned immediately as another PENDING session, with its own dependencies. This recursively preserves the zero-debt rule.

## Dogfood exemplar

PIT2ME:

- 0003-VD: broad product/protocol/ecosystem landscape;
- 0010-VD: UCP-specific adoption, implementations, derivative projects and competitive-boundary drill-down;
- 0010-VD depends on 0003-VD and therefore cannot start until 0003-VD's required result is available.

This is deliberately different from placing “later research UCP” in a TODO. The future work already has identity, scope, prompt, provenance and start conditions.

## Seed integration target

A future FlowDisP Seed should provide:

- dependency fields in session metadata;
- validation of the dependency DAG;
- a deterministic start/readiness check;
- explicit blocked/readiness state;
- provenance of consumed upstream outputs;
- templates for broad-research → dependent-drill-down patterns.

This proposal does not require rebuilding the Seed ZIP during PIT2ME dogfood. PIT2ME remains the implementation/evidence site; upstream consolidation can occur in the next appropriate FlowDisP Seed release.
