# Repository Bootstrap Protocol — RBP 0.1

**ID:** FLOWED-REPOSITORY-BOOTSTRAP  
**Versão:** 0.1-draft  
**Status:** DOGFOODING  
**Owner de domínio:** FlowED  
**Escopo:** formação inicial de repositórios  

## 1. Propósito

O RBP define como um novo repositório deve nascer de forma homogênea, rastreável, validável e transportável entre humanos, IDEs e agentes de IA.

O RBP não define o produto que será construído. Ele define a infraestrutura inicial necessária para que o projeto consiga descobrir, planejar, comunicar, versionar e evoluir sem depender da memória de uma pessoa ou de um fornecedor de IA.

## 2. Princípio central

```text
PROTOCOL != TEMPLATE != INSTANCE
```

- O protocolo é a autoridade.
- Templates são implementações substituíveis do protocolo.
- Cada repositório criado é uma instância materializada.

Um ZIP, template repository ou skeleton pode acelerar o bootstrap, mas nunca se torna autoridade normativa por existir antes.

## 3. Fontes e boas práticas consolidadas

O RBP incorpora práticas compatíveis com:

- scaffolding declarativo e reprodutível;
- template repositories;
- geração parametrizada;
- validação pós-geração;
- separação entre regras canônicas e gateways específicos de ferramentas;
- estrutura progressiva por estágio;
- manifestos machine-readable;
- operação idempotente;
- evidência antes de promoção;
- atualização futura do template sem confundir template com instância.

## 4. Bounded contexts

O FlowED orquestra o bootstrap, mas não absorve os domínios especializados.

```text
FlowED / RBP
  -> cria estrutura mínima
  -> registra identidade, estágio e autoridade
  -> aciona perfis e protocolos aplicáveis

TFP
  -> formação de Tool

InterMembers / IA Sessions
  -> atores, sessões, inbox/outbox e comunicação

ISO29110-Lite
  -> estrutura/documentação controlada quando adotada

Dec-B
  -> políticas e mecânica de SCM/versionamento

WSL-PortableEnv
  -> ambiente reproduzível quando adotado
```

## 5. Entradas mínimas

Nunca inventar campos ausentes. Usar `UNKNOWN` quando necessário.

```text
repository_name
owner_scope
project_id
repository_purpose
repository_profile
visibility
primary_authority
initial_actor
initial_session
source/origin
parent_project
adopted_protocols
known_constraints
```

## 6. Estados de bootstrap

```text
B0 — DECLARED
B1 — MATERIALIZED
B2 — VALIDATED
B3 — OPERATING
```

### B0 — Declared

Existe intenção explícita e manifest inicial.

### B1 — Materialized

Estrutura física mínima foi criada.

### B2 — Validated

Validator comprova que a estrutura corresponde ao perfil selecionado e que não existem conflitos básicos de identidade, regras ou caminhos.

### B3 — Operating

O repositório completou pelo menos um ciclo real de trabalho com commit/evidência e pode continuar por seu próprio protocolo de domínio.

## 7. Lei de materialização progressiva

Não criar arquivos vazios apenas para satisfazer uma árvore ideal.

```text
CREATE WHEN REQUIRED BY CURRENT STAGE OR PROFILE
```

Por outro lado, quando a informação já é conhecida e útil para tornar o repositório operacional, materializá-la no bootstrap é preferível a deixá-la apenas na memória do incubador.

## 8. Estrutura mínima geral

```text
<repository>/
├── README.md
├── REPOSITORY-MANIFEST.json
├── .RULES.md
├── AGENTS.md
├── .github/
│   └── copilot-instructions.md
├── docs/
│   └── bootstrap/
│       ├── ORIGIN.md
│       └── CURRENT-STATE.md
├── _dev/
│   └── README.md
└── scripts/
    └── validate_bootstrap.py        # quando validator executável for adotado
```

Perfis podem acrescentar estrutura.

