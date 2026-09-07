# Repository Seed

Status: `INCUBATION / DOGFOODING`

## Purpose

Materialize the minimum repository state required by the current stage, based on an approved repository design.

This stage is generic. It must not mention or require future internal products unless the current task genuinely depends on them.

## Inputs

- approved repository plan;
- project identity;
- known facts;
- unknowns;
- current stage;
- current human authority;
- current AI/runtime needs, if any;
- applicable repository profile.

## Materialization principles

```text
CREATE WHEN REQUIRED BY CURRENT STAGE OR PROFILE
PRESERVE USER-OWNED CONTENT
UNKNOWN REMAINS UNKNOWN
NO FUTURE TOOL LEAKAGE WITHOUT OPERATIONAL NEED
```

## Generic AI-ready seed

When an external AI must work on the repository before a durable local session system exists, materialize only the minimum self-describing context needed for that work. Candidate artifacts include:

- `MISSION.md`;
- `CURRENT-STATE.md`;
- `DECISIONS.md` or a structured decision log;
- `HANDOFF.md`;
- `INBOX/` and `OUTBOX/` only when the adopted communication protocol requires them;
- evidence/source pointers;
- stop/escalation conditions;
- current output contract.

The receiving AI must not be told about a future framework merely because that framework may later adopt or normalize the repository.

## New-project seed

For a newly materialized repository, defer to the active Repository Bootstrap Protocol/profile for canonical files, manifests, rules, gateways and validation.

## Existing-repository seed

For a repository that already exists:

1. inspect before writing;
2. preserve existing user-owned content;
3. add only missing minimum context;
4. never overwrite silently;
5. record provenance of every materialized artifact;
6. stop on ownership conflict.

## Completion

The seed succeeds when a new human or AI actor can understand the current mission, authority, state, demand, evidence and expected output without relying on private memory from the conversation that created the seed.
