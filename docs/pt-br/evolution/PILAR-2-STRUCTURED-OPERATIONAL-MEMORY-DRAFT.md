# Draft — Pilar 2: memória operacional estruturada e aprendizagem

**Status:** Referência Experimental para fechamento do Pilar 2 do Manifesto FlowED.

## 1. Pergunta

É realizável fazer com que toda ação executada através de um contrato público FlowED produza automaticamente um registro estruturado, capaz de ser ligado à memória de decisões e posteriormente usado para aprendizagem, auditoria, análise e evolução da forma de trabalhar?

## 2. Conclusão provisória de realizabilidade

**Sim.** Há prior art científico, normativo e técnico suficiente para não ser necessário inventar do zero a captura de eventos estruturados.

A composição candidata é:

**contrato público FlowED → execução → evento estruturado derivado do contrato → memória operacional/event stream → ligação com decisão/racional/proveniência → análise/aprendizagem → possível revisão da referência ou forma de trabalho.**

O residual do FlowED não está em inventar structured logging. Está em orquestrar, sob uma mesma linguagem e identidade contratual, o que foi pretendido, o que foi executado, o que aconteceu e por que aquela decisão/referência existia.

## 3. Prior art que sustenta a ideia

### 3.1 IEEE XES / Process Mining

IEEE 1849-2023 define o eXtensible Event Stream (XES) para interoperabilidade em event logs e event streams, com metodologia unificada e extensível para capturar comportamento de sistemas por eventos.

Isso demonstra que eventos estruturados podem ser tratados como artefato interoperável e analisável, não apenas como texto de log.

Referência: IEEE 1849-2023, IEEE Standard for eXtensible Event Stream (XES) for Achieving Interoperability in Event Logs and Event Streams.

### 3.2 Ciência de Process Mining

A literatura de Process Mining parte de event logs para descobrir, monitorar e melhorar processos. Há trabalhos científicos sobre qualidade de event logs, geração semiautomática de logs e ligação de bancos de dados a eventos processáveis.

Consequência para FlowED: produzir o log já estruturado no momento da execução pode evitar grande parte do trabalho posterior de reconstrução/extração do comportamento real.

Referências candidatas:
- Suriadi et al. (2017), *Event log imperfection patterns for process mining*.
- Andrews et al. (2020), *Quality-informed semi-automated event log generation for process mining*.
- González López de Murillas, Reijers & van der Aalst (2019), *Connecting databases with process mining: a meta model and toolset*.

### 3.3 W3C PROV

PROV-DM modela proveniência por entidades, atividades, agentes e relações de derivação/responsabilidade. Foi projetado para permitir que representações específicas de domínio sejam traduzidas para um modelo comum e trocadas entre sistemas.

Consequência para FlowED: o evento operacional pode preservar não apenas 'o que aconteceu', mas relações com agente, entidade produzida/alterada, atividade, fonte e derivação.

Referência: W3C Recommendation, *PROV-DM: The PROV Data Model* (2013).

### 3.4 OpenTelemetry

O OpenTelemetry Logs Data Model fornece um modelo comum para logs de múltiplas fontes e define Events como formato estruturado de LogRecord, com EventName, Resource, InstrumentationScope, Attributes e contexto de trace.

Consequência para FlowED: há infraestrutura madura para transportar/armazenar eventos estruturados sem criar um pipeline proprietário de observabilidade.

OpenTelemetry é referência técnica/industrial, não evidência científica principal.

### 3.5 CloudEvents

CloudEvents define um envelope vendor-neutral e protocol-agnostic para eventos, com identidade, origem, tipo, versão e payload específico do domínio.

Consequência para FlowED: o contrato pode gerar eventos portáveis sem acoplar a memória a um broker, banco ou protocolo específico.

CloudEvents é referência técnica/normativa de ecossistema, não evidência científica principal.

### 3.6 Event Sourcing

Event Sourcing preserva a evolução temporal do estado através de eventos, permitindo reconstrução e observabilidade histórica. A literatura também explora observabilidade por arquiteturas event-sourced.

Consequência para FlowED: quando adequado, uma sequência imutável de eventos pode ser fonte histórica da execução, sem obrigar o FlowED a usar Event Sourcing como arquitetura universal.

## 4. Separação essencial: execução não é decisão

O Pilar 2 deve evitar fundir dois tipos de memória:

### A. Memória operacional

Registra **o que ocorreu**.

Exemplos de informação candidata:
- contract/version;
- request/operation ID;
- actor/agent;
- target/context;
- timestamp/start/end;
- inputs públicos relevantes;
- resultado/status;
- outputs/artefatos referenciados;
- erro/falha;
- provider/materializador quando for relevante;
- correlation/causation IDs;
- evidence links.

