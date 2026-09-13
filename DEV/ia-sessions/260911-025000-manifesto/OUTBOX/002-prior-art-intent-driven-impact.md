# MAN-001 → PO — impacto de prior art e convergência intent/spec-driven

**Origem:** HUMAN_CHAT + verificação externa de MAN-001 em 2026-09-11.

O humano trouxe uma consultoria paralela alegando que literatura e mercado 2024–2026 validariam grande parte da direção FlowED. A verificação mostra um resultado importante, mas diferente da consultoria: **há convergência externa forte com partes centrais do FlowED, porém a consultoria mistura fontes acadêmicas, ensaios de mercado, exageros e pelo menos um erro categorial grave.**

## Resultado executivo

Não recomendo interpretar o achado como “FlowED comprovado pela ciência” nem como “FlowED tornou-se redundante”. O efeito mais defensável é duplo:

1. **reduz a novidade possível de algumas formulações superficiais** — intenção acima de implementação, especificação/contrato como artefato durável, desired state/policy, runtime adaptativo e design rationale já têm antecedentes fortes;
2. **aumenta a relevância temporal da direção**, porque academia, padrões e ferramentas industriais recentes estão deslocando o centro de gravidade para intenção, especificações executáveis, contratos, geração de implementações e adaptação.

A consequência para o manifesto é positiva somente se FlowED for preciso sobre seu residual: **não reivindicar a invenção desses elementos, mas explicitar a hierarquia/reponderação e a composição particular que propõe.** Isso já é compatível com A0.2 e com o trabalho atual de P2.3.

## Evidências verificadas com alta relevância

### 1. Microsoft Research / workshop 2025 — real e diretamente relevante

`Intent-based System Design and Operation` (Anand et al., 2025) é real, aparece na Microsoft Research e no arXiv. Propõe *intent* como nova abstração no contexto de design e operação de sistemas, codificando requisitos funcionais e operacionais em alto nível para automatizar design, implementação, operação e evolução.

- Microsoft Research: https://www.microsoft.com/en-us/research/publication/intent-based-system-design-and-operation/
- arXiv: https://arxiv.org/abs/2502.05984

Isto converge fortemente com separação intenção/materialização. Não prova o FlowED como um todo e não é evidência de que “intent-driven” tenha nascido em 2025.

### 2. Intent-driven é anterior a 2024–2026

Há uma revisão sistemática de 2020 sobre intent-driven systems, com literatura pesquisada até 2018, e o RFC 9315 (2022) formaliza conceitos de Intent-Based Networking. Logo, qualquer alegação de novidade geral de “intent-driven” seria indefensável.

- Silvander, Wnuk, Svahnberg (2020): https://doi.org/10.1049/iet-sen.2018.5338
- RFC 9315: https://www.rfc-editor.org/info/rfc9315/

### 3. Convergência industrial ainda mais próxima: specifications as source

Uma referência não citada na consultoria é especialmente importante para nós: Sean Grove (OpenAI), na palestra `The New Code` no AI Engineer World’s Fair 2025, argumenta que especificações rigorosas e versionadas podem funcionar como source of truth e gerar documentação, avaliações, comportamento de modelos e possivelmente código. O evento descreve explicitamente comunicação de intenção como habilidade central.

- AI Engineer: https://www.ai.engineer/talks/8rABwKRsec4-specifications-are-the-new-code
- schedule/abstract original: https://ai.engineer/worldsfair/2025/schedule

Isso toca de modo direto nossa ideia de uma fonte durável projetando múltiplas materializações. Deve entrar no audit de posicionamento.

### 4. GitHub Spec Kit — sobreposição prática substancial

O GitHub Spec Kit materializa Spec-Driven Development e declara explicitamente que SDD inverte a relação tradicional: especificações tornam-se artefato primário e código torna-se expressão/materialização. A documentação atual também descreve o harness como intent-driven e independente de agente específico.

- https://github.com/github/spec-kit
- https://github.com/github/spec-kit/blob/main/spec-driven.md
- https://github.github.com/spec-kit/

Isto provavelmente é o prior art/produto adjacente mais importante para comparar com o FlowED no eixo intenção→especificação→implementação. Recomendo comparação formal, não apenas menção bibliográfica.

### 5. AUTOSAR Adaptive — parte correta, mas consultoria exagera

AUTOSAR Adaptive realmente usa SOA, service discovery e pode permitir escolha de instância em runtime. A documentação oficial também trata versionamento de service contracts. Porém isso **não** demonstra que a indústria “abandonou interfaces estáticas”, nem que AUTOSAR seja uma implementação geral de arquitetura intent-driven. Classic e Adaptive coexistem; e o próprio Adaptive admite diferentes graus de descoberta/configuração.

- AUTOSAR oficial, Platform Design: https://www.autosar.org/fileadmin/standards/R23-11/AP/AUTOSAR_AP_EXP_PlatformDesign.pdf
- estudo 2026: https://arxiv.org/abs/2607.05227

O estudo industrial de 2026 é especialmente útil como contraponto: identifica pain-points arquiteturais, de ferramentas, acoplamento, observabilidade, coordenação e complexidade epistemológica no uso de AUTOSAR Adaptive. Portanto, adaptabilidade dinâmica não elimina por si só o problema de coerência/cognição; em alguns contextos cria novas necessidades de tooling e compreensão.