## 9. REPOSITORY-MANIFEST

Mínimo recomendado:

```json
{
  "schema": "flowed/repository-bootstrap/v0.1",
  "repository": "owner/name",
  "project_id": "UNKNOWN",
  "profile": "GENERIC",
  "bootstrap_stage": "B0",
  "status": "DRAFT",
  "authority": {
    "owner_scope": "UNKNOWN",
    "primary_actor": "UNKNOWN"
  },
  "origin": {
    "type": "ROOT",
    "source": "UNKNOWN"
  },
  "adopted_protocols": [],
  "ai_ready": false,
  "validator_state": "NOT_RUN"
}
```

Identidade, estágio, workflow e implementação não devem ser misturados em um único campo.

## 10. Regras canônicas e gateways

O repositório deve manter uma única autoridade de comportamento por escopo.

```text
.RULES.md = regra canônica
```

Gateways específicos de ferramentas devem apontar para a regra canônica e adicionar somente requisitos inevitavelmente específicos daquela ferramenta.

Exemplos:

```text
AGENTS.md
.github/copilot-instructions.md
CLAUDE.md
GEMINI.md
.windsurf/rules/...
```

Evitar copiar integralmente a mesma política em todos eles.

## 11. Preparação para agentes de IA

Quando `ai_ready=true`, o bootstrap deve garantir que um novo agente consiga responder antes de agir:

```text
Quem sou?
Qual é meu projeto?
Qual é minha sessão?
Qual minha autoridade?
O que posso escrever?
O que não posso alterar?
Qual estado devo ler?
Qual entrada devo processar?
Como devo fechar minha unidade de trabalho?
```

A memória do chat não é fonte de verdade do repositório.

## 12. Sessões, inbox/outbox e planejamento

O RBP não define o protocolo de comunicação; ele apenas pode materializar o profile adotado pelo InterMembers.

Quando um profile de IA Sessions for selecionado, o repositório deve poder conter, por ator/sessão:

```text
identity / manifest
inbox
outbox
planning
state
cognition
handoff
evidence
```

A semântica pertence ao protocolo responsável, não ao RBP.

## 13. `_dev/`

`_dev/` contém material do desenvolvimento do próprio repositório que não é parte do produto/artefato consumido.

Exemplos:

- hipóteses;
- experimentos;
- pesquisas internas;
- propostas;
- evidência de bootstrap;
- artefatos temporários.

Por padrão:

```text
_dev = NON_NORMATIVE
```

Um artefato só deixa `_dev/` quando é explicitamente promovido para a área canônica apropriada.

## 14. Perfis

O RBP geral é composto com profiles.

Perfis iniciais previstos:

```text
GENERIC
AI_RESEARCH
TOOL_FORMATION
PRODUCT
DOCUMENTATION_ONLY
INCUBATION
```

Cada profile declara:

```text
required_inputs
required_paths
required_rules
adopted_protocols
validation_rules
promotion_condition
```

## 15. Tool Formation como composição

Quando `profile=TOOL_FORMATION`, o RBP não recria o TFP.

Ele materializa o repositório mínimo e aponta para o TFP como protocolo de formação.

O TFP mantém suas leis principais:

```text
RESEARCH BEFORE ARCHITECTURE
ADOPT BEFORE ADAPT
COMPOSE BEFORE BUILD
BUILD ONLY THE PROVEN RESIDUAL
EVIDENCE BEFORE PROMOTION
```

## 16. Bootstrap algorithm

```text
1. RECEIVE INPUT
2. RESOLVE PROFILE
3. VALIDATE REQUIRED INPUT
4. CREATE REPOSITORY IF NEEDED
5. MATERIALIZE MINIMUM STRUCTURE
6. WRITE MANIFEST
7. INSTALL CANONICAL RULES
8. INSTALL TOOL/AGENT GATEWAYS
9. APPLY PROFILE
10. APPLY ADOPTED DOMAIN PROTOCOL POINTERS
11. VALIDATE STRUCTURE
12. CREATE INITIAL COMMIT
13. RUN FIRST REAL WORK CYCLE
14. VALIDATE AGAIN
15. PROMOTE B3 OR REPORT BLOCKERS
```

