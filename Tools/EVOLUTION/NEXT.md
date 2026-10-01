# NEXT — after SESSION-CLOSE-005

Este arquivo contém trabalho **fora do norte da sessão 005** e trabalho explicitamente
pausado durante a SESSION-006.

## SESSION-006 pause point — 2026-10-01

R0/R1 foi autorizado e iniciado, mas **pausado por novo norte prioritário de
reorganização da org MyTrues** antes de R1 ser retomado.

Ponto exato preservado:

- `Tools/EVOLUTION/SESSION-006.md` abriu formalmente o norte R0 -> R1;
- investigação de retenção reproduziu a falha de `actions/upload-artifact@v4`
  no probe mínimo:
  - run: https://github.com/appLaboware/FlowED/actions/runs/36882969125
  - conclusão: `startup_failure`;
  - Jobs API: `jobs: []`;
  - portanto o comportamento histórico do run `36870956574` não era específico
    do workflow MyTrues;
  - GitHub ainda não expôs causa mais específica, então **não** chamar de quota,
    billing ou policy sem evidência;
- alternativa de retenção durável em branch `evidence` foi criada como
  `.github/workflows/r0-evidence-branch-probe.yml`;
- primeiro run dessa alternativa:
  https://github.com/appLaboware/FlowED/actions/runs/36883086593
  estava `queued` no momento da pausa e ainda precisa ser validado antes de
  fechar R0;
- contrato/linter de disciplina de RESULTS.md ainda não foi materializado;
- inventário canônico de recursos, ownership/tagging, custo/duração/quota e
  versões exatas ainda precisam ser normalizados;
- **R1 não foi retomado após a abertura da SESSION-006**;
- pesquisa preliminar upstream de Porter identificou que v1.x ainda expõe
  `mongodb-docker`/MongoDB como storage administrativo oficial e que o
  `testplugin` upstream também é Mongo-backed; nenhuma alternativa oficial
  aceitável foi ainda executada ou declarada suficiente.

Retomada futura: continuar exatamente deste ponto, primeiro fechar R0 e só então R1.

## R0 — discipline debt

- completar inventário canônico de recursos externos por run;
- ownership/tagging para cleanup seguro;
- custo/duração/quota por experimento;
- padronizar versões exatas em todos os RESULTS;
- fechar mecanismo de retenção de artefatos aceito pela configuração atual do repo;
- revalidar o run do branch `evidence` e registrar URL durável acessível depois do run.

## R1 — Porter/CNAB ainda aberto

- **PRIORIDADE: storage administrativo com licença aceitável**;
- MongoDB 8.0/SSPL transitivo continua VERMELHO para baseline de produto;
- esgotar storage/plugin oficial sem fork e sem substituto proprietário;
- minimizar dependency output wiring vazio observado em R1-P02;
- comparar com upstream/current/canary antes de workaround;
- minimizar Dependencies v2/shared failure de R1-P03;
- signing/verification;
- secrets/signing plugins;
- experimental file sources;
- MCP `analyze_failure`;
- lifecycle Azure uninstall no mesmo accepted experiment;
- same contract across Docker/Azure.

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
