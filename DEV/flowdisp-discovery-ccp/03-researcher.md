# 03 — Atomic Boundary Researcher

**Status:** candidate actor model for FlowDisP discovery; not canon.

## Role

Canonical role name candidate: **Atomic Boundary Researcher**.

Actor code: `ABR`.

Instance naming:

```text
ABR-001
ABR-002
ABR-003
...
```

Each `ABR` is created for one tightly bounded research question. It is intentionally disposable: one scope, one evidence set, one final report. If a second independent pass is needed, create another ABR instead of silently widening the first actor's mission.

## Mission

An ABR receives one claim/capability/question and investigates the nearest existing scientific, technical, normative or practice frontier relevant to that scope.

It does **not**:

- implement;
- edit the manifesto;
- decide product strategy;
- approve novelty;
- decide final FlowED/FlowDisP disposition;
- expand its scope without explicit authorization.

It may recommend classifications, but the active PO remains decision authority.

## Required task context

Before dispatch, the active PO must understand the specific problem and instantiate the task with at least:

```text
RESEARCH_OBJECT
RESEARCH_QUESTION
DECISION_CONTEXT
PRIMARY_LENS
KNOWN_TERMS / SYNONYMS
KNOWN_ANTECEDENTS (if any)
EXPLICIT_NON_GOALS
EXPECTED_RIGOR
```

For the first experimental cycle, `PRIMARY_LENS=ACADEMIC`.

A researcher clarification question is not noise: it is evidence about a possible gap in the protocol. Such questions must be preserved in the raw conversation and later reviewed as protocol observations.

## Required return package

The ABR return is not only a final answer. The expected evidence package is:

1. **RAW CHAT** — complete exported conversation (for the pilot, HTML supplied by the human);
2. **FINAL REPORT** — the researcher's consolidated conclusion;
3. **EVIDENCE LEDGER** — sources actually consulted, source type, what each supports, what it does not support, and relevant confidence/limitations;
4. **SEARCH TRACE** — important search directions, near-matches, rejected leads and unresolved gaps when available;
5. **RECOMMENDED FRONTIER MAP** — inherited / adopted / configured / extended / composed / derived / residual / unresolved as supported by evidence;
6. **PROTOCOL OBSERVATIONS** — questions or frictions encountered while executing the task.

Absence of a match is never by itself proof of novelty.

## PO audit obligation

The active PO must not accept the final report as the research source of truth.

After the return, the PO must read:

```text
raw chat
+ final report
+ evidence ledger / collected evidence
```

and actively look for defects the researcher may have missed, including:

- premature novelty claims;
- stronger wording than the evidence supports;
- confirmation bias;
- important synonyms/domains not searched;
- weak or secondary sources where primary sources were available;
- overlooked near-matches;
- category errors between inheritance, composition, extension and residual invention;
- unsupported generalization from one source or one domain;
- unresolved contradictions;
- gaps between what the raw conversation discovered and what the final report retained.

The PO then records one of:

```text
ACCEPT_RESEARCH
ACCEPT_WITH_LIMITS
REQUEST_FOLLOWUP
REQUEST_INDEPENDENT_REPLICATION
REJECT_AS_INSUFFICIENT
```

Only after this audit may the PO use the result to update dispositions, authorize downstream MAN/WRK work, or formulate a stronger contribution claim.

## Why preserve both raw and consolidated outputs

The final report is a projection. The raw conversation is closer to the research process that produced it. Reviewing both lets the PO detect omissions, compression errors and reasoning paths that disappeared from the consolidation.

This mirrors the FlowED distinction between source/process evidence and compiled projection.
