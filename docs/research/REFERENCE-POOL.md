# FlowED — Reference Pool

**Status:** pool compartilhado de referências externas consultadas durante evolução do FlowED/CCP.

## Objetivo

Evitar pesquisas repetitivas, reduzir custo de contexto/tokens e permitir reutilização consciente de literatura científica, padrões, documentação técnica e outras fontes verificáveis já examinadas.

Este arquivo não é uma bibliografia ornamental. Cada item deve existir porque alguém o consultou e registrou por que ele é útil.

## Regra de uso

Antes de pesquisar externamente:

1. procurar neste pool por tema, claim ou tag;
2. verificar se alguma referência já consultada realmente sustenta a nova necessidade;
3. reutilizar quando pertinente;
4. pesquisar novamente somente quando houver lacuna, dúvida de atualidade, conflito ou necessidade de evidência mais forte;
5. adicionar novas fontes somente depois de efetivamente consultadas.

**Reutilização não significa validade automática.** Uma referência útil para uma alegação pode não sustentar outra; uma fonte antiga pode exigir atualização; uma fonte conceitual não substitui evidência empírica quando a alegação é empírica.

## Estados

- `CANDIDATE` — identificada, ainda não examinada o suficiente para reutilização.
- `CHECKED` — consultada e resumida.
- `ALIGNED` — consultada e considerada diretamente útil para princípios/decisões atuais.
- `LIMITED` — útil com limites importantes ou somente para parte da alegação.
- `REJECTED` — consultada, mas inadequada para a finalidade considerada.
- `STALE-CHECK` — já útil, porém precisa de nova verificação de atualidade antes de novo uso.

## Schema por referência

```text
REF_ID:
TITLE:
AUTHORS_OR_BODY:
YEAR:
TYPE: paper | standard | official-doc | book | empirical-study | review | other
URL_OR_DOI:
STATUS:
TAGS:
CONSULTED_BY:
LAST_CHECKED:
SUPPORTS:
DOES_NOT_SUPPORT:
KEY_NOTES:
FLOWED_USAGE:
```

## Referências já presentes no histórico de trabalho

Os itens abaixo são pontos de partida conhecidos do trabalho anterior. Antes de usá-los como evidência em nova alegação, o ator deve abrir/reconsultar a fonte e completar `LAST_CHECKED`, `SUPPORTS` e `DOES_NOT_SUPPORT` com precisão.

### REF-AGILE-MANIFESTO

```text
TITLE: Manifesto for Agile Software Development
AUTHORS_OR_BODY: Agile Manifesto authors
YEAR: 2001
TYPE: official-doc
URL_OR_DOI: https://agilemanifesto.org/
STATUS: CANDIDATE
TAGS: manifesto, values, rhetorical-structure, software-engineering
CONSULTED_BY: historical FlowED work
LAST_CHECKED: pending reconfirmation
SUPPORTS: candidate reference for manifesto structure and value-comparison rhetoric
DOES_NOT_SUPPORT: empirical proof of FlowED claims
KEY_NOTES: use as genre/rhetorical precedent, not scientific validation
FLOWED_USAGE: potential comparison for manifesto voice and recurring authorial grammar
```

### REF-KARLSKRONA-MANIFESTO

```text
TITLE: Karlskrona Manifesto for Sustainability Design
AUTHORS_OR_BODY: Becker et al. / Karlskrona initiative
YEAR: 2015-era publication lineage
TYPE: paper/manifesto
URL_OR_DOI: pending exact bibliographic normalization
STATUS: CANDIDATE
TAGS: manifesto, software-engineering, sustainability, principles
CONSULTED_BY: historical FlowED work
LAST_CHECKED: pending reconfirmation
SUPPORTS: candidate reference for manifesto genre and principle framing in software-related research
DOES_NOT_SUPPORT: direct validation of CCP or FlowED architecture
KEY_NOTES: normalize exact citation before academic use
FLOWED_USAGE: comparison of manifesto form and scientific positioning
```

### REF-NASA-SWEHB-SRS

```text
TITLE: NASA Software Engineering Handbook — requirements/SRS guidance
AUTHORS_OR_BODY: NASA
YEAR: living/updated handbook
TYPE: official-doc
URL_OR_DOI: pending exact section URL normalization
STATUS: CANDIDATE
TAGS: requirements, normative-docs, traceability, software-engineering
CONSULTED_BY: historical FlowED work
LAST_CHECKED: pending reconfirmation
SUPPORTS: candidate reference for explicit requirements, traceability and engineering documentation practice
DOES_NOT_SUPPORT: primacy of CCP over consolidated artifacts without additional evidence
KEY_NOTES: use exact section and revision when cited
FLOWED_USAGE: comparison with normative/consolidated engineering artifacts
```

### REF-ISO-IEC-DIRECTIVES

```text
TITLE: ISO/IEC Directives
AUTHORS_OR_BODY: ISO/IEC
YEAR: living/updated directives
TYPE: standard/official-doc
URL_OR_DOI: pending exact part/version normalization
STATUS: CANDIDATE
TAGS: normative-language, standards, requirements, document-structure
CONSULTED_BY: historical FlowED work
LAST_CHECKED: pending reconfirmation
SUPPORTS: candidate reference for distinctions in normative drafting and authoritative language
DOES_NOT_SUPPORT: FlowED-specific claims by itself
KEY_NOTES: version matters; recheck before citation
FLOWED_USAGE: vocabulary/structure for norms, requirements and determinations
```

## Topics queued for research

These topics have been identified as needing stronger scientific support. They are not claims of established evidence until sources are added and evaluated:

- generation effect;
- insight / Aha! experience;
- processing fluency;
- inference and memory/retention;
- surprise and incongruity resolution;
- progressive disclosure;
- design rationale / decision rationale;
- provenance of decisions;
- cognitive load by expertise;
- technical communication and safety instructions;
- human factors and risk communication;
- adaptive information density for humans;
- structured prompting / information adaptation for LLMs;
- empirical comparison of generic vs consumer-specific adapters.

## Maintenance rule

Whenever an actor consults a scientific article, standard or technical reference that materially influences analysis or decision:

- add or update its entry in the same work cycle;
- record what claim it supports and what it does not support;
- prefer DOI/canonical URL and exact version when available;
- never describe a source as evidence for a stronger claim than it actually establishes.