### B. Memória decisória/cognitiva

Registra **por que aquilo foi feito/permitido/escolhido**, incluindo referência, decisão, racional, alternativas, evidência conhecida, divergência e revisão.

No animal atual do FlowED, EDT/CCP definem principalmente o conteúdo/linhagem que interessa preservar; MyTrues é candidato a persistir, relacionar, consultar e projetar essa memória.

As duas memórias devem permanecer distinguíveis, mas relacionáveis por identidades estáveis.

## 5. Hipótese de mecanismo FlowED

Como todo comando/operação pública possui contrato versionado, o mesmo contrato pode declarar também o **evento mínimo obrigatório produzido pela execução**.

Assim, o provider não escreve texto arbitrário como única evidência. Ele devolve/produz um evento conformante ao contrato público.

Hipótese de envelope lógico mínimo:

- event_id;
- event_type;
- contract_id + contract_version;
- request_id;
- correlation_id / causation_id quando aplicável;
- actor/provenance;
- target/context;
- started_at / ended_at ou timestamp aplicável;
- outcome/status;
- public inputs/outputs relevantes;
- artifact/evidence references;
- decision/reference links quando existirem;
- provider-specific extension area fora do núcleo contratual.

A sintaxe física ainda não deve ser inventada. XES, CloudEvents, OpenTelemetry e PROV devem ser avaliados/adaptados antes de qualquer DSL ou schema próprio.

## 6. Papel candidato do MyTrues

MyTrues não precisa ser o logger nem o executor.

Uma divisão conceitualmente mais limpa é:

1. FlowED/contrato define a semântica pública e o mínimo evento observável;
2. providers executam e emitem eventos conformantes;
3. infraestrutura de eventos/logs coleta e preserva a memória operacional;
4. MyTrues relaciona essa memória operacional com decisões, referências, racional, evidências e trajetória cognitiva;
5. mecanismos de análise/EDT usam essas relações para produzir projeções, detectar divergências, acumular evidência e propor revisão;
6. decisão humana/organizacional continua soberana sobre mudança normativa quando aplicável.

MyTrues pode materializar mais de um desses papéis futuramente, mas o manifesto não deve depender de uma implementação única.

## 7. Aprendizagem automática versus decisão automática

O sistema pode automatizar:
- captura;
- correlação;
- agregação;
- consulta;
- métricas;
- comparação entre esperado e observado;
- detecção de padrões/anomalias;
- preparação de evidência;
- geração de propostas de revisão.

Isso não implica que toda aprendizagem resulte automaticamente em mudança de norma/referência. A promoção de evidência e a autoridade para alterar uma prática são problemas separados de governança.

## 8. Formulação mais forte para o Pilar 2

Hipótese de manifesto:

> **Toda execução relevante deve poder deixar uma memória operacional estruturada e relacionável às decisões, referências e evidências que a contextualizam. O FlowED deve permitir que essa memória seja reutilizada para compreender o que ocorreu, confrontar intenção com resultado e evoluir conscientemente a forma de trabalhar.**

Isso é mais forte do que 'registrar experiência' e mais fraco do que exigir uma implementação específica de memória ou IA.

## 9. Por que o mecanismo é realizável

A realizabilidade já possui caminhos concretos independentes:

- structured events/logs: OpenTelemetry;
- envelope interoperável: CloudEvents;
- event-log interoperability/análise: IEEE XES + Process Mining;
- provenance: W3C PROV;
- histórico temporal: Event Sourcing quando adequado;
- decisão/racional/projeção: EDT/CCP + MyTrues como linha própria.

Não é necessário que uma única ferramenta faça tudo. O FlowED pode compor essas capacidades por contratos e referências.

## 10. Gap residual para o manifesto

Para fechar o Pilar 2, ainda precisa ser decidido apenas o princípio mínimo:

- todo evento deve ser registrado ou apenas execução 'relevante'?
- quem/que contrato decide relevância?
- a capacidade de correlacionar execução com decisão/referência é constitutiva do FlowED ou apenas uma materialização preferida?

Schema, banco, broker, observability stack, MyTrues implementation, algoritmo de aprendizagem e análise podem permanecer como linhas abertas sem bloquear o manifesto.

## 11. Estado

**Realizabilidade:** R1/R2 em nível conceitual — componentes individuais são maduros e demonstrados; a composição específica FlowED ainda não foi implementada.

**Rota:** ADOPT/COMPOSE. Não inventar structured logging, provenance ou event-log format antes de demonstrar residual.
