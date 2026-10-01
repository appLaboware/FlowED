# Neo4j decision-memory — referência histórica/modelagem

**STATUS: NOT A PRODUCT RUNTIME DEPENDENCY.**

Esta pasta preserva o material utilizado no
`Tools/IDEOS/experiments/EXP-007-decision-memory`.

A banca de 2026-10-01 classificou Neo4j Community/GPLv3 como **VERMELHO** para a
baseline de produto. Portanto:

- MyTrues de referência continua usando SQLite;
- nenhum cliente/protocolo MyTrues depende de Neo4j;
- este diretório serve para reconstruir o experimento e estudar o modelo de grafo;
- o `docker-compose.yml` daqui não é recomendação de runtime;
- trabalho futuro de graph/vector retrieval deve usar implementação com licença
  aprovada ou permanecer documental.

O schema conceitual experimentado continua útil:

- Failure;
- Decision;
- Action;
- Guard;
- Evidence;
- Execution / Outcome.

EXP-007 também experimentou índice vetorial para candidate retrieval, mas similaridade
nunca foi autoridade de execução. Essa regra independe do backend.
