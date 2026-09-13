# Protocolo de Discovery e Validação Progressiva

**Status:** proposta de adoção composta — baseada em métodos científicos e de Engenharia de Software já estabelecidos; ainda sujeita à simulação FlowED e à validação de adequação.

## 1. Problema

O FlowED precisa normalizar como uma referência, teoria, prática, mecanismo ou tecnologia entra no sistema, cresce em maturidade e aumenta ou reduz sua sustentação sem ser promovida prematuramente a verdade.

A pesquisa realizada não encontrou um único método que cubra sozinho todo esse ciclo. Entretanto, há componentes maduros e complementares que cobrem praticamente todas as partes necessárias. Portanto, pela regra Adapt First, a proposta é **adotar uma composição de métodos existentes antes de inventar um processo próprio**.

## 2. Ancestrais/métodos a adotar

### 2.1 Evidence-Based Software Engineering — EBSE

Uso principal no FlowED: **Discovery, prior art e síntese de evidência externa**.

Kitchenham, Dybå e Jørgensen propõem que decisões em Engenharia de Software sejam informadas por evidência acumulada, com atenção aos limites específicos do domínio. Revisões sistemáticas são usadas para identificar, avaliar e sintetizar evidência de forma explícita e auditável.

Adaptação FlowED: toda referência relevante deve declarar o nível de diligência da busca realizada, bases/fontes consultadas, recorte temporal, critérios de inclusão/exclusão e lacunas conhecidas. A intensidade da busca deve ser proporcional ao risco e à importância da decisão.

### 2.2 Design Science Research Methodology — DSRM

Uso principal no FlowED: **construção e avaliação de artefatos, métodos e mecanismos novos ou adaptados**.

O processo de Peffers et al. contém seis atividades: identificação/motivação do problema; objetivos da solução; design/desenvolvimento; demonstração; avaliação; comunicação.

Adaptação FlowED: DSRM torna-se o esqueleto preferencial quando o objeto de pesquisa é um artefato ou método criado/adaptado, evitando que uma solução seja tratada apenas como opinião conceitual.

### 2.3 Technology Transfer Model — TTM / Gorschek-Wohlin

Uso principal no FlowED: **validação progressiva da academia/conceito para uso real**.

O modelo amadurece uma solução por etapas e tipos diferentes de evidência. A literatura de transferência em Engenharia de Software distingue validação estática/mais controlada de validação dinâmica em contexto real, e só então liberação mais ampla.

Adaptação FlowED: uma referência pode subir de maturidade conforme atravessa ambientes progressivamente mais realistas. Resultado negativo pode fazê-la retornar, restringir escopo ou ser abandonada.

### 2.4 Estudos de caso e Action Research

Uso principal no FlowED: **validação contextual e evolução durante uso real**.

Estudos de caso permitem investigar fenômenos contemporâneos no contexto natural. Action Research é apropriada quando a pesquisa não apenas observa, mas participa da mudança organizacional.

Adaptação FlowED: quando uma prática FlowED é implantada e modificada junto com a organização, a rodada deve ser tratada explicitamente como intervenção, com contexto, participantes, mudança realizada, dados coletados, ameaças à validade e efeitos observados.

### 2.5 Goal Question Metric — GQM

Uso principal no FlowED: **medição orientada a objetivos**.

GQM parte de um objetivo, deriva perguntas que permitam avaliar esse objetivo e só então seleciona métricas.

Adaptação FlowED: nenhuma métrica deve existir apenas porque é fácil de coletar. Cada métrica precisa apontar para uma pergunta e cada pergunta para um objetivo/hipótese.

### 2.6 Technology Readiness Levels — TRL

Uso principal no FlowED: **inspiração para estados explícitos de maturidade/realizabilidade**, não como score de evidência.

TRL demonstra que maturidade pode ser representada por níveis sucessivos, desde princípios observados até operação comprovada em ambiente real. FlowED não deve copiar os nove níveis mecanicamente; deve adotar o princípio de separar maturidade/realizabilidade de eficácia e força de evidência.

## 3. Composição proposta para o FlowED

O processo canônico de Discovery e Validação Progressiva passa a ter sete macrofases:

