# MyTrues v0.2 Conformance Results

Status: **PASS**.

## Accepted Actions evidence

Workflow:

`MyTrues open MVP conformance`

Successful run:

- run: `36871180992`
- job: `protocol`
- conclusion: `success`

Evidence class: **EVIDENCE-B**.

## v0.2 schema validation proved

The conformance workflow loaded every JSON Schema under the v0.2 protocol surface and
validated each schema against JSON Schema Draft 2020-12.

The run then validated concrete protocol messages for:

- decision request;
- decided response;
- pending response;
- provider resolution;
- problem-schema definition.

The two schemas that still identified themselves as v0.1 were corrected before the
accepted run:

- `decision-request.schema.json`;
- `problem.schema.json`.

The run explicitly printed:

`MYTRUES V0.2 SCHEMAS: PASS`

## Behavioral cycle proved in the same run

The same job also re-proved:

- two independent provider MyTrues instances;
- same known failure -> provider-specific outcome;
- unknown failure -> `202 awaiting-provider-decision`;
- sanitized case packet;
- explicit provider resolution;
- paused request -> decided;
- provider-scoped learning;
- restart;
- learned decision survives restart in provider A;
- provider B does not inherit provider A's learned decision.

The job log printed:

- `TWO INDEPENDENT PROVIDER MYTRUES: PASS`;
- `UNKNOWN CASE PAUSES: PASS`;
- `HUMAN TEACH -> RESUME: PASS`;
- `PROVIDER-SCOPED LEARNING: PASS`;
- `MEMORY SURVIVES RESTART: PASS`;
- `ANONYMIZED CASE PACKET: PASS`.

## Artifact-upload boundary

An immediately preceding workflow revision added:

`actions/upload-artifact@v4`

That revision produced:

- run: `36870956574`;
- conclusion: `startup_failure`;
- jobs: none.

Removing only the artifact-upload step allowed the conformance workflow to start and
pass as run `36871180992`.

Therefore, for this repository configuration:

**artifact attachment through `actions/upload-artifact@v4` is not executable in
Actions at this time.**

GitHub supplied no job log because the workflow failed before job scheduling, so this
document does not claim a more specific policy/platform cause.

Current accepted evidence is the workflow run and job log. The JSON report is emitted
verbatim to the job log.

## Limits not closed by this run

This run does not prove:

- OpenAPI document validation;
- RFC 9457 response behavior on every error path;
- provider authentication/authorization;
- CloudEvents/AsyncAPI;
- W3C PROV;
- production durability beyond Docker-volume restart;
- cross-host persistence;
- a proprietary decision algorithm.

Those remain open in `Tools/EVOLUTION/ROADMAP.md`.
