<!--
DRIVE ARCHAEOLOGY COPY — NOT NORMATIVE
Source Drive file ID: 17lLtdsAMckjqnaVZumeogKHzoO8gml1_
Source title: MYTRUES-DISCOVERY-001-EXTERNAL-LLM-PROMPT.md
Source URL: https://drive.google.com/file/d/17lLtdsAMckjqnaVZumeogKHzoO8gml1_/view?usp=drivesdk
Copied on: 2026-10-01
Purpose: preserve MyTrues/EDT/CCP lineage before canonical consolidation.
-->

# MYTRUES-DISCOVERY-001 — EXTERNAL LLM EXECUTION CONTRACT

## 0. EXECUTION MODE

You are executing a **bounded scientific discovery task** for the MyTrues research program.

This file is the complete execution contract.

Follow it literally.

Do not reinterpret the mission.
Do not reduce the scope.
Do not select a preferred architecture.
Do not produce a prose-only answer.
Do not return only recommendations.
Do not stop after finding a plausible solution.
Do not optimize for brevity.

Your output MUST be a single ZIP file as defined in this contract.

If any mandatory gate cannot be satisfied, you MUST still produce the ZIP, but mark the run as `DONT_GO` and document exactly why.

---

# 1. MISSION

The mission is:

> **Discover, enumerate, structure, source, and parameterize the broadest defensible design space known to science and engineering for building a highly relational cognitive memory/knowledge system capable of deep vertical reasoning, broad horizontal association, and transversal reuse of knowledge.**

The target is NOT to decide what is best.

The target is NOT to design MyTrues.

The target is NOT to consolidate theories into one model.

The target is NOT to imitate the human brain biologically.

The target is:

> **to discover everything that may vary in a future experimentally testable cognitive architecture.**

The final product of this discovery must be a **machine-readable experimental design space** containing mechanisms, models, architectures, variables, parameter domains, compatibility relationships, incompatibilities, assumptions, constraints, evidence, benchmarks, unresolved questions, and provenance.

---

# 2. SCIENTIFIC SCOPE

Search as broadly as necessary across the historical and current scientific record.

At minimum investigate relevant knowledge from:

- cognitive science;
- cognitive psychology;
- neuroscience;
- computational neuroscience;
- artificial intelligence;
- symbolic AI;
- subsymbolic AI;
- connectionism;
- hybrid cognitive architectures;
- knowledge representation;
- semantic memory;
- episodic memory;
- procedural memory;
- working memory;
- associative memory;
- memory consolidation;
- forgetting;
- interference;
- retrieval;
- attention;
- spreading activation;
- semantic networks;
- concept networks;
- graph-based cognition;
- knowledge graphs;
- temporal knowledge graphs;
- case-based reasoning;
- analogical reasoning;
- rule systems;
- production systems;
- logic-based reasoning;
- probabilistic reasoning;
- Bayesian cognition;
- predictive processing;
- active inference;
- reinforcement learning;
- decision theory;
- influence diagrams;
- belief revision;
- truth maintenance systems;
- assumption-based truth maintenance systems;
- defeasible reasoning;
- argumentation frameworks;
- bipolar argumentation;
- value-based argumentation;
- causal representation;
- provenance;
- temporal reasoning;
- contextual reasoning;
- cognitive control;
- metacognition;
- memory indexing;
- information retrieval;
- vector retrieval;
- hybrid retrieval;
- graph traversal;
- spreading activation algorithms;
- graph centrality;
- PageRank-like retrieval;
- Hebbian learning;
- associative plasticity;
- chunking;
- rehearsal;
- salience;
- recency/frequency effects;
- priming;
- activation decay;
- retrieval inhibition;
- memory reconsolidation;
- cognitive architectures;
- agent memory;
- lifelong learning;
- continual learning;
- retrieval-augmented systems;
- agentic memory;
- reasoning traces;
- decision journals;
- design rationale;
- argument mining;
- dialogue modeling;
- scientific knowledge graphs;
- machine-readable literature synthesis.

This list is a minimum, not a maximum.

---

# 3. REQUIRED HISTORICAL COVERAGE

The discovery MUST include both historical and modern approaches.

Do not only search recent LLM literature.

At minimum include, where scientifically relevant:

