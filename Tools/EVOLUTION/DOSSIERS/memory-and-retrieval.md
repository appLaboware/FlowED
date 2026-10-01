# Dossiê — Memória, Grafo e Recuperação

## SQLite

Papel atual:

- referência mínima;
- persistência por fornecedor;
- prova de restart;
- fácil portabilidade.

Próximos testes:

- migrations;
- concorrência;
- locking;
- backup;
- export/import;
- retention;
- versionamento de casos.

SQLite não é tratado como limite de produto.

## Neo4j

Papel:

- property graph para Failure/Case/Decision/Evidence/Execution;
- vector indexes;
- candidate retrieval;
- exploração de graph + semantic retrieval.

Estado observado em 2026:

- Community Edition oferece vector indexes;
- Neo4j 2026.04/Cypher 25 depreca procedures antigas de vector query em favor da
  cláusula `SEARCH`.

Logo, o laboratório deve evitar cristalizar APIs já depreciadas.

## Regra de autoridade

Vector similarity recupera candidatos; não autoriza ação operacional.

A autoridade pode vir de:

- decisão humana aprovada;
- regra explícita;
- policy aprovada;
- futuro Core validado e dentro de constraints.

## Estado da arte a explorar

- BM25/lexical baseline;
- dense vector;
- graph traversal;
- hybrid retrieval;
- reranking;
- temporal/version-aware retrieval;
- provenance-aware retrieval;
- case competence;
- diversity;
- novelty detection;
- out-of-distribution detection.

## Benchmark

Medir:

- recall@k de casos relevantes;
- precision@k;
- MRR/NDCG quando houver ranking;
- latência;
- custo;
- taxa de caso desconhecido corretamente abstido;
- efeito no resultado decisório final.

## Gate

Escolher backend por benchmark e requisitos operacionais, não por preferência de
tecnologia.
