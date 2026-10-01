# Roadmap para o Estado da Arte e Fronteira da Ciência Conhecida

Este roadmap não é roadmap de features. É roadmap de **redução de ignorância**.

## R0 — Congelar evidência atual

Objetivo: transformar POCs em baseline confiável.

Entregáveis:

- indexar todos os experimentos e runs;
- marcar recursos de laboratório criados;
- adicionar cleanup idempotente;
- separar claims A/B/C/D;
- documentar custos e tempos;
- registrar versões exatas.

Gate: nenhuma capacidade importante depende de memória da conversa.

## R1 — Esgotar Porter/CNAB

Executar antes de criar qualquer "intent engine":

- parameter sets;
- credential sets;
- outputs;
- custom actions;
- bundle dependencies;
- dependency wiring;
- bundle interfaces;
- namespaces/labels;
- signing/verification;
- OCI push/pull;
- storage plugins;
- secrets plugins;
- mixins oficiais;
- exec apenas como último recurso;
- lifecycle install/upgrade/uninstall em ao menos 2 targets.

Gate: matriz de capacidades Porter/CNAB preenchida e lacunas reproduzíveis.

## R2 — Esgotar materialização aberta

Comparar o mesmo artefato em:

- Docker/Compose;
- Azure ACI;
- Azure Container Apps;
- App Service quando aplicável;
- VM;
- Kubernetes;
- OpenTofu/Terraform;
- Ansible;
- Cloud Native Buildpacks.

Métricas:

- authoring específico por target;
- número de conceitos expostos;
- tempo até endpoint;
- rollback/uninstall;
- secrets;
- persistência;
- TLS/DNS;
- custo;
- portabilidade.

Gate: identificar exatamente o que Porter resolve e o que ele não pretende resolver.

## R3 — Formalizar MyTrues Open Protocol

Adotar:

- OpenAPI 3.2.1;
- RFC 9457;
- W3C Trace Context;
- CloudEvents stable;
- AsyncAPI 3.1.0;
- W3C PROV;
- DMN 1.5 formal;
- BPMN 2.0.2 formal.

Entregáveis:

- OpenAPI conformance;
- AsyncAPI;
- event catalogue;
- problem-type registry;
- provenance schema;
- idempotency;
- versioning;
- compatibility policy.

Gate: cliente e fornecedor independentes interoperam sem conhecimento da implementação.

## R4 — Baseline de ciência decisória

Implementar/avaliar, sempre na superfície OPEN:

1. regras determinísticas/decision tables;
2. CBR clássico;
3. MCDA/MCDM;
4. Bayesian decision support;
5. graph retrieval;
6. vector retrieval;
7. hybrid retrieval;
8. learning-to-rank;
9. uncertainty calibration;
10. abstention/reject option;
11. human expert elicitation;
12. outcome feedback;
13. causal reasoning onde houver intervenção.

Cada método deve entrar com:

- dataset/cases;
- benchmark;
- métrica;
- custo;
- explicabilidade;
- robustez;
- failure modes.

Gate: baseline pública comparável e reproduzível.

## R5 — Human-in-the-loop de produção

Objetivo: preservar protagonismo do sênior.

Provar:

- pause durável;
- checkpoint durável;
- notificação assíncrona;
- caso anonimizado;
- sandbox sintético;
- aprovação autenticada;
- resolução versionada;
- resume idempotente;
- timeout/escalation;
- revogação de decisão;
- auditoria.

Gate: nenhum caso desconhecido é transformado em verdade operacional sem autoridade.

## R6 — Benchmark do "decide melhor"

Criar benchmark MyTrues independente de fornecedor.

Avaliar:

- top-1 decision accuracy/utility;
- regret/custo;
- taxa de abstenção;
- tempo humano;
- incident recurrence;
- rollback rate;
- unsafe decision rate;
- calibration;
- consistency;
- generalização entre contextos;
- melhoria por outcome feedback.

Comparar apenas métodos públicos nesta fase.

Gate: definir qual parte do problema permanece mal resolvida.

## R7 — Science Frontier Review

Produzir uma revisão explícita:

- métodos pesquisados;
- implementações reproduzidas;
- resultados;
- lacunas;
- artigos/standards;
- tentativas de composição;
- upstream contributions consideradas.

Se uma baseline pública fechar a lacuna, **ADOPT** e encerrar.

Se a lacuna persistir, criar `FRONTIER-CLAIM.md`.

## R8 — MyTrues Core

Somente depois de R7.

Primeiro Core deve ser pequeno, substituível e comparável.

Critério de aceite:

- supera baseline pública definida;
- ganho estatisticamente/operacionalmente relevante;
- benchmark reproduzível;
- sem violar protocolo aberto;
- pode ser desligado e substituído por baseline OPEN.
