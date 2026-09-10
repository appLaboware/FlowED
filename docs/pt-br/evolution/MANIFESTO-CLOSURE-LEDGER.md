# Ledger de fechamento do Manifesto FlowED

**Status:** regra operacional de fechamento conceitual da fase atual.

## Regra de fechamento

O objetivo imediato é **terminar o manifesto**, não implementar todas as materializações nem fechar todas as linhas de pesquisa derivadas.

Para cada pilar ou afirmação estrutural do manifesto, a rodada deve responder somente o suficiente para estabelecer que:

1. o conceito é coerente com o animal FlowED;
2. não depende de uma implementação única;
3. existe pelo menos um caminho plausível/realizável de materialização;
4. gaps de implementação, formalização ou pesquisa podem ser deixados como linhas abertas para continuidade posterior;
5. uma linha aberta não bloqueia o manifesto quando sua realizabilidade conceitual já está suficientemente estabelecida.

A partir desse ponto, a discussão deve avançar para o próximo elemento do manifesto. O aprofundamento técnico fica para ciclos posteriores.

## Pilar 1 — Unidade operacional e liberdade governada

**Estado para fechamento do manifesto:** suficientemente realizável nesta fase.

A discussão estabeleceu que FlowED pode se orientar por uma linguagem pública comum e contratos públicos, mantendo implementações livres e substituíveis. `flwd`, YAML, API e outros clientes podem projetar a mesma semântica pública sem obrigar o FlowED a conhecer mecanismos internos.

Ports, adapters, providers, mocks, contract testing e demais mecanismos permanecem como possíveis materializações e linhas de continuidade, não como assuntos que precisem ser fechados antes do manifesto.

A linha de pesquisa derivada da composição test-driven/contract-driven permanece aberta e não bloqueia o manifesto.

## Pilar 2 — Autoeducação e conhecimento vivo

**Estado para fechamento do manifesto:** o componente de memória operacional estruturada atingiu maturidade de realizabilidade suficiente; resta consolidar a formulação constitutiva final e a fronteira com MyTrues/EDT/CCP.

A exigência de maturidade desta rodada foi elevada: não basta uma filosofia plausível. Para fechar um pilar, deve existir no horizonte uma tecnologia pronta ou uma composição concreta de tecnologias capaz de cumprir o futuro contrato, em nível semelhante ao atingido pelo Pilar 1.

A pesquisa de realizabilidade identificou um caminho tecnológico forte:

- CDEvents já padroniza eventos comuns para partes relevantes do SDLC, com foco explícito em interoperabilidade e desacoplamento entre ferramentas;
- OpenTelemetry fornece modelo estável e infraestrutura executável para logs/events/traces, incluindo semantic conventions para CI/CD e VCS;
- CloudEvents fornece envelope genérico e extensível;
- ActivityStreams 2.0 demonstra uma abstração genérica de atividade com ator, objeto, alvo, origem, resultado e instrumento;
- OCEL 2.0 oferece event logs multiobjeto, relações qualificadas, mudanças temporais, schemas e formatos JSON/XML/SQLite, inclusive com dataset real de commits do Angular;
- W3C PROV e OpenLineage fornecem proveniência e lineage extensíveis;
- AsyncAPI e schema registries permitem contratos machine-readable, versionamento e validação de compatibilidade;
- Kafka, Redpanda, Pulsar, NATS JetStream e event stores fornecem caminhos alternativos para transporte, persistência e replay;
- OpenTelemetry Collector já implementa pipelines de receivers/processors/exporters e possui integração com Kafka;
- XES/Process Mining e OCEL/OCPM fornecem caminhos concretos para análise posterior dos eventos.

A conclusão da rodada é que **não existe uma única ferramenta que seja o Pilar 2**, mas existe uma composição executável hoje que cobre todas as responsabilidades essenciais da memória operacional estruturada. Portanto, o contrato FlowED pode ser criado posteriormente a partir das melhores propriedades dessas referências sem depender de inventar infraestrutura fundamental.

Hipótese arquitetural preservada:

**ciência + padrões + grandes projetos → propriedades maduras → contrato FlowED → implementação futura substituível**.

O futuro projeto de memória/log estruturado deve ser uma capability separada, assim como outros projetos horizontais FlowED. Ele poderá compor várias ferramentas, mas nenhuma delas deve subir como dependência conceitual obrigatória.

A relação com MyTrues permanece:

- **memória operacional:** o que aconteceu, representado por eventos estruturados e correlacionáveis;
- **memória decisória/cognitiva:** por que aconteceu, qual referência/decisão/racional/evidência estava vigente;
- **autoeducação:** capacidade de relacionar intenção/decisão, execução, resultado e evidência para alimentar revisão consciente da forma de trabalhar.

A parte de memória operacional está fortemente realizável. MyTrues/EDT/CCP permanecem mais frágeis e em evolução, mas já possuem caminho conceitual plausível e não precisam ser implementados antes do manifesto.

Formulação candidata do Pilar 2:

> **FlowED transforma execução em memória operacional estruturada e relacionável ao conhecimento que a motivou, permitindo que experiência, decisão e evidência retroalimentem conscientemente a evolução da forma de trabalhar.**

O manifesto não deve alegar que um único vocabulário FlowED já cobre empiricamente todos os domínios da Engenharia de Software. O que está suficientemente sustentado é a **realizabilidade da arquitetura** e a existência de tecnologia capaz de cumprir um contrato extensível por domínio.

Documentos de aprofundamento:

- `PILAR-2-STRUCTURED-OPERATIONAL-MEMORY-DRAFT.md`;
- `PILAR-2-REFERENCE-STACK-DRAFT.md`;
- `PILAR-2-FEASIBILITY-RESEARCH-001.md`.

## Próximo passo

Consolidar entre nós apenas a formulação constitutiva final do Pilar 2 e, se não surgir contradição relevante, marcá-lo como suficientemente fechado para o manifesto. Depois avançar diretamente ao Pilar 3 — sustentação científica e empírica explícita.
