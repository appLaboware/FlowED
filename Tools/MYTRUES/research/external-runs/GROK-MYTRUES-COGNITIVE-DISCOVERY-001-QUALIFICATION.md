# GROK-MYTRUES-COGNITIVE-DISCOVERY-001 — Qualification

Date: 2026-10-01

Status: **PRESERVED — NOT QUALIFIED FOR PROMOTION**

Source upload SHA-256:
`1689128dc707fd10991eb04d4424b85ba2deb2d09ac1420c0366d322c8e7af1d`

Declared provider/model: xAI / Grok 4.5.
Declared contract: `MYTRUES-DISCOVERY-001` v1.0.0.
Declared overall status: `DONT_GO`.

## Integrity

The package `SHA256SUMS.txt` matches every listed payload file.

## Qualification findings

The package does **not** satisfy its own machine-readability gate as received.

Invalid required JSON files:

- `06_CONSTRAINTS.json`: `CON-000021` contains
  `"then": {"approx_7"}`, which is not valid JSON.
- `07_ARCHITECTURES_AND_MODELS.json`: contains
  `"year_origin": 1980s`, which is not valid JSON.
- `08_EXPERIMENTS_AND_BENCHMARKS.json`: `BENCH-000013` closes
  `expected_output` with a square bracket and does not parse.

Therefore G7 must be treated as `DONT_GO` independently of the producer's
self-declaration.

The manifest also declares 42 mechanisms and 68 variables, while the delivered
parseable payload contains 20 mechanisms and 23 variables. The package's own
executive map reports 20 and 23.

## Parseable candidate research surface

- mechanisms: 20;
- variables: 23;
- relationships: 35;
- compatibilities: 22;
- open questions: 18;
- contradictions: 12;
- sources: 45;
- design-space dimensions: 15.

Mechanism families include spreading activation, semantic networks, production
systems, TMS, Hopfield memory, argumentation, CBR, RAG, Hebbian learning,
chunking, episodic/working memory, graph traversal, dense retrieval, AGM,
predictive processing and continual learning.

Design-space dimensions include representation, memory organization, retrieval,
activation, learning, revision, context/temporality, forgetting,
attention/capacity, decision/reasoning, provenance, hybrid fusion, granularity,
persistence and confidence/evidence.

## Boundary

No external bibliographic verification was performed during this intake.

The 45 received source identities remain candidate sources until independently
verified against primary/authoritative material.

Do not repair the original package in place. A repaired derivative requires a
new identity/hash and explicit transformation record.

## Intake decision

- preserve;
- do not promote as qualified Discovery;
- mine candidate mechanisms/questions only after provenance checking;
- retain as a negative conformance example for external-run qualification.
