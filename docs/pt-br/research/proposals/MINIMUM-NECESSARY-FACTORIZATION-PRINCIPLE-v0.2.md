# FlowED — Proposta de Pesquisa: Princípio da Mínima Fatoração Necessária v0.2

**ID:** FLOWED-RESEARCH-MNF-001  
**Versão:** 0.2-draft  
**Status:** RESEARCH PROPOSAL / UNVALIDATED / PRIOR-ART-NARROWED  
**Domínio:** FlowED / Project Genesis  
**Nome em português:** Princípio da Mínima Fatoração Necessária  
**Rótulo inglês provisório:** Sourcing-Oriented Minimum Necessary Factorization  

## 1. Mudança principal em relação à v0.1

A v0.1 corria o risco de misturar dois problemas:

1. minimizar a superfície proprietária necessária;
2. decidir quando parar uma decomposição.

O dogfood de prior art encontrou antecedente direto para o segundo problema em Systems Engineering e literatura adjacente de requisitos/arquitetura.

Logo, esta v0.2 abandona qualquer pretensão de novidade sobre `quando parar decomposição` em sentido genérico.

## 2. Formulação candidata refinada

> **Uma proposta deve ser decomposta somente até o menor nível de granularidade capaz de produzir decisões estáveis, auditáveis e suficientemente fundamentadas sobre sourcing, transformação, composição, diferenciação, risco e incerteza, sem destruir relações arquiteturais relevantes.**

Forma compacta:

> **O PMFN busca a fatoração mais grosseira que ainda seja suficiente para decisão.**

Isso é uma hipótese de pesquisa, não uma alegação de novidade estabelecida.

## 3. Problema científico específico

A literatura já trata de:

```text
functional decomposition
decomposition stopping
requirements granularity
architecture alignment
component sourcing
COTS selection
OSS/COTS/in-house/outsourcing
software reuse
component composition
open innovation
```

A pergunta que permanece é mais estreita:

> **Existe uma granularidade mínima, reproduzível e orientada a sourcing em que novas divisões deixam de alterar materialmente decisões evidence-backed sobre realização de uma ideia inicial de software?**

## 4. Prior art confirmado nesta rodada

### 4.1 Generic decomposition stopping

Park et al. (2026), IEEE Access, DOI `10.1109/ACCESS.2026.3683195`, trata explicitamente de quando parar decomposição funcional com quality gates e LLMs.

Conseqüência:

```text
generic stopping criterion = PRIOR ART
```

### 4.2 Component-origin decision

Badampudi, Wohlin e Petersen (2016), DOI `10.1016/j.jss.2016.07.027`, revisam decisões entre in-house, OSS, COTS e outsourcing e apontam a necessidade de suporte a combinações.

### 4.3 Industrial sourcing

Borg et al. (2019), DOI `10.1016/j.infsof.2019.03.015`, estudam decisões práticas entre múltiplas opções de sourcing em sistemas intensivos em software.

### 4.4 COTS selection and combination

Cortellessa et al. (2007), DOI `10.1145/1321631.1321697`, propõem seleção ótima de combinações COTS guiada por requisitos e custo.

### 4.5 Opportunistic reuse

Mäkitalo et al. (2020), DOI `10.1007/s00607-020-00833-6`, descrevem software construído por reutilização e combinação oportunística de componentes independentes.

### 4.6 Requirements/architecture granularity

RE4SA, DOI `10.1016/j.infsof.2021.106535`, aborda alinhamento e granularidade entre requisitos e arquitetura.

### 4.7 External innovation sourcing

West e Bogers (2014), DOI `10.1111/jpim.12125`, sintetizam pesquisa sobre obtenção, integração e comercialização de inovação externa.

## 5. Residual científico atual

Não é:

```text
reuse before build
make/buy
component selection
composition
when to stop decomposition generically
```

Candidato atual:

```text
PMFN-Discovery
=
coarse-first factorization
+
sourcing-aware split gates
+
evidence provenance
+
realization ontology
+
architecture-preserving decomposition
+
neutral project-position record
+
longitudinal decision genealogy
```

Cada item ainda deve ser confrontado separadamente com prior art.

## 6. Regra de parada candidata

Para um fator `f`, considere um split:

```text
f → {c1, c2, ..., cn}
```

Avaliar qualitativa ou empiricamente mudanças em:

```text
ΔS — sourcing
ΔT — transformation
ΔA — architecture/composition
ΔX — differentiation/exclusivity
ΔR — risk
ΔE — evidence/uncertainty
```

A decomposição continua somente se a divisão alterar materialmente pelo menos uma dessas decisões.

Forma conceitual:

```text
ContinueSplit(f) = material(ΔS, ΔT, ΔA, ΔX, ΔR, ΔE)
```

Uma forma numérica futura poderá ser testada, mas nenhum peso, distância ou limiar está validado.

Forma abstrata:

```text
F* = argmin Complexity(F)
subject to DecisionSufficiency(F) = true
```

## 7. Separação entre PMFN e residual de construção

PMFN trata principalmente de **granularidade suficiente para decisão**.

A quantidade de implementação própria remanescente é consequência da investigação, não definição completa do princípio.

Por isso a operação usa:

```text
FR = Residual Factorization
```

em vez de concluir automaticamente que o residual é invenção.

Regra:

> **Ausência de solução admissível encontrada não prova novidade mundial.**

`MNI` pode permanecer como constructo de pesquisa futuro somente quando `invention` for semanticamente demonstrável.

## 8. Ontologia de realização candidata

Evitar escada única.

