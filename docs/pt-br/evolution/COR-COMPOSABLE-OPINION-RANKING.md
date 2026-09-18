# COR — Composable Opinion Ranking

**Status:** nome candidato de produto / materializador de referência do Pilar 3. Não normativo para o FlowED.

## 1. Decisão desta rodada

O classificador composto de referência do Pilar 3 recebe o nome candidato **COR — Composable Opinion Ranking**.

COR é uma ferramenta/produto, não o contrato FlowED e não uma autoridade epistemológica do framework.

O papel do FlowED é afirmar que sustentação científica, normativa e empírica deve poder ser explicitada, transportada, relacionada e consultada por contrato. **Como transformar esses sinais em ranking, percentil, peso, score, classe ou opinião pertence ao classificador.**

Assim, toda a discussão metodológica de julgamento quantitativo é deslocada para o COR e para classificadores concorrentes. O Manifesto FlowED não deve carregar essa metodologia.

## 2. Princípio arquitetural

> **FlowED define a capacidade e o contrato; COR produz uma opinião através desse contrato.**

A confiabilidade, validade, qualidade metodológica, fontes, normalizações, pesos, composições, populações de ranking e demais decisões analíticas são responsabilidade do COR — ou de qualquer provider concorrente que ocupe a mesma capability.

O FlowED pode apresentar uma resposta recebida como, por exemplo, **“segundo COR, a avaliação é X”**. A autoria epistemológica da avaliação continua sendo do COR. O FlowED apenas preserva e projeta a identidade do provider e sua saída conforme o contrato.

Uma discordância sobre a nota do COR é, portanto, crítica ao COR. Uma crítica de que o contrato não consegue expressar informação necessária é crítica ao FlowED.

## 3. Hipótese metodológica interna do COR

Esta seção preserva as ideias discutidas até aqui como backlog metodológico do produto. Nenhuma delas é norma FlowED.

### 3.1 Reconhecimento científico formal

COR pode tratar como um sinal a existência de reconhecimento científico formal comprovável, distinguindo classes de artefato e processo quando necessário. Esse sinal não deve ser apresentado como verdade universal; é uma dimensão observável da sustentação.

### 3.2 Influência científica

COR pode consumir métricas externas no nível do trabalho, incluindo contagem de citações e indicadores normalizados por campo, idade e/ou tipo de publicação, como FWCI, FCR, CNCI ou equivalentes quando disponíveis.

Citações devem ser interpretadas como sinal de influência/atenção, não como prova automática de concordância ou correção.

### 3.3 Evidência operacional

COR pode considerar tempo de operação, volume de exposição/execuções, diversidade de contextos, incidentes, falhas, sucesso observado, recência e outros sinais operacionais quando disponíveis.

Tempo sozinho não precisa possuir o mesmo peso que tempo combinado com exposição suficiente; a fórmula é responsabilidade do produto.

### 3.4 Métricas sem máximo natural

Quando um indicador não possui máximo natural — por exemplo, número bruto de citações ou anos de uso — COR pode preferir posição relativa, ranking ou percentil em uma população comparável declarada em vez de inventar um teto arbitrário.

O universo comparável, a data do snapshot e os critérios de inclusão pertencem à metodologia do COR e devem ser explicitáveis quando necessários à interpretação da saída.

### 3.5 Composição

COR pode compor diferentes famílias de indicadores numa opinião agregada. Métricas fortemente correlacionadas ou que observem essencialmente o mesmo fenômeno devem ser tratadas cuidadosamente para evitar dupla contagem.

Métodos de composite indicators, análise de sensibilidade e outras técnicas reconhecidas são referências candidatas para o desenvolvimento do produto.

A eventual escala final — 0–10, 0–100, classes, percentis ou outra — é decisão do COR, não do contrato FlowED.

## 4. Transparência da opinião

Uma saída COR deve ser concebida como opinião identificável e reproduzível segundo sua própria versão metodológica. Como princípio de produto, o COR deve ser capaz de informar, conforme seu desenho evoluir:

- identidade e versão do classificador;
- valor/classe/opinião emitida;
- data ou snapshot relevante;
- fontes e métricas consideradas;
- transformações, ranking/percentis e normalizações aplicadas;
- pesos ou regras de composição quando existirem;
- dados ausentes ou incertezas relevantes;
- explicação/decomposição suficiente para auditoria;
- versão da metodologia.

Esses itens são backlog do COR. O contrato FlowED deverá exigir somente os metadados públicos que forem realmente necessários para interoperabilidade e correta interpretação da opinião, sem impor a metodologia interna.

## 5. Liberdade de providers

COR não recebe privilégio contratual por ser a implementação de referência. Uma equipe FlowED pode:

- usar COR;
- usar outro classificador;
- usar vários classificadores simultaneamente;
- comparar opiniões;
- ignorar score agregado e consumir somente evidências/observações;
- criar seu próprio classificador.

Um classificador concorrente pode usar metodologia completamente diferente e ainda ser plenamente conforme, desde que satisfaça o contrato público aplicável.

## 6. Confiabilidade do COR

A qualidade do COR é problema do próprio COR.

COR deve construir sua sustentação por pesquisa, referências científicas, benchmarking, validação, estudos de caso, uso longitudinal e demais evidências adequadas. O próprio COR pode ser avaliado como uma Referência dentro do Pilar 3.

Logo:

> **conformidade do COR com o contrato FlowED não prova qualidade da opinião do COR.**

Essa qualidade precisa ser defendida e melhorada pelo próprio projeto.

## 7. Papel no ecossistema

COR é candidato a produto aberto e progressivamente melhorável. Pode ser utilizado em contexto educacional, acadêmico, por bancas, laboratórios ou organizações, se seus usuários considerarem sua metodologia adequada.

Contribuições e metodologias alternativas são bem-vindas no projeto COR sem alterar a neutralidade do contrato FlowED.

O produto pode funcionar como materialização de referência, dogfood e prova de realizabilidade da capability de avaliação, mas nunca como fonte normativa obrigatória do FlowED.

## 8. Relação com o manifesto

O Pilar 3 deve defender apenas a posição filosófica/contratual de que **a sustentação de referências é informação relevante e deve poder permanecer explícita, rastreável e utilizável na decisão**.

O manifesto não deve especificar fórmula, peso, ranking, percentil, métrica preferida ou score canônico.

Em termos simples:

> **FlowED defende que o fator seja considerado e contratualmente representável. COR decide como julgá-lo.**

## 9. Naming

`COR — Composable Opinion Ranking` permanece nome candidato até revisão de naming/marca. O nome não deve ser promovido a conceito científico nem a termo normativo do FlowED sem análise específica.