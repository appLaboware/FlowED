# Pilar 3 — horizonte de contrato para sustentação científica e empírica

**Status:** Referência Experimental para fechamento do Pilar 3 do Manifesto FlowED.

## 1. Objetivo desta rodada

O objetivo não é implementar o contrato nem escolher um fornecedor obrigatório. É demonstrar, no mesmo nível de maturidade exigido para os Pilares 1 e 2, que existe tecnologia real suficiente na ponta para permitir um contrato FlowED substituível.

Critério da rodada:

**provedores reais -> propriedades já praticadas -> mínimo semântico comum -> contrato FlowED -> adapters/providers substituíveis**.

## 2. Amostragem de provedores e propriedades úteis

### OpenAlex

Propriedades relevantes observáveis em nível de trabalho:

- identidade e resolução de works;
- DOI e outros identificadores;
- tipo e data de publicação;
- fonte/venue e tópicos/subcampos;
- `cited_by_count`;
- `counts_by_year`;
- `fwci` em nível de work;
- `citation_normalized_percentile`;
- relações de referências/citações.

O FWCI do OpenAlex já é normalizado por tipo de work, ano e subcampo, com 1.0 como média mundial.

### Elsevier SciVal / Scopus

Propriedades relevantes:

- Citation Count;
- Citations per Publication;
- FWCI;
- métricas com refinamentos como exclusão de autocitações;
- percentis de citação e outras métricas bibliométricas.

O FWCI compara citações observadas com o esperado para publicações similares por ano, tipo e disciplina.

### Dimensions

Propriedades relevantes em nível de publicação:

- total citations;
- recent citations;
- Field Citation Ratio (FCR);
- Relative Citation Ratio (RCR);
- exposição das mesmas métricas via DSL/API em produtos que as suportam.

FCR compara uma publicação com trabalhos de idade e área semelhantes; valores são centrados em 1.0.

### Semantic Scholar

Propriedades relevantes:

- `citationCount`;
- `influentialCitationCount`;
- campos de estudo;
- tipo e data de publicação;
- relações de citations/references;
- classificação de uma citação como influente em sua API.

Isso demonstra que um provider pode oferecer não apenas contagem bruta, mas uma interpretação própria da influência de citações.

### Crossref

Propriedades relevantes:

- DOI e metadados bibliográficos depositados por publishers;
- tipos de work;
- datas, autores, ORCID/ROR, funding, licenças e relações;
- `is-referenced-by-count` quando disponível;
- updates pós-publicação;
- corrections/retractions;
- integração de dados da Retraction Watch;
- registros de peer review quando estes são depositados e relacionados ao item revisado.

Limite importante: a presença de um `journal-article` no Crossref não constitui, por si só, prova universal de que o artigo foi peer-reviewed. O contrato FlowED não pode inferir reconhecimento científico formal apenas da existência de DOI ou tipo de publicação.

## 3. Consequência arquitetural

As ferramentas acima não usam exatamente os mesmos nomes nem os mesmos algoritmos, mas convergem em classes de informação suficientes para prever um contrato sem amarrá-lo a um fornecedor específico.

O contrato deve padronizar **semântica**, não a fórmula proprietária de cada métrica.

Exemplo: o contrato não exige `FWCI`. Ele pode admitir uma classe semântica `field_normalized_citation_impact`, dentro da qual um provider declara:

- nome externo da métrica: FWCI, FCR, CNCI ou equivalente;
- valor;
- baseline/centro esperado quando aplicável;
- unidade/interpretação;
- dimensões de normalização usadas;
- população de comparação;
- janela temporal;
- inclusão/exclusão de autocitação;
- provider;
- versão/metodologia do provider;
- data de cálculo/consulta;
- provenance/evidence link.

Dessa forma, duas métricas diferentes não são silenciosamente declaradas idênticas; elas podem ocupar a mesma **classe funcional** e preservar suas diferenças metodológicas.

## 4. Horizonte do contrato público

Uma capability de sustentação científica/empírica poderia expor, no mínimo, os seguintes objetos semânticos.

### 4.1 ReferenceIdentity

Representa a referência avaliada:

- `reference_id` interno estável;
- identificadores externos: DOI, OpenAlex ID, Semantic Scholar ID e outros quando existirem;
- título;
- tipo de artefato;
- data/ano;
- autores/organizações quando relevantes;
- versão/edição;
- source/venue;
- relações conhecidas com outras referências.

