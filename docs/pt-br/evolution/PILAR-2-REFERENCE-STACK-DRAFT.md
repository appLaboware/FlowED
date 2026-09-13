# Draft — Pilar 2: composição de referências para contrato de memória operacional

**Status:** Referência Experimental. Não normativa; usada para demonstrar realizabilidade do Pilar 2 sem acoplar o FlowED a uma implementação única.

## 1. Correção conceitual

O objetivo não é escolher agora uma stack de implementação nem decidir que Kafka, OpenTelemetry, AsyncAPI, XES, OpenLineage, PROV, MyTrues ou qualquer outro produto será obrigatório.

A proposta é anterior à implementação: **estudar os grandes sistemas, padrões e frameworks que já resolvem partes do problema, extrair deles as boas propriedades e transformar essa composição em um contrato público genérico do FlowED**.

Portanto, a sequência correta é:

**prior art maduro → extração das boas propriedades → composição semântica → contrato público FlowED → projeto/materialização futura**.

O contrato é desenhado já sabendo que deverá ser realizável por ferramentas reais, mas não pertence a nenhuma delas.

## 2. Regra de compatibilidade entre pilares

O Pilar 2 não pode violar o Pilar 1.

Consequências obrigatórias:

- toda capability pública é expressa por contrato;
- implementações permanecem desacopladas;
- ports/adapters podem materializar o contrato sem se tornarem parte do conceito;
- nenhuma ferramenta concreta vira dependência conceitual obrigatória;
- substituição continua possível quando o comportamento público contratado é preservado;
- desenho e validação do contrato podem seguir a linha test-driven/contract-driven em estudo, sem que esse método precise ser fechado antes do manifesto.

Assim, os pilares são cumulativos: um pilar posterior deve respeitar invariantes já estabelecidos pelos anteriores.

## 3. Fontes candidatas de propriedades para o contrato

As tecnologias abaixo são tratadas como **fontes de boas ideias**, não como componentes obrigatórios de uma arquitetura final:

- **CloudEvents** — identidade e envelope interoperável de eventos;
- **OpenTelemetry** — contexto observável, logs/events/traces e correlação;
- **IEEE XES / Process Mining** — estrutura analisável de event logs e comportamento processual;
- **W3C PROV** — proveniência entre entidades, atividades e agentes;
- **OpenLineage** — relações entre execução, run/job, inputs e outputs;
- **AsyncAPI** — descrição machine-readable de interações assíncronas;
- **Kafka e outros event-streaming systems** — persistência, replay, consumidores desacoplados, ordenação e garantias de entrega quando necessárias;
- **Event Sourcing** — histórico temporal reconstruível quando adequado;
- **MyTrues / EDT / CCP** — memória decisória, racional, referência, evidência, revisão e projeção do conhecimento.

A tarefa futura é identificar, de cada família, quais propriedades merecem subir para o contrato genérico FlowED e quais devem permanecer detalhe de implementação.

## 4. Contrato genérico como síntese

O contrato de memória operacional deve ser uma síntese mínima das melhores propriedades encontradas, por exemplo:

- identidade estável do evento;
- identidade e versão do contrato que originou a execução;
- actor/origin/context;
- correlação e causação;
- estado/outcome observável;
- entradas e saídas públicas relevantes;
- referências a artefatos e evidências;
- proveniência/lineage suficiente;
- capacidade de persistência e recuperação conforme a necessidade contratual;
- extensibilidade sem quebrar compatibilidade;
- ligação possível com decisão/referência/racional;
- regras de compatibilidade e versionamento.

A lista é provisória e deve ser validada contra o prior art antes de qualquer consolidação.

## 5. Projeto futuro dedicado

Depois que o manifesto estiver fechado, deve existir um projeto/capability próprio do ecossistema FlowED para essa área de **memória operacional estruturada**, da mesma forma que outros projetos especializados podem existir para ISO 29110 ou outras capacidades.

Esse projeto deverá:

- implementar o contrato público definido pelo FlowED;
- integrar memória operacional e memória decisória sem fundi-las;
- possuir MyTrues como implementação de referência candidata para a dimensão decisória/cognitiva;
- poder usar Kafka, OpenTelemetry, XES, PROV, OpenLineage, AsyncAPI ou equivalentes conforme fizer sentido;
- preservar ports/adapters para substituição;
- permitir outros providers que implementem o mesmo contrato.

O FlowED conceitual continua conhecendo o contrato, não a implementação.

## 6. Relação entre memória operacional e MyTrues

O contrato deve permitir que uma execução estruturada seja ligada a:

- decisão que a autorizou ou motivou;
- referência vigente naquele momento;
- evidência usada na decisão;
- racional e alternativas quando disponíveis;
- revisão posterior decorrente dos resultados observados.

A memória operacional responde principalmente **o que aconteceu**. MyTrues/EDT/CCP respondem principalmente **por que se decidiu assim e como o conhecimento evoluiu**.

O valor do Pilar 2 surge da capacidade de correlacionar os dois lados sem acoplá-los tecnicamente.

## 7. Consequência para o manifesto

O Pilar 2 não precisa prometer uma ferramenta específica. Precisa afirmar que o FlowED transforma execução em memória estruturada relacionável ao conhecimento decisório, de modo que a organização possa aprender com sua própria prática.

Uma formulação candidata é:

> **A execução relevante deve poder produzir memória operacional estruturada e relacionável às decisões, referências, evidências e aprendizados que a contextualizam. O FlowED deve permitir que essa memória seja reutilizada para compreender o que ocorreu e evoluir conscientemente a forma de trabalhar.**

## 8. Estado

**Realizabilidade:** suficientemente plausível para o manifesto, porque cada componente necessário já possui materializações maduras em prior art conhecido; a contribuição específica do FlowED está na composição contratual e na integração com memória decisória.

**Rota:** ADOPT/COMPOSE. Não inventar mecanismos já existentes. O eventual residual de contribuição deve ser tratado como linha de pesquisa separada e não bloqueia o manifesto.
