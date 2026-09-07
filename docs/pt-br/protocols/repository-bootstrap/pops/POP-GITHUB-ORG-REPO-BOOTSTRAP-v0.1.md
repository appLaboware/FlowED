# POP — GitHub Organization + Repository Bootstrap

**ID:** FLOWED-RBP-POP-GITHUB-ORG-REPO-BOOTSTRAP  
**Versão:** 0.1-draft  
**Status:** DOGFOODING  
**Owner:** FlowED / RBP  
**Documento associado:** `../docs/DOC-GITHUB-ORG-REPO-BOOTSTRAP-v0.1.md`  
**Prompt associado:** `../prompts/GITHUB-ORG-REPO-BOOTSTRAP-v0.1.md`

## 1. Objetivo

Executar o bootstrap administrativo de uma organização GitHub e de seu primeiro repositório, separando claramente automação, gates humanos e handoff ao ChatGPT.

## 2. Entradas

- `PRODUCT_OR_PROJECT_NAME`
- `ORGANIZATION`
- `REPOSITORY`
- `VISIBILITY`
- `DEFAULT_BRANCH`
- `DESCRIPTION`
- `REFERENCE_ORGANIZATION`
- `INCUBATION_REPOSITORY`
- `GITHUB_APP_NAME`
- `GITHUB_APP_URL`
- `GITHUB_APP_INSTALL_URL`

Campos desconhecidos usam `UNKNOWN`; não devem ser omitidos silenciosamente.

## 3. Responsabilidades

### Copilot/agent

- verificar/criar organização quando permitido;
- verificar/criar repositório quando permitido;
- executar tudo que não dependa de interação humana;
- nunca abortar a tarefa inteira por causa de um gate manual;
- retornar handoff estruturado.

### Humano

- MFA, consentimento, confirmação de owner e demais controles não delegáveis;
- instalar/autorizar GitHub App quando exigido;
- selecionar repositórios na instalação quando necessário.

### ChatGPT

- verificar instalação e repositórios acessíveis;
- assumir o bootstrap de conteúdo depois que o conector enxergar o repositório;
- validar a evidência de execução.

## 4. Procedimento

1. Receber a tabela de variáveis.
2. Validar obrigatórias; marcar desconhecidas como `UNKNOWN`.
3. Verificar se a organização existe.
4. Se não existir, tentar criá-la.
5. Se a criação exigir ação humana, registrar `MANUAL GATE` e continuar qualquer etapa independente possível.
6. Verificar se o repositório existe.
7. Se não existir, tentar criá-lo com os parâmetros declarados.
8. Não transferir, apagar ou alterar o repositório de incubação.
9. Tratar instalação do `ChatGPT Codex Connector` como gate humano quando a interface exigir consentimento.
10. Fornecer ao humano o link de instalação, sem tentar criar uma GitHub App alternativa.
11. Após o gate, solicitar verificação independente pelo ChatGPT.
12. Encerrar com relatório de handoff machine-readable.

## 5. Regra contra desistência precoce

```text
ONE MANUAL STEP != WHOLE JOB IMPOSSIBLE
```

O executor deve tentar cada operação autorizada e isolar somente a etapa realmente não executável.

## 6. Saída mínima

```text
ORGANIZATION_EXISTS = YES|NO
ORGANIZATION_CREATED = YES|NO|NOT_POSSIBLE
REPOSITORY_EXISTS = YES|NO
REPOSITORY_CREATED = YES|NO|NOT_POSSIBLE
GITHUB_APP_INSTALLATION_REQUIRED = YES|NO|UNKNOWN
MANUAL_GATE = NONE|<descrição>
MANUAL_GATE_URL = <URL|NONE>
CHATGPT_VERIFICATION_REQUIRED = YES|NO
BLOCKERS = <lista|NONE>
NEXT_ACTOR = COPILOT|HUMAN|CHATGPT
NEXT_ACTION = <uma única ação>
```

## 7. Encerramento

O POP termina quando o repositório existe e está visível ao conector do ChatGPT, ou quando existe um blocker objetivo que impede chegar a esse estado.
