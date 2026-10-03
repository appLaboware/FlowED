# IDEOS Experiment Audit — EXP-001..007

Audit date: 2026-10-01.

Evidence classes follow `Tools/EVOLUTION/PROTOCOL.md`:

- A — real external/infrastructure execution in Actions;
- B — reproducible conformance/integration execution;
- C — synthetic/unit evidence;
- D — documentation/design only.

A failed Actions run is still an A-class observation of the **failure**, not proof of
the intended capability.

| Experiment | Audited state | Accepted evidence | Honest claim |
|---|---|---|---|
| EXP-001 PHP+MySQL | PASS | A — run `36769533522` | containerized Porter materialized and removed PHP+MySQL on Docker host |
| EXP-002 containerized Porter | PASS | A — run `36769533522` | host Docker -> controller -> Porter -> CNAB -> Compose worked |
| EXP-003 Azure trust | PARTIAL | A — run `36795844036`; D for undispatched E2E workflow | OIDC/RG read/Contributor write proved; EXP-003 ACI E2E not run |
| EXP-004 dual target | NOT PROVEN | D; audited runs are `startup_failure` with zero jobs | same-contract Docker+Azure claim remains open |
| EXP-005A GRyCAP IM | PASS WITH AZURE IDENTITY LIMIT | A — runs `36800909647`, `36801390616` | official IM booted and really materialized Docker; current Azure connector did not accept lab OIDC shape |
| EXP-005B Porter one-command Azure | PASS | A — run `36796448509` | one Porter command created and verified a public Azure site |
| EXP-006 PHP+MySQL+DNS | NOT PROVEN | A for bootstrap failure; D for intended materialization | runs stopped before OIDC/Porter because DNS-provider credentials were absent |
| EXP-007 decision memory | PASS WITH EPHEMERAL-MEMORY LIMIT | A — run `36806662068` | two known failures resolved through decision graph and Azure delivery continued; cross-run Neo4j retain not proved |

## Non-inheritance rule

A later experiment may supersede or solve a gap, but it does not rewrite the outcome
of an earlier experiment.

Examples:

- later Azure deployment does not make EXP-004 pass;
- later MyTrues DNS fallback does not make EXP-006 custom DNS pass;
- later persistent SQLite memory does not make EXP-007's ephemeral Neo4j memory
  cross-run persistent.

This audit is the baseline for `EVOLUTION/INVENTORY.md`.


## Licensing boundary — post-audit decision

A banca de 2026-10-01 adicionou dois gates de licença sem alterar os resultados
históricos:

- Neo4j Community/GPLv3: **VERMELHO** para runtime de produto; EXP-007 permanece
  evidência histórica, mas Neo4j é somente referência de schema/modelagem;
- Porter administrative MongoDB 8.0/SSPL: **VERMELHO** transitivo para baseline de
  produto; EXP-002 permanece evidência histórica, mas R1 precisa provar storage
  alternativo aceitável.

SQLite permanece a memória persistente de referência do MyTrues.
