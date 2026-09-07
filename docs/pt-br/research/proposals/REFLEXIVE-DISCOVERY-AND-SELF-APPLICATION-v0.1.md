# Reflexive Discovery and Self-Application — research seed v0.1

Status: `RESEARCH SEED / PRIOR ART FOUND / NOVELTY NOT ESTABLISHED`

## Motivation

Project Genesis is currently being used to investigate Project Genesis itself. This is not merely ordinary product dogfooding because the findings of the investigation can modify the protocol and tool that produced those findings.

The research problem is therefore not simply "does dogfooding help?" but how to control an evidence-informed discovery process when object and instrument partially overlap and co-evolve.

## Prior art already identified

### Dogfooding / implicit testing

Dogfooding is established practice in software engineering: developers and organizations use their own software and may discover defects or requirements during ordinary use. Warren Harrison discussed benefits and limits of dogfooding in IEEE Software (2006), and later empirical work treats internal use as a form of implicit defect detection.

This means `use your own artifact` is not a novelty claim.

### Reflexive practice in design research

Yoram Reich's 2017 **Principle of Reflexive Practice (PRP)** is especially close conceptually. It argues that design researchers should apply design principles, methods, and tools to their own research practice, including a strong form in which researchers use their own tools on their own research to obtain early and rich feedback.

Therefore, `a method being used to help develop itself` is also established prior art.

### Meta-application / bootstrapping risk

Work on model-assisted software development reports a development cycle where a methodology and its supporting tool co-evolve through self-application. The reported benefits include a tight feedback loop, while explicitly acknowledging nested recursion and the risk of overfitting to the tool's own use cases.

This is a strong antecedent for the current concern that self-application can improve a method while also biasing it toward one privileged case.

## Current residual hypothesis

The potential research residual is narrower:

> How should an evidence-informed project-discovery protocol control provenance, circularity, version changes, re-analysis, overfitting, and rule promotion when the investigated artifact is also part of the instrument that performs and evolves the investigation?

This is only a hypothesis. A systematic mapping is still required.

## Candidate distinctions

The current Project Genesis case combines at least four known ideas:

```text
dogfooding
+
reflexive practice
+
bootstrapping / meta-application
+
evidence-informed project discovery
```

The possible residual may lie in the explicit governance of their intersection rather than in any one component.

Candidate mechanisms requiring prior-art investigation:

- evidence provenance classes distinguishing external and self-derived claims;
- anti-circularity constraints for self-confirming rules;
- explicit object-version / protocol-version / evidence-snapshot / result-version separation;
- dependency-scoped re-analysis after protocol evolution;
- promotion gates from self-dogfood rule to generic protocol rule;
- measurable control of self-case overfitting;
- convergence/stability criteria for co-evolving object and discovery instrument.

## Candidate research questions

- **RQ1:** How can self-derived evidence and independent evidence be represented and weighted without discarding useful self-application feedback?
- **RQ2:** When the discovery protocol changes, which previous conclusions must be re-opened?
- **RQ3:** Can dependency-scoped re-analysis avoid both full restart and stale conclusions?
- **RQ4:** How can circular self-validation be operationally detected?
- **RQ5:** How can overfitting of a protocol to its own dogfood case be detected before generalization?
- **RQ6:** Under what conditions do reflexively generated rules generalize to external cases?
- **RQ7:** Does the reflexive process converge toward a stable factorization/sourcing model, and how should stability be defined?

## Candidate empirical design

A future experiment could compare:

```text
A. protocol developed without self-application
B. protocol developed through self-application only
C. protocol developed through self-application + explicit reflexive overlay
D. protocol developed through self-application + overlay + external-case promotion gate
```

Potential measures:

- inter-case generalization;
- number of rules later reverted;
- unsupported claims;
- circular evidence incidents;
- stale-result incidents after protocol change;
- re-analysis cost;
- external-case decision quality;
- factorization stability;
- sourcing/reuse discovery yield.

No superiority hypothesis is authorized yet.

## Immediate engineering consequence

Project Genesis MUST treat `Project Genesis analyzes Project Genesis` as a special overlay case, not as the definition of generic discovery.

Rules discovered only in this self-case remain overlay-specific until they survive external cases.

## Prior-art references for next mapping

- Warren Harrison. *Eating Your Own Dog Food*. IEEE Software, 23(3), 2006. DOI: `10.1109/MS.2006.72`.
- Yoram Reich. *The principle of reflexive practice*. Design Science, 2017.
- Literature on implicit defect detection and internal product use in software engineering.
- Meta-application / bootstrapping studies in model-assisted software development, including explicit discussion of recursive self-use and overfitting risk.

## Claim boundary

At this stage we may claim:

- reflexive self-application is a real and recognized methodological pattern;
- dogfooding and reflexive practice provide substantial prior art;
- self-application can generate fast feedback but can introduce perspective and overfitting risks;
- Project Genesis needs additional controls because its self-case changes the instrument used for later analysis.

We may NOT claim:

- that Reflexive Discovery is a novel scientific principle;
- that the proposed overlay is validated;
- that the identified research residual is unique;
- that convergence necessarily occurs;
- that the proposed provenance or promotion rules are optimal.