### 4.2 ScientificRecognition

Representa somente aquilo que pode ser provado sobre o processo científico/institucional:

- `status`: confirmed / absent / unknown / conflicting;
- `recognition_type`: peer_review, thesis_defense, conference_review, registered_report, standardization_process ou outro tipo versionado;
- autoridade/fonte que afirma o reconhecimento;
- evidência verificável;
- data;
- limitações.

Regra: ausência de evidência não vira automaticamente `false`; pode permanecer `unknown`.

### 4.3 InfluenceObservation

Representa sinais bibliométricos sem chamá-los de verdade:

- `metric_class`;
- `provider_metric_name`;
- `value`;
- `raw_citation_count` quando disponível;
- normalização aplicada;
- campo/subcampo;
- ano/tipo usados na comparação;
- população/baseline;
- janela temporal;
- autocitações incluídas/excluídas/desconhecidas;
- provider e versão;
- retrieved/calculated_at;
- provenance.

Classes candidatas já materializáveis:

- raw citation count;
- recent citation count;
- field-normalized citation impact;
- normalized citation percentile;
- influential citation count;
- top-percentile membership.

### 4.4 ScientificState

Representa fatos que podem alterar a interpretação da referência:

- active/normal;
- corrected;
- expression_of_concern;
- retracted;
- reinstated;
- superseded;
- unknown.

Cada estado precisa de fonte e provenance. O FlowED não deve inferir retratação por heurística quando houver fonte autoritativa disponível.

### 4.5 OperationalEvidence

Conecta o Pilar 3 à memória do Pilar 2 sem misturar ciência e operação:

- primeira/última observação;
- tempo em operação;
- quantidade de exposições/execuções;
- contextos/projetos/organizações observados quando disponíveis;
- sucessos/falhas e critérios usados;
- versão da referência/prática observada;
- event/evidence IDs;
- provenance.

Evidência operacional reforça a dimensão operacional; não transforma uma referência em cientificamente reconhecida.

### 4.6 AssessmentProfile

É uma projeção calculada das observações anteriores, não a própria evidência.

Pode conter:

- scientific recognition/compliance;
- influence indicators;
- operational evidence indicators;
- data/provenance completeness;
- warnings/conflicts;
- policy result quando uma organização aplica uma política específica;
- `assessment_rule_version`.

O contrato deve preservar os dados subjacentes para que qualquer score seja auditável e recalculável.

### 4.7 ClassifierOpinion

O contrato deve também admitir providers que produzam uma **opinião quantitativa composta** sobre o conjunto de evidências.

Esse objeto não é obrigatório para todos os providers e não representa um score canônico do FlowED. Ele permite que classificadores independentes — inclusive uma implementação de referência mantida pelo ecossistema FlowED — expressem uma composição própria, desde que transparente e versionada.

Campos semânticos candidatos:

- `classifier_id`;
- `classifier_version`;
- `method_id` / `method_version`;
- valor agregado e escala;
- interpretação da escala;
- dimensões/componentes;
- snapshots de entrada;
- normalizações;
- pesos e método de agregação;
- tratamento de dados ausentes;
- warnings/conflitos;
- robustez/incerteza quando disponível;
- provenance;
- `assessed_at`.

Diferentes classificadores podem produzir opiniões distintas sobre a mesma evidência sem violar o contrato. A comparação deve preservar metodologia e decomposição, e não supor equivalência matemática entre scores.

## 5. Operações públicas candidatas

Sem fechar sintaxe de CLI/API, a capability precisa ser capaz de materializar operações semanticamente equivalentes a:

1. **resolve reference** — resolver uma referência a partir de DOI/ID/metadados;
2. **collect evidence** — coletar observações científicas e bibliométricas de um ou mais providers;
3. **get scientific state** — consultar correções/retrações/outros estados conhecidos;
4. **get influence** — obter métricas brutas/normalizadas preservando metodologia e provenance;
5. **attach operational evidence** — relacionar observações operacionais do Pilar 2;
6. **assess** — aplicar uma política/regra versionada sobre as observações;
7. **explain assessment** — devolver todos os sinais, regras e provenance que produziram o resultado;
8. **compare providers** — expor diferenças entre providers sem forçar equivalência falsa;
9. **get classifier opinion** — solicitar opinião composta de um classificador específico;
10. **compare classifier opinions** — comparar opiniões de classificadores preservando escala, método e componentes.

