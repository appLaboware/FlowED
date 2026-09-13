# FlowDisP — FlowED Discovery Protocol (POC)

**Version:** 0.1.0-poc  
**Status:** executable proof of concept; not a novelty claim and not yet a canonical FlowED standard.

FlowDisP is a protocol for answering a deceptively simple question before a team claims novelty or starts building:

> **What already exists, how close is it to the proposal, where is the boundary of the existing domain, and what residual—if any—remains?**

The protocol works for different discovery objects, including product/capability ideas, academic/conceptual claims, methods/protocols, architectural patterns and standards/specifications.

## Core rule

FlowDisP does **not** ask a researcher to judge whether an idea is good, whether code is elegant, or whether a product should be built.

It asks a bounded researcher to test a **claim about a dimension**, under an explicit **decision context** and **refutation condition**.

```text
proposal
→ claim
→ dimension
→ refutation condition
→ antecedent search
→ match classification
→ boundary
→ residual
→ owner convergence review
→ disposition / handoff
```

## Roles

- **Discovery Owner (DO):** owns the case, defines the claim, asks follow-ups, commissions replication, reads raw research conversations, integrates evidence and decides when the research is sufficient for the decision.
- **ABR — Atomic Boundary Researcher:** investigates one tightly scoped claim. ABR does not implement, does not perform general code review, does not decide product strategy, and does not edit downstream manifesto/specification text.

See `roles/`.

## Research is iterative

An ABR is not necessarily one-shot. The DO may ask successive rounds until the case reaches operational saturation. If disagreement remains, that is preserved as `CONTESTED` or `UNRESOLVED`; agreement is not mandatory.

A second ABR may be launched for independent replication.

## Raw source is mandatory

The final report is a projection, not the whole research path. The DO should receive and inspect the **raw conversation** used to produce it, typically as `.html`, `.md`, or `.txt`, plus the evidence/search trail.

Raw files are never overwritten by normalized views.

## Quick start

Create a case:

```bash
python scripts/fldp.py new-case \
  --id FDP-AR-001 \
  --mode product \
  --claim "A universal API description can generate a ready-to-use interface automatically." \
  --dimension capability \
  --decision-context "Decide whether a new product is justified." \
  --refutation-condition "A public prior implementation that substantially performs this capability is enough to refute capability-level novelty."
```

Add a researcher round:

```bash
python scripts/fldp.py add-researcher --case cases/FDP-AR-001 --actor ABR-001
```

Normalize a raw HTML/TXT/MD source without replacing it:

```bash
python scripts/fldp.py normalize --input conversation.html --output conversation.normalized.txt
```

Validate the case package:

```bash
python scripts/fldp.py validate --case cases/FDP-AR-001
```

Create a ZIP of the case:

```bash
python scripts/fldp.py pack --case cases/FDP-AR-001
```

## What counts as refutation depends on the claim

A public prototype on GitHub may be sufficient to refute **capability novelty**, even if the code is poor, abandoned or commercially unusable. It does **not** automatically prove production readiness, adoptability, architectural equivalence or commercial equivalence.

Likewise, in academic mode, absence of the same name is not absence of the same concept. The ABR must search semantic equivalents and neighboring domains.

## Case output

A mature case should contain, at minimum:

```text
case.json
RAW/
NORMALIZED/
RESEARCH/
EVIDENCE/
OWNER/
HANDOFF/
```

The final downstream artifact is `HANDOFF/APPROVED-EVIDENCE-PACK.md`. MAN/WRK/product teams should consume that frozen projection rather than an unfinished research conversation.

## Start here

1. Read `PROTOCOL.md`.
2. Read `roles/DISCOVERY-OWNER.md` and `roles/ABR.md`.
3. Select a mode from `docs/MODES.md`.
4. Create a case with `scripts/fldp.py`.
5. Generate an ABR prompt from `prompts/ABR-LAUNCH.md`.
6. Preserve the raw conversation and research outputs.
7. Use `prompts/OWNER-REVIEW.md` for convergence review.
