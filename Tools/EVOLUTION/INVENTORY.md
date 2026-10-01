# Inventário de Ferramentas e Maturidade

Data-base: 2026-10-01.

Legenda de evidência:

- **A** — execução real em infraestrutura/serviço externo via GitHub Actions;
- **B** — conformance/integration reproduzível em GitHub Actions;
- **C** — sintético/unitário;
- **D** — documentação/design ainda não executado.

Um run falho pode ser classe A/B para a **falha observada**, nunca para a capacidade que
não chegou a executar.

| Domínio | Ferramenta/padrão | Estado real | Estágio | Evidência | Classe | Próxima fronteira |
|---|---|---|---|---|---|---|
| Lifecycle | Porter 1.6.1 | PASS parcial: install/upgrade/uninstall, sets, outputs, custom action, OCI/archive; Azure real também provado | E2 | R1-P01 run `36818953832`; Azure run `36796448509` | A+B | dependencies, signing, plugins, file-sources, failure analysis; storage sem SSPL |
| Agent interface | Porter MCP | PASS com defeito confirmado de pureza stdio durante writes | E2 | R1-P01 run `36818953832` | B | minimizar/reportar stdout pollution; exercise `analyze_failure` |
| Packaging | CNAB | PASS parcial: bundles reais, lifecycle e OCI local/externo | E2 | EXP-001 `36769533522`; R1-P01 `36818953832`; Azure `36796448509` | A+B | signing/verification, dependency boundaries, distribution hardening |
| Dependencies v1 | Porter dependencies | PARTIAL: direct dependency + version strategy pass; documented output interpolation unresolved | E2 | R1-P02 run `36819797057` | B | minimize output-wiring gap and compare upstream/canary |
| Dependencies v2 | Porter shared dependencies | FAILED/NOT PROVEN after fixture publish; independent shared-infra install returns non-zero | E1 experimental | R1-P03 run `36820579778` | B-failure | minimize, correct diagnostics, upstream-first |
| Infrastructure manager | GRyCAP IM | PASS for real Docker materialization; current Azure OIDC shape incompatible with tested connector | E2 | runs `36800909647`, `36801390616` | A | no secret downgrade; revisit only if upstream adds federation path |
| Decision protocol | MyTrues open protocol | PASS partial: provider-scoped decide/pause/resolve/resume implemented; v0.2 JSON messages schema-validated | E3 | conformance `36874885791`; WordPress delivery `36815666277` | A+B | OpenAPI validation; events/provenance/versioning |
| MyTrues schemas v0.2 | JSON Schema | PASS: meta-schema + request/response/pending/provider-resolution concrete messages | E2 | conformance runs `36871180992`, `36874885791` | B | add negative cases and compatibility/version-policy tests |
| MyTrues decision fixture | seed-004 | PASS: 16 sanitized cases; senior-a 11, senior-b 8; 4 shared divergent; unknown control pauses both; SQLite state survives restart | E2 | seed conformance `36874885444` | B | keep as conformance fixture; do not call it scientific benchmark |
| Human decision cycle | MyTrues pause→sanitize→resolve→resume | PASS | E3 | runs `36809927549`, `36810420973`, `36871180992` | B | authenticated provider resolution, durable async notification |
| Provider-scoped memory | SQLite | PASS for isolation + restart persistence; **runtime de referência aprovado** | E2 | run `36810420973` | B | migrations, concurrency, retention/export |
| Graph model | Neo4j Community | **HISTORICAL POC ONLY**: EXP-007 provou lookup/grafo, mas banca classificou GPLv3 como VERMELHO; não é dependência/runtime de produto | E1 histórico | EXP-007 run `36806662068` | B histórico | preservar apenas schema/modelagem; reproduzir graph retrieval em backend/licença aceitável |
| Porter admin storage | MongoDB 8.0 default/plugin path | observado no EXP-002; banca marcou SSPL transitivo como VERMELHO para baseline de produto | E0/E1 risk | EXP-002 run `36769533522` + audit note | A observation + D policy | provar/configurar storage alternativo aceitável antes de runtime de produto |
| Decision science | deterministic approved-case lookup | PASS for known cases only | E1 | EXP-007 + MyTrues conformance | A+B | CBR/MCDA/Bayes/ranking/calibration baselines |
| Decision science | CBR/MCDA/Bayes/LTR/calibration/causal | NOT RUN | E0 | roadmap/docs only | D | reproduce public baselines before any Core claim |
| Process semantics | BPMN 2.0.2 | NOT RUN formally; conceptual mapping only | E0 | docs | D | formal state mapping for pending/receive/resume |
| Decision semantics | DMN 1.5 | NOT RUN formally | E0 | docs | D | map decision service/input/output without requiring DMN engine |
| API | OpenAPI | PARTIAL: 3.1 spec exists; not validated in current conformance | E1 | repo spec | D | validation; later migration to 3.2.1 |
| Errors | RFC 9457 | PARTIAL: problem schema exists; current provider paths do not have complete conformance | E1 | repo schema | D | stable problem-type registry + tests |
| Tracing | W3C Trace Context | HISTORICAL B proof; current v0.2 conformance does not assert end-to-end trace | E1 | earlier open-protocol conformance run `36809281176` | B historical | restore current assertion across pause/resume |
| Events | CloudEvents | NOT RUN | E0 | docs | D | decision.requested/resolved/outcome events |
| Async API | AsyncAPI | NOT RUN | E0 | docs | D | AsyncAPI 3.1 contract |
| Provenance | W3C PROV | NOT RUN | E0 | docs | D | map Case/Decision/Evidence/Execution/Agent |
| Identity | GitHub OIDC -> Azure | PASS for federated login, RG read and Contributor write | E2 | EXP-003 run `36795844036` | A | least privilege/immutable subject hardening |
| Test executor | GitHub Actions | PASS as laboratory executor; `actions/upload-artifact@v4` is not executable in actions in current repo configuration (startup_failure with zero jobs) | E2 | accepted runs; artifact attempt `36870956574` | A+B + startup-failure observation | separate test runner from product runtime; artifact retention via allowed mechanism |
| Azure target | ACI | PASS for public PHP/MySQL and WordPress fixtures | E2 | Porter Azure `36796448509`; WordPress `36815666277` | A | compare Container Apps/App Service/AKS/VM |
| DNS provider | Cloudflare API | NOT PROVEN in audited EXP-006 Actions path; missing credentials observed | E0/E1 | EXP-006 run `36805070315` | A-failure | provider bootstrap or sanctioned mock/sandbox; no fake success |
| App fixture | WordPress | PASS as real PHP application fixture, not architectural abstraction | E1 | run `36815666277` | A | retain as fixture only; add other app families |
| Runtime fixture | PHP + MySQL | PASS on Docker and Azure in separate experiments | E2 | EXP-001 `36769533522`; Azure successor runs | A | persistent storage, TLS, backup/restore |
| Dual-target same contract | EXP-004 | NOT PROVEN; startup failures with zero jobs | E0 | runs e.g. `36796429401` | D for capability | repair/re-run or preserve as historical gap |
| Build | Cloud Native Buildpacks | NOT RUN | E0 | docs | D | source→image experiments with multiple app families |
| IaC | OpenTofu/Terraform | NOT RUN | E0 | docs | D | compare against provider CLI/lifecycle |
| Orchestration | Kubernetes/Helm | NOT RUN | E0 | docs | D | real cluster bundle |
| Config management | Ansible | NOT RUN | E0 | docs | D | VM/bare-metal experiment |

## Audit authority

Detailed historical IDEOS experiment truth is in:

`Tools/IDEOS/experiments/AUDIT.md`

R1 experiment-specific truth is in each:

`Tools/EVOLUTION/experiments/R1-P0*/RESULTS.md`
