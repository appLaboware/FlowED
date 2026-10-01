# RESULTS — EXP-004 Dual Target

Status: **NOT PROVEN**.

## Intended claim

The experiment intended to prove that the same Application contract could be
materialized on:

- Docker;
- Azure;

through the same `materialize.sh` interface.

## Actions evidence

Known runs include:

- `36793565569`
- `36795751324`
- `36796417704`
- `36796429401`

GitHub classified these runs as `startup_failure`.

For the audited runs, the Actions Jobs API returns:

`jobs: []`

Therefore no Docker or Azure job step executed and there is no runtime evidence for
the dual-target claim.

Evidence classification:

- workflow/script design: **EVIDENCE-D**;
- dual-target runtime claim: **NO ACCEPTED EVIDENCE**.

Because the failure occurred before job scheduling, there are no job logs from which
to claim a specific runtime root cause. This document does not invent one.

## Related evidence that does not close EXP-004

Docker materialization and Azure materialization were each proved in other
experiments. They do not prove that EXP-004's *same Application contract* executed
successfully on both targets.

## Honest conclusion

EXP-004 remains an unclosed experiment. It must either be repaired and executed in
Actions or retained as an explicit historical gap.