Essas operações são horizonte de contrato, não API final.

## 6. Provider de referência e substituição

Uma primeira implementação educacional/gratuita pode ser plausivelmente composta sobre fontes abertas, sobretudo OpenAlex + Crossref + Semantic Scholar, adicionando a memória operacional FlowED.

Uma implementação empresarial pode possuir adapters para SciVal/Scopus, Dimensions, Web of Science/InCites e outras fontes licenciadas, sem alterar a semântica pública do contrato.

Além dos providers de evidência, o ecossistema FlowED deve manter um **classificador composto de referência** como alternativa pronta. Esse classificador deverá usar os melhores indicadores disponíveis segundo uma metodologia aberta/versionada e produzir uma opinião quantitativa reproduzível.

Ele terá o mesmo estatuto de qualquer outro classificador compatível. Uma equipe poderá substituí-lo, comparar vários classificadores ou ignorar scores agregados e trabalhar apenas com o vetor de evidências.

A metodologia do classificador de referência deve seguir prior art de construção de composite indicators, incluindo normalização, peso, agregação, correlação, compensabilidade e análise de sensibilidade/robustez. Naming comercial fica aberto.

Documento relacionado: `PILAR-3-REFERENCE-OPINION-CLASSIFIER-DRAFT.md`.

## 7. Determinismo possível

O contrato permite determinismo no nível correto:

- mesma observação armazenada + mesma versão de regra -> mesmo resultado de assessment;
- mesma entrada + mesma versão de classificador/metodologia -> mesma opinião do classificador;
- o resultado declara quais providers, timestamps, metodologias e versões alimentaram o cálculo;
- uma atualização posterior da base pode alterar a observação, mas gera novo snapshot/assessment, não reescreve silenciosamente o anterior;
- ausência/indisponibilidade de dado produz estado explícito, não valor inventado.

O FlowED não promete que dois providers ou classificadores retornarão o mesmo número. Promete que cada número possui identidade semântica, provenance e regras de interpretação explícitas.

## 8. O que a amostragem prova

A amostragem mostra que já existem sistemas em produção capazes de fornecer os elementos centrais do futuro contrato:

- resolução e metadados científicos;
- relações bibliográficas;
- contagens de citação;
- métricas normalizadas por campo/tempo/tipo;
- percentis;
- citações influentes;
- estados de correção/retração;
- alguns registros explícitos de peer review;
- APIs/DSLs capazes de automatizar coleta.

A literatura de composite indicators mostra ainda que há método estabelecido para transformar múltiplos indicadores heterogêneos em índices compostos, desde que normalização, pesos, agregação, correlação e incerteza sejam tratados explicitamente.

Logo, o FlowED não depende de inventar infraestrutura bibliométrica nem metodologia geral de composição de indicadores para materializar o Pilar 3.

## 9. Limites preservados

Ainda ficam para pesquisa posterior:

- quais processos contam como reconhecimento científico para cada classe de artefato;
- normalização entre métricas não equivalentes de providers distintos;
- tratamento de citações negativas, autocitações e manipulação bibliométrica;
- qualidade mínima de provenance;
- composição de evidência científica e operacional;
- fórmula específica do classificador de referência;
- validação de pesos, agregação e robustez;
- validação da relação entre o perfil FlowED e qualidade/resultados reais de Engenharia de Software.

Essas lacunas não impedem um contrato inicial porque o contrato pode preservar o vetor de observações e permitir classificadores concorrentes sem inventar um ranking universal.

## 10. Decisão para o manifesto

**Estado de realizabilidade:** suficientemente forte para fechamento do Pilar 3 nesta fase.

Há tecnologia real na ponta, fontes abertas e comerciais, métricas já operadas em escala, APIs e identificadores estáveis. Existe um caminho plausível para uma implementação gratuita/educacional, providers empresariais alternativos e um classificador composto de referência não autoritativo.

Formulação candidata do Pilar 3:

> **O FlowED torna explícita e rastreável a sustentação disponível para cada referência relevante, distinguindo reconhecimento científico, influência observável, estado da evidência e experiência operacional. Avaliações são produzidas por regras versionadas sobre evidências identificáveis e podem ser recalculadas ou substituídas sem confundir score com verdade.**

O contrato definitivo e a fórmula do classificador de referência serão produzidos em projeto posterior, guiados por contract tests e adapters, sem bloquear o manifesto atual.
