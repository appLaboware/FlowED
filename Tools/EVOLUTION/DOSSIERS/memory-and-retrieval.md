# Dossiê — Memória, Grafo e Recuperação

## Decisão de licenciamento da banca — 2026-10-01

A baseline de produto **não** adota Neo4j Community como runtime de memória.

Classificação recebida:

- Neo4j Community: GPLv3 — **VERMELHO**;
- Porter administrative storage observado com MongoDB 8.0: SSPL transitivo — **VERMELHO**.

Consequência:

- SQLite continua sendo a memória persistente de referência do MyTrues;
- Neo4j fica apenas como referência histórica de experimento e como inspiração de
  **schema/modelagem de grafo**;
- nenhuma arquitetura MyTrues pode assumir Neo4j como dependência;
- Porter precisa provar/configurar storage administrativo com licença aceitável antes
  de qualquer promoção a runtime de produto.

Esta decisão não apaga a evidência histórica dos experimentos que executaram essas
tecnologias.

## SQLite — runtime de referência

Papel atual:

- referência mínima;
- persistência por fornecedor;
- prova de restart;
- fácil portabilidade;
- runtime aprovado para conformance atual.

Próximos testes:

- migrations;
- concorrência;
- locking;
- backup;
- export/import;
- retention;
- versionamento de casos.

SQLite é baseline executável, não limite científico nem backend final obrigatório.

## Modelo de grafo — aberto e independente de backend

O modelo conceitual continua válido:

- Failure / Case;
- Decision;
- Action;
- Guard;
- Evidence;
- Execution / Outcome;
- Provenance.

Recuperação em grafo, vetorial ou híbrida é técnica pública e permanece OPEN. A
implementação futura deve poder ser trocada sem alterar o protocolo MyTrues.

## Neo4j — somente referência histórica/schema

EXP-007 utilizou Neo4j Community e provou um POC de decision memory.

Daqui em diante:

- `Tools/MYTRUES/memory/neo4j/` é referência histórica/modelagem;
- seu `docker-compose.yml` não define runtime de produto;
- novos claims de produto não podem depender dele;
- detalhes Cypher/vector não entram no protocolo aberto;
- benchmarks futuros precisam de backend/licença aceitável.

## Porter administrative storage

EXP-002 observou o runtime administrativo Porter criando
`porter-mongodb-docker-plugin`.

A banca marcou o caminho MongoDB 8.0/SSPL como risco transitivo VERMELHO para produto.

Antes de promover Porter de laboratório a runtime de produto, R1 deve:

1. identificar opções oficiais de storage;
2. executar ao menos uma opção com licença aceitável;
3. verificar lifecycle/state/restart;
4. documentar migração/backup;
5. manter upstream imutável.

Nenhum fork é autorizado apenas para contornar licença enquanto configuração/plugin
oficial puder resolver.

## Regra de autoridade

Similaridade, grafo ou vetor recuperam candidatos; não autorizam ação operacional.

A autoridade pode vir de decisão humana aprovada, regra/policy explícita ou futuro Core
validado dentro de constraints.

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

- recall@k;
- precision@k;
- MRR/NDCG quando houver ranking;
- latência;
- custo;
- taxa de caso desconhecido corretamente abstido;
- efeito no resultado decisório final;
- licença/redistribuição como gate não funcional.

## Gate

Escolher backend por benchmark, requisitos operacionais **e licença**. Nenhum backend
de memória faz parte do protocolo MyTrues.
