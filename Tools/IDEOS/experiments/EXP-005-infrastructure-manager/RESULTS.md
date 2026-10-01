# Results

## Status

Not yet executed.

## Phase A — official product boots

Pending GitHub Actions run.

## Phase B — Azure authentication compatibility

Current evidence from the IM client documentation and Azure connector shows that the Azure connector expects either:

- subscription + username/password; or
- subscription + client ID + client secret + tenant.

The existing FlowED Azure setup uses GitHub OIDC without a client secret.

This difference is part of the experiment and must not be hidden by manually creating permanent credentials merely to make the test pass.

## Phase C — PHP → Azure → URL

Pending Phase B decision.
