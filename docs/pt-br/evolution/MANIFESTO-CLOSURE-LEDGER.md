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

**Estado para fechamento do manifesto:** realizabilidade técnica fortemente estabelecida; modelo de scoring refinado, ainda não fechado em fórmula única.

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

A tecnologia necessária para representar, validar, consultar e aplicar políticas sobre evidências já existe por composição.

A discussão de scoring adotou uma postura mais humilde. Publicação científica, citações e tempo de operação não devem ser chamados de medida de verdade. Eles representam dimensões distintas de sustentação.

Direção atual:

- **reconhecimento científico formal** pode ser uma dimensão determinística, preservando o tipo de revisão/publicação;
- **influência científica** pode usar citações e métricas normalizadas quando disponíveis;
- **métricas do veículo** podem ser registradas, mas não devem funcionar automaticamente como proxy de qualidade do artigo individual;
- **evidência operacional** deve considerar tempo, exposição, diversidade de contexto, sucessos/falhas, recência e versões quando esses dados existirem;
- **rastreabilidade/proveniência** qualifica a confiabilidade dos próprios sinais usados.

A fórmula simples `publicação × score do periódico + citações + tempo` não é aceita ainda porque pode produzir falsa precisão, dupla contagem e vieses de campo/idade. O estado preferido nesta fase é um vetor auditável e determinístico; agregação posterior só deve existir se seus pesos e normalizações forem defensáveis.

Importante: existência de publicação científica não é gate global de Full FlowED. Ela pode ser uma condição de **compliance científico** ou dimensão do perfil de sustentação. Uma organização pode adotar referência não publicada e acumular evidência operacional forte, desde que a situação seja explícita e rastreável.

Formulação candidata mais humilde para o Pilar 3:

> **Toda referência relevante deve tornar explícitos os tipos de sustentação que possui, sua proveniência, sua influência científica quando mensurável, sua evidência operacional e suas lacunas. O FlowED pode calcular indicadores determinísticos a partir de sinais externos e regras versionadas, sem declarar que esses indicadores medem verdade.**

Documento de scoring: `PILAR-3-DETERMINISTIC-EVIDENCE-SCORING-DRAFT.md`.

O residual metodológico/científico permanece em P02/P03/P06/P09 e não invalida a realizabilidade técnica do pilar.

## Estratégia LaboWare relacionada, mas externa ao manifesto

A estratégia da LaboWare de usar versões educacionais gratuitas para formar familiaridade acadêmica e favorecer posterior difusão industrial foi registrada separadamente em `LABOWARE-ACADEMIA-INDUSTRY-DIFFUSION-STRATEGY.md`.

Essa estratégia se beneficia de propriedades FlowED — linguagem comum, contratos, progressividade, continuidade do modelo mental e substituibilidade — mas não deve virar requisito de conformidade do framework.

A hipótese científica correspondente amplia P07: investigar se ferramentas contínuas entre academia e indústria podem inverter parcialmente a direção usual de difusão tecnológica.

## Próximo passo

Debater se a formulação humilde do Pilar 3 é suficiente para fechamento do manifesto. Se sim, marcar o Pilar 3 como suficientemente realizável e avançar ao Pilar 4 — progressividade governada — aplicando o mesmo gate de realizabilidade tecnológica.