### D0 — Formulação e enquadramento

Registrar problema, contexto, atores, risco, impacto, estado atual, hipótese inicial e o que seria considerado sucesso ou falha.

Saída mínima: `Research/Reference Brief` versionado.

### D1 — Discovery / anterioridade / estado da arte

Aplicar Adapt First:

**adotar → adaptar → compor → inventar somente o residual demonstrado**.

A busca deve começar por referências estabelecidas, padrões, literatura científica, implementações maduras e evidência operacional relevante.

A diligência é proporcional ao risco. Para decisões pequenas pode haver rapid review/scoping search; para claims fortes, publicação científica, baseline central ou certificação, usar protocolo sistemático mais rigoroso.

Saída mínima: mapa de prior art, evidências encontradas, lacunas, residual candidato e limite declarado da busca.

### D2 — Hipóteses e objetivos mensuráveis

Usar GQM:

**objetivo → perguntas → métricas/observações**.

Declarar hipótese principal, alternativas concorrentes quando existirem, critérios que fortaleceriam ou enfraqueceriam a referência e ameaças de interpretação.

Saída mínima: plano de avaliação antes do teste.

### D3 — Construção/adaptação

Quando houver artefato, método ou mecanismo a criar, usar DSRM:

problema → objetivos → design/desenvolvimento → demonstração.

Toda invenção precisa apontar para o residual que não pôde ser adequadamente adotado ou adaptado.

### D4 — Validação controlada / estática

Testar em ambiente reduzido ou controlável antes de exposição maior. Pode usar análise, experimento, simulação, revisão por especialistas, benchmark ou protótipo.

Objetivo: descobrir falhas baratas e testar plausibilidade, eficácia inicial, coerência e escalabilidade potencial.

### D5 — Validação contextual / dinâmica

Executar piloto ou uso real. Preferir estudo de caso quando observacional e Action Research quando houver intervenção colaborativa.

Registrar contexto suficiente para avaliar transferibilidade: pessoas, organização, domínio, escala, duração, limitações, adaptação local e efeitos adversos.

### D6 — Síntese, atualização e decisão

Confrontar resultado com a evidência anterior e atualizar separadamente:

- realizabilidade/maturidade;
- sustentação científica;
- sustentação empírica/operacional;
- aplicabilidade contextual;
- riscos/gaps;
- decisão de adoção.

Decisões possíveis: adotar, manter experimental, adaptar, restringir escopo, repetir, suspender, abandonar ou abrir nova pesquisa.

A referência volta ao fluxo quando nova evidência relevante surgir.

## 4. Como uma coisa cresce e se valida progressivamente

O crescimento não deve ser um único número. A ciência e a engenharia usam diferentes métodos porque cada etapa responde a perguntas distintas.

Uma referência pode, por exemplo:

- ser altamente realizável e pouco sustentada;
- ter forte literatura, mas baixa validação no contexto local;
- funcionar em piloto e falhar ao escalar;
- ter evidência operacional positiva e teoria científica ainda insuficiente;
- perder sustentação após novas replicações ou falhas.

Portanto, FlowED deve preservar **vetores de estado**, não uma escada única de verdade.

## 5. Fórmulas e scoring

### 5.1 Não adotar soma ingênua

Não usar fórmula do tipo `paper + teste + uso = score total` sem uma teoria de mensuração. Evidências de naturezas diferentes não são automaticamente comensuráveis.

### 5.2 Adotar inicialmente perfil multidimensional

Cada referência deve possuir pelo menos dimensões independentes:

- `R` — realizabilidade/maturidade;
- `S` — sustentação científica;
- `E` — sustentação empírica/operacional;
- `C` — adequação/contextualidade;
- `T` — rastreabilidade/proveniência;
- `V` — estado de validação/replicação.

Os nomes e escalas ainda são pesquisa. A regra imediata é **não colapsar tudo em escalar único**.

### 5.3 GQM antes da métrica

Para cada dimensão ou claim:

`Objetivo → Pergunta → Métrica/Observação → Critério de interpretação`.

Nenhuma métrica entra no score sem essa linhagem.

### 5.4 Bayesian updating apenas quando defensável

