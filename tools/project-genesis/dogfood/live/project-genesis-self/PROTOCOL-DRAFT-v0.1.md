# Project Genesis — Viability Discovery Protocol Draft v0.1

Status: `EMERGENT / DOGFOOD-DERIVED / UNVALIDATED`
Date: 2026-09-07
Origin: Project Genesis self-dogfood runs 001–004

## 1. Nature

Este documento não foi escrito antes do uso.

Ele é uma primeira consolidação das regras que surgiram ao analisar o próprio Project Genesis.

O protocolo deve continuar mudando quando novos casos revelarem falhas.

## 2. Founding rule

> **A ideia não é avaliada para receber aprovação. Ela é posicionada diante das evidências disponíveis e de suas alternativas de realização.**

## 3. Entrada mínima

```yaml
idea_statement: required
human_intent: required
known_constraints: optional
known_evidence: optional
known_artifacts: optional
```

Não exigir identidade, nome, domínio ou repositório antes de discovery suficiente.

## 4. Primeira sequência experimental

```text
RAW IDEA
   ↓
Q0 DEFINE CURRENT DECISION QUESTION
   ↓
SEARCH WHOLE EQUIVALENTS
   ↓
WHOLE ADMISSIBLE COVERAGE?
   ├─ sufficient → record coverage; do not decompose for sourcing reasons
   └─ insufficient / heterogeneous
          ↓
PROPOSE MINIMUM SPLIT
          ↓
DECLARE changed_decisions[]
          ↓
ΔD(split) MATERIAL?
   ├─ no → reject split
   └─ yes
          ↓
SEARCH EACH FACTOR
          ↓
CLASSIFY EVIDENCE RELATION
          ↓
MAP REALIZATION OPTIONS
          ↓
REGISTER UNCERTAINTY / COVERAGE
          ↓
REPEAT ONLY WHERE DECISIONALLY NECESSARY
```

## 5. Q0 — Decision Question

Toda passagem deve declarar a pergunta que a pesquisa pretende reduzir.

Exemplos:

```text
"Existe uma solução integral admissível?"
"Esta capability precisa ser própria?"
"Este split altera sourcing?"
"A diferenciação está no fator ou na relação?"
```

Sem pergunta decisória explícita, pesquisa pode acumular informação sem produzir decisão útil.

## 6. Whole-before-parts rule

Antes da primeira fatoração, procurar equivalentes integrais admissíveis.

Motivo:

Se um produto existente já resolve o conjunto de requisitos aceitavelmente, decompor primeiro pode desperdiçar esforço e criar falsa necessidade de composição própria.

## 7. Split admission rule

Um novo fator só entra na árvore se houver pelo menos uma decisão materialmente alterada.

Registro mínimo:

```yaml
split_id:
parent_factor:
child_factors: []
changed_decisions:
  - sourcing
  - candidate_correspondence
  - transformation
  - architecture
  - evidence_confidence
  - risk
  - license
  - cost
  - ownership
rationale:
delta_d: qualitative | experimental_numeric
```

Se `changed_decisions` estiver vazio, o split é superfatoração candidata.

## 8. Evidence relation classes

Todo candidato encontrado deve indicar a relação com o fator:

```text
WHOLE_EQUIVALENT
PARTIAL_CAPABILITY
COMPONENT_PROVIDER
STANDARD_PATTERN
ADJACENT_SOLUTION
ACADEMIC_ANTECEDENT
INSTITUTIONAL_PRACTICE
```

Essas classes podem evoluir com dogfood.

## 9. Evidence record mínimo

```yaml
claim_id:
claim:
status: fact | inference | hypothesis
factor_id:
evidence_relation:
sources: []
search_scope:
search_date:
coverage:
confidence:
counterevidence: []
assumptions: []
open_questions: []
```

## 10. Perfis separados

O protocolo não pode colapsar em uma nota única:

```text
PROBLEM / OPPORTUNITY EVIDENCE
REALIZATION / SOURCING
EXCLUSIVITY / DIFFERENTIATION
EVIDENCE STRENGTH
HUMAN ALIGNMENT
```

