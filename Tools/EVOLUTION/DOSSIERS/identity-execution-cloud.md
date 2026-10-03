# Dossiê — Identidade, Executor e Cloud

## GitHub Actions

Papel atual: executor de laboratório e prova reproduzível.

Não assumir que GitHub Actions será runtime do produto.

Já provado:

- workflows independentes;
- OIDC;
- integração Azure;
- conformance MyTrues;
- E2E real.

Dívida:

- impedir fan-out acidental de workflows;
- concurrency groups;
- cleanup;
- artifacts/reports;
- resource ownership tags;
- cost/quota accounting.

## GitHub OIDC -> Azure

Baseline preferida: workload identity federation em vez de secrets Azure de longa duração.

Hardening a adotar:

- claims/subjects mínimos;
- política por branch/environment;
- usar subject imutável por repository IDs quando aplicável;
- least privilege;
- scope por resource group;
- auditar role assignments.

## Azure

ACI é target de laboratório, não conclusão de arquitetura.

Comparar:

- ACI;
- Container Apps;
- App Service;
- AKS/Kubernetes;
- VM;
- serviços gerenciados de banco.

O mesmo artefato e intenção devem ser usados para comparar.

## Cloudflare

Tratar como provider DNS externo por API.

MyTrues pode decidir fallback quando o provider está indisponível; não deve duplicar
o que a API Cloudflare já resolve.

## Gate

Separar claramente:

- decisão;
- materialização;
- provider;
- autenticação;
- executor de teste.

Nenhum deles deve virar dependência obrigatória do protocolo MyTrues.
