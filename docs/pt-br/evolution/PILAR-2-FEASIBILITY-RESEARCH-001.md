# Pesquisa de realizabilidade — Pilar 2: memória operacional estruturada

**Status:** evidence/research note para fechamento do Manifesto FlowED.  
**Objetivo:** responder se existe tecnologia suficientemente madura, isolada ou por composição, para materializar um contrato FlowED de memória operacional estruturada sem violar o Pilar 1.

## 1. Pergunta de fechamento

O FlowED pretende que execuções relevantes possam produzir memória operacional estruturada, correlacionável a decisões, referências, evidências e resultados. Antes de consolidar esse princípio no manifesto, é necessário verificar se há tecnologia concreta capaz de materializar esse contrato em nível suficientemente plausível.

A pergunta desta rodada não é qual schema FlowED será criado nem qual ferramenta será obrigatória. A pergunta é:

> **existe no horizonte tecnológico atual uma composição concreta, madura e substituível capaz de receber, transportar, persistir, correlacionar e analisar eventos estruturados suficientemente genéricos para cobrir diferentes áreas da Engenharia de Software?**

## 2. Conclusão

**Sim, com alta plausibilidade de realizabilidade por composição.**

Nenhuma tecnologia pesquisada cobre sozinha toda a hipótese FlowED. Entretanto, existe uma cadeia de padrões e implementações maduras que cobre todas as funções essenciais do mecanismo. Além disso, algumas referências já atacam diretamente o mesmo problema de interoperabilidade entre ferramentas de software.

Isto permite classificar o mecanismo do Pilar 2 como **realizável em princípio com caminho tecnológico concreto identificado**, em nível semelhante ao critério usado para fechar o Pilar 1. A universalidade semântica para todos os domínios de Engenharia de Software ainda precisa ser testada futuramente; ela não é necessária para afirmar realizabilidade do mecanismo.

## 3. Evidência mais forte encontrada: CDEvents

CDEvents, projeto da Continuous Delivery Foundation, define uma especificação comum para eventos do ecossistema de produção de software. Seu objetivo explícito é interoperabilidade entre ferramentas independentes, redução de vendor lock-in e uso de uma linguagem comum de eventos.

A especificação cobre atualmente categorias como:

- source code control;
- continuous integration;
- testing;
- continuous deployment;
- continuous operations/incidents;
- tickets;
- core pipeline/task runs.

CDEvents estende CloudEvents, usa schemas de eventos, versionamento e permite produtores e consumidores desenvolvidos/deployados independentemente.

Este é um antecedente especialmente relevante porque demonstra que a ideia de criar **eventos comuns para ferramentas heterogêneas do SDLC** já é materializável e possui integrações/PoCs com ferramentas como Argo, Flux, Jenkins, Tekton, Spinnaker, Testkube, Tracetest e outras.

Limite: CDEvents não pretende cobrir todos os domínios da Engenharia de Software. Ele é forte evidência de realizabilidade e uma fonte de boas propriedades para o contrato FlowED, não o contrato FlowED pronto.

## 4. Representação genérica de eventos

### 4.1 OpenTelemetry Logs/Events

O OpenTelemetry Logs Data Model é estável e foi desenhado como modelo comum para logs de múltiplas fontes, incluindo arquivos de aplicação, eventos gerados por máquina e logs de sistema. Ele define campos como timestamp, observed timestamp, trace/span IDs, resource, instrumentation scope, attributes, body e event name.

A documentação afirma que formatos existentes devem poder ser mapeados de forma semanticamente significativa para esse modelo. O OpenTelemetry também possui semantic conventions para várias áreas, incluindo CI/CD e VCS.

Isto demonstra a existência de uma representação operacional suficientemente genérica para transportar eventos FlowED sem exigir formato proprietário desde o primeiro momento.

### 4.2 CloudEvents

CloudEvents fornece envelope vendor-neutral e protocol-agnostic para eventos. Ele separa metadados comuns do payload específico do domínio e permite extensões.

Isto é compatível com a hipótese FlowED de possuir um núcleo contratual estável e extensões específicas por capability/domínio.

### 4.3 ActivityStreams 2.0

O W3C ActivityStreams 2.0 define uma abstração extremamente genérica de `Activity`, capaz de representar ações passadas, presentes ou futuras, com propriedades como `actor`, `object`, `target`, `origin`, `result` e `instrument`.