Em particular:

```text
PERTINENCE != NEED_FOR_PROPRIETARY_BUILD
EVIDENCE != HUMAN PREFERENCE
EXCLUSIVITY != BUSINESS VALUE
ABSENCE_FOUND != NOVELTY
```

## 11. Realization model — ainda experimental

Não assumir escada linear definitiva.

Registrar provisoriamente pelo menos:

```yaml
provenance: existing | modified | invented | unknown
transformation: none | configure | extend | adapt | unknown
architecture: direct | compose | reconfigure | unknown
source: OSS | COTS | service | standard | internal | outsourced | unknown
```

A antiga lista `ADOPT/CONFIGURE/EXTEND/ADAPT/COMPOSE/INVENT` pode continuar como projeção humana, mas não é ainda a ontologia canônica.

## 12. Stopping rule

Parar de decompor quando nova divisão não alterar materialmente as decisões relevantes.

Hipótese formal em investigação:

```text
ΔD(split) < ε
```

Não existe ainda escala ou valor validado para `ε`.

## 13. Process states

Estados do protocolo não são decisões humanas.

Candidatos iniciais:

```text
INSUFFICIENT_EVIDENCE
CONTINUE_INVESTIGATION
FACTOR_STABLE_FOR_CURRENT_SCOPE
WHOLE_COVERAGE_SUFFICIENT
READY_FOR_NEXT_STAGE
MATERIALIZATION_BLOCKED
```

Não usar como equivalente automático de:

```text
BUILD
PIVOT
STOP
INVEST
```

## 14. Pre-materialization gate

Materialização de nova capability/projeto fica bloqueada enquanto houver qualquer um:

```text
DOMAIN_OWNERSHIP_UNRESOLVED
SOURCING_UNRESOLVED
RESIDUAL_NOT_ESTABLISHED
MATERIALIZATION_NOT_AUTHORIZED
```

Protótipos prematuros podem existir apenas como artefatos reversíveis e não autoritativos.

## 15. Foreign artifact ingestion

Artefato vindo de fora do fluxo entra como:

```text
FOREIGN / NON-AUTHORITATIVE EVIDENCE
```

Seu conteúdo é avaliado por átomo:

```text
ADOPT
MODIFY
REJECT
```

sem herdar autoridade de domínio, topologia ou maturidade.

## 16. Dual output obrigatório

Cada run deve produzir:

### A — project-position evidence

O que aprendemos sobre a proposta analisada.

### B — protocol/implementation evidence

O que aprendemos que o próprio protocolo/tool precisa mudar ou suportar.

Modelo:

```text
OBSERVATION
   ↓
RESULT DELTA
   ↓
MISSING RULE
   ↓
PROTOCOL CHANGE
   ↓
IMPLEMENTATION REQUIREMENT
```

## 17. Dogfood-derived development rule

> **Nenhuma correção pode ser apenas textual. Toda correção material deve declarar qual ausência, ambiguidade ou erro de regra permitiu o problema.**

## 18. Reproducibility record

Cada execução deve preservar:

```yaml
assessment_id:
protocol_version:
date:
subject_version:
evidence_snapshot:
search_queries:
sources:
factorization_before:
factorization_after:
rules_added_or_changed: []
implementation_requirements: []
```

## 19. Current limitations

Este protocolo ainda não possui:

- systematic search procedure;
- search saturation criterion validado;
- coverage metric validada;
- confidence grading validado;
- `ΔD` operacionalizado;
- inter-rater calibration;
- scoring calibration;
- validated ontology;
- empirical proof of usefulness.

Portanto esta versão é um artefato de aprendizagem, não um standard.

## 20. Próximo teste

Aplicar esta versão manualmente em `A1 — elicitation / assumptions` do próprio Project Genesis.

O próximo run deve registrar:

1. entrada manual original;
2. saída usando este protocolo;
3. delta entre ambas;
4. regra ausente encontrada;
5. mudança de protocolo;
6. requisito de implementação correspondente.
