# Roadmap para o Estado da Arte e Fronteira da Ciência Conhecida

Este roadmap é de **redução de ignorância**, não de acumulação de features.

Legenda:

- **A** real external/infrastructure Actions evidence;
- **B** reproducible conformance/integration Actions evidence;
- **C** synthetic/unit evidence;
- **D** documentation/design only;
- **—** no accepted evidence yet.

## R0 — Congelar evidência atual

| Item | Estado | Evidência | Classe |
|---|---|---|---|
| Auditar EXP-001..007 sem herança de claims | DONE | `Tools/IDEOS/experiments/AUDIT.md` + referenced Actions runs | A+D |
| Garantir RESULTS.md honesto para EXP-001..007 | DONE, incluindo dois EXP-005 históricos | repo docs | D grounded in A/B |
| Classificar INVENTORY por A/B/C/D | DONE | este documento + INVENTORY | D |
| Registrar versões exatas em todos os experimentos | PARTIAL | vários RESULTS registram Porter/host; não todos | A/B parcial |
| Indexar recursos externos criados por run | PARTIAL | alguns workflows/relatórios; não canônico | A parcial |
| Cleanup idempotente por experimento | PARTIAL | alguns uninstall/delete; outros preservaram recursos | A/B parcial |
| Custos, duração e quota por experimento | NOT DONE | — | D |
| Artefatos de evidência retidos por workflow | **not executable in actions** via `actions/upload-artifact@v4` in current repo configuration: run `36870956574` failed at startup with zero jobs; GitHub exposed no narrower cause | startup-failure run + successful same workflow after removal | D + execution-limit observation |

**Gate R0:** OPEN. Falta ownership/cleanup/cost/artifact discipline uniforme.

## R1 — Esgotar Porter/CNAB

| Capacidade | Estado | Evidência | Classe |
|---|---|---|---|
| named config contexts | PASS | R1-P01 `36818953832` | B |
| parameter sets | PASS | R1-P01 `36818953832` | B |
| credential sets | PASS | R1-P01 `36818953832` | B |
| outputs | PASS | R1-P01 `36818953832` | B |
| sensitive-output MCP policy | PASS | R1-P01 `36818953832` | B |
| custom actions | PASS | R1-P01 `36818953832` | B |
| OCI publish/inspect | PASS local registry | R1-P01 `36818953832` | B |
| bundle archive | PASS | R1-P01 `36818953832` | B |
| MCP read-only/write opt-in | PASS with stdout interoperability defect | R1-P01 `36818953832` | B |
| dependency v1 direct lifecycle | PASS | R1-P02 `36819797057` | B |
| dependency version strategy exact/max-patch | PASS | R1-P02 `36819797057` | B |
| dependency output wiring | UNRESOLVED | R1-P02 output exists but root interpolation empty | B-failure observation |
| dependencies v2/shared | NOT PROVEN | R1-P03 `36820579778` fails before sharing behavior | B-failure |
| signing/verification | NOT RUN | — | D |
| storage plugins beyond lab default | NOT EXHAUSTED | — | D |
| secrets plugins | NOT RUN | — | D |
| signing plugins | NOT RUN | — | D |
| experimental file sources | NOT RUN | — | D |
| MCP `analyze_failure` | NOT RUN | — | D |
| lifecycle Docker install/uninstall | PASS | EXP-001 `36769533522` | A |
| lifecycle Azure install + HTTP | PASS | `36796448509` | A |
| lifecycle Azure uninstall in same accepted experiment | NOT PROVEN | — | D |
| same bundle/contract across two targets | NOT PROVEN | EXP-004 startup failures | D |

**Gate R1:** OPEN. Não inventar intent/execution replacement while these rows remain open.

## R2 — Esgotar materialização aberta

| Target/mechanism | Estado | Evidência | Classe |
|---|---|---|---|
| Docker/Compose | PASS | EXP-001 `36769533522` | A |
| Azure ACI | PASS | `36796448509`, `36815666277` | A |
| Azure Container Apps | NOT RUN | — | D |
| Azure App Service | NOT RUN | — | D |
| VM | NOT RUN | — | D |
| Kubernetes/Helm | NOT RUN | — | D |
| OpenTofu/Terraform | NOT RUN | — | D |
| Ansible | NOT RUN | — | D |
| Cloud Native Buildpacks | NOT RUN | — | D |
| same artifact/intent benchmark across targets | NOT RUN completely | EXP-004 did not start jobs | D |

**Gate R2:** OPEN.

## R3 — Formalizar MyTrues Open Protocol

