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

**Prior-art requirement:** PPX (Preference Profile Exchange) 0.1-draft is direct
prior art and MUST be evaluated before MyTrues defines any portable preference
profile format.

Historical W3C CC/PP and related portable-profile work must also be included in
the lineage review.

The default research hypothesis is now:

`adopt PPX/profile prior art -> map to DecisionEngine semantics -> measure
semantic preservation/loss`

not:

`invent a new DecisionPolicyProfile interchange format`.

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


## External-run qualification gate

A Discovery package produced by an external model/provider does not qualify
itself merely by declaring its own gates as GO.

Before any external run contributes to the canonical design space, intake MUST
independently check at least:

- package checksum integrity;
- JSON/CSV parseability;
- required-file presence;
- unique IDs;
- source-reference integrity;
- manifest counts recomputed from payload;
- agreement between manifest and executive summaries;
- contradiction/open-question counts where declared;
- numeric-range provenance;
- candidate-source verification against primary/authoritative records.

A self-declared G7/MACHINE_READABILITY result is not evidence of parseability.

The Grok Discovery intake of 2026-10-01 is the first preserved negative example:
its checksums pass, but three required JSON files fail parsing and the manifest
counts disagree with the delivered mechanism/variable arrays.

See:

`external-runs/GROK-MYTRUES-COGNITIVE-DISCOVERY-001-QUALIFICATION.md`

## Metaobjective on record: MyTrues applied to MyTrues

The preserved `MTR-METAOBJECTIVE-001` proposes a long-range research loop in
which MyTrues records architecture experiments as:

```text
context
+ configuration
+ question set
-> observed consequence
```

Its recurring shorthand is `SQLDAVELHA`: accumulated experience may replace
repeated uncertain reasoning where prior situations/consequences have become
queryable.

This is a research hypothesis, not a production architecture.

The same document proposes a strict experimental boundary:

- LLMs may interpret language and propose candidate relations;
- candidate relations are not canonical relations;
- deterministic/registered evidence determines epistemic state;
- an LLM renderer may change representation, not what the system is authorized
  to claim.

## Microbrain proposal boundary

`MYTRUES-META-PROPOSAL-001` proposes a future controlled
`MYTRUES-MICROBRAIN-V0` before architecture selection.

The package is preserved as a proposal only.

No implementation is authorized until the PO explicitly promotes it.

If promoted later, it should remain an experimental measurement instrument and
must not be treated as the final ontology, final storage architecture, or proof
of novelty.


## Cross-engine profile semantics gate

A possible scientific residual remains only if portable preference/profile prior
art does not already solve the **execution semantics** across heterogeneous
decision engines.

Any claim here MUST compare at least multiple engine families, for example:

- rule/DMN;
- policy/OPA;
- MCDA/value models;
- CBR;
- preference/conditional-preference engines;
- learned or hybrid engines.

The experiment must record:

- portable source profile/version;
- engine + adapter version;
- mapping/transformation rules;
- unsupported profile claims;
- decision context/evidence;
- result;
- provenance;
- divergence from other engines;
- replay result.

Candidate metrics include:

- semantic coverage;
- mapping loss;
- constraint violations;
- preference adherence;
- cross-engine behavioral agreement where equivalence is expected;
- explainable divergence where engine semantics differ;
- temporal replay accuracy.

A useful result may be that no universal cross-engine semantic mapping is
possible. Negative results are valid frontier evidence.


## Experience-first branch gate

A batch-002 conversation reconstruction introduces a broader research branch in
which `Experience` is the primary conceptual unit and Decision is one derived
epistemic/operational object.

This branch MUST NOT silently redefine the current MyTrues Open Decision
Protocol.

Before any promotion, perform two separate gates.

### Gate A — provenance / PO intent — RESOLVED

The original chat was forensically audited.

Result:

- `Experience` as primary MyTrues unit — **not explicitly PO-approved**;
- `MyTrues is the SQL of experience` — **not explicitly PO-approved**;
- decision memory superseded by broader experiential memory — **NO**;
- user-owned memory replacing provider-scoped memory — **NO**.

The PO did explicitly approve a broader experimental/metaobjective direction:
organized memories + deterministic Systematic Agent + registration/linking
component + LLM-assisted candidate linking/language.

That approval was immediately scoped as **metaobjective / experiment**, not
product redefinition or implementation demand.

See:

`../docs/archaeology/forensics/EXPERIENCE-FIRST-CHAT-FORENSIC-001.md`.

### Gate B — prior art / science — CONDITIONAL

Gate A did **not** establish Experience-first as a product/domain pivot.

Therefore this gate applies only if the PO later promotes the experimental
metaobjective or one of its mechanisms for scientific investigation.

If promoted, compare it against at least:

- Case-Based Reasoning and case retention/reuse;
- episodic/semantic agent memory;
- Truth Maintenance / Assumption-Based TMS;
- AGM/belief revision;
- defeasible and structured argumentation;
- temporal/provenance models;
- planning/search experience reuse;
- knowledge compilation / memoization;
- automated algorithm configuration;
- cognitive architectures and spreading activation where relevant.

Candidate research questions include:

- whether defeated paths reduce repeated deliberation under context equivalence;
- how to represent `KNOWN / CONSIDERED / INFLUENCED` without causal overclaim;
- how to preserve current and historical positions under AS-KNOWN-THEN;
- whether provider-replaceable user-owned memory can preserve authority and
  isolation simultaneously;
- whether retrieval/activation can be cleanly separated from epistemic support;
- whether a Decision Cell adds measurable value over established design-rationale
  and provenance representations.

No novelty claim follows merely from naming these concepts.
