# Run 004 — Primeira passagem de descoberta de viabilidade

Status: `ACTIVE / EXPLORATORY / UNVALIDATED`
Date: 2026-09-07
Subject: `Project Genesis` analisado por `Project Genesis`

## 1. Pergunta deste run

Não perguntar se a ideia é "boa".

Perguntar:

> Qual é a posição observável do Project Genesis diante do que já existe e qual parcela, se alguma, continua exigindo desenvolvimento ou pesquisa próprios?

Este run também deve produzir regras para a próxima versão do próprio protocolo.

## 2. Escopo mínimo desta passagem

Esta passagem testa apenas a região:

```text
A — Evidence Positioning & Discovery
```

Não assume que os fatores internos atuais estejam corretos.

## 3. Busca exploratória realizada

Foram pesquisadas cinco famílias de antecedente:

1. AI idea validation / evidence-first startup analysis;
2. component sourcing / make-or-buy / OSS-COTS-in-house decision support;
3. software reuse decision frameworks;
4. evidence-first validation methods;
5. project discovery / planning systems adjacentes.

Esta não é uma revisão sistemática e não autoriza claim de saturação.

## 4. Evidência encontrada

### 4.1 Idea validation/evidence positioning é categoria existente

Produtos recentes já oferecem:

- competitor discovery;
- market evidence;
- live-source research;
- evidence-linked claims;
- structured reports;
- scoring, verdicts ou next actions.

Exemplos observados nesta passagem:

- MITPO Idea Validation — competitor signals e pressure-test por lentes;
- Preuve AI — múltiplas fontes, competitor mapping, viability scoring e sourced claims;
- RoastIdea — research com evidência, assumptions explícitas e verdict;
- Idea Score — market/competitor report + scorecard;
- outros validadores adjacentes.

Conclusão parcial:

```text
"AI analisa ideia com pesquisa e evidência"
```

não é residual defensável por si só.

### 4.2 Sourcing de componentes possui literatura e processos prévios

A literatura encontrada cobre decisões entre:

```text
IN-HOUSE
OUTSOURCE
COTS
OSS
```

Há evidência industrial de que múltiplas opções são consideradas e que decisões continuam fortemente dependentes de expert judgment.

Também há trabalho propondo process-line para seleção de origem e componentes e estudos sobre critérios estruturados de sourcing.

Conclusão parcial:

```text
"decidir entre fazer, comprar ou reutilizar"
```

é conhecido e não deve ser reivindicado como invenção.

### 4.3 Evidence-first sem score também não é suficiente como diferenciação

Há abordagens que explicitamente criticam score instantâneo e defendem evidência comportamental ou separação entre evidence e inference.

Logo:

```text
NO SCORE
+
EVIDENCE FIRST
```

sozinho também não estabelece residual próprio.

## 5. Primeiro efeito PMFN

A região `Evidence Positioning & Discovery` ainda é grossa demais.

A busca mostra pelo menos três decisões distintas:

```text
A1 — problem/assumption elicitation
A2 — external evidence discovery
A3 — realization/sourcing analysis of factors
```

O split é material porque:

- A1 pode ser amplamente atendido por LLM/workflow comum;
- A2 pode ser fornecido por search/research providers;
- A3 conecta decomposição suficiente com sourcing/reuse e parece depender de semântica própria ainda não comprovada.

Portanto:

```text
ΔD(split) = MATERIAL
```

sem valor numérico.

## 6. Novo fator candidato que emergiu da experiência

O protocolo precisa distinguir duas perguntas que estavam misturadas:

```text
Q1 — EXISTE EVIDÊNCIA SOBRE O PROBLEMA/OPORTUNIDADE?
Q2 — COMO A SOLUÇÃO PROPOSTA DEVE SER REALIZADA?
```

Elas pertencem a planos diferentes.

Uma proposta pode ter:

```text
alta pertinência do problema
+
baixa necessidade de construção própria
```

ou o inverso.

Logo, `PERTINENCE` e `REALIZATION/SOURCING` não podem compartilhar um único score ou verdict.

## 7. Hipótese residual atual — ainda não claim

Depois desta passagem, o residual mais interessante continua concentrado em:

1. fatoração mínima decisionalmente suficiente;
2. vínculo explícito entre cada fator e alternativas de realização;
3. stopping rule de decomposição baseada em ganho decisional;
4. preservação de relações arquiteturais enquanto se busca reuso;
5. evidence coverage/confidence acopladas a cada conclusão;
6. genealogia temporal da proposta e das decisões;
7. continuidade do discovery até artefatos de projeto sem confundir discovery com materialização.

