# FlowED — Proposta de Tese: Princípio da Mínima Fatoração Necessária

**ID:** FLOWED-RESEARCH-MNF-001  
**Versão:** 0.1-draft  
**Status:** RESEARCH PROPOSAL / UNVALIDATED  
**Domínio:** FlowED  
**Nome em português:** Princípio da Mínima Fatoração Necessária  
**Rótulo inglês provisório:** Minimum Necessary Factorization Principle (MNFP)  
**Nota terminológica:** a tradução inglesa é provisória e deverá ser validada academicamente, pois `factorization` pode carregar sentidos matemáticos e de decomposição distintos do uso pretendido aqui.

## Formulação candidata

> **Ao decidir como realizar uma capacidade de software, deve-se construir propriedade nova somente na extensão residual que não possa ser atendida de forma admissível por adoção, configuração, extensão, composição, adaptação ou derivação de soluções existentes.**

Forma compacta:

> **Fatorar apenas o que precisa existir como fator novo.**

Esta formulação é uma hipótese/princípio de pesquisa, não uma alegação de novidade estabelecida.

## Motivação

A decisão de engenharia normalmente não é binária entre `BUILD` e `BUY`. Uma solução pode ser obtida por múltiplos graus de reutilização e transformação.

Escada operacional candidata:

```text
0. DON'T
1. ADOPT
2. CONFIGURE
3. EXTEND
4. COMPOSE
5. ADAPT
6. FORK
7. INVENT COMPONENT
8. INVENT SYSTEM
```

O princípio propõe que a decisão preferencial seja a alternativa de menor criação proprietária que ainda satisfaça requisitos funcionais, qualidade, risco, sustentabilidade, soberania, custo total, manutenção e demais restrições relevantes.

## Definição operacional de "fatoração"

Neste trabalho, `fatoração` não significa simplesmente refatoração de código.

Ela representa a materialização de um **fator proprietário novo** que passa a exigir responsabilidade de engenharia própria: desenho, implementação, testes, manutenção, evolução, segurança, compatibilidade e suporte.

Assim, um fator pode ser:

- componente;
- adapter;
- contrato;
- orquestração;
- integração;
- transformação;
- algoritmo;
- workflow;
- serviço;
- sistema completo.

A pergunta central é:

> **Qual é o menor conjunto de fatores novos cuja propriedade própria ainda é necessária depois de esgotadas as alternativas admissíveis de reutilização?**

## Relação com prior art já identificado

A busca exploratória inicial NÃO encontrou o termo exato `Minimum Necessary Factorization Principle` como princípio consolidado de engenharia de software.

Entretanto, partes importantes da ideia já existem e precisam ser tratadas como prior art, não como contribuição própria:

### Reuse before buy before build

Princípios de arquitetura pública e empresarial já determinam reutilizar sistemas existentes antes de comprar e construir. A European Interoperability Architecture registra explicitamente `Reuse, before buy, before build`; arquiteturas empresariais e referências históricas também usam variações de `reuse before buy before build`.

Referências iniciais:

- European Interoperability Architecture / EIF — `Reuse, before buy, before build`: https://interoperable-europe.ec.europa.eu/collection/common-assessment-method-standards-and-specifications-camss/solution/elap/reuse-buy-build
- Oracle Reference Architecture, Software Engineering 3.0 — princípio de reuse e sequência `Reuse before Version before Buy before Build`.

### Component sourcing / make-or-buy ampliado

A literatura de Component-Based Software Engineering trata múltiplas alternativas de sourcing, incluindo desenvolvimento interno, outsourcing, COTS e OSS. Pesquisa empírica mostra que organizações consideram múltiplas opções e que a adequação funcional atua como filtro inicial.

Referência inicial:

- Badampudi et al. Selecting component sourcing options: A survey of software engineering's broader make-or-buy decisions. Information and Software Technology 112 (2019), 18–34. DOI: https://doi.org/10.1016/j.infsof.2019.03.015

### Software reuse e composição

Software reuse já estabelece que sistemas devem ser construídos a partir de ativos existentes quando isso é adequado. A tradição Unix também explicita a combinação de componentes existentes com mínimo de invenção nova.

### Architectural innovation

A literatura de inovação arquitetural demonstra que diferenciação pode residir na recombinação ou relação entre componentes existentes, sem exigir novidade em todos os componentes.

### Minimum Viable Capability / MVP

Há literatura sobre minimizar o escopo necessário para validar ou entregar capacidade, porém isso não é equivalente ao problema aqui: o foco do MNFP não é minimizar features de uma entrega, mas minimizar **propriedade nova necessária** depois da busca de reutilização, sourcing e composição.

## Resultado preliminar do novelty gate

### O que parece conhecido

