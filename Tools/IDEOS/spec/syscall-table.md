# IDEOS Syscall Table

Status: initial capability table; **not a promise of final CLI spelling**.

The term `syscall` here means a stable IDEOS capability request crossing from
intent resolution into an adopted execution/decision capability.

| Capability call | Purpose | Current mechanism | Evidence state |
|---|---|---|---|
| `materialize` | create/materialize the requested workload | Porter/CNAB + adopted provider/materializer | Docker and Azure paths proved separately |
| `inspect` | inspect bundle/installation/capability state | Porter native inspect/show surfaces | reproduced in R1-P01 |
| `destroy` | reverse a materialization through lifecycle | Porter uninstall | Docker proved; same accepted Azure install+uninstall experiment still open |
| `decide` | request an operational/domain decision without embedding decision memory in IDEOS | `DecisionMemory` port; first adapter is MyTrues | MyTrues v0.2 protocol/conformance proved; IDEOS adapter split pending canonical repos |

## Rules

1. A syscall names an IDEOS need, not a vendor command.
2. The implementation behind the syscall is replaceable.
3. A syscall does not authorize IDEOS to reimplement an adopted upstream.
4. New syscalls require an observed capability boundary and evidence.
5. CLI syntax may evolve independently while preserving the capability contract.

## Not yet declared

No canonical syscall is declared yet for generic natural-language interpretation,
target inference, billing, marketplace behavior or InFabric integration.
Those would exceed the current evidence/north.
