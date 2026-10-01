# EXP-005 — Results

## Phase A — official product boots

**PASS**

Run: `36800909647`

Validated with the official images:

- `grycap/im:latest`
- `ghcr.io/grycap/im-client:latest`

The IM REST service started and the official client connected successfully.

Observed output:

- `IM service container is running.`
- `Official IM client is executable.`
- `EXP-005 phase A: PASS`

## Phase B — IM performs a real materialization

**PASS**

Run: `36801390616`

The experiment exposed the GitHub runner Docker Engine to the official IM Docker connector and submitted a RADL description through the official IM client.

The IM:

1. accepted the RADL;
2. created an Infrastructure ID;
3. asynchronously materialized the requested Docker workload.

This proves that IM is not merely a parser or documentation artifact: its deployment engine and Docker connector execute real materialization.

## Human input still required by IM

The Docker baseline was not expressed as human intent.

We had to provide:

- provider type: Docker;
- provider endpoint;
- CPU architecture;
- CPU count;
- memory;
- network;
- image URL;
- deployment cardinality;
- RADL syntax;
- IM service credentials.

Therefore the tested interface is:

`technical infrastructure description -> IM -> materialization`

not:

`human intent -> materialization`

## Phase C — existing Azure identity compatibility

The FlowED laboratory already has an Azure application identity configured for GitHub OIDC.

Available identity material:

- Azure client ID;
- Azure tenant ID;
- Azure subscription ID;
- GitHub federated identity.

There is deliberately no permanent Azure client secret.

The current GRyCAP IM Azure connector implementation accepts only these credential shapes:

1. `subscription_id + client_id + secret + tenant`; or
2. `subscription_id + username + password`.

The connector instantiates `ClientSecretCredential` or `UsernamePasswordCredential`.

It does not currently accept the GitHub OIDC/federated-token credential shape already used by this laboratory.

### Experimental consequence

We will **not create a permanent client secret merely to make IM pass**.

Doing that would move provider bootstrap work back to the human/operator and would hide exactly the abstraction boundary this experiment is intended to measure.

Current result:

**IM materialization engine: validated.**

**Existing Azure OIDC identity -> IM Azure connector: incompatible without an additional credential/bootstrap step.**

## IDEOS criterion

At this stage IM does not satisfy:

`"publique este site PHP na Azure" -> URL`

It does satisfy a lower layer:

`RADL/TOSCA + compatible provider credentials -> provisioned infrastructure`

This makes IM a plausible execution/materialization component beneath an intent resolver, but not an intent-to-materialization product by itself.
