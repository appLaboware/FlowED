# Dossiê — Protocolos, Proveniência e Observabilidade

## HTTP API

### OpenAPI

Repo atual começou em OpenAPI 3.1.
A versão publicada mais recente em 2026-09-10 é OpenAPI 3.2.1.

Plano:

- migrar descrição para 3.2.1;
- validar schemas;
- gerar cliente de conformance;
- política semver do protocolo MyTrues.

### Errors

RFC 9457 é a baseline para Problem Details.

Não criar formato próprio de erro.

Criar registry estável de `type` URIs MyTrues.

## Decisão/processo

### DMN

Adotar DMN 1.5 formal como referência normativa estável.
OMG lista DMN 1.7 como beta; acompanhar, não tornar beta requisito de interoperabilidade.

### BPMN

Adotar BPMN 2.0.2 formal para semântica de wait/receive/resume/escalation quando útil.
MyTrues não precisa se tornar um BPMN engine.

## Eventos

### CloudEvents

Usar como envelope neutro.

Eventos candidatos:

- decision.requested;
- decision.pending;
- decision.resolved;
- decision.applied;
- decision.outcome.observed;
- decision.revoked.

### AsyncAPI

Adotar AsyncAPI 3.1.0 para descrever operações orientadas a mensagens.

## Trace

W3C Trace Context para correlacionar:

intent -> failure -> decision request -> provider -> resolution -> retry -> outcome.

## Proveniência

Adotar W3C PROV como baseline conceitual.

Mapeamento inicial:

- Entity: Case, Evidence, Decision, Artifact;
- Activity: Execution, Evaluation, Resolution, Retry;
- Agent: Client, Provider, Senior, Automated Engine;
- wasGeneratedBy / used / wasAssociatedWith / wasDerivedFrom.

Objetivo: explicar origem e cadeia de uma decisão sem expor algoritmo proprietário futuro.

## Gate

Nenhum protocolo MyTrues novo deve ser inventado enquanto esses padrões cobrirem
adequadamente a necessidade.
