# CONTEXT — WRK-001

**Actor:** `WRK-001`
**Role:** worker de materialização CCP/POC
**Session:** `260911-025000-worker`

## Mission

Build a minimal vertical proof of concept for the CCP materializer.

Target pipeline:

```text
preserved source/log
→ marking/indexing
→ structured CCP
→ projection contract
→ adapter
→ compiled artifact
```

## First POC goal

Use one real cognitive unit and demonstrate multiple projections of the same base, at minimum:

- `REDUCT-MAX`;
- `BASE`;
- `DEFESA`;
- provenance back to the preserved source.

Prefer an executable end-to-end slice before generalizing POP, DOC, additional readers or complex ontologies.

## Boundaries

- do not revise manifesto wording;
- do not redefine FlowED/CCP philosophy unilaterally;
- send conceptual blockers to `PO-001` through its `INBOX/`;
- record architecture and delivery in the repository, not only in chat;
- every commit must start with `[WRK-001]`.

Read `DEV/ia-sessions/COORDINATION.md` before starting work.
