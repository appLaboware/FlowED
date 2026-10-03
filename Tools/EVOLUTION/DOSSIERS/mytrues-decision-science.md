# Dossiê — MyTrues e Ciência da Decisão

## Produto ensaiado

MyTrues é memória decisória pertencente a um técnico/equipe/fornecedor.

Conhecido:

`case -> provider memory -> approved decision -> resume`

Desconhecido:

`pause -> anonymize -> human sandbox -> explicit resolution -> retain -> resume`

## Regra open-first

Tudo que já existe na ciência entra na baseline aberta.

Isso inclui métodos de ranking, recuperação, decisão probabilística, MCDA, CBR,
regras, grafos, vetores e calibração quando forem técnicas publicadas.

"Privado" e "proprietário" são categorias diferentes:

- memória de um técnico pode ser privada por confidencialidade;
- um algoritmo público usado sobre essa memória continua sendo conhecimento aberto;
- Core só começa quando existir delta original mensurável.

## Baselines científicas a reproduzir

### Symbolic / deterministic

- regras;
- decision tables;
- DMN;
- constraint/guard evaluation.

### Experience-based

- Case-Based Reasoning:
  retrieve -> reuse -> revise -> retain;
- similarity functions;
- adaptation;
- case competence/coverage.

### Multi-criteria

- MCDA/MCDM;
- preference elicitation;
- criteria weighting;
- outranking/value functions;
- robust ordinal approaches.

### Probabilistic

- Bayesian decision theory;
- probabilistic graphical models;
- expected utility;
- uncertainty propagation.

### Retrieval

- lexical;
- graph;
- vector;
- hybrid;
- reranking.

### Learning

- supervised ranking;
- learning-to-rank;
- contextual feedback;
- calibration;
- abstention/reject option.

### Human-centered

- expert elicitation;
- approval;
- disagreement;
- escalation;
- audit;
- provenance;
- decision revision/revocation.

## Estado da arte que importa ao MyTrues

Não basta "acertar decisão".

O benchmark deve medir:

- utilidade da decisão;
- risco;
- confiança/calibração;
- capacidade de abstener;
- tempo do sênior;
- consistência;
- explicabilidade/provenance;
- recuperação de caso relevante;
- adaptação;
- efeito do feedback;
- erro perigoso;
- custo de rollback.

## Science Frontier Gate específico

MyTrues Core só pode nascer depois que:

1. famílias acima tiverem baseline;
2. benchmark tiver casos com múltiplas decisões plausíveis;
3. resultados públicos forem comparados;
4. lacuna persistente estiver documentada;
5. uma melhoria nossa tiver hipótese falsificável.

Até lá, `core/` permanece sem algoritmo proprietário.