Atualização Bayesiana é candidata para hipóteses quantitativas em que priors, likelihood e dados possam ser definidos de forma defensável. Não deve ser o mecanismo universal de scoring do FlowED.

Quando aplicável:

`Posterior odds = Prior odds × Bayes factor`.

O benefício é tratar evidência nova como atualização explícita de crença, mas isso não resolve por si só heterogeneidade de contexto, qualidade metodológica ou validade de constructo.

### 5.5 Gates além de score

Algumas condições devem ser tratadas como gates e não compensadas por pontuação. Exemplos: risco de segurança inaceitável, violação legal, ausência de rastreabilidade mínima para claim crítico ou teste que contradiga diretamente uma premissa constitutiva no escopo declarado.

## 6. Níveis de diligência de Discovery

O protocolo deve ser proporcional ao risco:

- **Diligência L0 — lookup:** confirmar conceito/fonte conhecida;
- **L1 — exploratory/scoping search:** verificar plausibilidade e prior art suficiente para R1;
- **L2 — structured rapid review:** perguntas e critérios explícitos, múltiplas fontes/bases, registro reproduzível;
- **L3 — systematic review/mapping:** protocolo formal, busca ampla, seleção, avaliação de qualidade e síntese;
- **L4 — revisão/publicação científica:** revisão sistemática adequada ao claim, dados e protocolo publicáveis/criticáveis externamente.

O nível necessário depende de impacto, irreversibilidade, risco, novidade e força do claim.

## 7. Gates de promoção

Uma referência só avança para exposição maior se:

1. o estado de realizabilidade permitir o próximo teste;
2. gaps bloqueantes do próximo escopo estiverem resolvidos ou mitigados;
3. critérios de sucesso/falha tiverem sido definidos antes da observação quando possível;
4. o contexto e riscos estiverem declarados;
5. a evidência produzida e adversa estiver sendo preservada;
6. houver decisão explícita de promoção.

Promoção não significa verdade; significa autorização para uma etapa de validação mais exigente.

## 8. Relação com o protocolo de simulação existente

`THEORY-SIMULATION-PROTOCOL.md` permanece válido, mas passa a ser uma especialização operacional dentro deste processo maior.

O novo encadeamento proposto é:

**Discovery (EBSE/Adapt First) → hipótese e mensuração (GQM) → construção (DSRM) → validação progressiva (TTM) → estudo contextual/Action Research → síntese e atualização → nova rodada**.

O protocolo de simulação continua normalizando Referências Experimentais, gaps, evidências, decisões e linhagem tipo-MyTrues.

## 9. Decisão provisória FlowED

A rotina de Discovery e crescimento progressivo **não deve ser inventada do zero**. Há prior art suficiente para compor um processo robusto.

A contribuição candidata do FlowED não é criar novos métodos científicos, mas:

1. selecionar e normalizar quando cada método deve ser usado;
2. conectar Discovery, construção, validação, evidência, score e decisão em uma única linhagem operacional;
3. manter estados epistemológicos e de maturidade separados;
4. tornar o processo proporcional ao risco;
5. fazer a própria referência retornar continuamente ao ciclo quando houver nova evidência.

## 10. Impacto nos gaps

- `GAP-M013` Adapt First: avanço forte; candidato a regra constitutiva do Discovery.
- `GAP-M014` portas de entrada do fluxo: avanço forte; fluxo deve aceitar adoção, adaptação, composição e invenção residual.
- `GAP-M017` fronteira mínima de busca: avanço parcial; níveis L0–L4 propostos, ainda precisam ser testados.
- `GAP-M002` score multidimensional: reforço da decisão de evitar escalar único e usar GQM antes de métricas.
- `GAP-M009` classes de sustentação: reforço da necessidade de preservar classes independentes.

## 11. Próximos testes

1. aplicar D0–D6 ao próprio Manifesto FlowED;
2. aplicar o protocolo a um único princípio do manifesto e verificar custo/clareza;
3. comparar a classificação da mesma referência em dois contextos distintos;
4. testar se L0–L4 realmente reduzem burocracia sem perder rastreabilidade;
5. somente depois propor escalas quantitativas de score.
