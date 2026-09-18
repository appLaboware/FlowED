# 05 — Atomic Research Protocol

**Status:** candidate execution protocol for PO review; not canon.

## Purpose

Normalize how the active PO instantiates, dispatches and audits one atomic discovery research task.

The protocol is designed so the PO understands the project-specific problem first, then asks an independent researcher to investigate one bounded frontier, and finally audits the researcher's complete trace instead of trusting only the summary.

## Roles

```text
ACTIVE PO
  understands project context
  defines the atomic task
  dispatches ABR
  audits raw + consolidated return
  decides next action

ABR — Atomic Boundary Researcher
  investigates one bounded question
  gathers evidence
  returns raw trace + consolidated report
  does not make final product/novelty decision

HUMAN
  transports the prompt and, in the pilot, exports/returns the full chat HTML
  does not become the semantic integrator between actors
```

## Naming

Research actor instances:

```text
ABR-001
ABR-002
ABR-003
...
```

Research task IDs:

```text
FDP-AR-001
FDP-AR-002
FDP-AR-003
...
```

`FDP` is a candidate short identifier for FlowDisP artifacts. `FLDP` remains reserved as the candidate future CLI/execution surface until PO review decides otherwise.

One ABR normally owns one task only.

## Phase A — PO framing

Before creating the researcher prompt, the active PO must record:

```text
TASK_ID=
ACTOR_ID=
RESEARCH_OBJECT=
RESEARCH_QUESTION=
DECISION_CONTEXT=
PRIMARY_LENS=
EXPECTED_RIGOR=
KNOWN_TERMS=
KNOWN_ANTECEDENTS=
EXPLICIT_NON_GOALS=
DELIVERABLES=
```

The PO should formulate the question to falsify or locate the boundary, not to defend a desired conclusion.

Example posture:

```text
Do not assume novelty.
Find the closest antecedent.
Determine exactly what it covers.
Identify what, if anything, remains residual.
Preserve UNRESOLVED where evidence is insufficient.
```

## Phase B — ABR execution

The ABR researches independently within the bounded scope.

It should prefer primary and authoritative sources when available and preserve enough provenance to support later audit.

If the ABR asks a clarification question, the question is preserved as part of the research trace. The active PO later decides whether that question indicates:

```text
CASE_SPECIFIC_CLARIFICATION
or
PROTOCOL_GAP_CANDIDATE
```

The first observed pilot example was a question about whether the research would support internal architecture, requirements scope or academic writing. This exposed `DECISION_CONTEXT` as a candidate mandatory task field.

## Phase C — Required return

The task is not complete when a researcher posts a conclusion.

Expected package:

```text
RAW_CHAT.html              # complete pilot conversation export
FINAL-REPORT.md            # consolidated researcher report
EVIDENCE-LEDGER.*          # sources and claim support/limits
SEARCH-TRACE.*             # important paths, near-matches, rejected leads, gaps
PROTOCOL-OBSERVATIONS.md   # execution frictions/questions, if any
```

The exact serialization is experimental. Content is mandatory; filenames/formats may evolve.

## Phase D — PO forensic audit

The active PO reads the **raw conversation**, not only the final report.

The audit asks:

```text
1. Did the researcher answer the actual atomic question?
2. Did the scope drift?
3. Were important search terms or adjacent domains missed?
4. Were sources sufficiently primary/authoritative?
5. Did any source get interpreted more strongly than it supports?
6. Were near-matches dismissed too easily?
7. Did the final report omit caveats found in the raw chat?
8. Did the researcher mistake absence-of-evidence for evidence-of-novelty?
9. Is the proposed residual truly residual at the chosen granularity?
10. Is another independent ABR needed?
```

The PO must distinguish:

```text
EVIDENCE
RESEARCHER INTERPRETATION
PO INTERPRETATION
PO DECISION
```

## Phase E — PO disposition

Allowed research-audit outcomes:

```text
ACCEPT_RESEARCH
ACCEPT_WITH_LIMITS
REQUEST_FOLLOWUP
REQUEST_INDEPENDENT_REPLICATION
REJECT_AS_INSUFFICIENT
```

If accepted sufficiently for decision, the PO may then classify the project's relation to the frontier, using candidate dispositions such as:

```text
ADOPT
CONFIGURE / PERSONALIZE
EXTEND / OVERLAY
COMPOSE
FORK / MODIFY
DERIVE / INSPIRE
BUILD_RESIDUAL
UNRESOLVED
```

These disposition labels are themselves candidates pending PO review of the broader FlowDisP CCP.

## Independence rule

Parallel ABRs researching independent claims should not receive conclusions from sibling ABRs unless those conclusions are explicitly part of their research object. This reduces cross-contamination and gives the PO independent evidence streams to compare.

## Downstream gate

MAN and WRK should not receive a stronger claim or implementation order merely because one ABR produced a persuasive report.

The active PO must first complete the raw-trace audit and decide whether the evidence is sufficient for the intended downstream action.

## Pilot success criteria

The pilot is successful if it teaches us both:

```text
A. something reliable about the scientific/technical frontier;
and
B. something observable about how the discovery protocol itself should improve.
```

The research result and the protocol-learning result are separate outputs.
