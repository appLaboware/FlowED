# RBP Profile — AI_RESEARCH 0.1

**Profile:** `AI_RESEARCH`  
**Status:** DRAFT / DOGFOODING  
**Parent protocol:** `FLOWED-REPOSITORY-BOOTSTRAP@0.1`  

## 1. Purpose

Create a repository that can be operated by human and AI researchers without relying on provider memory, while preserving origin, authority, research plan, evidence, inbox/outbox communication and reproducible handoff.

## 2. Required inputs

```text
repository_name
research_question
research_scope
research_authority
initial_actor
initial_session
origin
allowed_external_research
expected_outputs
```

Unknown values are `UNKNOWN`.

## 3. Required adopted concepts

The profile adopts, by reference, compatible concepts from the current IA Sessions / InterMembers incubation:

```text
Actor != Session != Runtime
chat memory != repository authority
canonical rules != vendor gateway
raw source != cognition != handoff != evidence
inbox != outbox
```

These references remain replaceable by future canonical InterMembers versions.

## 4. Initial tree

```text
<repo>/
├── README.md
├── REPOSITORY-MANIFEST.json
├── .RULES.md
├── AGENTS.md
├── .github/
│   └── copilot-instructions.md
├── docs/
│   ├── bootstrap/
│   │   ├── ORIGIN.md
│   │   └── CURRENT-STATE.md
│   └── research/
│       ├── QUESTION.md
│       ├── PLAN.md
│       ├── SOURCES.md
│       ├── FINDINGS.md
│       ├── CANDIDATES.md
│       ├── COMPARISON.md
│       └── DECISION.md
├── actors/
│   └── <actor>/
│       └── sessions/
│           └── <session>/
│               ├── SESSION-MANIFEST.json
│               ├── COGNICAO.md
│               ├── HANDSOFF.md
│               ├── inbox/
│               ├── outbox/
│               ├── planning/
│               │   ├── ROADMAP.md
│               │   ├── BACKLOG.md
│               │   └── SPRINT-001.md
│               └── evidence/
├── _dev/
│   ├── README.md
│   └── experiments/
└── scripts/
    └── validate_bootstrap.py     # when executable validator is materialized
```

Only materialize files required for the current experiment; do not fabricate content to fill the tree.

## 5. Research discipline

Every research claim should record enough provenance to recover the source:

```text
source
source_type
publisher/maintainer
url/reference
access_date
version/date when applicable
claim supported
confidence
decision impact
```

Prefer primary sources for technical claims.

Separate:

```text
SOURCE FACT
INTERPRETATION
HYPOTHESIS
DECISION
EVIDENCE
```

## 6. Session startup cycle

Before substantive work:

```text
1. load canonical rules
2. resolve actor/session/authority
3. inspect child outboxes when this actor supervises children
4. inspect own inbox
5. reconcile state
6. update/confirm plan
7. delegate when needed
8. execute own research/work
```

## 7. Work closure cycle

```text
1. materialize findings/evidence
2. commit only the coherent work unit
3. inspect child outboxes again when applicable
4. reconcile new information
5. emit superior-facing information through own outbox when needed
6. update cognition/state/handoff
7. commit closure artifacts if changed
```

The exact communication semantics belong to InterMembers when promoted.

## 8. Research outputs

At minimum, a completed AI research cycle should be able to answer:

```text
What was asked?
What was searched?
Which sources were authoritative?
Which candidates were found?
What evidence supports each comparison?
What remains unknown?
What decision is recommended?
What would falsify that recommendation?
What is the next action?
```

## 9. Promotion from research to implementation

`AI_RESEARCH` does not automatically authorize product implementation.

Research may produce:

```text
ADOPT
CONFIGURE
ADAPT
COMPOSE
BUILD_RESIDUAL_CANDIDATE
DEFER
DON'T_GO
```

A domain-specific protocol decides whether implementation is authorized.

## 10. First dogfood specimen

The first intended instance of this profile is:

```text
appLaboware/start-repo-ia-research
```

Mission:

Research the best available ways to create, update, validate and operate repository scaffolds for AI-assisted projects, comparing existing scaffolders and repository-template mechanisms before recommending what FlowED should adopt, compose, adapt or build as residual.

The specimen must feed findings back to the RBP instead of silently changing the protocol.