Embora criado para outro contexto, ele prova que uma estrutura genérica ator-ação-objeto-resultado pode ser serializada de forma extensível e interoperável.

## 5. Eventos complexos envolvendo múltiplos objetos

### OCEL 2.0 — Object-Centric Event Logs

OCEL 2.0 é particularmente importante para o FlowED porque evita a limitação de associar um evento a um único “caso”. Um evento pode estar relacionado a múltiplos objetos tipados, e as relações podem receber qualificadores. O modelo também suporta relações entre objetos e mudanças de atributos ao longo do tempo.

Isto se aproxima fortemente de cenários reais de Engenharia de Software, em que uma única ação pode relacionar simultaneamente commit, issue, branch, build, teste, artefato, ambiente, agente e decisão.

O standard possui formatos JSON, XML e SQLite com schemas de validação. O ecossistema publica inclusive um event log real de commits do projeto Angular, demonstrando aplicação direta a eventos de desenvolvimento de software.

OCEL 2.0 não precisa ser adotado como formato FlowED; ele demonstra que o problema de eventos multiobjeto, relações qualificadas e evolução temporal já possui uma solução concreta e executável.

## 6. Proveniência e lineage

### W3C PROV

PROV-DM fornece modelo de proveniência baseado em entidades, atividades, agentes, derivação e responsabilidade. É suficientemente genérico para representar de onde artefatos/resultados vieram e quem participou de sua produção.

### OpenLineage

OpenLineage fornece uma especificação executável e extensível para eventos de execução ligados a Jobs, Runs, Inputs e Outputs. Sua arquitetura de `facets` permite enriquecimento de metadados sem alterar o modelo central.

Para FlowED, estes antecedentes sustentam a capacidade de correlacionar execução, artefatos, entradas/saídas e origem sem inventar lineage do zero.

## 7. Contrato machine-readable e evolução

### AsyncAPI

AsyncAPI é protocol-agnostic e descreve APIs message-driven em formato machine-readable. Pode declarar canais, operações, mensagens e schemas sem pressupor Kafka, MQTT, AMQP, WebSocket ou outra tecnologia.

Isto fornece uma forma concreta de materializar parte do contrato event-driven FlowED sem acoplar contrato a transporte.

### Schema Registry / compatibility

Ferramentas como Apicurio Registry já validam schemas e compatibilidade entre versões para formatos como Avro, JSON Schema, Protobuf, OpenAPI e XSD.

Isto demonstra que o contrato pode ser versionado e submetido automaticamente a regras de compatibilidade em vez de depender apenas de documentação humana.

## 8. Transporte, persistência, replay e substituição

### Apache Kafka

Kafka oferece armazenamento durável de eventos em tópicos, produtores e consumidores desacoplados, replay por offsets e garantias configuráveis de entrega/processamento. Ele é um possível backend de referência, não parte da semântica FlowED.

### Alternativas reais

A substituibilidade não é apenas teórica. Há tecnologias com modelos semelhantes ou compatibilidade suficiente para ocupar esse papel, como Redpanda, Pulsar, NATS JetStream e event stores dedicados como Kurrent/EventStoreDB.

Redpanda, por exemplo, declara compatibilidade com clientes Kafka e suporta produce/consume/transactions, demonstrando que uma implementação pode ser trocada mantendo grande parte do contrato tecnológico de acesso.

### OpenTelemetry Collector

O OpenTelemetry Collector já implementa uma arquitetura de receivers → processors → exporters. Recebe telemetria, transforma/enriquece e exporta para múltiplos destinos. Há componentes Kafka receiver/exporter para traces, metrics e logs.

Isto fornece um **mecanismo executável hoje** para receber eventos estruturados, processá-los e roteá-los a um backbone ou storage sem que cada produtor conheça os consumidores.

## 9. Projeção para análise e aprendizagem

IEEE XES padroniza event logs/event streams interoperáveis para análise de comportamento. Process Mining fornece técnicas de discovery, conformance e improvement sobre esses logs.

OCEL 2.0 amplia a expressividade para cenários multiobjeto.

Logo, a memória operacional capturada não precisa ser apenas arquivada: já existem técnicas e ferramentas capazes de analisá-la posteriormente.

## 10. Caminho de materialização concretamente disponível

