# Prompt Template — GitHub Organization + Repository Bootstrap v0.1

**ID:** FLOWED-RBP-PROMPT-GITHUB-ORG-REPO-BOOTSTRAP  
**Versão:** 0.1-draft  
**Status:** DOGFOODING  
**Owner de domínio:** FlowED / RBP  
**Escopo:** delegação operacional ao GitHub Copilot/agent quando o ChatGPT connector não possui ação administrativa equivalente.

## 1. Propósito

Este prompt existe para reduzir ambiguidade, evitar desistência precoce do executor e separar explicitamente:

- ações automatizáveis pelo Copilot/agent;
- ações que exigem intervenção humana;
- ações que serão retomadas pelo ChatGPT após o bootstrap administrativo.

A execução deve ser baseada em:

```text
PROMPT TEMPLATE + VARIABLE TABLE = EXECUTION REQUEST
```

Não é necessário reenviar o prompt completo a cada uso. O executor pode receber apenas a referência deste template e a tabela de variáveis da execução.

## 2. Regra de divisão de responsabilidade

```text
COPILOT/AGENT:
- verificar existência da organização;
- criar organização quando tecnicamente permitido;
- criar repositório quando tecnicamente permitido;
- configurar propriedades básicas solicitadas;
- reportar exatamente qualquer limitação.

HUMANO:
- autenticação, MFA, consentimento e confirmações obrigatórias;
- instalação/autorizações de GitHub Apps quando o GitHub exigir interação humana;
- seleção manual de repositórios no fluxo da GitHub App quando necessário.

CHATGPT:
- verificar instalações e repositórios visíveis pelo connector;
- assumir bootstrap de conteúdo do repositório após o acesso existir;
- criar/editar arquivos, branches, commits, issues e PRs quando permitido pelo connector.
```

O executor NÃO deve abandonar toda a tarefa porque uma etapa manual existe. Deve executar todas as etapas independentes possíveis antes e depois do gate manual, quando houver mecanismo para continuar.

## 3. GitHub App conhecida

A integração oficial atualmente adotada é:

```text
GITHUB_APP_NAME = ChatGPT Codex Connector
GITHUB_APP_OWNER = OpenAI
GITHUB_APP_URL = https://github.com/apps/chatgpt-codex-connector
GITHUB_APP_INSTALL_URL = https://github.com/apps/chatgpt-codex-connector/installations/new
```

A instalação da GitHub App é considerada um **MANUAL GATE** quando exigir interação humana.

O executor não deve tentar criar uma GitHub App substituta.

## 4. Prompt template canônico

```text
OBJETIVO

Preparar a organização GitHub e o primeiro repositório de {{PRODUCT_OR_PROJECT_NAME}}, executando automaticamente tudo o que for tecnicamente permitido e isolando somente as etapas realmente manuais.

PARÂMETROS

ORGANIZATION = {{ORGANIZATION}}
REPOSITORY = {{REPOSITORY}}
VISIBILITY = {{VISIBILITY}}
DEFAULT_BRANCH = {{DEFAULT_BRANCH}}
DESCRIPTION = {{DESCRIPTION}}
PRODUCT_OR_PROJECT_NAME = {{PRODUCT_OR_PROJECT_NAME}}
REFERENCE_ORGANIZATION = {{REFERENCE_ORGANIZATION}}
INCUBATION_REPOSITORY = {{INCUBATION_REPOSITORY}}
GITHUB_APP_NAME = {{GITHUB_APP_NAME}}
GITHUB_APP_URL = {{GITHUB_APP_URL}}
GITHUB_APP_INSTALL_URL = {{GITHUB_APP_INSTALL_URL}}

REGRAS DE EXECUÇÃO

1. Não trate uma etapa manual como motivo para desistir da tarefa inteira.
2. Execute primeiro todas as ações independentes que puder realizar com segurança.
3. Quando uma ação realmente exigir interação humana, classifique-a como MANUAL GATE.
4. Não invente limitações: tente a operação e reporte o erro real quando houver falha.
5. Não tente contornar MFA, consentimento, owner approval ou outros controles de segurança.
6. Não crie GitHub Apps alternativas.
7. Não altere {{INCUBATION_REPOSITORY}}.
8. Não transfira ou apague repositórios nesta execução.
9. Não habilite recursos pagos sem autorização explícita.
10. Não faça trabalho de conteúdo/bootstrap interno do repositório que o ChatGPT poderá executar depois, salvo instrução explícita.

FASE A — ORGANIZAÇÃO

1. Verifique se `{{ORGANIZATION}}` existe.
2. Se existir e o usuário atual tiver autoridade suficiente, reutilize-a.
3. Se não existir, tente criar a organização `{{ORGANIZATION}}` usando plano gratuito quando possível.
4. Se a criação não puder ser realizada pela interface/agent atual, reporte o motivo real e a ação humana mínima necessária.
5. Depois da existência da organização, continue para a próxima fase sempre que possível.

FASE B — REPOSITÓRIO

1. Verifique se `{{ORGANIZATION}}/{{REPOSITORY}}` existe.
2. Se não existir, tente criar o repositório com:
   - visibility = {{VISIBILITY}}
   - default branch = {{DEFAULT_BRANCH}}
   - description = {{DESCRIPTION}}
3. Não inicialize conteúdo adicional além do estritamente necessário para a criação do repositório, a menos que isso seja requisito da interface utilizada.
4. Se não puder criar o repositório, reporte o erro real e a ação humana mínima necessária.

FASE C — GITHUB APP

A GitHub App adotada é:

{{GITHUB_APP_NAME}}
{{GITHUB_APP_URL}}

Não tente instalar automaticamente se a instalação exigir interação humana.

Quando a instalação/autorização exigir ação humana, reporte:

MANUAL GATE — INSTALL CHATGPT CONNECTOR
URL = {{GITHUB_APP_INSTALL_URL}}
TARGET_ORGANIZATION = {{ORGANIZATION}}
TARGET_REPOSITORY = {{REPOSITORY}}
RECOMMENDED_SCOPE = only selected repository when sufficient

Depois desse gate, não invente que a instalação foi concluída. Apenas informe que o ChatGPT deve verificar o acesso por seu próprio connector.

FASE D — VERIFICAÇÃO E HANDOFF

Ao final, produza exatamente este relatório:

ORGANIZATION_EXISTS = YES|NO
ORGANIZATION_CREATED = YES|NO|NOT_POSSIBLE
REPOSITORY_EXISTS = YES|NO
REPOSITORY_CREATED = YES|NO|NOT_POSSIBLE
GITHUB_APP_INSTALLATION_REQUIRED = YES|NO|UNKNOWN
MANUAL_GATE = NONE|<descrição curta>
MANUAL_GATE_URL = <URL ou NONE>
CHATGPT_VERIFICATION_REQUIRED = YES|NO
BLOCKERS = <lista objetiva ou NONE>
NEXT_ACTOR = COPILOT|HUMAN|CHATGPT
NEXT_ACTION = <uma única próxima ação>

Depois do relatório, PARE.
```

