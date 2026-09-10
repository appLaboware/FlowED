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

**Estado para fechamento do manifesto:** realizabilidade fortemente estabelecida; ainda em debate apenas sobre a formulação constitutiva final.

A primeira formulação — apenas registrar experiência e permitir que ela altere conscientemente a forma de trabalhar — foi considerada fraca. O aprofundamento estabeleceu uma direção mais concreta: cada execução relevante pode produzir memória operacional estruturada e relacionável à memória decisória/cognitiva.

A regra metodológica para esta capability é compatível com o Pilar 1: o FlowED não escolhe uma tecnologia obrigatória. Em vez disso, deve estudar sistemas, padrões e frameworks maduros que resolvem partes do problema, extrair deles as melhores propriedades e compor um **contrato público genérico**.

Fontes candidatas de propriedades incluem CloudEvents, OpenTelemetry, IEEE XES/Process Mining, W3C PROV, OpenLineage, AsyncAPI, Kafka e outros event-streaming systems, Event Sourcing e MyTrues/EDT/CCP para a dimensão decisória/cognitiva.

Essas referências são matéria-prima para o contrato, não dependências conceituais do FlowED.

A sequência conceitual é:

**prior art maduro → boas propriedades → composição semântica → contrato público FlowED → projeto/materialização futura substituível**.

A futura capability/projeto de memória operacional estruturada pode integrar MyTrues como implementação de referência da memória decisória, mas deve continuar desacoplada por contracts/ports para permitir outros providers.

A relação essencial permanece:

- memória operacional — **o que aconteceu**;
- memória decisória/cognitiva — **por que foi feito, escolhido ou alterado**.

O valor de autoeducação surge ao correlacionar execução, decisão, referência, evidência, resultado e revisão.

Formulação candidata do Pilar 2:

> **A execução relevante deve poder produzir memória operacional estruturada e relacionável às decisões, referências, evidências e aprendizados que a contextualizam. O FlowED deve permitir que essa memória seja reutilizada para compreender o que ocorreu e evoluir conscientemente a forma de trabalhar.**

Implementação, stack concreta, schema, storage, broker, engine de análise e integração física com MyTrues ficam para projeto posterior e não bloqueiam o manifesto.

Apenas a redação constitutiva final do pilar e a definição mínima de relevância de execução permanecem abertas para debate antes de marcar o Pilar 2 como fechado.

Documento de aprofundamento: `PILAR-2-REFERENCE-STACK-DRAFT.md`.

## Próximo passo

Fechar a formulação mínima do Pilar 2 sem implementar sua stack. Depois avançar diretamente ao Pilar 3.
