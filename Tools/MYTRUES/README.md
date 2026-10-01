# MyTrues

MyTrues é um ensaio de um produto geral de **memória decisória de um fornecedor humano**.

## Unidade de confiança

Um MyTrues pertence a um técnico, equipe ou fornecedor.

O cliente escolhe **qual MyTrues consultar**. Essa escolha pode mudar o processo e o
resultado materializado porque cada fornecedor mantém:

- sua própria memória de casos;
- suas próprias decisões aprovadas;
- sua própria experiência acumulada;
- seu próprio algoritmo de recuperação/ranking;
- seu próprio histórico de outcomes.

Dois MyTrues podem falar o mesmo protocolo e decidir de formas diferentes.

## Regra central

MyTrues NÃO inventa uma decisão quando não possui uma solução aprovada.

Fluxo:

```
intent
  -> execution
  -> known problem?
       yes -> provider MyTrues decides -> resume
       no  -> PAUSE
              -> sanitize/generalize case
              -> awaiting-provider-decision
              -> senior solves synthetic sandbox case
              -> decision is stored in THAT provider's MyTrues
              -> pending request becomes decided
              -> execution resumes
```

O protagonismo é do humano sênior. LLMs podem pesquisar, organizar ou sugerir,
mas uma sugestão não vira automaticamente verdade operacional.

## Protocolo aberto; inteligência privada

Aberto:

- HTTP/OpenAPI;
- request/response;
- estado pending/decided;
- pacote de caso anonimizado;
- submissão de resolução;
- tracing;
- eventos;
- conformance.

Privado por provedor:

- memória;
- casos;
- ranking;
- pesos;
- embeddings;
- grafo físico;
- heurísticas;
- aprendizagem;
- algoritmo que escolhe entre decisões aprovadas.

## Padrões adotados

- OMG DMN 1.5: vocabulário de decisão;
- BPMN 2.0.2: semântica de pausa/espera por mensagem humana;
- OpenAPI 3.1: API síncrona;
- RFC 9457: problemas HTTP;
- W3C Trace Context: correlação;
- CloudEvents + AsyncAPI: notificação assíncrona opcional.

O protocolo compõe padrões existentes; não tenta substituí-los.