- classical cognitive theories;
- early symbolic AI;
- semantic network research;
- spreading activation;
- production systems;
- cognitive architectures;
- connectionist models;
- case-based reasoning;
- truth maintenance;
- belief revision;
- argumentation theory;
- probabilistic cognitive models;
- modern neural retrieval;
- knowledge graphs;
- agent memory;
- temporal memory;
- LLM-era memory systems.

Historical approaches MUST NOT be discarded merely because they are old.

Modern approaches MUST NOT be privileged merely because they are recent.

Every approach is a candidate variable source until experimentally excluded.

---

# 4. SCIENTIFIC SOURCE POLICY

## 4.1 Source priority

Use sources in this priority order:

1. peer-reviewed journal articles;
2. peer-reviewed conference papers;
3. scholarly books from recognized academic publishers;
4. standards/specifications from recognized standards bodies;
5. official documentation for technologies/frameworks;
6. authoritative university/research-lab publications;
7. high-quality preprints when peer-reviewed sources are unavailable;
8. technical reports from recognized research institutions;
9. implementation repositories only for implementation-specific facts;
10. secondary sources only for navigation or historical orientation.

Do not use blogs, marketing pages, SEO pages, forum posts, or unsourced summaries as scientific authority.

They may be used only as discovery leads.

---

## 4.2 Primary-source preference

For every important theory, model, mechanism, architecture, or algorithm:

- prefer the original paper when identifiable;
- also include one or more later authoritative surveys/reviews when available;
- distinguish original claim from later interpretation.

---

## 4.3 Review and survey requirement

For each major family of approaches, attempt to find:

- at least one primary/original source;
- at least one review, survey, or comparative study;
- at least one empirical or benchmark study when applicable.

If one of these does not exist or cannot be found, mark it explicitly.

---

## 4.4 Evidence classification

Every relevant claim MUST be classified as one of:

- `EMPIRICAL_HUMAN`
- `EMPIRICAL_ANIMAL`
- `EMPIRICAL_COMPUTATIONAL`
- `FORMAL_THEORETICAL`
- `COGNITIVE_MODEL`
- `NEUROBIOLOGICAL_MODEL`
- `ENGINEERING_TECHNIQUE`
- `STANDARD_SPECIFICATION`
- `IMPLEMENTATION_FACT`
- `SURVEY_CONCLUSION`
- `HYPOTHESIS`
- `ANALOGY`
- `UNSOURCED_CANDIDATE`

Never collapse these categories.

A biological analogy is not an engineering fact.
A computational model is not proof of human cognition.
A useful algorithm is not proof that the brain implements it.

---

# 5. ANTI-HALLUCINATION RULES

You MUST NOT invent:

- papers;
- authors;
- DOIs;
- publication years;
- experiments;
- benchmarks;
- parameter ranges;
- algorithm names;
- standards;
- repositories;
- empirical findings.

If uncertain, mark:

`UNVERIFIED`

If no defensible source is found, mark:

`UNSOURCED_CANDIDATE`

Do not fabricate a citation to avoid an empty field.

---

# 6. RESEARCH QUESTION

The controlling question is:

> **What mechanisms, models, representations, variables, parameters, constraints, interactions, and experimentally testable combinations have been proposed, observed, modeled, or engineered across the scientific history of cognition and intelligent memory that may contribute to a relational cognitive system with vertical depth, horizontal association, transversal reuse, temporal evolution, context sensitivity, and evidence-grounded revision?**

Do not answer this with a recommendation.

Convert the answer into a design space.

---

# 7. REQUIRED OUTPUT CONCEPTS

The discovery MUST distinguish at least the following object types:

- `THEORY`
- `COGNITIVE_MECHANISM`
- `COMPUTATIONAL_MECHANISM`
- `MODEL`
- `ARCHITECTURE`
- `REPRESENTATION`
- `MEMORY_TYPE`
- `RETRIEVAL_METHOD`
- `ASSOCIATION_METHOD`
- `ACTIVATION_METHOD`
- `LEARNING_METHOD`
- `REVISION_METHOD`
- `DECISION_METHOD`
- `CONTEXT_METHOD`
- `TEMPORAL_METHOD`
- `FORGETTING_METHOD`
- `ATTENTION_METHOD`
- `PROVENANCE_METHOD`
- `ARGUMENTATION_METHOD`
- `REASONING_METHOD`
- `INDEXING_METHOD`
- `SIMILARITY_METHOD`
- `GRAPH_METHOD`
- `VECTOR_METHOD`
- `HYBRID_METHOD`
- `BENCHMARK`
- `METRIC`
- `DATASET`
- `OPEN_PROBLEM`
- `VARIABLE`
- `PARAMETER`
- `CONSTRAINT`
- `COMPATIBILITY`
- `INCOMPATIBILITY`
- `ASSUMPTION`

