# Science Frontier Discovery Gate

Status: **research method — not protocol runtime**

Purpose: define the minimum discovery discipline required before MyTrues claims
that an original decision mechanism expands the scientific/engineering frontier.

## Historical source

This gate is directly descended from the Google Drive artifact:

`MYTRUES-DISCOVERY-001 — EXTERNAL LLM EXECUTION CONTRACT`

Preserved at:

`docs/archaeology/drive/2026-09-mytrues-discovery-001.md`

The historical contract is evidence of methodology evolution, not proof of
scientific novelty.

## Governing rule

Before an original MyTrues Decision Engine is authorized:

`ADOPT -> PERSONALIZE -> FORK -> INSPIRE -> INVENT`

must be interpreted scientifically as:

`discover design space -> reproduce OPEN baselines -> parameterize differences
-> preserve contradictions -> benchmark -> isolate residual gap -> test candidate`

No candidate crosses this gate merely because it is different.

## Required discovery properties

The discovery phase MUST:

1. cover historical and contemporary approaches;
2. include independent scientific traditions rather than one fashionable family;
3. distinguish empirical, formal, cognitive-model, engineering and analogy claims;
4. prefer primary/authoritative sources and use surveys for synthesis;
5. extract mechanisms, variables, parameter domains and constraints;
6. preserve incompatible variants rather than harmonizing them prematurely;
7. preserve contradictory findings;
8. identify reproducible benchmarks/tasks and known baselines;
9. avoid guessed numeric ranges;
10. remain architecture-neutral until the design space has been mapped;
11. produce machine-readable evidence/provenance sufficient for deterministic
    experiment generation.

## Decision-specific baseline families

For an original decision engine, the minimum candidate baseline families include,
when applicable:

- formal decision tables / DMN;
- MCDA/MCDM and utility/value models;
- Bayesian decision models / influence diagrams;
- Case-Based Reasoning;
- rule/production systems;
- belief revision / truth-maintenance approaches;
- argumentation and defeasible reasoning;
- preference elicitation / preference learning;
- conditional preference models;
- retrieval-based decision support;
- calibration and abstention/reject-option methods;
- human/expert elicitation;
- outcome-feedback learning;
- causal decision methods where the task actually requires causality.

This list is a floor, not a claim that every family is relevant to every task.

## Decision Policy Profile gate

A portable decision-preference/profile layer is allowed as an OPEN protocol
candidate, but its semantics must be separated from any specific engine.

The discovery must distinguish at least:

- case-specific criteria;
- persistent provider/authority preferences;
- hard constraints;
- trade-off preferences;
- risk/uncertainty attitude;
- temporal/support-horizon preference;
- reversibility preference;
- evidence threshold;
- abstention policy;
- profile-update/learning policy.

A single observed decision MUST NOT silently become a durable preference.

Profile updates should be explicit/versioned decisions with provenance.

## Original-engine admission test

A candidate original engine may enter experimental implementation only when:

- OPEN baselines for the relevant task are executable;
- the benchmark/corpus is frozen and scoring is defined;
- the claimed residual gap is stated without marketing language;
- the candidate can be compared using the same inputs and outputs;
- ablations can identify which original mechanisms produce any gain;
- decision reproducibility records the engine version, profile version, evidence
  snapshot and context;
- negative results are retained.

## Publication boundary

If an algorithm is claimed as a scientific contribution, enough of the method
must be published for independent reproduction.

Commercial implementations may retain operational optimization, scale/tuning
infrastructure and private provider data, but they cannot substitute secrecy for
scientific reproducibility.

## Current state

MyTrues v0.2 does **not** claim an original decision algorithm.

It provides an open decision protocol/reference behavior and therefore remains a
valid baseline/client surface while this gate is being investigated.