- reuse before build;
- buy/make/sourcing decisions;
- COTS/OSS/component selection;
- composição de componentes;
- architectural innovation;
- MVP/MVC e minimização de escopo;
- open innovation e adoção/modificação de soluções externas.

### Residual científico potencial

A contribuição NÃO pode ser simplesmente:

> "reutilize antes de construir".

Isso já existe.

O possível residual está em formalizar e testar um protocolo integrado que:

1. decompõe uma intenção em capabilities;
2. pesquisa sistematicamente soluções completas e parciais;
3. classifica alternativas em `ADOPT / CONFIGURE / EXTEND / COMPOSE / ADAPT / FORK / INVENT`;
4. calcula explicitamente o residual proprietário;
5. mede a **Mínima Fatoração Necessária**;
6. separa quantidade de invenção de valor de diferenciação;
7. associa cada decisão a evidência, contraevidência, incerteza e confiança;
8. reabre a decisão quando o ecossistema externo muda;
9. testa se a redução de fatoração própria diminui custo e manutenção sem degradar qualidade, autonomia e diferenciação.

Classificação inicial:

```text
REUSE-BEFORE-BUILD                = KNOWN
MULTI-OPTION SOFTWARE SOURCING    = KNOWN
ARCHITECTURAL COMPOSITION         = KNOWN
MINIMUM PROPRIETARY RESIDUAL      = POTENTIAL RESEARCH RESIDUAL
FORMAL MEASUREMENT OF THAT RESIDUAL = INSUFFICIENT EVIDENCE / INVESTIGATE
```

## Métricas candidatas

### MNF-B — Minimum Necessary Factorization Breadth

Proporção de capabilities que exigem algum fator proprietário novo:

```text
MNF-B = capabilities com fatoração própria necessária
        ----------------------------------------------
        capabilities necessárias ao processo estudado
```

### MNF-W — Minimum Necessary Factorization Weighted

Versão ponderada por esforço, criticidade, custo, manutenção, risco ou outro peso explicitamente definido:

```text
MNF-W = soma dos pesos das capabilities proprietárias necessárias
        ----------------------------------------------------------
        soma dos pesos de todas as capabilities necessárias
```

Os pesos NÃO podem ser combinados arbitrariamente. Cada estudo deve declarar a dimensão ponderada.

### Complemento — Reuse Coverage

```text
RC = 1 - MNF-B
```

quando breadth for a unidade adotada.

## Distinção fundamental

> **Tamanho da invenção não é valor da inovação.**

Um residual pequeno pode produzir quase todo o diferencial comercial ou científico.

Portanto o estudo deve separar, no mínimo:

- `MNF` — quanto precisa ser criado;
- `DV` — valor de diferenciação do residual;
- `P` — pertinência da intenção;
- `XC` — exclusividade conceitual;
- `XA` — exclusividade arquitetural/composicional;
- `XE` — exclusividade de execução;
- `EC` — confiança da evidência.

## Pergunta de pesquisa principal

> **É possível reduzir sistematicamente a quantidade de propriedade de software nova necessária para realizar uma intenção, por meio de um protocolo evidence-based de sourcing, reutilização e composição, mantendo ou melhorando qualidade, diferenciação, sustentabilidade e independência operacional?**

## Perguntas derivadas

**RQ1.** Um protocolo explícito encontra mais oportunidades admissíveis de reutilização que a decisão convencional baseada predominantemente em julgamento especialista?

**RQ2.** MNF-B e MNF-W podem ser medidos de forma reprodutível com concordância aceitável entre avaliadores?

**RQ3.** Projetos guiados pelo princípio apresentam menor custo total de propriedade, esforço de manutenção e volume de código próprio sem perda relevante de qualidade?

**RQ4.** A mínima fatoração própria preserva ou melhora o tempo de entrega e a capacidade de evolução?

**RQ5.** Qual relação existe entre tamanho do residual proprietário e valor de diferenciação percebido/medido?

**RQ6.** Em quais contextos adotar, compor ou adaptar aumenta risco a ponto de tornar racional uma fatoração própria maior?

**RQ7.** Como mudanças no ecossistema externo alteram dinamicamente o valor de MNF ao longo do tempo?

## Hipóteses candidatas

**H1 — Proprietary Surface Reduction**  
Um protocolo explícito de descoberta e sourcing reduz a superfície proprietária construída em relação ao baseline sem protocolo.

**H2 — Maintenance Reduction**  
Menor superfície proprietária reduz esforço de manutenção próprio, controladas diferenças de domínio e qualidade.

**H3 — Quality Preservation**  
A redução de fatoração própria não implica necessariamente perda de qualidade quando as soluções adotadas satisfazem gates de adequação.

**H4 — Differentiation Independence**  
O valor de diferenciação não é função monotônica da quantidade de fatoração própria.

