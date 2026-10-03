# Evidence — MYTRUES-COGNITIVE-RETRIEVAL-V1

Date: 2026-10-03

Branch: `experiment/mytrues-dual-memory-ab`

GitHub Actions run: `37093252514`

Job: `111117881686`

Conclusion: **benchmark completed successfully**

## Blindness

Both retrievers read only:

- the persisted backend state assigned to that line;
- `questions.json`.

Neither retriever reads `answer-key.json`.

The answer key is opened only after both retrieval outputs exist.

## Corpus

- 6 cognition histories
- 30 human-readable retrieval questions
- 2 explicit control histories
- 4 histories involving revision, reconsideration, exception, correction or supersession

## Aggregate result

- Open provider/reference: **12 / 30**
- Atom / Occurrence / Binding on TypeDB: **30 / 30**

## By dimension

| Dimension | Questions | Provider/reference | Atom/Occurrence/Binding |
|---|---:|---:|---:|
| present-state | 6 | 6/6 | 6/6 |
| history | 11 | 1/11 | 11/11 |
| context | 3 | 3/3 | 3/3 |
| rationale | 2 | 2/2 | 2/2 |
| causality | 4 | 0/4 | 4/4 |
| history+rationale | 2 | 0/2 | 2/2 |
| relations | 2 | 0/2 | 2/2 |

## By history

| Case | Questions | Provider/reference | Atom/Occurrence/Binding |
|---|---:|---:|---:|
| single-decision control | 4 | 4/4 | 4/4 |
| evidence-before-decision control | 3 | 3/3 | 3/3 |
| immutable-runtime revision | 6 | 1/6 | 6/6 |
| LTS preference → exception → return | 6 | 1/6 | 6/6 |
| SQLite → PostgreSQL → SQLite reconsideration | 6 | 1/6 | 6/6 |
| Reader auth → reuse existing MyTrues OAuth | 5 | 2/5 | 5/5 |

## Interpretation

The open provider/reference line performs correctly for the current state and for context/rationale already present at the original decision request.

The measured loss appears when later cognition must remain independently recoverable:

- prior decisions;
- multiple historical decisions for one subject;
- causal event that triggered a revision;
- rationale of the previous state;
- explicit supersession relation;
- counts of explicit evidence/history events.

The Atom/Occurrence/Binding line preserved all tested information in this corpus.

## Important boundary

This is **not** an overall ranking of MyTrues implementations.

The provider/reference implementation is an operational decision-resolution profile. Its current persistence is optimized around a current decision keyed by `failure_code`, not necessarily a full historical cognition ledger.

The private production MCP/PostgreSQL implementation has not yet been scored against these 30 questions. It must be treated as a third independent line until measured.

## Reproduction

- `corpus.json`
- `questions.json`
- `answer-key.json`
- `materialize.py`
- `retrieve_provider.py`
- `retrieve_typedb.py`
- `score.py`
- `.github/workflows/mytrues-cognitive-retrieval-v1.yml`

Runtime:

- Ubuntu 24.04 GitHub-hosted runner
- TypeDB CE 3.12.1
- typedb-driver 3.13.6
- fresh ephemeral SQLite and TypeDB stores
