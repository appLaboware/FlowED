# Inventário de Ferramentas e Maturidade

Data-base desta fotografia: 2026-10-01.

| Domínio | Ferramenta/padrão | Papel atual | Estágio | Evidência atual | Próxima fronteira |
|---|---|---|---|---|---|
| Lifecycle | Porter 1.6.1 | executor CNAB e lifecycle | E2 | lifecycle, sets, outputs, actions, OCI, archive e MCP nativos; run 36818953832 | dependencies, signing, plugins, file sources, failure analysis |
| Agent interface | Porter MCP | interface first-party de agente para Porter | E1–E2 | read-only + write opt-in + lifecycle reais; run 36818953832 | corrigir/confirmar poluição stdout; Azure real; analyze_failure |
| Packaging | CNAB | contrato de bundle distribuído | E1 | bundles reais + OCI publish/archive | dependencies/spec boundaries, signing/attestation |
| Decision protocol | MyTrues Open Protocol | request/pause/resolve/resume | E3 | conformance + E2E | formalizar provenance, events e compatibilidade |
| Decision science | CBR/DMN/MCDA/etc. | baseline futura do decisor | E0–E1 | CBR mínimo + regras | reproduzir famílias de métodos antes de Core |
| Process semantics | BPMN 2.0.2 | modelo de pause/wait/resume | E0 | conceito aplicado | mapear estados MyTrues para BPMN formal |
| API | OpenAPI | contrato HTTP | E1 | spec atual 3.1 no repo | migrar e validar OpenAPI 3.2.1 |
| Errors | RFC 9457 | problem details | E1 | schema presente | conformance completa e problem types estáveis |
| Tracing | W3C Trace Context | correlação | E1 parcial | echo de traceparent | tracing ponta a ponta |
| Events | CloudEvents | envelope de eventos | E0 | planejado | emitir decision.requested/resolved/outcome |
| Async API | AsyncAPI | contrato de eventos | E0 | planejado | adotar 3.1.0 |
| Provenance | W3C PROV | proveniência de decisão | E0 | ausente | mapear Case/Decision/Evidence/Execution |
| Memory | SQLite | memória persistente simples | E1 | restart proof | migrations, concurrency, retention |
| Graph memory | Neo4j | grafo + vector candidate retrieval | E1 | POC | modelagem PROV, hybrid retrieval, benchmark |
| Identity | GitHub OIDC -> Azure | autenticação sem secret longo | E2 | login/read/write reais | subject imutável e hardening |
| Test executor | GitHub Actions | laboratório reproduzível | E2 | múltiplos E2E | separar lab runner de runtime de produto |
| Azure lab | Azure Container Instances | target simples de materialização | E2 | PHP/MySQL/WordPress reais | comparar Container Apps/App Service/AKS/VM |
| DNS | Cloudflare API | target DNS externo | E0/E1 | auth anterior fora do E2E final | protocolo/provider adapter, fallback |
| App artifact | WordPress | aplicação real de referência | E1 | WordPress publicado | manter como fixture, nunca acoplar arquitetura |
| Runtime | PHP + MySQL | workload genérico de referência | E2 | live Azure | storage persistente real, TLS, backups |
| Build | Cloud Native Buildpacks | detecção/build candidata | E0 | ainda não esgotado neste branch | experimento source->image multi-app |
| IaC | OpenTofu/Terraform | materialização candidata | E0 | não esgotado | comparar lifecycle com provider CLI |
| Orchestration | Kubernetes/Helm | target/extensão candidata | E0 | não esgotado | bundle para cluster real |
| Config mgmt | Ansible | target/extensão candidata | E0 | não esgotado | avaliar VM/bare metal |