```yaml
provenance: existing | modified | invented | unknown
transformation: none | configure | extend | adapt | unknown
architecture: direct | compose | reconfigure | unknown
source: OSS | COTS | service | standard | internal | outsourced | unknown
```

Os conceitos de source/origin devem ser mapeados à literatura existente antes de qualquer extensão.

## 9. Pergunta principal de pesquisa

> **Can an early software-project idea be decomposed to a minimum decision-sufficient granularity such that further decomposition no longer materially changes evidence-backed sourcing, transformation, composition, differentiation, risk, or uncertainty decisions?**

## 10. Perguntas derivadas

**RQ1.** Diferentes analistas conseguem identificar, com concordância mensurável, um ponto de fatoração decision-sufficient?

**RQ2.** Gates orientados a sourcing descobrem oportunidades de reutilização que análises holísticas ou decomposição genérica deixam de encontrar?

**RQ3.** A fatoração PMFN produz menos fatores que decomposição exaustiva mantendo qualidade decisória equivalente ou superior?

**RQ4.** Como preservar diferenciação arquitetural quando todos ou quase todos os componentes já existem?

**RQ5.** As dimensões `XC`, `XA` e `XE` apresentam validade discriminante suficiente para uso operacional?

**RQ6.** Evidência explícita de cobertura, confiança e contraevidência reduz alegações de exclusividade sem suporte?

**RQ7.** Um LLM guiado por PMFN apresenta resultados mais reprodutíveis que um LLM livre?

**RQ8.** Em que ponto mais decomposição aumenta custo e ruído sem alterar decisões?

## 11. Hipóteses candidatas

- PMFN encontra mais oportunidades relevantes de reuso que análise holística equivalente.
- PMFN reduz superfatoração sem degradar decisões de sourcing.
- PMFN aumenta concordância interavaliadores sobre o ponto de parada.
- diferenciação arquitetural pode permanecer alta mesmo com baixa fatoração residual.
- apresentar cobertura e maturidade da evidência reduz interpretações indevidas de exclusividade.

Nenhuma hipótese está confirmada.

## 12. Programa experimental candidato

### Estudo A — Systematic Mapping Study

Mapear interseções entre:

```text
functional decomposition stopping
requirements granularity
component sourcing
software reuse
technology scouting
architecture decision support
innovation sourcing
```

### Estudo B — Expert elicitation

Especialistas decompõem as mesmas ideias e registram por que continuam ou param.

### Estudo C — Experimento controlado

Condições candidatas:

```text
A — free-form human/LLM
B — generic decomposition quality gates
C — PMFN sourcing-aware gates
```

Métricas possíveis:

- fatores gerados;
- oportunidades de reuso descobertas;
- matches inválidos;
- estabilidade das decisões;
- inter-rater agreement;
- tempo;
- unsupported novelty claims;
- utilidade percebida por especialistas.

### Estudo D — Pré-consultoria

Testar se um dossiê evidence-informed permite que o especialista humano dedique mais tempo a julgamento de alto valor e menos à coleta repetitiva de contexto.

## 13. Relação com Project Genesis

Project Genesis pode ser o artefato experimental e ambiente de dogfood.

Ele NÃO é a justificativa científica.

A hipótese deve sobreviver mesmo que Project Genesis seja substituído por composição integral de ferramentas existentes.

## 14. Reflexividade

Como Project Genesis está sendo usado para investigar o próprio PMFN, conclusões self-derived estão sujeitas ao `Reflexive Discovery Overlay`.

Logo:

> **Nenhuma regra descoberta apenas no self-dogfood é automaticamente generalizável.**

Casos externos são obrigatórios para promoção ao protocolo genérico.

## 15. Critérios de falsificação

Reduzir, reformular ou rejeitar a contribuição se:

- um método existente já cobre integralmente o alvo sourcing-aware;
- os avaliadores não conseguem alcançar concordância útil;
- a fatoração não melhora decisões de sourcing/reuso;
- o custo de decomposição supera o ganho decisório;
- as dimensões propostas não apresentam validade suficiente;
- o protocolo apenas renomeia práticas existentes;
- o resultado só funciona no self-dogfood de Project Genesis.

## 16. Estado atual

```text
GENERIC DECOMPOSITION STOPPING        = KNOWN PRIOR ART
MULTI-OPTION SOFTWARE SOURCING        = KNOWN PRIOR ART
COTS/OSS/IN-HOUSE/OUTSOURCE           = KNOWN PRIOR ART
SOFTWARE REUSE / COMPOSITION          = KNOWN PRIOR ART
REQUIREMENTS/ARCHITECTURE GRANULARITY = KNOWN PRIOR ART

DISCOVERY-SPECIFIC SOURCING STOP GATE = INVESTIGATE
EVIDENCE-AWARE FACTOR REALIZATION     = INVESTIGATE
NEUTRAL POSITION PROFILE              = INVESTIGATE
LONGITUDINAL GENEALOGY                = INVESTIGATE

NOVELTY CLAIM                         = NOT AUTHORIZED
DOCTORAL OPPORTUNITY                  = STILL PLAUSIBLE, NARROWER
```

## 17. Próxima ação científica

Não escrever artigo de contribuição ainda.

Primeiro:

1. concluir o Phase 01 dogfood e homologar a representação da ideia;
2. rerodar prior art sobre a representação homologada;
3. executar Systematic Mapping Study;
4. confrontar explicitamente o framework de Park et al. com o alvo PMFN-Discovery;
5. determinar se há residual mensurável antes de formular claim de tese.