Sem definir ainda o contrato FlowED final, um POC futuro poderia ser realizado hoje com tecnologias existentes:

1. contrato de mensagem descrito em AsyncAPI + JSON Schema/Protobuf;
2. evento envelopado como CloudEvent;
3. evento emitido como OpenTelemetry Event/LogRecord ou convertido para ele;
4. OpenTelemetry Collector recebe, valida/enriquece e encaminha;
5. Kafka/Redpanda ou outro event store persiste e permite replay;
6. PROV/OpenLineage enriquecem proveniência/lineage quando necessário;
7. projeção OCEL/XES alimenta process mining/análise;
8. MyTrues recebe apenas as correlações/decisões/racional necessárias para ligar memória operacional à memória cognitiva/decisória.

Esse caminho usa componentes existentes e pode ser implementado sem criar previamente um broker, collector, event store, lineage system ou process-mining engine próprios.

## 11. O que o contrato FlowED pode absorver das referências

A pesquisa sugere que o contrato futuro deve estudar, sem copiar cegamente, boas propriedades já comprovadas:

- identidade global do evento;
- tipo e versão;
- timestamp/observed timestamp;
- ator/origem;
- ação/operação;
- objetos envolvidos e seus papéis;
- target/context;
- resultado/outcome;
- correlation/causation/trace;
- inputs/outputs/artefatos;
- provenance/lineage;
- schema/version/compatibility;
- extensões específicas do domínio sem quebrar o núcleo comum;
- delivery/persistence/replay somente como garantias públicas quando necessárias;
- projeções para análise, sem exigir um único formato de storage.

A lista é fonte para o futuro trabalho de contrato, não o contrato definitivo.

## 12. Relação com o Pilar 1

A materialização do Pilar 2 deve obedecer ao Pilar 1:

- FlowED define contrato, não implementação;
- tecnologias concretas ficam abaixo do contrato;
- nenhuma ferramenta é obrigatória;
- implementações podem ser substituídas quando preservam garantias públicas;
- a criação do contrato pode ser guiada por exemplos/testes executáveis;
- o projeto futuro de memória/log deve nascer como capability separada e desacoplada.

## 13. Relação com MyTrues

O estudo fortalece a separação entre:

- **memória operacional:** fatos estruturados do que ocorreu;
- **memória decisória/cognitiva:** razões, referências, evidências, alternativas e decisões.

A primeira possui caminho tecnológico fortemente demonstrado. A segunda continua dependente do desenvolvimento/validação de MyTrues/EDT/CCP.

O mecanismo FlowED não exige que MyTrues armazene o event stream bruto. Ele pode correlacionar entidades/IDs e construir a relação `decisão ↔ execução ↔ resultado ↔ evidência`.

## 14. Decisão de maturidade para o manifesto

**Maturidade atual do componente “memória operacional estruturada”: suficiente para fechamento conceitual do Pilar 2.**

Razões:

1. há padrões genéricos de evento e proveniência;
2. há padrões específicos para eventos do ciclo de software (CDEvents);
3. há modelos multiobjeto adequados a eventos complexos (OCEL 2.0);
4. há representação e instrumentação operacional madura (OpenTelemetry);
5. há contratos machine-readable e schema compatibility (AsyncAPI/registries);
6. há múltiplas tecnologias maduras para transporte, persistência e replay;
7. há mecanismos de análise/process mining;
8. existe um POC concreto possível hoje usando apenas componentes existentes.

O que **não** está comprovado é que um único vocabulário semântico FlowED já consiga cobrir todos os domínios de Engenharia de Software. Isso permanece como trabalho futuro de síntese/contrato e precisa de testes por domínio. O manifesto pode afirmar realizabilidade da arquitetura sem afirmar universalidade já demonstrada.

## 15. Referências externas principais

- CDEvents — common specification for Continuous Delivery events, Continuous Delivery Foundation.
- OpenTelemetry Logs Data Model e Semantic Conventions.
- OpenTelemetry Collector Architecture.
- CloudEvents specification.
- AsyncAPI Specification.
- W3C ActivityStreams 2.0.
- W3C PROV-DM.
- OpenLineage Specification.
- IEEE 1849-2023 XES.
- OCEL 2.0 Specification, RWTH Aachen/PADS.
- Apache Kafka documentation.
- Apicurio Registry compatibility rules.