You may add additional types, but may not remove these from consideration.

---

# 8. VARIABLE EXTRACTION CONTRACT

For every discovered mechanism/model/architecture, extract all experimentally meaningful variables you can defend.

Examples:

- activation depth;
- activation decay;
- propagation function;
- edge weighting;
- edge directionality;
- fan-out;
- retrieval threshold;
- top-k;
- similarity metric;
- embedding strategy;
- vector dimensionality;
- graph traversal depth;
- temporal decay;
- recency weighting;
- frequency weighting;
- salience weighting;
- evidence weighting;
- confidence representation;
- context filtering;
- context scoring;
- assumption-set handling;
- memory consolidation schedule;
- forgetting policy;
- revision policy;
- contradiction handling;
- supersession handling;
- defeater handling;
- retrieval fusion;
- reranking;
- decision policy;
- utility function;
- argument acceptance semantics;
- activation initialization;
- activation normalization;
- working-memory capacity;
- chunk size;
- episodic granularity;
- case granularity;
- graph granularity;
- temporal resolution;
- provenance granularity;
- learning rate;
- retention threshold.

For each variable, record:

- unique ID;
- canonical name;
- aliases;
- parent mechanism;
- definition;
- type;
- allowed values or known range;
- units if applicable;
- default values reported in literature if any;
- observed/tested values;
- whether the range is theoretical, empirical, implementation-specific, or unknown;
- dependencies;
- incompatibilities;
- source IDs;
- confidence in extraction.

Never invent a numeric range.

If literature uses multiple incompatible ranges, preserve all of them as separate sourced observations.

---

# 9. COMBINATION-FIRST RULE

Whenever two papers, models, architectures, or implementations vary the same mechanism in different ways:

DO NOT reconcile them.

Instead:

1. create separate variants;
2. identify the differing dimensions;
3. turn those differences into variables or constraints;
4. preserve provenance.

Example:

If two spreading-activation models differ in decay:

DO NOT write:

`spreading activation uses decay`

Write:

- Variant A: no decay;
- Variant B: linear decay;
- Variant C: exponential decay;
- Variant D: learned decay;
- source for each;
- parameterization for each;
- compatibility constraints.

The purpose is to maximize future experimental combinations.

---

# 10. CONTRADICTION PRESERVATION RULE

Contradictions are valuable.

If sources disagree:

- preserve both claims;
- identify the disagreement;
- attach source IDs;
- classify disagreement type;
- do not choose a winner unless one claim is clearly retracted or invalidated by authoritative evidence;
- even then preserve historical lineage.

Required disagreement types:

- `EMPIRICAL_CONFLICT`
- `THEORETICAL_CONFLICT`
- `IMPLEMENTATION_VARIANT`
- `DEFINITIONAL_CONFLICT`
- `SCOPE_CONFLICT`
- `CONTEXT_DEPENDENT`
- `HISTORICAL_SUPERSESSION`
- `UNRESOLVED`

---

# 11. GO / DONT_GO GATES

The run MUST execute all gates.

## GATE G0 — SOURCE ACCESS

GO only if you can access enough scientific sources to support the discovery.

DONT_GO if you cannot perform source-grounded research.

If DONT_GO:
- still produce ZIP;
- document limitation;
- do not pretend completion.

---

## GATE G1 — SCIENTIFIC BREADTH

GO only if the research spans multiple independent traditions, including:

- symbolic;
- connectionist/subsymbolic;
- cognitive-architecture;
- memory/retrieval;
- probabilistic;
- graph/relational;
- argumentation/revision;
- modern agent/LLM memory.

DONT_GO if the result is dominated by one paradigm.

---

