# Dossiê — Build e Materialização de Aplicações

## Princípio

Aplicação de ponta é payload, não identidade do sistema.

WordPress foi escolhido por ser uma aplicação PHP+MySQL real e não porque o sistema
deve saber "instalar WordPress".

O teste validado publicou WordPress oficial usando:

- source archive;
- bootstrap específico do aplicativo;
- runtime PHP genérico;
- MySQL;
- Porter/CNAB;
- Azure.

Run: 36815666277.

## O que ainda precisamos adotar

### Build

- Cloud Native Buildpacks;
- OCI images;
- SBOM;
- provenance/attestation;
- reproducible builds;
- image signing.

### Runtime/deploy

- Docker/Compose;
- ACI;
- Container Apps;
- Kubernetes;
- VM;
- App Service;
- declarative IaC.

### Data

- persistent volumes;
- managed DB;
- backup/restore;
- migration;
- disaster recovery.

### Edge

- DNS;
- TLS;
- health checks;
- readiness;
- observability;
- rollback.

## Critério de genericidade

Uma capacidade só pode ser chamada genérica quando for provada com mais de uma
família de aplicação.

WordPress conta como um caso PHP/MySQL real, não como universalidade.

Próximas fixtures recomendadas:

- PHP framework app;
- static site;
- Java service;
- Node/Vue/Nuxt app;
- database-only service;
- repository/service tool.

## Gate

Não criar modelo próprio de aplicação antes de esgotar Buildpacks/OCI e mecanismos
de source-to-image existentes.
