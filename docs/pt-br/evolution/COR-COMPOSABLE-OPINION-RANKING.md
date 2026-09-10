# COR — Composable Opinion Ranking

**Status:** nome candidato de produto / materializador de referência do Pilar 3. Não normativo para o FlowED.

## Decisão desta rodada

O classificador composto de referência do Pilar 3 recebe o nome candidato **COR — Composable Opinion Ranking**.

COR é uma ferramenta/produto, não o contrato FlowED e não uma autoridade epistemológica do framework.

O papel do FlowED é definir o contrato público da capability de avaliação/sustentação. Qualquer ferramenta que cumpra esse contrato pode ser usada e pode ser considerada uma materialização válida da capability. COR será apenas uma implementação de referência oferecida pelo ecossistema.

## Princípio arquitetural

**FlowED = contrato. COR = uma opinião que materializa esse contrato.**

A confiabilidade, qualidade metodológica, escolhas de normalização, pesos, composição de métricas, população de ranking e demais decisões analíticas pertencem ao COR e às ferramentas concorrentes, não ao contrato FlowED, exceto pelos metadados estritamente necessários para interoperabilidade e interpretação do resultado.

## Sentido do nome

- **Composable** — a ferramenta pode compor diferentes fontes, índices, métricas e adapters sem tornar nenhum deles obrigatório;
- **Opinion** — o resultado é uma opinião quantitativa produzida por uma metodologia específica, não uma verdade declarada pelo FlowED;
- **Ranking** — quando uma métrica não possui máximo natural, a ferramenta pode preferir posição relativa/ranking/percentil em uma população declarada, além de poder produzir uma classificação agregada própria.

## Liberdade de providers

COR não recebe privilégio contratual por ser a implementação de referência. Uma equipe FlowED pode:

- usar COR;
- usar outro classificador;
- usar vários classificadores simultaneamente;
- comparar opiniões;
- não usar score agregado e consumir apenas as evidências do contrato.

A qualidade de cada classificador é responsabilidade do próprio classificador e pode, por sua vez, ser avaliada como qualquer outra referência dentro do Pilar 3.

## Relação com o manifesto

O Pilar 3 deve defender o **fazer contratual**: sustentação explícita, rastreável e avaliável por providers substituíveis. Não deve defender COR nem qualquer ferramenta concreta.

COR existe paralelamente como prova de materialização plausível e como futuro produto por composição.

## Naming

`COR — Composable Opinion Ranking` permanece nome candidato até revisão de naming/marca. O nome não deve ser promovido a conceito científico nem a termo normativo do FlowED sem análise específica.
