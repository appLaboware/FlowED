# Draft — Pilar 2: stack de referência para memória operacional e autoeducação

**Status:** Referência Experimental. Não normativa; usada para demonstrar realizabilidade do Pilar 2 sem acoplar o FlowED a uma implementação única.

## 1. Decisão conceitual

O Pilar 2 pode ser materializado por uma **composição de padrões e ferramentas maduras**, cada uma usada naquilo que já faz bem, mantendo o FlowED orientado apenas pelo contrato público.

A referência preferencial de implementação não deve ser uma tecnologia monolítica nem um requisito obrigatório. Deve existir como **stack de referência substituível por ports/adapters**, de modo que outra implementação possa atender ao mesmo contrato público.

Regra:

> **FlowED governa a semântica e o contrato público da memória operacional; a stack de referência demonstra uma materialização possível; qualquer componente pode ser substituído se preservar o comportamento contratado.**

## 2. Separação de papéis

Kafka não deve ser tratado como o contrato semântico do FlowED. Seu papel mais adequado é transporte/event backbone durável. A definição do contrato deve ficar em uma camada protocol-agnostic e machine-readable.

A composição de referência candidata é:

- **AsyncAPI** — contrato machine-readable da interface/event API entre produtores e consumidores;
- **CloudEvents** — envelope interoperável e protocol-agnostic para identidade e metadados fundamentais do evento;
- **OpenTelemetry** — modelo e instrumentação para logs/events/traces e contexto observável;
- **Apache Kafka** — backbone/event stream durável, ordenado por partição, com capacidades de idempotência/transações quando necessárias;
- **OpenLineage** — modelo para ligar execução, job/run, inputs, outputs e lineage operacional;
- **W3C PROV** — referência geral de proveniência por entidades, atividades e agentes;
- **IEEE XES + Process Mining** — projeção/análise de event logs para descoberta, conformance, monitoramento e melhoria de processos;
- **MyTrues + EDT/CCP** — camada candidata de memória decisória/cognitiva: razões, referências, alternativas, evidências, decisões, revisões e projeções.

Nenhuma dessas tecnologias deve se tornar dependência conceitual obrigatória do FlowED. Elas formam uma implementação de referência composta.

## 3. Fluxo de referência

Contrato público FlowED
→ descrição event-driven machine-readable (AsyncAPI ou equivalente)
→ evento interoperável (CloudEvents ou equivalente)
→ instrumentação/telemetria estruturada (OpenTelemetry ou equivalente)
→ stream/broker persistente (Kafka ou equivalente)
→ lineage/proveniência (OpenLineage/W3C PROV ou equivalentes)
→ memória operacional consultável
→ correlação com MyTrues/EDT/CCP
→ análise/process mining
→ evidência e possível revisão da referência ou forma de trabalho.

## 4. Contrato público acima da stack

O contrato público FlowED deve definir apenas o que precisa permanecer estável para qualquer materialização:

- identidade da operação e da versão de contrato;
- identidade/correlação/causação do evento;
- ator/origem/proveniência relevante;
- alvo/contexto público;
- estado/result/outcome observável;
- inputs/outputs públicos relevantes;
- referências a artefatos/evidências;
- ligações opcionais/obrigatórias com decisão/referência conforme o contrato;
- regras mínimas de compatibilidade e evolução;
- garantias observáveis relevantes de entrega, ordenação, duplicação ou persistência somente quando a capability realmente depender delas.

Detalhes como tópico Kafka, partições, storage engine, collector, schema registry, banco de lineage ou representação interna do MyTrues ficam abaixo do contrato.

## 5. O papel específico do Kafka

Kafka ajuda fortemente como implementação de referência da **memória operacional em fluxo** porque oferece log distribuído persistente, ordenação por partição, replay, consumer groups, idempotent producer e transações.

Isso permite que diferentes consumidores usem o mesmo fato operacional sem acoplamento direto: observabilidade, MyTrues, auditoria, process mining, métricas, scoring e futuras ferramentas podem consumir o stream independentemente.

