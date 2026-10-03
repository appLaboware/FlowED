<!--
ARCHAEOLOGY COPY — NOT NORMATIVE
Source repository: InitProjHQ/InitProj
Source path: docs/plans/PLAN-MYTRUES-THESIS-0001.md
Source blob SHA: 6155909e20ff546ac33c163cabf5431997e462d6
Copied for historical/research preservation during MyTrues consolidation.
-->

# PLAN-MYTRUES-THESIS-0001 — MyTrues como protocolo executável (tese)

**Status:** PROPOSTA (planejamento apenas)
**Data:** 2026-01-22
**Base:** DEV/drafts/mytrues/estudo01.md

---

## 1) Veredito (faz sentido?)

**Faz sentido** se o foco for: **protocolo executável** (não “novo paradigma”) com **PROV + Design Rationale**, **merge/reavaliação**, **views compiladas** e **avaliação empírica**. Sem isso, não é tese A1; vira “mais uma ferramenta”.

---

## 2) Tese (enquadramento)

**Tese A (forte):** CCP como protocolo executável mapeado para **PROV-DM** + **IBIS/QOC**, com **semântica de reavaliação/merge** e **views compiladas** (ADR/Onboarding/Policy), validado por métricas.

**MyTrues = implementação de referência** do protocolo (não o “produto” em si).

---

## 3) Adoções (usar o mundo, não reinventar)

**Padrões:**

- PROV-DM (proveniência)
- IBIS/QOC (design rationale)
- ADR (como *view* renderizada)

**Ferramentas (plugáveis):**

- Vector DB: **Chroma ou Qdrant** (planejado; não reimplementar)
- Publicação: **MkDocs/Docusaurus** para views

**Status:**

- PROV/IBIS/ADR: **planejado (adotar)**
- Vector DB: **planejado (plugar)**
- Publicação: **planejado (plugar)**

---

## 4) Modelo mínimo do protocolo (CCP)

### 4.1 Entidades (núcleo)

- **Issue** (pergunta/decisão)
- **Option** (alternativa)
- **Criteria** (critérios)
- **Decision** (escolha)
- **Rationale** (argumentos)
- **Evidence** (links/documentos)
- **Provenance** (PROV: entity/activity/agent)

### 4.2 Semântica operacional

- **reopen** (reavaliar)
- **supersede** (substituir decisão anterior)
- **deprecate** (obsoletar)
- **valid_from / valid_to**
- **trigger** (condição para reabrir)

---

## 5) Views compiladas (não manual)

- **ADR view** (auto‑gerada)
- **Onboarding view**
- **Policy/Rule view**
- **Risk view**
- **Change timeline view**

---

## 6) Avaliação (mínimo A1)

**Hipóteses mensuráveis:**

- Redução do tempo de re‑deliberação (X%)
- Redução de inconsistência entre decisões correlatas
- Melhoria no onboarding (tempo até primeira entrega válida)

**Baseline comparativo:**

- ADR puro vs MyTrues (CCP + views + agente consultando)

---

## 7) Plano de implementação (fases)

### Fase 1 — Protocolo e schema

- Definir schema CCP mapeado para PROV/IBIS/QOC
- Definir semântica de reavaliação/merge
- Definir views alvo (ADR/Policy/Onboarding)

### Fase 2 — Ferramentas de referência

- CLI: criar/editar/merge/conflict
- Export: JSONL
- Static docs: MkDocs/Docusaurus

### Fase 3 — Integração com InitProj

- Injeção de contexto nos prompts (já existe)
- Gate de consistência de CCP (lint/validate)

### Fase 4 — Avaliação empírica

- Executar estudo comparativo (ADR vs CCP)
- Medir métricas e publicar resultados

---

## 8) Descrição e tags dos repositórios (MyTrues org)

### Repo PROD (MyTrues)

**Descrição sugerida:**
“Creator Cognitive Path (CCP) protocol and tools for decision provenance, rationale, and compiled knowledge views.”

**Tags sugeridas:**
`provenance`, `design-rationale`, `adr`, `decision-records`, `knowledge-graph`, `ccp`, `agentic`, `governance`, `documentation`, `llm`

### Repo DEV (MyTrues_p)

**Descrição sugerida:**
“Development workspace for MyTrues CCP protocol, experiments, and integration with InitProj.”

**Tags sugeridas:**
`dev`, `experiments`, `ccp`, `initproj`, `provenance`, `design-rationale`

---

## 9) Arquivos relacionados no projeto (caminhos)

- tools/MyTrues/MyTrues.sh
- tools/MyTrues/tools/mytrues_vector.py
- tools/MyTrues/tools/mytrues_uuid.py
- tools/MyTrues/tools/mytrues_export.py
- tools/MyTrues/tools/mytrues_merge.py
- tools/MyTrues/tools/mytrues_static.py
- tools/MyTrues/docs/pt-br/*
- config/mytrues.env
- client-template/config/mytrues.env
- scripts/py/tools/prompt_ops.py

---

**Fim do plano — aguardando aprovação humana.**