## GATE G2 — HISTORICAL DEPTH

GO only if both historical and contemporary literature are represented.

DONT_GO if the research is mostly post-2020.

---

## GATE G3 — PRIMARY-SOURCE COVERAGE

GO only if major families have primary or authoritative sources.

DONT_GO if major mechanisms are supported only by secondary summaries.

---

## GATE G4 — VARIABLE EXTRACTION

GO only if discovered mechanisms have been converted into machine-readable variables/parameters where possible.

DONT_GO if the result remains mainly narrative.

---

## GATE G5 — CONTRADICTION PRESERVATION

GO only if disagreements and incompatible variants remain explicit.

DONT_GO if the output harmonizes everything into one architecture.

---

## GATE G6 — NO WINNER SELECTION

GO only if no preferred final architecture is selected.

DONT_GO if you recommend “the best architecture”.

---

## GATE G7 — MACHINE READABILITY

GO only if all required JSON/CSV files parse correctly.

DONT_GO if the structured output is invalid.

---

## GATE G8 — PROVENANCE

GO only if every important mechanism, variable, constraint, benchmark, and scientific claim points to one or more sources or is explicitly marked unsourced.

DONT_GO if provenance is missing.

---

## GATE G9 — PARAMETER HONESTY

GO only if numeric ranges/defaults are sourced.

DONT_GO if numerical values were guessed.

---

## GATE G10 — DESIGN-SPACE ORIENTATION

GO only if the final result can be consumed by a deterministic program that later generates experiment configurations.

DONT_GO if a human must reread prose to reconstruct the variables.

---

# 12. REQUIRED ZIP NAME

Return exactly one ZIP.

Filename:

`<MODEL>-MYTRUES-COGNITIVE-DISCOVERY-001.zip`

Replace `<MODEL>` with your model/provider identity in uppercase ASCII-safe form.

Examples:

- `CHATGPT-MYTRUES-COGNITIVE-DISCOVERY-001.zip`
- `CLAUDE-MYTRUES-COGNITIVE-DISCOVERY-001.zip`
- `GEMINI-MYTRUES-COGNITIVE-DISCOVERY-001.zip`
- `DEEPSEEK-MYTRUES-COGNITIVE-DISCOVERY-001.zip`

Do not return multiple ZIPs.

---

# 13. REQUIRED ZIP STRUCTURE

The ZIP MUST contain exactly one root directory with the same basename as the ZIP.

Required structure:

```text
<MODEL>-MYTRUES-COGNITIVE-DISCOVERY-001/
│
├── 00_RUN_MANIFEST.json
├── 01_EXECUTIVE_MAP.md
├── 02_MECHANISMS.json
├── 03_VARIABLES.json
├── 04_RELATIONSHIPS.json
├── 05_COMPATIBILITIES.json
├── 06_CONSTRAINTS.json
├── 07_ARCHITECTURES_AND_MODELS.json
├── 08_EXPERIMENTS_AND_BENCHMARKS.json
├── 09_OPEN_QUESTIONS.json
├── 10_SOURCES.csv
├── 11_SOURCES.json
├── 12_CONTRADICTIONS.json
├── 13_DESIGN_SPACE.json
├── 14_SCIENTIFIC_REPORT.md
├── 15_GO_DONTGO_REPORT.md
├── 16_GAPS_AND_UNCERTAINTIES.md
└── SHA256SUMS.txt
```

No required file may be omitted.

Additional files are allowed only under:

`SUPPLEMENTARY/`

---

# 14. RUN MANIFEST

`00_RUN_MANIFEST.json` MUST contain at least:

```json
{
  "contract": "MYTRUES-DISCOVERY-001",
  "contract_version": "1.0.0",
  "model_provider": "",
  "model_name": "",
  "model_version_if_known": "",
  "run_started_at": "",
  "run_finished_at": "",
  "web_access": true,
  "source_count": 0,
  "primary_source_count": 0,
  "peer_reviewed_source_count": 0,
  "mechanism_count": 0,
  "variable_count": 0,
  "relationship_count": 0,
  "compatibility_count": 0,
  "constraint_count": 0,
  "architecture_count": 0,
  "benchmark_count": 0,
  "contradiction_count": 0,
  "open_question_count": 0,
  "overall_status": "GO",
  "gates": {}
}
```

