# MyTrues Cognitive Retrieval Benchmark v1

Status: experimental, isolated, reproducible.

## Question

Given the same sequence of explicit cognitive events, how much of the cognition can each persistence model recover later?

This benchmark compares two independent lines without merging either one:

### Line A — existing provider/reference

Reuses unchanged:

- `Tools/MYTRUES/reference/provider_server.py`
- `mytrues.decision/v1`
- its SQLite persistence semantics

No schema or behavior is patched to improve historical retrieval.

### Line B — Atom / Occurrence / Binding

Reuses unchanged:

- `Tools/MyTrues/typedb-poc-bridge/00-schema.tql`
- TypeDB CE 3.12.1
- Atom
- Occurrence <: Atom
- Binding(Occurrence, Key, Value)

## Blindness boundary

Files are deliberately separated:

- `corpus.json`: neutral source cognition histories
- `questions.json`: retrieval questions, no expected answers
- `answer-key.json`: expected answers, read only by the scorer
- `retrieve_provider.py`: reads provider persistence + questions
- `retrieve_typedb.py`: reads TypeDB persistence + questions
- `score.py`: reads both outputs + answer key

Neither retriever reads `answer-key.json`.

## Corpus

Six cases:

1. single-decision control;
2. evidence-before-decision control;
3. immutable-runtime re-evaluation;
4. LTS preference → exception → return to LTS;
5. SQLite → PostgreSQL → SQLite reconsideration;
6. GitHub OAuth → reuse existing MyTrues OAuth.

The controls exist specifically to make sure the benchmark is not constructed only around history-heavy cases that favor the incidence model.

## Questions

30 deterministic questions across:

- present state;
- historical state;
- rationale;
- original/current context;
- causal trigger;
- explicit supersession;
- event history.

## Provider ingestion fairness

The provider line receives its first decision through its normal request/resolution API.

For later changes to a known `failure_code`, the open reference exposes no new re-evaluation endpoint. The benchmark therefore uses the supported provider-resolution path on the existing decision request. It does not add a hidden history table or change the provider implementation.

This limitation is part of the behavior under test, not an artificial handicap.

## Claim boundary

This benchmark evaluates **retrieval from persisted cognition** in the open provider/reference implementation versus the TypeDB incidence model.

It does not claim:

- that TypeDB is universally superior;
- that the private production MCP/PostgreSQL implementation has identical persistence semantics to the open SQLite reference;
- that the benchmark measures latency, cost, operational complexity, security, or decision quality.

A later production-line run can populate a third result column without changing this corpus, question set, or answer key.
