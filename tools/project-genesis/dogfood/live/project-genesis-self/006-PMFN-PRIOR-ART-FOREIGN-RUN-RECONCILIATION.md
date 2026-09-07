# Run 006 — PMFN Prior-Art Foreign Run Reconciliation

Status: `INGESTED / PARTIALLY VERIFIED / NON-AUTHORITATIVE SOURCE`
Date: 2026-09-07
Subject: `Project Genesis / PMFN`
Origin: external parallel team package `DOGFOOD-002-PMFN-prior-art.zip`

## 1. Why this artifact exists

A parallel team produced a second PMFN prior-art study before the current Project Genesis protocol and domain placement were stabilized.

The package MUST NOT be imported directly into the repository topology proposed by that team.

It is treated as:

```text
FOREIGN PARALLEL INVESTIGATION
        ↓
ATOM-BY-ATOM RECONCILIATION
        ↓
verified evidence + hypotheses + rejected authority
```

This is a real dogfood case for the foreign-artifact ingestion rule and for the Reflexive Discovery overlay.

## 2. Phase-order caveat

The current Project Genesis process now requires protected Phase 01 understanding before viability/prior-art analysis.

This foreign run was produced before that correction.

Therefore:

- it is useful as evidence;
- it is NOT proof that the future canonical process may skip Phase 01;
- its conclusions must be rechecked after the Phase 01 idea record is homologated;
- no downstream materialization is authorized by this artifact.

## 3. Package findings worth preserving

The following findings materially improve the current research position.

### F-006-01 — Generic decomposition stopping criteria already have direct prior art

The package identified Park et al. (2026), `When to Stop Decomposing: LLM-Assisted Quality Gates for Functional Decomposition in Systems Engineering`, IEEE Access, DOI `10.1109/ACCESS.2026.3683195`.

Independent verification on 2026-09-07 confirmed the publication, DOI, IEEE Access venue, LLM-assisted gate workflow and explicit stopping criteria based on FR → DP → IM mappings.

Consequence:

> PMFN MUST NOT claim novelty for the generic question `when to stop decomposing`.

Classification: `ADOPT / BOUNDARY-CONSTRAINING PRIOR ART`.

### F-006-02 — Software sourcing is already a mature multi-option decision space

The package identified Badampudi, Wohlin and Petersen (2016), DOI `10.1016/j.jss.2016.07.027`.

Independent verification confirmed that the systematic literature review treats component origins including:

- in-house;
- OSS;
- COTS;
- outsourcing;

and explicitly identifies the need to support combinations of origins.

Consequence:

> Project Genesis should adopt established sourcing concepts instead of inventing a private make/buy taxonomy.

Classification: `ADOPT`.

### F-006-03 — Industrial sourcing decisions already include broader make-or-buy alternatives

The package identified Borg et al. (2019), DOI `10.1016/j.infsof.2019.03.015`.

Independent verification confirmed the industrial survey and the four sourcing alternatives. The study supports the view that sourcing is multi-option and decision-support oriented rather than a trivial binary choice.

Classification: `ADOPT / ADAPT`.

### F-006-04 — Optimal COTS combinations are not a new contribution

The package identified Cortellessa et al. (2007), DOI `10.1145/1321631.1321697`.

Independent verification confirmed a requirements-phase framework that selects combinations of COTS components through optimization while satisfying system requirements and minimizing cost.

Consequence:

> `select or combine existing components optimally` cannot be claimed as PMFN novelty.

Classification: `ADOPT AS PRIOR ART`.

### F-006-05 — Opportunistic reuse and composition of independently developed assets are established

The package identified Mäkitalo et al. (2020), DOI `10.1007/s00607-020-00833-6`.

Independent verification confirmed that the paper studies software built by reusing and combining independently developed assets.

Consequence:

> `COMPOSE` is not itself a novelty claim and should remain an architectural relation rather than a presumed ordinal rung.

Classification: `ADOPT`.

### F-006-06 — Requirements/architecture granularity already has dedicated methods

The package identified the RE4SA work, DOI `10.1016/j.infsof.2021.106535`.

Independent verification confirmed that it addresses alignment and granularity between requirements and software architecture.

Classification: `ADAPT / INVESTIGATE FOR REPRESENTATION`.

### F-006-07 — External innovation sourcing is established innovation-management territory

The package identified West and Bogers (2014), DOI `10.1111/jpim.12125`.

Independent verification confirmed a review of external sources of innovation and an inbound process involving obtaining, integrating and commercializing external innovations.

Classification: `ADOPT AS BACKGROUND`.

## 4. Findings retained as hypotheses, not yet promoted

The package also contains useful but not yet sufficiently verified or generalized claims around:

- technology-scouting products;
- evidence-based idea-validation products;
- commercial product boundaries;
- execution exclusivity as a distinct operational construct;
- neutral Project Position Profile as a novel artifact;
- longitudinal project genealogy as a product/research residual.

These remain `INVESTIGATE`.

## 5. Findings NOT imported as authority

The following are explicitly rejected as authority-bearing decisions from the foreign package:

- destination under InitProj;
- `tools/project-discovery/` sovereignty;
- any direct import instruction targeting InitProj;
- any naming or downstream-tool boundary declared by the package;
- `MNI` as canonical operational metric;
- a single ordinal `ADOPT → CONFIGURE → EXTEND → ADAPT → COMPOSE → INVENT` ontology;
- any novelty conclusion based only on exploratory search.

Current sovereign location remains:

```text
appLaboware/FlowED
└── tools/project-genesis/
```

## 6. PMFN correction produced by this run

Before this prior-art confrontation, PMFN risked being interpreted as two overlapping claims:

```text
A. minimize proprietary construction
B. know when to stop decomposing
```

The evidence forces a narrower formulation.

Generic decomposition stopping is already directly addressed in prior art.

The surviving PMFN research question is more specific:

> At what coarsest decision-sufficient factorization does further decomposition cease to materially change evidence-backed sourcing, transformation, composition, differentiation, risk or uncertainty decisions during early software-project discovery?

This is a research hypothesis, not a novelty claim.

## 7. Safer operational distinction

The package used `residual invention` in several places.

Current Project Genesis semantics use `FR — Residual Factorization` because:

```text
no admissible existing realization found
        ≠
world novelty demonstrated
```

Therefore:

- `FR` remains the operational measure;
- `MNI` / residual invention may remain a research construct only after explicit evidence shows invention rather than merely owned implementation is involved.

## 8. Revised realization representation

The foreign run reinforces the decision not to use a single ladder as canonical ontology.

Current candidate representation remains multidimensional:

```yaml
provenance: existing | modified | invented | unknown
transformation: none | configure | extend | adapt | unknown
architecture: direct | compose | reconfigure | unknown
source: OSS | COTS | service | standard | internal | outsourced | unknown
```

The source dimension should be reconciled with established component-origin literature rather than independently invented.

## 9. New protocol rules discovered

### PR-006-01 — Prior-art collision narrows the claim, not the project automatically

Finding antecedent work invalidates or narrows the overlapping contribution claim. It does not automatically issue a project GO/NO-GO decision.

### PR-006-02 — Generic method prior art must be adopted before specialized residual is formulated

If a mature method already solves the generic problem, Project Genesis must treat it as substrate or comparator and formulate only the still-uncovered decision target.

### PR-006-03 — Citation existence is not enough

Before a prior-art item changes protocol authority, minimally verify:

```text
identity
venue/source
DOI or canonical reference
direct relevance to the claim being changed
```

### PR-006-04 — Foreign research may inform but may not reorder the canonical pipeline

A useful study produced out of phase can be ingested as evidence without legitimizing its process order.

### PR-006-05 — Prior-art evidence must distinguish `known mechanism` from `candidate residual`

Every research claim should be classifiable as:

```text
KNOWN / ADOPT
ADJACENT / ADAPT
COMPOSABLE
RESIDUAL HYPOTHESIS
UNKNOWN
```

### PR-006-06 — Self-derived residuals require external challenge

Because this run investigates PMFN with PMFN-related reasoning, any claimed residual remains under the Reflexive Discovery overlay until tested against external projects and systematic prior-art procedures.

## 10. Implementation requirements discovered

### IR-010 — Prior-art collision register

The tool should record which original claim is narrowed, superseded or preserved by each prior-art item.

### IR-011 — Evidence verification state

Each source needs a verification state such as:

```text
DISCOVERED
IDENTITY_VERIFIED
CLAIM_VERIFIED
CONTRADICTED
UNRESOLVED
```

### IR-012 — Research residual ledger

The tool should maintain a live ledger separating:

```text
known/adopted substrate
adjacent prior art
candidate residual
falsified residual
open uncertainty
```

### IR-013 — Out-of-order artifact quarantine

Useful evidence produced before its canonical phase must be ingestible without changing the authorized stage or materialization state.

## 11. Current position after Run 006

```text
GENERIC DECOMPOSITION STOPPING       = KNOWN PRIOR ART
MULTI-OPTION COMPONENT SOURCING      = KNOWN PRIOR ART
COTS COMBINATION/SELECTION           = KNOWN PRIOR ART
SOFTWARE REUSE / COMPOSITION         = KNOWN PRIOR ART
REQUIREMENT/ARCHITECTURE GRANULARITY = KNOWN/ADJACENT PRIOR ART

PMFN DISCOVERY-SPECIFIC STOP TARGET  = RESIDUAL HYPOTHESIS
EVIDENCE-AWARE FACTOR REALIZATION    = RESIDUAL HYPOTHESIS
NEUTRAL POSITION PROFILE             = RESIDUAL HYPOTHESIS
LONGITUDINAL GENEALOGY/HANDOFF       = RESIDUAL HYPOTHESIS
NOVELTY CLAIM                         = NOT AUTHORIZED
```

## 12. What this dogfood proves about the process

This run does not prove PMFN is new.

It proves that the protocol must be able to accept a parallel investigator's artifact, extract useful evidence, reject misplaced authority, verify critical collisions, narrow its own hypothesis, and preserve the phase boundary.

That is itself useful implementation evidence for Project Genesis.
