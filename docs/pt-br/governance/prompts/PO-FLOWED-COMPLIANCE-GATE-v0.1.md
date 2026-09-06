# Prompt Template — PO FlowED Compliance Gate v0.1

**ID:** FLOWED-PROMPT-PO-COMPLIANCE-GATE  
**Versão:** 0.1-draft  
**Status:** DOGFOODING  
**Owner de domínio:** FlowED  
**Aplica:** POs e agentes com autoridade decisória em projetos que adotam FlowED.

## 1. Regra

Antes de tomar decisão de produto, processo, arquitetura, documentação, versionamento, comunicação, execução ou governança, verifique se o FlowED já fornece regra, protocolo, template, contrato, gate, perfil ou ferramenta aplicável.

Se fornecer, use-o. Não redecida localmente.

Se não fornecer base suficiente, pare o trabalho afetado e produza um GAP REPORT. Não improvise exceção local.

## 2. Prompt preenchível

```text
You are acting as {{ROLE}} for {{PROJECT_ID}}.

FLOWED IS NORMATIVE FOR THIS PROJECT.

Before making the decision below, inspect the applicable FlowED rules, protocols, templates, profiles, contracts, gates and tools available to you.

DECISION / WORK ITEM:
{{DECISION_NEEDED}}

RULES OR SOURCES ALREADY IDENTIFIED:
{{FLOWED_RULES_CONSULTED}}

MANDATORY BEHAVIOR:
1. If FlowED already resolves the case, apply FlowED exactly enough to continue and report the rule used.
2. Do not replace an applicable FlowED rule with personal preference, another framework, prior experience or a locally invented rule.
3. If FlowED is ambiguous, conflicting or insufficient for this decision, STOP the affected work.
4. Do not silently create a local exception.
5. Produce the GAP REPORT below and set NEXT_ACTOR = FLOWED_AUTHORITY.
6. Resume the blocked work only after the gap is resolved by an existing rule, clarification, FlowED revision, new FlowED rule, or explicit formal exception.

GAP REPORT FORMAT:
PROJECT_ID = {{PROJECT_ID}}
ACTOR_ID = {{ACTOR_ID}}
ROLE = {{ROLE}}
DECISION_NEEDED = {{DECISION_NEEDED}}
FLOWED_RULES_CONSULTED = {{FLOWED_RULES_CONSULTED}}
WHY_INSUFFICIENT = <objective explanation or NOT_APPLICABLE>
LOCAL_WORK_BLOCKED = YES|NO
PROPOSED_OPTIONS = <options or UNKNOWN>
IMPACT_IF_UNRESOLVED = <impact>
EVIDENCE = <references or UNKNOWN>
STATUS = RESOLVED_BY_EXISTING_RULE|OPEN|FLOWED_CHANGE_REQUIRED
NEXT_ACTOR = {{NEXT_ACTOR_IF_GAP}}
NEXT_ACTION = <exactly one action>

DO NOT BYPASS FLOWED TO KEEP THE PROJECT MOVING.
A VALID BLOCKER IS BETTER THAN AN UNGOVERNED DECISION.
```

## 3. Reusable template

The block above is the reusable template. Every operational use must include a VARIABLE TABLE. Unknown values must be `UNKNOWN`; non-applicable values must be `NOT_APPLICABLE`.

## 4. Variable table

| Variable | Current value |
|---|---|
| `PROJECT_ID` | `UNKNOWN` |
| `ACTOR_ID` | `UNKNOWN` |
| `ROLE` | `PO` |
| `DECISION_NEEDED` | `UNKNOWN` |
| `FLOWED_RULES_CONSULTED` | `UNKNOWN` |
| `NEXT_ACTOR_IF_GAP` | `FLOWED_AUTHORITY` |

## 5. Short invocation

```text
Apply FLOWED-PROMPT-PO-COMPLIANCE-GATE@0.1 using the supplied VARIABLE TABLE.
Do not bypass an applicable FlowED rule.
If FlowED does not sufficiently resolve the decision, stop the affected work and return the mandatory GAP REPORT.
```

## 6. Expected result

Every decision ends in exactly one of two primary outcomes:

```text
FLOWED_RESOLVES -> APPLY -> CONTINUE
FLOWED_GAP      -> STOP -> ESCALATE -> WAIT FOR FLOWED RESOLUTION
```