## 5. Variable table — schema

Toda execução deve fornecer uma tabela equivalente a:

| Variável | Obrigatória | Valor padrão/regra |
|---|---:|---|
| `PRODUCT_OR_PROJECT_NAME` | sim | nome humano do produto/projeto |
| `ORGANIZATION` | sim | owner GitHub desejado |
| `REPOSITORY` | sim | nome do primeiro repositório |
| `VISIBILITY` | sim | `private` por padrão em incubação |
| `DEFAULT_BRANCH` | sim | `main` |
| `DESCRIPTION` | sim | descrição curta |
| `REFERENCE_ORGANIZATION` | não | organização de referência, ex. `appLaboware` |
| `INCUBATION_REPOSITORY` | não | repo pré-existente que não deve ser alterado |
| `GITHUB_APP_NAME` | sim | `ChatGPT Codex Connector` |
| `GITHUB_APP_URL` | sim | `https://github.com/apps/chatgpt-codex-connector` |
| `GITHUB_APP_INSTALL_URL` | sim | `https://github.com/apps/chatgpt-codex-connector/installations/new` |

Campos desconhecidos devem usar `UNKNOWN`. Não remover a variável silenciosamente.

## 6. Forma curta de invocação

Quando este arquivo estiver acessível ao executor, a solicitação preferida é:

```text
Siga integralmente o template:
FLOWED-RBP-PROMPT-GITHUB-ORG-REPO-BOOTSTRAP@0.1

Use exatamente a VARIABLE TABLE fornecida abaixo.

Não reinterprete o objetivo, não omita fases e não abandone toda a execução por causa de um MANUAL GATE.
```

Abaixo dessa instrução deve ser enviada apenas a tabela de variáveis da execução.

## 7. Evidência da experiência de dogfooding

A criação da organização `intermembers` mostrou que:

- instalar a GitHub App pode exigir interação humana;
- depois da instalação o ChatGPT consegue detectar a organização pelo connector;
- uma instalação pode existir sem nenhum repositório estar acessível;
- criação/autorização do repositório precisa ser tratada separadamente;
- prompts que misturam ações possíveis e impossíveis aumentam a chance de o executor desistir cedo;
- o prompt deve ordenar explicitamente: tentar, executar o possível, isolar manual gate, continuar/reportar.

## 8. Regra final

```text
DO NOT ABORT THE WHOLE JOB BECAUSE ONE STEP IS MANUAL.
TRY THE OPERATION BEFORE CLAIMING IT IS IMPOSSIBLE.
ISOLATE MANUAL GATES.
RETURN A MACHINE-READABLE HANDOFF.
CHATGPT TAKES OVER AFTER CONNECTOR ACCESS EXISTS.
```