**H5 — Dynamic Residual**  
A mínima fatoração necessária de um mesmo problema muda ao longo do tempo conforme novas soluções externas aparecem.

## Desenho experimental candidato

Comparar projetos ou decisões equivalentes:

```text
GRUPO / BASELINE A
processo convencional de decisão

GRUPO / TRATAMENTO B
protocolo MNF
  ↓
mesmo problema
mesmos requisitos
mesmos gates de qualidade
  ↓
medir:
- candidatos descobertos
- cobertura de reutilização
- MNF-B / MNF-W
- LOC/propriedade própria
- tempo
- custo
- manutenção
- defeitos
- dependências
- lock-in
- qualidade
- diferenciação
```

Também é possível usar benchmark retrospectivo: esconder soluções conhecidas que foram descobertas tarde em projetos históricos e verificar se o protocolo as encontra antes de autorizar construção própria.

## Critérios de falsificação

A tese deve ser rejeitada, reduzida ou reformulada se:

- o protocolo não reduzir significativamente fatoração própria;
- as métricas MNF não apresentarem confiabilidade suficiente;
- a economia aparente for anulada por custo de integração, dependência, licenciamento ou manutenção externa;
- a adoção/composição causar perda relevante de qualidade ou autonomia;
- o residual científico já estiver integralmente coberto por método existente;
- o princípio produzir apenas uma renomeação de `reuse before buy before build` sem mecanismo, métrica ou resultado novo demonstrável.

## Oportunidade de doutorado

### Linha candidata

**Decision Engineering for Minimum Necessary Proprietary Software Factorization**

### Contribuição de tese potencial

Uma tese defensável precisaria entregar mais que o princípio verbal. Possíveis contribuições cumulativas:

1. taxonomia operacional de alternativas de sourcing e transformação;
2. protocolo de descoberta adversarial e saturação;
3. método de decomposição de intenção em capabilities;
4. definição formal e instrumentos de MNF-B/MNF-W;
5. dataset/benchmark de decisões reais e Late Discovery Defects;
6. modelo de decisão com evidência e confiança;
7. ferramenta executável para apoiar decisões;
8. avaliação longitudinal de custo, qualidade, manutenção e diferenciação;
9. análise de validade externa em múltiplos tipos de software.

### Possível antítese científica

A tese também pode descobrir que minimizar fatoração própria NÃO é ótimo em certos contextos, por exemplo:

- domínio estratégico altamente diferenciador;
- risco de supply chain;
- dependência crítica de fornecedor;
- requisitos regulatórios;
- alta volatilidade de APIs externas;
- custos de integração superiores ao desenvolvimento próprio;
- necessidade de conhecimento interno estratégico.

Nesse caso, a contribuição pode ser um **modelo de fronteira ótima**, em vez de uma regra absoluta.

## Relação com FlowED

O FlowED pode servir como laboratório, não como justificativa da tese.

A implementação experimental pode observar o pipeline:

```text
INTENT
 ↓
CAPABILITY DECOMPOSITION
 ↓
ADVERSARIAL DISCOVERY
 ↓
ADOPT / CONFIGURE / EXTEND / COMPOSE / ADAPT / FORK / INVENT
 ↓
MNF
 ↓
EVIDENCE-BASED BUILD STRATEGY
```

O resultado científico deve permanecer válido mesmo se o FlowED deixar de existir.

## Estado atual

```text
EXACT TERM FOUND AS ESTABLISHED PRINCIPLE = NO, in initial exploratory search
STRONG PRIOR ART AROUND CORE IDEA          = YES
NOVELTY CLAIM AUTHORIZED                   = NO
DOCTORAL RESEARCH OPPORTUNITY              = YES, subject to systematic prior-art gate
NEXT REQUIRED STEP                         = systematic literature review / mapping study
```

## Referências iniciais

- Badampudi, D. et al. Selecting component sourcing options: A survey of software engineering's broader make-or-buy decisions. Information and Software Technology 112 (2019), 18–34. DOI: https://doi.org/10.1016/j.infsof.2019.03.015
- European Interoperability Architecture. Reuse, before buy, before build. https://interoperable-europe.ec.europa.eu/collection/common-assessment-method-standards-and-specifications-camss/solution/elap/reuse-buy-build
- Binder, R. Introducing the Minimum Viable Capability Strategy. Carnegie Mellon Software Engineering Institute, 2018. https://www.sei.cmu.edu/blog/introducing-the-minimum-viable-capability-strategy/
- Additional mandatory literature: software reuse, CBSE, COTS/OSS selection, make-or-buy, architectural innovation, open innovation, software ecosystems, transaction cost economics, technical debt, supply-chain risk and empirical software engineering.

## Regra de pesquisa

Nenhuma publicação deve afirmar que o `Princípio da Mínima Fatoração Necessária` é novo antes de revisão sistemática e busca adversarial de prior art.
