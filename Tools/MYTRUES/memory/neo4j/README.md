# Neo4j decision-memory adapter

Esta pasta contém a promoção da memória experimentada no
`Tools/IDEOS/experiments/EXP-007-decision-memory`.

Ela é uma implementação de armazenamento/retrieval, não o algoritmo MyTrues.

O grafo guarda:

- Failure;
- Decision;
- Action;
- Guard;
- Execution/outcome.

O índice vetorial existe para recuperação de candidatos. A seleção/ranking entre
candidatos pertence ao `DecisionEngine` e pode ser substituída por uma implementação
proprietária.

O seed contém, para a mesma falha de DNS, duas decisões aprovadas:

- usar FQDN Azure;
- expor IP público.

Isto permite que dois engines conformes escolham decisões diferentes sem mudar o
protocolo externo.