Entretanto, usar Kafka como semântica central criaria acoplamento indevido. O FlowED deve poder trocar Kafka por outro broker/log/event store desde que as garantias públicas relevantes sejam preservadas.

## 6. AsyncAPI como referência mais adequada para o contrato event-driven

AsyncAPI é uma referência particularmente forte porque foi criada para descrever interfaces assíncronas/message-driven de forma machine-readable e protocol-agnostic, podendo descrever canais, operações, mensagens e payloads independentemente de Kafka, MQTT, AMQP, WebSocket ou outros protocolos.

Por isso, no stack de referência, AsyncAPI é candidato mais natural que Kafka para representar o contrato técnico event-driven. O FlowED pode ainda possuir semântica própria acima dele e projetá-la para AsyncAPI.

## 7. OpenTelemetry e CloudEvents não são redundantes

CloudEvents trata principalmente da portabilidade do evento entre sistemas e protocolos por um envelope comum.

OpenTelemetry trata principalmente da observabilidade e do modelo de logs/events/traces, incluindo timestamps, resource, instrumentation scope, attributes e trace context.

Uma implementação pode mapear eventos FlowED simultaneamente para CloudEvents e OpenTelemetry sem obrigar que um substitua o outro.

## 8. Lineage e decisão são camadas diferentes

OpenLineage/W3C PROV respondem principalmente a relações como:

- qual atividade ocorreu;
- quais inputs foram usados;
- quais outputs foram produzidos;
- quem/qual agente participou;
- de onde uma entidade derivou.

MyTrues/EDT/CCP respondem a uma dimensão diferente:

- por que a atividade foi escolhida;
- qual referência/decisão autorizou ou motivou a ação;
- que alternativas existiam;
- que evidência sustentava a decisão naquele momento;
- o que foi aprendido posteriormente;
- por que a referência foi mantida, alterada ou substituída.

O valor do Pilar 2 surge da correlação entre ambas, sem fundi-las.

## 9. Consequência para autoeducação

A composição torna tecnicamente plausível um ciclo automatizável:

intenção/contrato → execução → evento → memória operacional → lineage/proveniência → ligação com decisão/racional → análise → evidência → proposta/revisão → nova referência.

O sistema pode automatizar captura, correlação, comparação e preparação de evidência. A autoridade para alterar uma norma/referência continua governada separadamente.

## 10. Critério de substituição

A stack acima é apenas uma **reference implementation architecture**. Um substituto pode trocar um ou vários elementos — por exemplo Kafka por NATS, Pulsar, Redpanda, RabbitMQ, um event store local ou outra tecnologia — sem deixar de ser FlowED, desde que satisfaça o contrato público aplicável.

O mesmo vale para observabilidade, schema, lineage, provenance e memória decisória.

## 11. Sustentação externa preliminar

- AsyncAPI define um contrato machine-readable entre senders e receivers e é protocol-agnostic, inclusive com bindings para Kafka.
- OpenTelemetry define um modelo estável de logs/events capaz de mapear múltiplas fontes preservando semântica.
- Kafka oferece capacidades de persistência/streaming e garantias de idempotência/transações úteis para implementações que delas precisem.
- OpenLineage define uma especificação extensível de lineage para job/run/dataset e pode inclusive transportar eventos via Kafka.
- CloudEvents, W3C PROV, IEEE XES e Process Mining complementam envelope, proveniência e análise.

## 12. Estado para o manifesto

A realizabilidade do mecanismo de memória operacional estruturada está fortemente sustentada por componentes já maduros. O que permanece aberto é a composição exata, o schema FlowED, as políticas de relevância/retention, a integração concreta com MyTrues e a avaliação empírica do ciclo de autoeducação.

Essas linhas podem continuar após o manifesto sem bloquear o Pilar 2, desde que ainda seja fechado o princípio constitutivo de quais execuções precisam gerar memória e quando essa memória precisa ser correlacionada a decisões/referências.
