# seed-004 — provider decision-memory fixture

Purpose: bridge the MyTrues reference implementation with sixteen sanitized failure
codes from the WordPress -> Azure ACI + SMB + edge/DNS line of work.

This package is a **conformance seed**, not a historical incident transcript.

## Provenance rule

The failure taxonomy is project-provided.

Contexts and decisions in `manifest.json` are sanitized/reconstructed reference
cases. They contain no real customer domain, secret, account, subscription, repository
or resource identifier.

They must not be cited as proof that a specific historical incident was resolved by
the exact JSON action shown here unless a separate evidence record says so.

## Distribution

- senior-a: Azure/ACI + WordPress/edge profile;
- senior-b: Docker/workspace profile;
- both providers, deliberately divergent:
  - `php.extension_missing`;
  - `wordpress.maintenance_transient`;
  - `sqlite.dropin_stub_deployed`;
  - `git.dubious_ownership`;
- no provider:
  - `observability.novel_failure_never_seen`.

Expected seeded decision counts:

- senior-a: 11;
- senior-b: 8;
- shared divergent cases: 4;
- control unknown cases: 1.

## Authority

The seed supplies provider memory/data only.

It does not change the open protocol and is not a proprietary algorithm.