Allowed `overall_status`:

- `GO`
- `DONT_GO`

---

# 15. MECHANISMS JSON

`02_MECHANISMS.json` MUST be an array.

Each object MUST contain:

```json
{
  "mechanism_id": "",
  "canonical_name": "",
  "aliases": [],
  "category": "",
  "description": "",
  "scientific_domain": [],
  "cognitive_function": [],
  "input_representation": [],
  "output_representation": [],
  "known_variants": [],
  "variable_ids": [],
  "relationship_ids": [],
  "source_ids": [],
  "evidence_classes": [],
  "maturity": "",
  "open_questions": [],
  "notes": ""
}
```

---

# 16. VARIABLES JSON

`03_VARIABLES.json` MUST be an array.

Each object MUST contain:

```json
{
  "variable_id": "",
  "mechanism_ids": [],
  "canonical_name": "",
  "aliases": [],
  "definition": "",
  "data_type": "",
  "domain": {
    "kind": "",
    "values": [],
    "min": null,
    "max": null,
    "unit": null
  },
  "reported_settings": [],
  "dependencies": [],
  "incompatibilities": [],
  "source_ids": [],
  "range_evidence_type": "",
  "confidence": "",
  "notes": ""
}
```

Allowed `domain.kind`:

- `categorical`
- `boolean`
- `integer`
- `float`
- `ordinal`
- `function`
- `graph_structure`
- `distribution`
- `algorithm`
- `unknown`

---

# 17. RELATIONSHIPS JSON

`04_RELATIONSHIPS.json` MUST describe semantic relations between mechanisms, representations, variables, architectures, memory types, and methods.

Required relationship types include consideration of:

- `SUPPORTS`
- `ATTACKS`
- `CONTRADICTS`
- `REFINES`
- `SUPERSEDES`
- `DERIVED_FROM`
- `REQUIRES`
- `OPTIONALLY_USES`
- `INCOMPATIBLE_WITH`
- `COMPATIBLE_WITH`
- `COMPOSES_WITH`
- `ALTERNATIVE_TO`
- `GENERALIZES`
- `SPECIALIZES`
- `EMPIRICALLY_COMPARED_WITH`
- `THEORETICALLY_RELATED_TO`
- `BIOLOGICALLY_INSPIRED_BY`
- `IMPLEMENTED_BY`

Do not force a relation if evidence is absent.

---

# 18. COMPATIBILITIES JSON

`05_COMPATIBILITIES.json` MUST contain explicit pairwise or n-ary compatibility information where defensible.

Each item:

```json
{
  "compatibility_id": "",
  "components": [],
  "status": "COMPATIBLE",
  "conditions": [],
  "known_compositions": [],
  "source_ids": [],
  "evidence_class": "",
  "confidence": "",
  "notes": ""
}
```

Allowed status:

- `COMPATIBLE`
- `INCOMPATIBLE`
- `CONDITIONALLY_COMPATIBLE`
- `UNKNOWN`

---

# 19. CONSTRAINTS JSON

`06_CONSTRAINTS.json` MUST contain constraints suitable for future deterministic experiment generation.

Examples:

- mechanism A requires graph representation;
- method B requires weighted edges;
- parameter X is irrelevant when mechanism Y is disabled;
- architecture C cannot use update mode D;
- technique E only applies to episodic memory;
- algorithm F assumes acyclic graph;
- method G requires probabilities.

Each constraint MUST contain:

```json
{
  "constraint_id": "",
  "kind": "",
  "if": {},
  "then": {},
  "source_ids": [],
  "confidence": "",
  "notes": ""
}
```

Allowed `kind`:

- `REQUIRES`
- `EXCLUDES`
- `CONDITIONAL`
- `RANGE`
- `DEPENDENCY`
- `STRUCTURAL`
- `EMPIRICAL`
- `THEORETICAL`
- `IMPLEMENTATION`

---

# 20. ARCHITECTURES AND MODELS JSON

`07_ARCHITECTURES_AND_MODELS.json` MUST include major integrated cognitive architectures and models.

For each:

