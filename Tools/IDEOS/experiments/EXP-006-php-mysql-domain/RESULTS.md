# RESULTS — EXP-006 Generic PHP + MySQL + custom DNS

Status: **ATTEMPTED, NOT PROVEN**.

## Intended claim

The experiment intended to prove:

`generic PHP artifact + MySQL + Azure + custom DNS -> reachable custom-domain URL`

through one Porter installation command.

## Actions evidence

Runs:

- `36804046816`
- `36804769146`
- `36805070315`

All three completed with `failure`.

In the audited runs, failure occurred in:

`Parse provider bootstrap credentials`

before:

- GitHub OIDC token request;
- Porter installation;
- application packaging;
- Porter credential-set application;
- materialization;
- HTTP verification.

The final audited run explicitly reported:

`CF_DNS_EDIT is unavailable.`

No Cloudflare secret value was exposed.

Evidence classification:

- missing-provider-bootstrap failure: **EVIDENCE-A**;
- PHP+MySQL+custom-DNS materialization claim: **NOT PROVEN**;
- manifest/README intent: **EVIDENCE-D**.

## Boundary learned

This experiment exposed that the original flow treated missing DNS-provider
credentials as a terminal bootstrap failure.

That observation later motivated the decision-memory/MyTrues fallback experiments,
but later successor experiments do not convert EXP-006 itself into a pass.

## Current Actions executability

The workflow is executable by Actions, but the original acceptance path requires
provider credentials that are intentionally absent in the current repository
configuration. Therefore a full custom-DNS run is **blocked by environment
bootstrap**, not proved impossible by Porter.

## Honest conclusion

EXP-006 did not reach Azure or DNS materialization. Its useful result was the observed
bootstrap failure boundary.
