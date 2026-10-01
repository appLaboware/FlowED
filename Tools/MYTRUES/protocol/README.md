# MyTrues Open Decision Protocol — draft 0.1

## Objetivo

Permitir que qualquer sistema consulte um serviço decisório sem conhecer:

- banco de dados;
- embeddings;
- grafo;
- heurísticas;
- pesos;
- modelo estatístico;
- LLM;
- algoritmo de ranking;
- implementação MyTrues.

## Operação síncrona mínima

`POST /v1/decisions/{decision-key}`

Para o protótipo:

`decision-key = resolve.failure`

## Semântica adotada de DMN

O protocolo usa os conceitos de:

- decision service;
- inputs;
- context;
- decision output.

Ele NÃO exige que o engine interno seja DMN nem que exponha tabelas/regras DMN.

## Request

Um request contém:

- `protocol`: versão do protocolo;
- `requestId`: identidade idempotente/correlacionável;
- `subject`: aquilo sobre o qual se decide;
- `context`: fatos disponíveis;
- `constraints`: limites impostos pelo chamador.

O cliente pode enviar `traceparent` e `tracestate` conforme W3C Trace Context.

## Response

Uma decisão bem sucedida informa:

- decisão selecionada;
- ação semântica;
- resultado proposto;
- guardas que foram satisfeitas;
- aviso que deve ser apresentado ao usuário;
- versão opaca do engine/policy.

O response **não precisa explicar o algoritmo de ranking**.

## Erros

Falhas do protocolo usam `application/problem+json` conforme RFC 9457.

Exemplos:

- decisão desconhecida;
- contexto insuficiente;
- nenhuma decisão aprovada;
- guardas não satisfeitas;
- engine indisponível.

## Eventos opcionais

Eventos como:

- decision.requested;
- decision.made;
- decision.executed;
- decision.outcome.observed;

podem ser emitidos em CloudEvents 1.0.

## Regra de interoperabilidade

Um cliente CONFORME não pode depender de:

- nome do banco;
- Neo4j;
- tamanho/dimensão de embedding;
- algoritmo de similaridade;
- pesos/ranking;
- fornecedor de LLM;
- implementação do engine.

Esses elementos são privados do decisor.