```json
{
  "architecture_id": "",
  "name": "",
  "aliases": [],
  "year_origin": null,
  "authors_or_originators": [],
  "scientific_domains": [],
  "memory_components": [],
  "reasoning_components": [],
  "learning_components": [],
  "decision_components": [],
  "attention_components": [],
  "representations": [],
  "mechanism_ids": [],
  "variable_ids": [],
  "benchmarks_or_evaluations": [],
  "limitations": [],
  "source_ids": [],
  "notes": ""
}
```

Do not canonize any architecture as superior.

---

# 21. EXPERIMENTS AND BENCHMARKS JSON

`08_EXPERIMENTS_AND_BENCHMARKS.json` MUST identify experiments, datasets, benchmarks, and evaluation methods useful for later automated testing.

For each:

```json
{
  "benchmark_id": "",
  "name": "",
  "type": "",
  "domain": "",
  "measures": [],
  "input": "",
  "expected_output": "",
  "ground_truth_available": false,
  "deterministic_scoring_possible": false,
  "known_baselines": [],
  "limitations": [],
  "source_ids": [],
  "notes": ""
}
```

Prioritize benchmarks with:

- known answers;
- reproducible scoring;
- public data;
- deterministic or objective evaluation;
- difficult relational/temporal/contextual memory problems;
- unresolved performance gaps.

---

# 22. OPEN QUESTIONS JSON

`09_OPEN_QUESTIONS.json` MUST preserve unresolved scientific and engineering questions.

Each:

```json
{
  "question_id": "",
  "question": "",
  "related_components": [],
  "why_unresolved": "",
  "known_positions": [],
  "source_ids": [],
  "experimentable": true,
  "candidate_experiment_variables": [],
  "notes": ""
}
```

---

# 23. SOURCES CSV

`10_SOURCES.csv` MUST have one row per source.

Required columns:

```text
source_id
title
authors
year
venue
source_type
peer_reviewed
primary_source
doi
url
publisher_or_organization
scientific_domain
evidence_class
accessed_at
notes
```

Use stable source IDs such as:

`SRC-000001`

---

# 24. SOURCES JSON

`11_SOURCES.json` MUST contain the same source registry in JSON form.

Do not put information in CSV that is absent from JSON or vice versa.

---

# 25. CONTRADICTIONS JSON

`12_CONTRADICTIONS.json` MUST preserve conflicting findings.

Each:

```json
{
  "contradiction_id": "",
  "topic": "",
  "type": "",
  "position_a": {
    "claim": "",
    "source_ids": []
  },
  "position_b": {
    "claim": "",
    "source_ids": []
  },
  "current_resolution": "UNRESOLVED",
  "context_conditions": [],
  "notes": ""
}
```

Allowed `type`:

- `EMPIRICAL_CONFLICT`
- `THEORETICAL_CONFLICT`
- `IMPLEMENTATION_VARIANT`
- `DEFINITIONAL_CONFLICT`
- `SCOPE_CONFLICT`
- `CONTEXT_DEPENDENT`
- `HISTORICAL_SUPERSESSION`
- `UNRESOLVED`

---

# 26. DESIGN SPACE JSON

`13_DESIGN_SPACE.json` is the most important deliverable.

It MUST provide a deterministic experimental design space.

Top-level structure:

```json
{
  "dimensions": [],
  "global_constraints": [],
  "candidate_composition_patterns": [],
  "unresolved_dimensions": [],
  "source_coverage_summary": {}
}
```

Each dimension:

```json
{
  "dimension_id": "",
  "name": "",
  "description": "",
  "candidate_values": [],
  "variable_ids": [],
  "mechanism_ids": [],
  "constraint_ids": [],
  "source_ids": []
}
```

Example dimensions to consider:

- representation;
- memory organization;
- memory type;
- retrieval;
- association;
- activation;
- learning;
- revision;
- contradiction handling;
- context;
- temporality;
- forgetting;
- attention;
- decision;
- reasoning;
- provenance;
- graph structure;
- vector strategy;
- similarity;
- hybrid fusion;
- granularity;
- persistence;
- confidence;
- evidence;
- assumption handling;
- activation propagation;
- edge semantics;
- edge weighting;
- case reuse;
- consolidation;
- replay;
- salience;
- novelty;
- inhibition.

Do not limit the output to this example.

---

# 27. SCIENTIFIC REPORT

