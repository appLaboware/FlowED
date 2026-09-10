# Ledger de fechamento do Manifesto FlowED

**Status:** regra operacional de fechamento conceitual da fase atual.

## Regra de fechamento

O objetivo imediato é **terminar o manifesto**, não implementar todas as materializações nem fechar todas as linhas de pesquisa derivadas.

A partir desta rodada, todos os pilares devem atingir o mesmo **gate de realizabilidade** antes de serem considerados suficientemente fechados: não basta coerência filosófica; deve existir no horizonte prior art e pelo menos uma tecnologia pronta ou composição tecnicamente plausível capaz de cumprir o futuro contrato.

Documento normativo da rodada: `MANIFESTO-PILLAR-FEASIBILITY-GATE.md`.

Regra resumida:

**prior art → propriedades úteis → composição → contrato FlowED → materialização de referência substituível**.

Se não houver tecnologia suficiente para sustentar o horizonte de materialização, o pilar não avança: pesquisa-se mais, reduz-se a claim ou abre-se uma linha de viabilidade.

## Pilar 1 — Unidade operacional e liberdade governada

**Estado para fechamento do manifesto:** suficientemente realizável nesta fase.

A discussão estabeleceu que FlowED pode se orientar por uma linguagem pública comum e contratos públicos, mantendo implementações livres e substituíveis. `flwd`, YAML, API e outros clientes podem projetar a mesma semântica pública sem obrigar o FlowED a conhecer mecanismos internos.

Ports, adapters, providers, mocks, contract testing e demais mecanismos permanecem como possíveis materializações e linhas de continuidade, não como assuntos que precisem ser fechados antes do manifesto.

A linha de pesquisa derivada da composição test-driven/contract-driven permanece aberta e não bloqueia o manifesto.

## Pilar 2 — Autoeducação e conhecimento vivo

**Estado para fechamento do manifesto:** suficientemente realizável nesta fase.

A exigência de maturidade foi elevada até existir um horizonte tecnológico comparável ao Pilar 1. A pesquisa demonstrou que a memória operacional estruturada pode ser materializada por composição de tecnologias e padrões existentes, sem depender de uma única implementação.

Horizonte identificado inclui CDEvents, OpenTelemetry, CloudEvents, OCEL, W3C PROV, OpenLineage, AsyncAPI/schema registries, Kafka/Redpanda/Pulsar/NATS/event stores e XES/Process Mining.

A conclusão é que não existe uma única ferramenta que seja o Pilar 2, mas existe tecnologia suficiente para construir uma futura capability de memória operacional capaz de cumprir um contrato extensível por domínio.

A relação conceitual permanece:

- memória operacional — o que aconteceu;
- memória decisória/cognitiva — por que foi feito, escolhido ou alterado;
- autoeducação — relacionar intenção/decisão, execução, resultado e evidência para alimentar revisão consciente da forma de trabalhar.

MyTrues/EDT/CCP permanecem mais frágeis e em evolução, mas essa fragilidade está explícita e não invalida a realizabilidade do núcleo técnico de memória operacional nem a proposição do pilar.

Formulação candidata:

> **FlowED transforma execução em memória operacional estruturada e relacionável ao conhecimento que a motivou, permitindo que experiência, decisão e evidência retroalimentem conscientemente a evolução da forma de trabalhar.**

Documentos relacionados:
- `PILAR-2-STRUCTURED-OPERATIONAL-MEMORY-DRAFT.md`;
- `PILAR-2-REFERENCE-STACK-DRAFT.md`;
- `PILAR-2-FEASIBILITY-RESEARCH-001.md`.

## Pilar 3 — Sustentação científica e empírica explícita

**Estado para fechamento do manifesto:** em avaliação pelo mesmo gate; horizonte tecnológico inicial já encontrado.

A pesquisa inicial identifica uma composição concreta capaz de representar e governar referências, claims, evidências e provenance:

- Evidence-Based Software Engineering como antecedente metodológico;
- Nanopublications para claims granulares com provenance;
- RO-Crate para pacotes machine-readable de evidências e artefatos;
- W3C PROV para provenance interoperável;
- RDF + SHACL para representação e validação de constraints;
- Crossref, DataCite e OpenAlex para identificação, enriquecimento e relações de literatura científica;
- in-toto/SLSA para attestations e evidência operacional verificável;
- OPA ou engines equivalentes para políticas/gates determinísticos;
- memória operacional do Pilar 2 como fonte de evidência contextual;
- MyTrues/EDT/CCP como possível camada decisória/cognitiva quando amadurecidos.

A tecnologia necessária para representar, validar, consultar e aplicar políticas sobre evidências já existe por composição. O principal residual aberto é metodológico/científico: como graduar força de evidência, comparar classes heterogêneas de sustentação e definir score/maturidade sem falsa precisão.

Esse residual já está separado nas linhas P02/P03/P06 e não invalida a realizabilidade técnica do pilar.

Documento de pesquisa: `PILAR-3-FEASIBILITY-RESEARCH-001.md`.

## Estratégia LaboWare relacionada, mas externa ao manifesto

A estratégia da LaboWare de usar versões educacionais gratuitas para formar familiaridade acadêmica e favorecer posterior difusão industrial foi registrada separadamente em `LABOWARE-ACADEMIA-INDUSTRY-DIFFUSION-STRATEGY.md`.

Essa estratégia se beneficia de propriedades FlowED — linguagem comum, contratos, progressividade, continuidade do modelo mental e substituibilidade — mas não deve virar requisito de conformidade do framework.

A hipótese científica correspondente amplia P07: investigar se ferramentas contínuas entre academia e indústria podem inverter parcialmente a direção usual de difusão tecnológica.

## Próximo passo

Debater a formulação constitutiva do Pilar 3 usando o mesmo critério: demonstrar que a proposição é tecnicamente realizável, explicitar o que já possui prior art e isolar o que continua sendo hipótese científica. Se o gate for satisfeito sem contradição relevante, marcar o Pilar 3 como fechado e avançar ao Pilar 4.
