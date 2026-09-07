# POC Governance Bridge v0.1

Status: `EXPERIMENTAL / GENERIC / UNVALIDATED`

## Purpose

Provide a minimum governance bridge for proofs of concept that are being executed outside InitProj, so useful evidence, decisions, exceptions and artifacts can later be adopted without losing provenance or contaminating product artifacts.

## Core rule

A POC may be lightweight, but it must not be memoryless.

A POC executed outside InitProj must preserve at least:

- purpose and hypothesis;
- scope and non-goals;
- current status;
- decisions and rejected alternatives;
- evidence produced;
- temporary exceptions;
- adopted external tools and their field evidence;
- known risks and unknowns;
- accepted direction;
- provenance sufficient for later migration or homologation.

## Minimal POC structure

```text
POC/
├── README.md
├── decisions/
├── evidence/
├── experiments/
├── exceptions/
├── backlog/
└── docs/
```

This structure is conceptual. Repositories may project it differently if ownership remains explicit.

## Gate — POC continuity

GO when:

- the POC objective is explicit;
- important decisions are traceable;
- experiments can be distinguished from accepted behavior;
- evidence is retained;
- rejected spikes are retained as learning evidence when material;
- product artifacts do not absorb planning/research noise;
- temporary exceptions are visible;
- later InitProj adoption can reconstruct why the POC evolved as it did.

DON'T-GO when:

- the only record of rationale is chat memory;
- temporary code is indistinguishable from accepted code;
- rejected experiments are silently deleted despite changing direction;
- external tools are adopted without field evidence;
- product documentation carries planning, research or process history;
- a later team cannot tell what is fact, decision, hypothesis, exception or experiment.

## External-tool field-study rule

When a POC adopts a tool, library, framework, generator, agent or external service, record:

1. domain problem;
2. candidate contract;
3. expected gain;
4. simplified real field test;
5. evidence;
6. failure modes;
7. outcome: `ADOPT | WRAP | ADAPT | FORK | REIMPLEMENT_CONCEPT | REJECT | MONITOR`;
8. monitoring policy if upstream evolution matters.

Adoption does not transfer domain authority to the adopted tool.

## Rejected-spike rule

A rejected spike is valid evidence when it:

- tests an explicit hypothesis;
- is isolated from accepted product behavior;
- produces a decision;
- records why it was rejected;
- records what risk or uncertainty it reduced;
- records the accepted next direction.

Rejected spikes must not remain as accidental production behavior.

## Documentation-boundary rule

Every durable POC document should have one dominant responsibility and one primary owner/layer.

Prefer:

- decision record for decisions;
- evidence record for observations/tests;
- experiment record for temporary exploration;
- exception record for deliberate deviations;
- product documentation only for product facts;
- research/planning notes outside product release artifacts.

## Engineering-compliance checkpoint

At material milestones, review whether the POC still demonstrates credible engineering rather than merely producing a demo.

Check, when applicable:

- value delivered;
- scope coherence;
- reuse/adoption before reinvention;
- architecture rationale;
- tests/validation appropriate to the phase;
- security/privacy appropriate to the phase;
- reproducibility;
- maintainability of accepted artifacts;
- explicit technical debt and exceptions.

A POC may deliberately defer production-grade qualities, but deferral must be visible rather than implicit.

## InitProj adoption bridge

When the POC later enters InitProj, migration must preserve rather than rewrite history.

Map at least:

```text
POC README / state      -> initial project/session context
POC decisions           -> decision history
POC evidence            -> evidence index
POC experiments         -> experiment/spike history
POC exceptions          -> explicit exception records
POC backlog             -> candidate backlog, not automatic commitment
POC docs                -> classify by sovereign destination before import
```

Import must not turn every historical artifact into current project authority.

## Provenance classes

Use at least:

```text
ORIGINATOR_STATEMENT
TEAM_DECISION
EXTERNAL_EVIDENCE
EXPERIMENTAL_EVIDENCE
REJECTED_PATH
TEMPORARY_EXCEPTION
ACCEPTED_PRODUCT_FACT
RESEARCH_HYPOTHESIS
```

## Final principle

The bridge exists to preserve enough engineering memory that a fast POC can later become a governed project without pretending that the governance existed retroactively.
