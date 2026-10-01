# NEXT — after SESSION-CLOSE-005

Este arquivo contém trabalho **fora do norte da sessão 005**.

Nada aqui impede o fechamento da sessão 005. Cada item volta a ser trabalho ativo
somente em nova autorização/norte.

## R0 — discipline debt

- completar inventário canônico de recursos externos por run;
- ownership/tagging para cleanup seguro;
- custo/duração/quota por experimento;
- padronizar versões exatas em todos os RESULTS;
- encontrar mecanismo de retenção de artefatos aceito pela configuração atual do repo.
  `actions/upload-artifact@v4` permanece marcado **not executable in actions** com
  base no startup failure `36870956574` sem jobs/log de causa mais específica.

## R1 — Porter/CNAB ainda aberto

- minimizar dependency output wiring vazio observado em R1-P02;
- comparar com upstream/current/canary antes de workaround;
- minimizar Dependencies v2/shared failure de R1-P03;
- signing/verification;
- secrets/signing plugins;
- experimental file sources;
- MCP `analyze_failure`;
- lifecycle Azure uninstall no mesmo accepted experiment;
- same contract across Docker/Azure;
- **storage administrativo com licença aceitável**:
  - MongoDB 8.0/SSPL transitivo está VERMELHO para baseline de produto;
  - identificar/configurar/executar opção oficial aceitável;
  - upstream imutável; sem fork antes de esgotar configuração/plugin.

## R2 — materialization breadth

Comparar o mesmo artefato/intenção em:

- Azure Container Apps;
- App Service;
- VM;
- Kubernetes/Helm;
- OpenTofu/Terraform;
- Ansible;
- Cloud Native Buildpacks.

## R3 — MyTrues protocol beyond current close

A referência v0.2 atual está fechada para o norte da sessão 005, mas o roadmap maior
continua com:

- validar o documento OpenAPI;
- migrar quando apropriado para OpenAPI 3.2.1;
- RFC 9457 completo;
- Trace Context no ciclo v0.2 atual;
- CloudEvents;
- AsyncAPI;
- W3C PROV;
- idempotency normativa;
- version/compatibility policy;
- autenticação/autorização provider-side.

## R4+ — decision science

`seed-004` é fixture de conformance, **não benchmark científico**.

Ainda devem ser reproduzidos como OPEN:

- CBR;
- formal DMN/decision tables;
- MCDA/MCDM;
- Bayesian decision support;
- lexical/graph/vector/hybrid retrieval;
- learning-to-rank;
- calibration;
- abstention/reject-option benchmark;
- expert elicitation;
- outcome feedback;
- causal methods quando pertinentes.

Neo4j Community não é runtime candidato após o gate GPLv3. Seu material permanece
somente referência de schema/modelagem histórica.

## Future Core

Não existe autorização para algoritmo proprietário ainda.

Qualquer candidato precisa atravessar o Science Frontier Gate e superar baseline OPEN
por benchmark reproduzível.