Cada item permanece `RESEARCH / INVESTIGATE`.

## 8. Protocolo descoberto por esta passagem

### VP-001 — Start with questions, not scores

O protocolo começa por perguntas decisórias explícitas. Score é projeção posterior e opcional.

### VP-002 — Separate problem evidence from solution realization

Pertinência do problema e estratégia de realização são eixos independentes.

### VP-003 — Search whole-equivalents before decomposition

Antes de fatorar, procurar solução integral admissível. Só fatorar quando a busca mostrar que diferentes partes exigem decisões diferentes.

### VP-004 — Factor only when the split changes a decision

Todo split precisa declarar qual decisão mudou.

### VP-005 — Search by factor after the split

Uma vez criado um fator, a busca passa a ser específica daquele fator. Concorrentes gerais não podem ser tratados como prova de cobertura de todas as partes.

### VP-006 — Evidence class must be explicit

Para cada achado, registrar se ele é:

```text
WHOLE EQUIVALENT
PARTIAL CAPABILITY
COMPONENT/PROVIDER
STANDARD/PATTERN
ADJACENT SOLUTION
ACADEMIC ANTECEDENT
INSTITUTIONAL PRACTICE
```

### VP-007 — No novelty from absence

`não encontrei` significa apenas ausência dentro do escopo pesquisado.

### VP-008 — No automatic verdict

O protocolo posiciona. Decisões como continuar, mudar, adotar ou parar pertencem ao humano/organização.

## 9. O que esta passagem diz sobre a viabilidade do Project Genesis

Ainda não há base para afirmar viabilidade comercial ou científica da tool inteira.

Há, porém, base suficiente para afirmar:

```text
BROAD IDEA VALIDATION            = heavily covered
GENERIC EVIDENCE RESEARCH        = heavily covered
GENERIC COMPONENT SOURCING       = known
GENERIC MAKE/BUY/REUSE            = known
NO-SCORE / EVIDENCE-FIRST         = not exclusive

PMFN stopping semantics           = investigate
factor→realization mapping        = investigate
architecture-preserving reuse     = investigate
longitudinal evidence genealogy   = investigate
integrated neutral pre-consulting = investigate
```

Portanto o resultado não é GO nem NO-GO.

É:

```text
CONTINUE INVESTIGATION AT NARROWER FACTORIZATION
```

como estado do processo, não como julgamento da ideia.

## 10. Próximo split ao vivo

Próxima passagem deve analisar separadamente:

```text
A1 — elicitation / assumptions
A2 — evidence discovery
A3 — factorization + realization matching
```

Para cada um:

1. buscar whole-equivalent;
2. buscar OSS/COTS/API/standard/paper;
3. classificar cobertura;
4. só subdividir se `ΔD(split)` for material;
5. registrar regras novas descobertas pela própria experiência.

## 11. Implementation requirements descobertos

### IR-010 — Question ledger

Cada execução precisa registrar a pergunta decisória corrente antes de pesquisar.

### IR-011 — Evidence-class taxonomy

Cada candidato precisa ter classe de relação com o fator analisado.

### IR-012 — Split-decision link

Nenhum fator novo pode existir sem um `changed_decisions[]` explícito.

### IR-013 — Separate problem and realization profiles

O schema deve impedir que pertinência seja confundida com necessidade de construção própria.

### IR-014 — Process-state vocabulary

Estados como `CONTINUE_INVESTIGATION`, `INSUFFICIENT_EVIDENCE` ou `READY_FOR_NEXT_STAGE` devem ser separados de decisões humanas como `BUILD`, `STOP` ou `PIVOT`.

## 12. Valor como exemplo

Este run demonstra o uso correto da ferramenta:

- começamos por uma pergunta grossa;
- buscamos antecedentes antes de inventar;
- descobrimos que a categoria ampla já existe;
- fatoramos somente porque a busca alterou decisões;
- não emitimos nota nem claim de novidade;
- a própria execução produziu regras do protocolo e requisitos de implementação.

A experiência é simultaneamente:

```text
USO
+
PESQUISA
+
DESIGN DO PROTOCOLO
+
DESIGN DA IMPLEMENTAÇÃO
+
DOCUMENTAÇÃO DE EXEMPLO
```
