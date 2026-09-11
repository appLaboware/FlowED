# PO-001 → WRK-001 — future target: dynamic `Como chegamos aqui`

**Status:** queued architectural target. Do not expand scope before completing the first vertical POC slice.

A future capability of the CCP materializer must investigate whether `Como chegamos aqui` can be generated from preserved raw cognitive sources rather than manually rewritten from memory.

Target hypothesis:

```text
raw chat/log/event source preserved
→ non-destructive marking/indexing
→ structured cognitive storage
→ atomic retrieval by subject/unit
→ dynamic projection: "Como chegamos aqui"
```

Important constraints:

- preserve the original source; structuring must not overwrite history;
- every structured element should keep provenance to its source spans/events;
- the generated path should distinguish chronology from causal/semantic relation;
- do not assume the whole raw conversation is durable cognition;
- allow progressive depth, from a compact path to underlying source evidence;
- avoid a free retrospective narrative when a traceable derivation can be produced;
- treat `DEFESA` as a different projection: argument/support is not identical to historical cognitive trajectory.

The first worker mission remains smaller: prove the source → structured CCP → projection/adapters pipeline. This item becomes a next target once that slice works.
