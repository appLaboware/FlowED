# Pilar 3 — COR como classificador de opinião de referência

**Status:** candidato a produto / implementação de referência. Não normativo. Não define a verdade nem o score canônico do FlowED.

## 1. Nome candidato

O classificador composto de referência recebe o nome candidato:

**COR — Composable Opinion Ranking**.

COR é uma ferramenta/produto, não o contrato FlowED e não uma autoridade epistemológica do framework.

## 2. Decisão desta rodada

O Pilar 3 deve possuir um horizonte de contrato e uma alternativa concreta de materialização. COR reúne indicadores externos já praticados e produz uma opinião quantitativa versionada sobre a sustentação de uma referência.

COR terá exatamente o mesmo estatuto de qualquer outro provider compatível com o contrato FlowED:

- não é autoridade do FlowED;
- não define verdade;
- não é obrigatório;
- pode ser substituído por outro classificador;
- pode coexistir com classificadores concorrentes;
- sua confiabilidade, validade, pesos, rankings, normalizações e qualidade metodológica são problema do próprio COR, não do contrato FlowED.

A organização pode escolher outro provider de assessment. COR existe como alternativa pronta, dogfood e prova de realizabilidade.

## 3. Princípio

O produto recebe observações preservadas pelo contrato do Pilar 3, escolhe sua própria metodologia de normalização/composição e produz uma projeção quantitativa resumida.

A saída é explicitamente uma **opinião baseada em métricas**.

Regra:

> **dados observados + metodologia do classificador = opinião do classificador; opinião não equivale a verdade FlowED.**

Cumprir o contrato demonstra conformidade de interface/comportamento. Não demonstra que a opinião seja cientificamente ou empiricamente confiável. Essa sustentação pertence ao próprio provider e pode ser avaliada como qualquer outra Referência FlowED.

## 4. Relação com o contrato

O contrato do Pilar 3 não deve determinar:

- quais índices COR deve usar;
- como COR deve normalizá-los;
- que pesos devem existir;
- se valores sem máximo devem virar rank ou percentil;
- qual população de comparação é melhor;
- como sinais conflitantes devem ser agregados;
- se a escala final deve ser 0–100 ou outra.

Essas são decisões metodológicas do classificador.

O contrato deve apenas tornar possível receber uma opinião de maneira semanticamente interoperável, com os metadados mínimos necessários para identificar quem produziu a opinião, sua versão, escala e momento, além de extensões quando o provider desejar explicar sua metodologia.

## 5. Estratégia interna candidata do COR

Como decisão própria do produto — e não regra FlowED — COR poderá compor boas métricas externas e agrupá-las em famílias para reduzir dupla contagem.

Quando uma métrica tiver máximo natural ou escala normalizada, poderá aproveitar essa escala. Quando não houver máximo natural, COR poderá usar ranking/percentil em população declarada em vez de inventar um teto.

COR poderá usar metodologia de composite indicators, análise de sensibilidade e outras técnicas reconhecidas. A qualidade dessas decisões deve ser defendida e validada pelo próprio projeto COR.

## 6. Liberdade do adotante

Uma organização FlowED pode:

- usar COR;
- usar outro classificador;
- usar vários classificadores;
- comparar opiniões;
- ignorar scores agregados e usar somente evidências/observações;
- criar sua própria política de decisão sobre os resultados.

Nenhuma dessas escolhas altera a conformidade FlowED quando o contrato aplicável é cumprido.

## 7. Relação com o Pilar 1

COR demonstra a regra transversal:

> **FlowED é rígido no contrato e livre na materialização.**

O contrato define a capability. COR é uma materialização. Ferramentas concorrentes são bem-vindas e possuem igual estatuto contratual quando cumprem as mesmas obrigações públicas.

## 8. Relação com o Pilar 2

Evidência operacional produzida no Pilar 2 pode ser entrada do COR, se a metodologia do classificador decidir utilizá-la. O contrato preserva a disponibilidade e a semântica da evidência; COR decide o peso que atribui a ela.

## 9. Relação com o Pilar 3

O Pilar 3 não defende COR. Defende que sustentação científica, normativa e empírica seja explícita, rastreável e suficientemente importante para poder participar de decisões técnicas e filosóficas.

COR oferece apenas uma opinião quantitativa possível sobre essa base.

## 10. Estado

**Realizabilidade:** forte em nível conceitual e metodológico.

**Rota:** COMPOSE / EXPERIMENTAL PRODUCT.

**Naming:** `COR — Composable Opinion Ranking` é nome candidato de produto, sujeito a revisão de naming/marca. Não é termo científico nem elemento normativo do FlowED.