## Problemas graves na consultoria recebida

### “Polyhedral” não é evolução de arquitetura hexagonal

`Automatic run-time mapping of polyhedral computations to heterogeneous devices with memory-size restrictions` é trabalho de **2013**, PDPTA 2013. O ResearchGate mostra upload em maio de 2024, que provavelmente originou a data errada da consultoria.

- repositório da Universidad de Valladolid: https://uvadoc.uva.es/handle/10324/70522

Além disso, *polyhedral* ali refere-se ao **polyhedral model** de computações/loops para mapeamento em hardware heterogêneo. Não é uma “arquitetura poliédrica” sucessora de Ports & Adapters. Associar esse artigo à evolução da arquitetura hexagonal é erro categorial e deve ser descartado.

### “50% melhor que arquiteturas estáticas” é generalização indevida

O artigo Springer `Multithreaded runtime framework for parallel and adaptive applications` relata até 50% de melhoria **numa aplicação específica de adaptive mesh refinement, comparando balanceamento dinâmico de carga com balanceamento estático**, em cenário HPC. Não valida genericamente “arquiteturas adaptativas” contra “arquiteturas estáticas”.

- https://link.springer.com/article/10.1007/s00366-022-01713-7

### “TDD evoluiu para Policy Verification” não é consenso científico demonstrado

A frase aparece no artigo comunitário da DEV.to sobre Intent Driven Development. É uma proposta/retórica do autor, não conclusão científica estabelecida. O texto LearnTeachMaster citado pela consultoria não contém essa formulação.

- DEV.to: https://dev.to/m8a-io/intent-driven-development-idd-is-our-current-future-5fh4
- LearnTeachMaster: https://www.learnteachmaster.org/post/intent-driven-engineering-architecture-the-five-layers-of-ai-native-systems

### Prathap 2026 é convergência conceitual, não validação científica

O texto `Intent-Driven Software Architecture: Formal Foundations, System Design Mechanics` existe e é muito próximo em linguagem a partes do nosso raciocínio — intenção declarativa, contratos executáveis, multi-agent synthesis, deterministic governance. Mas é um **whitepaper/post do LinkedIn**, com disclaimer de opiniões pessoais. Deve ser tratado como evidência de convergência de mercado/pensamento, não como paper peer-reviewed.

- https://www.linkedin.com/pulse/intent-driven-software-architecture-formal-foundations-prathap-m-hoelf

## Implicação para a relevância do FlowED

Minha leitura atual é: **a relevância do FlowED aumenta, mas sua área legítima de novidade se estreita.**

O que perde força como possível diferencial isolado:

- separar intenção de implementação;
- tratar especificação/contrato como artefato durável;
- geração de código/materialização a partir de especificações;
- políticas/desired state;
- adaptabilidade/runtime discovery;
- preservação de design rationale em sentido genérico.

O que continua parecendo residual potencialmente relevante — e precisa de prior-art audit antes de reivindicarmos novidade:

- reponderar explicitamente a **intenção como linguagem operacional estável** ao longo de tecnologias/materializadores;
- colocar **contratos como locus primário da coerência operacional organizacional**, não apenas como interface, schema ou policy local;
- tratar o **caminho cognitivo/racional como fonte epistemicamente primária**, mantendo uma projeção consolidada autoritativa sem confundir autoridade normativa com origem do conhecimento;
- gerar **projeções/adapters por audiência/consumidor** (humano, IA, executor, auditor etc.) a partir da mesma unidade cognitiva, com invariância semântica/epistêmica;
- tornar a substituibilidade da materialização uma consequência desejada: uma implementação melhor da filosofia não é ameaça à filosofia;
- conectar intenção → contrato → materialização → evidência de execução → revisão de forma rastreável.

## Recomendação ao PO

Não vejo razão para interromper P2.3; ao contrário, a formulação atual que começa reconhecendo que contratos já são amplamente usados ficou mais importante. Porém recomendo **abrir imediatamente um audit formal de prior art / positioning** antes de congelar o manifesto ou fazer alegações acadêmicas/comerciais de novidade.

Esse audit deveria comparar no mínimo:

- FlowED × Microsoft intent-based system design;
- FlowED × RFC 9315 / literatura intent-driven anterior;
- FlowED × Sean Grove / `The New Code`;
- FlowED × GitHub Spec Kit / Spec-Driven Development;
- FlowED × Policy-as-Code / desired state;
- FlowED × design rationale / architecture decision rationale;
- FlowED × AUTOSAR Adaptive apenas onde a comparação for semanticamente válida.

Sugiro que o PO incorpore as fontes confirmadas ao `docs/research/REFERENCE-POOL.md` e coordene o audit transversal. MAN-001 pode continuar revisando as proposições, mas deve evitar qualquer redação que trate esses mecanismos conhecidos como invenções do FlowED.

**Divergência com orientação anterior:** nenhuma orientação do PO é contrariada. Este input aumenta a urgência de prior-art/positioning e pode alterar futuramente a DEFESA e o enquadramento de novidade do manifesto.