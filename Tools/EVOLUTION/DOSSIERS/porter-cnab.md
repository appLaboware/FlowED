# Dossiê — Porter / CNAB

## Papel

Porter é atualmente o principal executor de lifecycle do laboratório.
CNAB fornece o formato para empacotar aplicação distribuída, ferramentas,
configuração e ações de lifecycle.

## Versão de baseline atual

`Porter v1.6.1` — release estável usada nos experimentos R1.

## O que já foi provado

- Porter containerizado;
- install / upgrade / uninstall;
- parameter sets;
- credential sets;
- outputs;
- sensitive outputs com secrets plugin de laboratório;
- custom actions stateless;
- named configuration contexts;
- OCI publish / inspect;
- bundle archive;
- mixins;
- Azure via OIDC;
- app PHP+MySQL;
- WordPress real como artefato PHP genérico;
- endpoint público;
- Porter MCP read-only;
- Porter MCP write opt-in;
- lifecycle executado por MCP.

Evidências principais:

- run `36796448509` — um comando Porter -> Azure site;
- run `36815666277` — WordPress real publicado pelo fluxo genérico;
- run `36818953832` — native state/lifecycle/OCI/MCP surface.

## Descoberta importante: Porter já possui MCP nativo

Porter 1.6.x inclui `porter mcp`, um servidor MCP first-party por stdio.

Modo padrão:

- inspection/read-only.

Com `--allow-write`:

- install;
- upgrade;
- uninstall;
- invoke custom action.

Consequência:

não devemos criar uma ponte proprietária "LLM -> Porter" antes de esgotar esse servidor.

### Defeito reproduzido

No run `36818953832`, operações MCP de escrita emitiram linhas não JSON em stdout,
poluindo o transporte stdio newline-delimited JSON.

Ações:

1. confirmar contra upstream/latest;
2. procurar issue existente;
3. reduzir para reprodução mínima;
4. propor/reportar upstream;
5. não internalizar workaround como produto.

## Capacidades upstream ainda não esgotadas

Antes de qualquer substituto próprio, explorar:

- direct dependencies;
- dependency output wiring;
- dependency parameter mapping;
- dependency version ranges;
- Dependencies v2 / shared dependencies (experimental);
- transitive dependency graph vs execution;
- persistent parameters;
- file sources (experimental);
- OCI copy;
- signing/verification (Cosign e Notation);
- storage plugins;
- secrets plugins adequados a produção;
- signing plugins;
- namespace/labels;
- installation resources;
- run history/log analysis;
- MCP `analyze_failure`;
- MCP failure handling;
- MCP against real Azure bundle;
- MCP behavior under strict client framing.

O próprio repositório Porter trata `exec` como mixin de último recurso; isso é regra
do laboratório.

## Hipótese a falsificar

"Porter/CNAB não consegue sustentar a UX de intenção desejada sem uma nova camada."

Essa hipótese **não está aceita**.

A existência do MCP nativo torna obrigatório testar primeiro:

`human intent -> generic MCP client/LLM -> porter mcp -> bundle -> target`

antes de qualquer engine de intenção próprio.

## Limites já observados

- Porter não infere intenção de negócio sozinho;
- authoring do bundle ainda conhece target/tooling;
- qualidade de mixins varia;
- dependências de imagens/registries podem falhar;
- provider constraints/quota continuam sendo problemas externos;
- MCP write path mostrou poluição stdout em v1.6.1 no laboratório.

Esses limites não implicam automaticamente necessidade de IDEOS.

## Próximo gate

Completar R1-P02 (dependencies/version selection/output wiring) e depois segurança,
plugins, file sources e failure-analysis MCP.

Matriz final obrigatória:

`capability | Porter native | CNAB native | mixin/plugin | composition | gap real`.
