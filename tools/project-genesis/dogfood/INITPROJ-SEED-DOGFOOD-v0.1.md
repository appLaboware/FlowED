# Project Genesis — InitProj Seed Dogfood

Status: `DOGFOOD / UNVALIDATED`

## Target

Assess the InitProj project/session seed as an existing product capability using the Project Genesis / PMFN discovery method.

This assessment does **not** authorize modifications to InitProj.

## Observed current seed responsibilities

The current InitProj seed implementation materializes a durable local AI session including, among other artifacts:

- `ia-sessions/<session>/raw/`;
- `INBOX/`;
- `OUTBOX/`;
- `_SYSTEM/knowledge/`;
- `_SESSION_RULES.md`;
- `CONTEXT.md`;
- `HANDOFF.md`;
- `session_resume.md`;
- `PROMPT.md`;
- an initial project-understanding INBOX;
- project memory bootstrap.

The implementation also attempts to preserve supplied POC/context artifacts and uses canonical templates when present.

## Reason for dogfood

The seed should itself be subjected to the same law it will eventually help downstream projects preserve:

> **Do not own or factor what can be adopted; decompose only until realization decisions become sufficiently stable.**

The goal is not to prove InitProj wrong. The goal is to determine which seed responsibilities are sovereign InitProj capabilities, which should be delegated, which can be adopted from standards/tools, and which residual is actually justified.

## Initial factor map

Starting hypothesis only:

```text
InitProj project/session seed
├── project facts acquisition
├── initial project brief normalization
├── durable session identity
├── session directory topology
├── raw artifact intake
├── inbox/outbox communication bootstrap
├── mission/context materialization
├── handoff/resumption semantics
├── session rules projection
├── prompt projection
├── project memory bootstrap
├── initial understanding demand
├── actor/role projection
├── template resolution
├── non-overwrite behavior
├── repository/project topology assumptions
└── transition from pre-project evidence into durable local session
```

## PMFN questions

For every factor:

1. Is this capability truly owned by InitProj's sovereign domain?
2. Is there an existing standard, protocol, product or library that should be adopted?
3. Is the current implementation merely one provider behind a stable InitProj contract?
4. Does the factor belong to InterMembers, FlowED, CRS, repository bootstrap or another domain rather than InitProj?
5. Does Project Genesis already produce information that should enter the seed directly instead of being rediscovered through `001-ENTENDIMENTO-PROJETO`?
6. Which fields can be inherited from the Project Evidence Dossier / Project Birth Record?
7. Which fields are still legitimately `UNKNOWN` at materialization time?
8. Where does further factorization stop changing sourcing, authority or evidence decisions?

## Important integration hypothesis

The Project Genesis output may become a richer upstream seed for InitProj.

Instead of:

```text
RAW IDEA
  ↓
InitProj seed
  ↓
MPO discovers project from near-zero
```

candidate future flow:

```text
RAW IDEA
  ↓
Project Genesis / PMFN investigation
  ↓
Project Evidence Dossier
  ↓
identity + repository design + birth record
  ↓
InitProj durable seed
  ↓
MPO resumes an already-evidenced project
```

This is a hypothesis. It must not create a circular dependency or violate domain sovereignty.

## Current implementation risk to verify

The current session seed script appears to reference `brief_for_ctx` before its later local initialization in the same function. This must be verified in execution before being treated as a confirmed defect.

## Expected assessment profile

No numeric profile should be invented before evidence collection:

```text
P   = UNKNOWN
EC  = UNKNOWN
XC  = UNKNOWN
XA  = UNKNOWN
XE  = UNKNOWN
FR  = UNKNOWN
EM  = UNKNOWN
RC  = UNKNOWN
```

## Dogfood output

The completed run should produce:

- factor map with stopping rationale;
- domain-owner classification per factor;
- adopt/configure/extend/adapt/compose/invent evidence per factor;
- duplication and sovereignty findings;
- candidate removals from InitProj;
- candidate interfaces to upstream Project Genesis artifacts;
- residual InitProj seed responsibilities;
- risks and unknowns;
- migration proposal only if evidence justifies it.

No InitProj implementation change is authorized by this document.