`14_SCIENTIFIC_REPORT.md` MUST explain:

1. search strategy;
2. scientific domains covered;
3. historical coverage;
4. major theory families;
5. mechanism families;
6. architecture families;
7. major variable families;
8. important contradictions;
9. important open problems;
10. areas where experimental parameterization appears feasible;
11. areas where parameterization would be scientifically misleading;
12. limitations of this discovery;
13. likely missing areas.

It MUST NOT recommend a final architecture.

---

# 28. GO / DONT_GO REPORT

`15_GO_DONTGO_REPORT.md` MUST contain one section per gate G0–G10.

For each gate:

```text
GATE:
STATUS: GO | DONT_GO
EVIDENCE:
LIMITATIONS:
```

The overall run is:

`GO`

only if all mandatory gates are GO.

Otherwise:

`DONT_GO`

The ZIP must still be delivered.

---

# 29. GAPS AND UNCERTAINTIES

`16_GAPS_AND_UNCERTAINTIES.md` MUST explicitly list:

- areas not searched deeply enough;
- inaccessible literature;
- uncertain citations;
- claims requiring replication;
- variables without defensible ranges;
- mechanisms with unclear implementation mapping;
- scientific controversies;
- missing benchmarks;
- possible hallucination risk areas;
- concepts that may be aliases rather than distinct mechanisms;
- concepts that may be distinct but are often conflated.

---

# 30. SHA256SUMS

`SHA256SUMS.txt` MUST contain SHA-256 hashes for every file in the root directory except itself.

Use conventional format:

```text
<sha256>  <filename>
```

---

# 31. DETERMINISM AND NORMALIZATION RULES

Use stable IDs.

Suggested prefixes:

- `SRC-`
- `MECH-`
- `VAR-`
- `REL-`
- `COMP-`
- `CON-`
- `ARCH-`
- `BENCH-`
- `Q-`
- `CONT-`
- `DIM-`

IDs MUST be unique within the package.

Use UTF-8.

JSON MUST be valid standard JSON.

Do not include comments inside JSON.

Do not use trailing commas.

CSV MUST be UTF-8 with a header row.

Dates SHOULD use ISO 8601.

---

# 32. DO NOT DO

You MUST NOT:

- choose a winner;
- design the final MyTrues architecture;
- optimize for one technology;
- collapse symbolic and subsymbolic approaches;
- collapse biological and computational claims;
- treat embeddings as truth;
- treat correlation as causation;
- treat analogy as evidence;
- invent parameter ranges;
- ignore older theories;
- ignore contradictory evidence;
- use only LLM-memory papers;
- produce only a literature review;
- produce only prose;
- silently discard difficult-to-combine mechanisms;
- silently discard obsolete approaches;
- silently discard negative results;
- merge incompatible definitions without recording the conflict;
- claim novelty for MyTrues;
- claim that any discovered mechanism is biologically correct;
- claim that any architecture is cognitively complete.

---

# 33. POSITIVE EXECUTION RULE

Whenever uncertain whether a candidate concept belongs in the design space:

prefer inclusion with explicit status:

`CANDIDATE`

rather than silent omission.

The purpose of this run is high recall.

Later experiments will reduce the space.

---

# 34. FINAL QUALITY TEST

Before packaging, verify:

- every required file exists;
- every JSON parses;
- every CSV parses;
- all IDs are unique where required;
- every source reference points to an existing source ID;
- every important mechanism has provenance or `UNSOURCED_CANDIDATE`;
- no final architecture winner is declared;
- contradictions remain explicit;
- variable ranges are sourced;
- design-space dimensions are machine-readable;
- GO/DONT_GO gates are complete;
- hashes are correct.

---

# 35. FINAL RESPONSE CONTRACT

Your visible response to the user MUST be minimal.

Do not paste the report into chat.

Do not summarize the findings unless explicitly asked.

Return:

1. the ZIP file;
2. its filename;
3. its SHA-256;
4. overall status: `GO` or `DONT_GO`.

Nothing else is required.

---

# 36. CONTROLLING SENTENCE

If any instruction is ambiguous, follow this sentence:

> **Do not discover the solution. Discover everything scientifically defensible that can vary in the solution, preserve its provenance and contradictions, and encode it so a deterministic program can later generate and test combinations.**
