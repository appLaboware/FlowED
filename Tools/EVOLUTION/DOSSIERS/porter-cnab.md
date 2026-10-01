# Dossiê — Porter / CNAB

## Papel

Porter é atualmente o principal executor de lifecycle do laboratório.
CNAB fornece o formato para empacotar aplicação distribuída, ferramentas,
configuração e ações de lifecycle.

## O que já foi provado

- Porter containerizado;
- install/uninstall;
- mixins;
- Azure via OIDC;
- app PHP+MySQL;
- WordPress real como artefato PHP genérico;
- endpoint público;
- lifecycle controlado por bundle.

Evidências principais:

- run 36796448509 — um comando Porter -> Azure site;
- run 36815666277 — WordPress real publicado pelo fluxo genérico.

## Capacidades upstream ainda não esgotadas

Antes de qualquer substituto próprio, explorar:

- parameter sets;
- credential sets;
- outputs;
- custom actions;
- dependencies;
- dependency graph/wiring;
- bundle interfaces;
- namespaces/labels;
- OCI distribution;
- signing/verification;
- storage/secrets/signing plugins;
- mixins específicos;
- lint/inspect;
- upgrade lifecycle;
- exec mixin apenas quando não existir mixin apropriado.

O próprio repositório Porter trata `exec` como mixin de último recurso; isso deve ser
regra do laboratório.

## Estado da arte relevante

CNAB continua sendo especificação cloud-agnostic para empacotar e administrar
aplicações distribuídas; Porter é listado pelo ecossistema CNAB como ferramenta para
autorá-las e instalá-las.

## Hipótese a falsificar

"Porter/CNAB não consegue sustentar a UX de intenção desejada sem uma nova camada."

Não aceitar essa hipótese até E2/R1 estar completo.

## Limites já observados

- Porter não infere intenção de negócio sozinho;
- authoring do bundle ainda conhece target/tooling;
- qualidade de mixins varia;
- dependências de imagens/registries podem falhar;
- provider constraints/quota continuam sendo problemas externos.

Esses limites não implicam automaticamente necessidade de IDEOS.

## Próximo gate

Completar R1 e produzir uma matriz:

`capability | Porter native | CNAB native | mixin/plugin | composition | gap real`.
