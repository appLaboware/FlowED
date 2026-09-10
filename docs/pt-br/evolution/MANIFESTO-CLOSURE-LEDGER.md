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

**Estado para fechamento do manifesto:** suficientemente realizável nesta fase.

A pesquisa identificou tecnologia real suficiente tanto para representar evidências quanto para materializar um futuro contrato substituível. Além das referências gerais de provenance/evidência já registradas, foi feita amostragem de ferramentas bibliométricas concretas na ponta.

Amostras principais:

- OpenAlex: resolução de works, DOI/IDs, relações bibliográficas, `cited_by_count`, séries por ano, FWCI e percentil normalizado em nível de work;
- SciVal/Scopus: Citation Count, Citations per Publication, FWCI, percentis e refinamentos como exclusão de autocitações;
- Dimensions: total/recent citations, FCR e RCR em nível de publicação;
- Semantic Scholar: citationCount, influentialCitationCount, tipos, campos e grafo de citations/references;
- Crossref: identidade DOI, tipos, metadados bibliográficos, relações, updates/retractions, dados da Retraction Watch e registros de peer review quando depositados.

Esses providers não são semanticamente idênticos, mas convergem em classes de informação suficientes para prever um contrato FlowED sem acoplá-lo a nenhuma métrica proprietária.

Regra arquitetural:

**provedores reais → propriedades praticadas → classes semânticas comuns → contrato FlowED → adapters/providers substituíveis.**

O contrato futuro não deve exigir `FWCI`, `FCR`, `RCR` ou outra métrica específica. Deve admitir classes como `field-normalized citation impact`, `raw citation count`, `normalized citation percentile` e `influential citation count`, preservando sempre provider, nome externo da métrica, metodologia/versão, população/baseline, janela temporal, normalização, timestamp e provenance. Métricas distintas podem ocupar a mesma classe funcional sem serem declaradas numericamente equivalentes.

Horizonte de objetos do contrato:

- `ReferenceIdentity` — identidade e metadados da referência;
- `ScientificRecognition` — processo científico/institucional efetivamente comprovável, com estados como confirmed/absent/unknown/conflicting;
- `InfluenceObservation` — observações bibliométricas brutas ou normalizadas com metodologia e provenance;
- `ScientificState` — normal/corrected/expression of concern/retracted/reinstated/superseded/unknown;
- `OperationalEvidence` — evidência de uso proveniente do Pilar 2;
- `AssessmentProfile` — projeção calculada e auditável sobre as observações, nunca confundida com a própria evidência.

Horizonte de operações públicas: resolver referência, coletar evidência, consultar estado científico, obter influência, anexar evidência operacional, avaliar por política versionada, explicar avaliação e comparar providers.

A implementação educacional/gratuita pode plausivelmente usar fontes abertas como OpenAlex + Crossref + Semantic Scholar. Implementações empresariais podem adicionar adapters para SciVal/Scopus, Dimensions, Web of Science/InCites ou outras fontes licenciadas sem alterar o contrato público.

A discussão de scoring mantém postura humilde. Publicação, citação e tempo de operação não medem verdade; são sinais distintos. Existência de DOI ou tipo `journal-article` também não prova, isoladamente, peer review. Ausência de evidência deve poder permanecer `unknown`.

O determinismo possível está no nível correto: **mesmas observações persistidas + mesma versão de regra = mesmo assessment**. Uma atualização posterior de uma base gera novo snapshot/assessment; não reescreve silenciosamente o passado.

Formulação candidata do Pilar 3:

> **O FlowED torna explícita e rastreável a sustentação disponível para cada referência relevante, distinguindo reconhecimento científico, influência observável, estado da evidência e experiência operacional. Avaliações são produzidas por regras versionadas sobre evidências identificáveis e podem ser recalculadas ou substituídas sem confundir score com verdade.**

Ainda ficam abertos para pesquisa P02/P03/P06/P09: definição exata de reconhecimento científico por classe de artefato, normalização entre providers, citações negativas/autocitações, composição entre evidência científica e operacional e eventual score agregado. Essas lacunas não bloqueiam o manifesto porque a arquitetura e o contrato podem preservar o vetor de observações sem inventar ranking universal.

Documentos relacionados:
- `PILAR-3-FEASIBILITY-RESEARCH-001.md`;
- `PILAR-3-DETERMINISTIC-EVIDENCE-SCORING-DRAFT.md`;
- `PILAR-3-RESPONSIBLE-RESEARCH-ASSESSMENT-REFERENCE.md`;
- `PILAR-3-CONTRACT-HORIZON-DRAFT.md`.

## Estratégia LaboWare relacionada, mas externa ao manifesto

A estratégia da LaboWare de usar versões educacionais gratuitas para formar familiaridade acadêmica e favorecer posterior difusão industrial foi registrada separadamente em `LABOWARE-ACADEMIA-INDUSTRY-DIFFUSION-STRATEGY.md`.

Essa estratégia se beneficia de propriedades FlowED — linguagem comum, contratos, progressividade, continuidade do modelo mental e substituibilidade — mas não deve virar requisito de conformidade do framework.

A hipótese científica correspondente amplia P07: investigar se ferramentas contínuas entre academia e indústria podem inverter parcialmente a direção usual de difusão tecnológica.

## Próximo passo

Avançar ao Pilar 4 — **Progressividade governada** — e aplicar o mesmo gate: definir a claim mínima, buscar prior art e tecnologias reais que já materializem seleção contextual de rigor/capability/policy, prever o horizonte de um contrato substituível e somente então considerar o pilar suficientemente fechado.
