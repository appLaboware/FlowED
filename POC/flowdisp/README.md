# FlowDisP — FlowED Discovery Protocol (POC)

**Version:** 0.1.0-poc  
**Status:** experimental, portable POC  
**CLI candidate:** `FLDP` (`fldp.py`)  
**Purpose:** discover what materially relevant antecedents already exist for a bounded claim, where the existing frontier lies, and what residual—if any—remains.

FlowDisP is not code review and is not a novelty generator. It asks first:

> What already exists that is materially relevant to the claim we are making, and what does that evidence allow us to say?

The POC is portable. Copy this folder into any unrelated project.

## Roles

- **Discovery Owner (DO):** frames the case, asks follow-ups, requests independent replication, audits raw traces, and decides when evidence is sufficient. In FlowED this role can map to the active PO.
- **ABR — Atomic Boundary Researcher:** researches one bounded claim, gathers antecedents/evidence, compares them to the claim and reports limits. It does not decide product architecture, implementation or final novelty claims.
- **Human Operator:** transports prompts/files and exports raw conversations when needed; it need not manually summarize the research.

## Research unit

FlowDisP researches a **claim about a dimension**, not “the whole idea”.

A case defines: research object, exact claim, dimension, comparison unit, decision context, expected rigor, and a refutation/weakening condition.

## Modes

- `product` — products/capabilities, including public prototypes and repositories;
- `academic` — concepts, theories, methods, taxonomies and literature;
- `method` — protocols, standards, practices and workflows;
- `architecture` — architectural patterns, mechanisms and structures.

See `PROFILES.md`.

## Quick pilot

Requires Python 3.10+ and no external packages.

```bash
python fldp.py init ../my-case --mode product --case-id FDP-AR-001
```

Then:

1. fill `../my-case/CASE.md`;
2. ingest any raw HTML/MD/TXT or evidence you already have:

```bash
python fldp.py ingest ../my-case some-chat.html --kind input
python fldp.py ingest ../my-case notes.txt --kind input
```

3. edit `rounds/001/RESEARCHER-PROMPT.md`;
4. open a fresh researcher chat and paste the prompt;
5. iterate with the same ABR while useful; add another ABR for independent replication when needed;
6. save/export each complete researcher conversation and ingest it:

```bash
python fldp.py ingest ../my-case abr-001-round-01.html --kind chat
```

7. store downloaded evidence with `--kind evidence`;
8. complete each round report and Discovery Owner review;
9. create follow-up rounds:

```bash
python fldp.py new-round ../my-case --actor ABR-001
```

10. validate and package:

```bash
python fldp.py validate ../my-case
python fldp.py pack ../my-case
```

Return the whole generated case ZIP.

## Required return package

At minimum: `CASE.md`, all raw inputs, complete raw researcher conversation export(s) when available (`html`, `md`, `txt`), normalized views, each round's search trace/evidence ledger/report, Discovery Owner reviews, convergence review and final Evidence Pack.

A negative or unresolved result is valid. “Nothing sufficient was found” must never become “it does not exist”.

## Package files

- `FLOWDISP-PROTOCOL.md`
- `RESEARCHER-CONTRACT.md`
- `PROFILES.md`
- `PILOT.md`
- `fldp.py`
- `templates/`
- `tests/`

## Non-goals

This POC does not prove FlowDisP itself is novel, automate literature review, certify patent novelty, replace systematic reviews, or make final build/adopt/fork decisions automatically.
