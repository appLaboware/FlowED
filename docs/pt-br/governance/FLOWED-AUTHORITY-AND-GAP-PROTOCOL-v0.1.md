# FlowED Authority and Gap Protocol — FAGP 0.1

**ID:** FLOWED-AUTHORITY-AND-GAP  
**Versão:** 0.1-draft  
**Status:** DOGFOODING  
**Owner de domínio:** FlowED  
**Escopo:** autoridade normativa do FlowED sobre projetos que o adotam e procedimento obrigatório quando o FlowED não oferece base suficiente para decidir ou executar.

## 1. Princípio central

Todo projeto que adota FlowED deve usar o FlowED como fonte normativa de processo, decisão institucionalizada, gates, padrões, templates, protocolos e ferramentas aplicáveis ao seu escopo.

```text
FLOWED IS THE LAW FOR FLOWED-ADOPTING PROJECTS.
```

Nenhum PO, PM, Dev ou agente pode simplesmente ignorar, substituir ou optar por não usar uma regra, protocolo, template, gate ou ferramenta aplicável do FlowED.

## 2. Regra de autoridade

Quando o FlowED já define como tratar uma situação:

```text
FLOWED HAS APPLICABLE RULE
        ↓
USE IT
        ↓
DO NOT RE-DECIDE LOCALLY
```

A existência de preferência pessoal, alternativa conhecida, experiência anterior ou ferramenta concorrente não autoriza bypass.

## 3. Gap de autoridade

Quando o FlowED não define base suficiente para uma decisão necessária:

```text
FLOWED DOES NOT RESOLVE THE CASE
        ↓
STOP
        ↓
DECLARE GAP
        ↓
ESCALATE TO FLOWED AUTHORITY
        ↓
RESOLVE / EXTEND FLOWED FIRST
        ↓
ONLY THEN RESUME PROJECT WORK
```

O ator não deve improvisar uma regra local permanente para contornar a ausência.

## 4. Stop-the-line

A ausência de regra adequada é um bloqueio legítimo.

```text
NO FLOWED BASIS -> NO LOCAL DECISION
```

O projeto pode permanecer parado pelo tempo necessário. Prazo, velocidade ou conveniência não têm precedência sobre coerência institucional quando não há cliente externo aguardando entrega contratual.

## 5. Crítica é permitida; bypass não

FlowED é normativo, mas criticável.

Um ator pode e deve registrar:

- insuficiência;
- ambiguidade;
- conflito entre regras;
- regra impraticável;
- custo excessivo;
- ausência de cobertura;
- oportunidade de melhoria.

Mas a crítica segue este fluxo:

```text
CRITICIZE
    ↓
MATERIALIZE GAP / CHANGE REQUEST
    ↓
FLOWED AUTHORITY REVIEWS
    ↓
FLOWED CHANGES OR REJECTS
    ↓
PROJECT CONTINUES UNDER RESOLVED RULE
```

## 6. Papel por nível

### PO

Pode identificar gaps, propor alternativas e justificar impacto, mas não criar exceção normativa silenciosa.

### PM

Deve aplicar o FlowED e escalar lacunas que impeçam decomposição ou coordenação.

### Dev

Deve executar instruções já delimitadas. Se a instrução exigir decisão não coberta, retorna blocker; não inventa política.

## 7. Artefato mínimo de gap

Todo gap deve registrar no mínimo:

- `PROJECT_ID`
- `ACTOR_ID`
- `ROLE`
- `DECISION_NEEDED`
- `FLOWED_RULES_CONSULTED`
- `WHY_INSUFFICIENT`
- `LOCAL_WORK_BLOCKED`
- `PROPOSED_OPTIONS`
- `IMPACT_IF_UNRESOLVED`
- `EVIDENCE`
- `STATUS`

Valores desconhecidos devem ser `UNKNOWN`.

## 8. Estados

```text
OPEN
UNDER_REVIEW
RESOLVED_BY_EXISTING_RULE
FLOWED_CHANGE_REQUIRED
FLOWED_CHANGED
REJECTED
CLOSED
```

## 9. Regra de retomada

O projeto só retoma o trabalho bloqueado quando houver uma destas condições:

```text
A) EXISTING FLOWED RULE IDENTIFIED
B) FLOWED RULE CLARIFIED
C) FLOWED RULE CREATED OR REVISED
D) FORMAL EXCEPTION EXPLICITLY AUTHORIZED BY FLOWED AUTHORITY
```

Sem uma dessas condições, o blocker permanece válido.

## 10. Relação com eficiência decisória

Este protocolo evita pagar novamente por decisões já tomadas e transforma lacunas reais em evolução do próprio FlowED.

```text
PROJECT GAP
    ↓
FLOWED LEARNS
    ↓
RULE / TEMPLATE / CONTRACT / TOOL
    ↓
NEXT PROJECT DOES NOT REPEAT THE CONVERSATION
```

## 11. Regra final

```text
USE FLOWED WHEN FLOWED KNOWS.
STOP WHEN FLOWED DOES NOT KNOW.
IMPROVE FLOWED BEFORE CONTINUING.
DO NOT BYPASS THE LAW LOCALLY.
```
