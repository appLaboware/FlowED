# MyTrues E2E — PHP + MySQL -> Azure

This integration reconnects the open MyTrues MVP to a real delivery workflow.

## User intent used by the experiment

```
deploy ./app \
  --target azure \
  --database mysql \
  --domain porter-lab.me.dev.br \
  --decision-provider senior-a
```

The current executable implementation is composed from Porter/CNAB, Azure CLI,
Azure Container Instances and the open MyTrues protocol.

## Expected incidents in this account

1. Azure split repository secrets are absent, while the legacy `AZURE` bundle exists.
   MyTrues senior-a decides whether the compatible fallback may be used.
2. Custom DNS was requested, but Cloudflare credentials are intentionally unavailable.
   After Azure materialization, MyTrues senior-a chooses the Azure provider hostname.

## Acceptance

The run is successful only when:

- PHP is reachable;
- PHP connects to MySQL;
- two HTTP requests show changing persisted visit state;
- final endpoint comes from the selected MyTrues decision;
- a human return report exposes all deviations and decisions;
- Azure resource is intentionally left running so the human can inspect it.
