# Production MCP validation contract

Purpose: allow the independent MCP/PostgreSQL implementation to participate in
`MYTRUES-COGNITIVE-RETRIEVAL-V1` without changing the benchmark or seeing the
answer key during retrieval.

## Non-negotiable isolation

The production-line validator MAY read:

- `corpus.json` during ingestion;
- `questions.json` during retrieval.

The production-line retriever MUST NOT read:

- `answer-key.json`;
- provider/reference answers;
- TypeDB answers;
- prior benchmark scores.

## Required procedure

1. Create an isolated benchmark namespace/account/store. Do not mix benchmark
   records with a user's canonical production memory.
2. Ingest the six histories from `corpus.json` through the production line's
   normal supported interfaces.
3. Do not add hidden history tables, compatibility fields, or special benchmark
   behavior unless those are already part of the production architecture.
4. After ingestion is complete, run all 30 questions from `questions.json`.
5. Persist only the answers in the output format below.
6. Only after the answer file is sealed may the scorer compare it with
   `answer-key.json`.

## Output format

```json
{
  "retriever": "production-mcp-postgresql",
  "source": "description of the actual interface used",
  "answers": {
    "q01": "...",
    "q02": 1,
    "q03": "...",
    "...": "...",
    "q30": "..."
  }
}
```

Every question id `q01` through `q30` MUST exist. Use JSON `null` when the
persisted production state cannot recover an answer. Do not guess.

## Questions are semantic, not SQL-specific

The production line is free to retrieve through MCP tools, an internal service
port, a repository/service adapter, or another normal supported interface.
It does not need to mimic either SQLite or TypeDB.

## Fairness

If the production implementation already preserves more cognition than the open
reference, it should score better naturally.

If it currently lacks a way to ingest one of the neutral event types, record the
unsupported event honestly; do not patch the system before the baseline run.

A later enhanced run may be performed after architectural changes, but it must
receive a new experiment id/version.

## Success criterion

"Success" means the run is reproducible and honest, not that it achieves a
particular score.

The first sealed production result becomes the baseline for future comparison.
