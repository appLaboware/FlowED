# Algorithm boundary

## Público

São parte do protocolo aberto:

- endpoint e métodos;
- schemas de request/response;
- problem details;
- códigos e namespaces públicos necessários à interoperabilidade;
- semântica de guardas/resultados;
- conformance suite;
- tracing/event envelope.

## Privado/substituível

Não são necessários para interoperar e podem compor o diferencial proprietário:

- geração de candidatos;
- recuperação semântica;
- embeddings;
- estrutura física de memória;
- estratégia de grafo;
- ranking;
- pesos;
- confiança/calibração;
- desempate;
- fusão de evidências;
- exploração x conservação;
- aprendizagem a partir de outcomes;
- seleção de quando pedir revisão humana;
- modelos estatísticos/LLMs;
- políticas internas de promoção/rebaixamento de casos.

A resposta pública pode identificar uma versão opaca do engine/policy para auditoria,
sem publicar como ela funciona.

## Regra

A implementação fechada deve poder ser trocada por outra implementação CONFORME sem
exigir alteração no cliente.