## 17. Idempotência

A futura CLI deve ser orientada a estado desejado.

Comandos conceituais:

```text
flowed repo init
flowed repo apply
flowed repo audit
flowed repo diff
flowed repo status
```

Sintaxe ainda não normativa.

Executar `apply` repetidamente não deve duplicar arquivos ou destruir mudanças legítimas do projeto.

## 18. Create vs update

O bootstrap deve distinguir:

```text
CREATE MISSING
UPDATE MANAGED
PRESERVE USER-OWNED
CONFLICT / STOP
```

Arquivos gerenciados pelo protocolo precisam declarar sua estratégia de ownership.

O gerador nunca deve sobrescrever silenciosamente conteúdo humano/projeto sem uma política explícita.

## 19. Git e unidade de trabalho

Cada ação do bootstrap deve produzir commits coerentes e limitados aos arquivos sob sua responsabilidade.

Regras:

```text
- não incluir arquivos alheios no commit;
- não reescrever histórico para esconder erros;
- correções preferem novo commit/revert quando apropriado;
- artefatos históricos recebidos/entregues devem seguir a imutabilidade do protocolo responsável;
- branch/PR é preferível quando a governança do repositório exige revisão.
```

## 20. Validator

Um validator RBP deve verificar apenas o que consegue provar estruturalmente.

Mínimo:

```text
manifest exists and parses
profile known
mandatory paths for profile exist
canonical rule source exists
agent gateways resolve
identity fields are coherent
adopted protocol references resolve
no required field silently invented
bootstrap stage consistent with evidence
no B3 without a real work-cycle evidence/commit
```

Estados de verdade:

```text
STRUCTURAL_PASS
DOCUMENTED_PASS
EVIDENCE_PASS
NOT_RUN
NOT_APPLICABLE
FAIL
UNPROVEN
```

## 21. Critérios para B3 — Operating

Um repositório não é considerado operacional só porque o skeleton existe.

B3 exige pelo menos:

```text
- bootstrap validated;
- actor/authority resolvable when applicable;
- one real work input;
- one materialized result;
- one coherent commit;
- state/handoff updated when AI profile applies;
- blockers explicit;
- next action resolvable.
```

## 22. Pesquisa de melhores implementações

Antes de construir uma CLI própria para scaffolding, avaliar e comparar ferramentas existentes para geração e atualização de repositórios.

Classes obrigatórias de candidatos:

```text
GitHub Template Repositories
Copier
Cookiecutter
Backstage Software Templates
Yeoman or equivalent generators
GitHub CLI/API composition
other maintained scaffolding engines
```

A disposição deve seguir:

```text
ADOPT
CONFIGURE
ADAPT
COMPOSE
BUILD_RESIDUAL
```

A CLI FlowED não deve reimplementar um scaffolder completo sem residual comprovado.

## 23. Dogfooding obrigatório

A primeira validação do RBP deve criar um repositório real usando o profile `AI_RESEARCH`.

Espécime inicial escolhido:

```text
start-repo-ia-research
```

Esse espécime deve pesquisar justamente como implementar o próprio bootstrap de repositórios e devolver ao FlowED evidências para revisar o RBP.

## 24. Regra final

```text
DECLARE BEFORE MATERIALIZE.
PROFILE BEFORE TREE.
ONE CANONICAL RULE, MANY GATEWAYS.
STATE BEFORE MEMORY.
VALIDATE BEFORE CLAIMING READY.
ADOPT A SCAFFOLDER BEFORE BUILDING ONE.
DOGFOOD THE PROTOCOL WITH A REAL REPOSITORY.
```