| Item | Estado | Evidência | Classe |
|---|---|---|---|
| provider-scoped request/decision API | PASS behaviorally | conformance runs `36809927549`, `36810420973` | B |
| unknown -> 202 pending | PASS | `36810420973` | B |
| sanitize case packet | PASS | `36810420973` | B |
| provider resolve -> resume | PASS | `36810420973` | B |
| provider memory survives restart | PASS | `36810420973` | B |
| two providers can decide differently | PASS | `36809927549` / `36810420973` | B |
| JSON Schemas v0.2 | PASS: Draft 2020-12 meta-schema + concrete request/response/pending/resolution | `36871180992` | B |
| OpenAPI 3.1 document | EXISTS, NOT CURRENTLY VALIDATED as OpenAPI document | repo | D |
| OpenAPI 3.2.1 migration | NOT RUN | — | D |
| RFC 9457 complete conformance | NOT RUN | — | D |
| Trace Context current v0.2 cycle | NOT ASSERTED | historical B only | B historical |
| CloudEvents | NOT RUN | — | D |
| AsyncAPI 3.1 | NOT RUN | — | D |
| W3C PROV mapping | NOT RUN | — | D |
| idempotency policy | PARTIAL implementation behavior, no protocol proof | — | D |
| version/compatibility policy | NOT DONE | — | D |

**Immediate R3 schema task:** DONE for JSON messages in run `36871180992`.

**Gate R3:** OPEN because OpenAPI/RFC9457/current trace/events/provenance/versioning remain incomplete.

## R4 — Baseline de ciência decisória

| Baseline | Estado | Evidência | Classe |
|---|---|---|---|
| deterministic approved-case lookup | PASS | EXP-007 + MyTrues | A+B |
| simple provider-specific stored decisions | PASS | MyTrues conformance | B |
| CBR 4R baseline | NOT REPRODUCED as benchmarked CBR | — | D |
| decision tables / formal DMN | NOT RUN | — | D |
| MCDA/MCDM | NOT RUN | — | D |
| Bayesian decision support | NOT RUN | — | D |
| graph retrieval benchmark | NOT RUN | — | D |
| vector retrieval benchmark | NOT RUN | — | D |
| hybrid retrieval | NOT RUN | — | D |
| learning-to-rank | NOT RUN | — | D |
| uncertainty calibration | NOT RUN | — | D |
| abstention/reject option benchmark | NOT RUN formally; unknown-case pause exists | B for behavior, D for science baseline |
| expert elicitation methodology | NOT RUN | — | D |
| outcome feedback benchmark | NOT RUN | — | D |
| causal reasoning | NOT RUN | — | D |

**Gate R4:** OPEN. Core remains unjustified.

## R5 — Human-in-the-loop de produção

| Capability | Estado | Evidência | Classe |
|---|---|---|---|
| pause on unknown case | PASS | `36810420973` | B |
| sanitize before provider | PASS | `36810420973` | B |
| explicit human/provider resolution API | PASS reference path | `36810420973` | B |
| provider-scoped retain | PASS | `36810420973` | B |
| restart persistence | PASS | `36810420973` | B |
| authenticated provider authority | NOT RUN | — | D |
| durable external checkpoint/orchestrator | NOT RUN | — | D |
| async notification | NOT RUN | — | D |
| timeout/escalation | NOT RUN | — | D |
| decision revocation/versioning | NOT RUN | — | D |
| audit/provenance chain | NOT RUN formally | — | D |

**Gate R5:** OPEN.

## R6 — Benchmark “decide melhor”

| Item | Estado | Evidência | Classe |
|---|---|---|---|
| benchmark corpus | NOT BUILT | — | D |
| top-1 utility/accuracy | NOT MEASURED | — | D |
| regret/cost | NOT MEASURED | — | D |
| abstention rate | NOT MEASURED | — | D |
| human time | NOT MEASURED | — | D |
| recurrence/rollback | NOT MEASURED | — | D |
| unsafe decision rate | NOT MEASURED | — | D |
| calibration | NOT MEASURED | — | D |
| consistency/generalization | NOT MEASURED | — | D |
| outcome-feedback improvement | NOT MEASURED | — | D |

**Gate R6:** OPEN.

## R7 — Science Frontier Review

| Item | Estado | Evidência | Classe |
|---|---|---|---|
| exhaustive relevant-method review | NOT DONE | — | D |
| public baseline reproduction complete | NOT DONE | — | D |
| residual gap demonstrated | NOT DONE | — | D |
| upstream/composition alternatives exhausted | NOT DONE | — | D |
| `FRONTIER-CLAIM.md` justified | NOT YET ALLOWED | — | D |

**Gate R7:** BLOCKED by R4/R6.

## R8 — MyTrues Core

| Item | Estado | Evidência | Classe |
|---|---|---|---|
| proprietary decision algorithm | INTENTIONALLY ABSENT | `Tools/MYTRUES/core/README.md` | D |
| measurable superiority over public baseline | NOT DEMONSTRATED | — | D |
| replaceable behind open protocol | architectural requirement only | docs | D |

**Gate R8:** BLOCKED. No proprietary algorithm claim is authorized.
