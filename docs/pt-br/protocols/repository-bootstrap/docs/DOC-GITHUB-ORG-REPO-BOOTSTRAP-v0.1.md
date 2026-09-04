# DOC — Controle do Bootstrap GitHub

**ID:** FLOWED-RBP-DOC-GITHUB-ORG-REPO-BOOTSTRAP  
**Versão:** 0.1-draft  
**Status:** DOGFOODING  
**Owner:** FlowED / RBP  
**POP associado:** `../pops/POP-GITHUB-ORG-REPO-BOOTSTRAP-v0.1.md`

## 1. Finalidade

Definir os critérios de qualidade, validação e evidência do POP de bootstrap GitHub. O POP descreve como executar; este DOC descreve como saber se a execução está correta e auditável.

## 2. Critérios de conformidade

### C1 — Identidade

- organização alvo identificada;
- repositório alvo identificado;
- produto/projeto identificado;
- valores ausentes explicitamente `UNKNOWN`.

### C2 — Separação de atores

A execução distingue claramente:

- ação automatizável;
- gate humano;
- verificação/handoff para ChatGPT.

### C3 — Não desistência

A existência de uma etapa manual não pode transformar etapas independentes automatizáveis em `NOT_POSSIBLE` sem tentativa ou evidência.

### C4 — Segurança

- nenhuma tentativa de contornar MFA/consentimento;
- nenhuma GitHub App substituta criada;
- nenhum recurso pago habilitado sem autorização;
- nenhum repositório de incubação transferido, apagado ou alterado fora do escopo.

### C5 — Conector

Quando utilizado o ChatGPT no GitHub:

```text
GITHUB_APP_NAME = ChatGPT Codex Connector
GITHUB_APP_URL = https://github.com/apps/chatgpt-codex-connector
GITHUB_APP_INSTALL_URL = https://github.com/apps/chatgpt-codex-connector/installations/new
```

A instalação deve ser verificada independentemente pelo ChatGPT depois do gate humano.

### C6 — Repositório operacional

PASS somente quando:

- o repositório alvo existe;
- a instalação do conector existe na organização quando requerida;
- o repositório aparece entre os repositórios acessíveis ao conector, ou há evidência explícita de que ainda falta autorização de repository scope.

## 3. Estados de avaliação

```text
STRUCTURAL_PASS
EVIDENCE_PASS
PARTIAL_PASS
MANUAL_GATE
FAIL
UNPROVEN
```

`STRUCTURAL_PASS` não prova acesso real. `EVIDENCE_PASS` exige teste do conector.

## 4. Evidências mínimas

Registrar, quando aplicável:

- nome da organização;
- Installation ID da GitHub App;
- lista/contagem de repositórios visíveis;
- repositório alvo visível: YES/NO;
- erro real retornado por uma ação que falhou;
- gate humano executado;
- próximo ator e próxima ação.

## 5. Não conformidades

Exemplos:

- executor desistiu de criar repositório porque não podia instalar a App;
- executor declarou uma ação impossível sem tentar;
- organização existe, App está instalada, mas nenhum repo está autorizado e o relatório diz `READY`;
- prompt omite variável desconhecida em vez de usar `UNKNOWN`;
- alteração acidental do repositório de incubação.

## 6. Critério de fechamento

```text
READY_FOR_CHATGPT =
  ORGANIZATION_EXISTS
  AND REPOSITORY_EXISTS
  AND CONNECTOR_INSTALLED_IF_REQUIRED
  AND REPOSITORY_VISIBLE_TO_CONNECTOR
```

Se falso, o documento deve identificar exatamente uma próxima ação executável.
