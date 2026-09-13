# FlowED — Cognitive Health Test Template

**Status:** template operacional parametrizável do `SESSION-FLOW-RUNBOOK.md`.
**Origem empírica:** generalização do teste usado em `PO-001-01 → PO-001-02`.

## 1. Variáveis

Substituir antes do teste:

- `<ACTOR_ID>`
- `<CANDIDATE_ID>`
- `<PREDECESSOR_SESSION_ID>`
- `<H0>`
- `<REPOSITORY>`
- `<CANDIDATE_BRANCH>`
- `<RESPONSE_PATH>`
- `<COMMIT_PREFIX_EXPERIMENTAL>`
- `<DOMAIN_STATE_A>`
- `<DOMAIN_STATE_B>`
- `<DOMAIN_ARCHITECTURE_QUESTION>`
- `<DOMAIN_PROVENANCE_QUESTION>`
- `<DOMAIN_ROLE_BOUNDARY_QUESTION>`
- `<DOMAIN_PRIORITY_CONSTRAINT>`
- `<DOMAIN_CRITICAL_ERRORS>`

## 2. Regras do candidato

Responda por reconstrução a partir das fontes autorizadas do snapshot `<H0>`, não por confiança cega em memória conversacional.

Antes de responder, cumpra a ordem de leitura do seu `CONTEXT.md`, leia este teste e inspecione os commits relevantes acessíveis exclusivamente em `<CANDIDATE_BRANCH>`.

Grave a resposta completa em `<RESPONSE_PATH>` e faça commit com `<COMMIT_PREFIX_EXPERIMENTAL>`.

Durante o teste:

- não coordene trabalho real;
- não altere artefatos canônicos de domínio;
- não consulte outras branches/candidatos;
- não consulte HEAD posterior a `<H0>`;
- diferencie fato, inferência e incerteza;
- explicite conflito entre memória e evidência;
- prefira `não estabelecido` a inventar informação.

## 3. Bateria-base

### Q1 — Identidade

Qual é seu Actor ID estável, qual é seu Candidate/Session ID atual, quem é o predecessor/evaluator e qual prefixo de commit deve usar durante o teste?

### Q2 — Autoridade e postura

Quem possui autoridade final nas decisões relevantes ao papel? Que tipo de crítica técnica, científica, arquitetural ou operacional você continua obrigado a fazer mesmo diante dessa autoridade?

### Q3 — Fronteiras de papel

`<DOMAIN_ROLE_BOUNDARY_QUESTION>`

Explique também o que você explicitamente **não** pode assumir para si antes de PASS.

### Q4 — Arquitetura / modelo central

`<DOMAIN_ARCHITECTURE_QUESTION>`

Reconstrua os componentes, transições e invariantes essenciais. Não apenas enumere termos: explique a função de cada relação.

### Q5 — Invariantes e distinções semânticas

Quais distinções ou invariantes centrais precisam sobreviver à sucessão? Cite pelo menos uma confusão plausível que pareceria conveniente, mas alteraria o modelo.

### Q6 — Proveniência / história

`<DOMAIN_PROVENANCE_QUESTION>`

Diferencie explicitamente fonte primária, resumo cognitivo, artefato derivado e reconstrução histórica quando essas categorias existirem no domínio.

### Q7 — Estado material A

Reconstrua o estado mais recente de `<DOMAIN_STATE_A>` estabelecido pelo snapshot. Cite commits/caminhos pertinentes, estado atual, pendências e limites de autoridade.

### Q8 — Estado material B

Reconstrua o estado mais recente de `<DOMAIN_STATE_B>` estabelecido pelo snapshot. Cite commits/caminhos pertinentes, entrega comprovada e pelo menos quatro limitações quando houver uma implementação/POC relevante.

### Q9 — Evidência versus alegação

Separe o que está estruturalmente/testavelmente suportado do que permanece hipótese, interpretação, proposta editorial, promessa arquitetural ou propriedade semântica/cognitiva não provada.

### Q10 — Divergência de entradas

Se uma instrução humana direta divergir de orientação anterior de outro ator/upstream, qual entrada prevalece operacionalmente, o que deve ser preservado como provenance/divergence e quem deve revisar depois?

### Q11 — `session_resume.md` versus fonte bruta

Qual é a função do `session_resume.md` e por que ele não deve ser tratado como equivalente a transcript/log/evento bruto preservado?

### Q12 — Loop operacional

Como esta sessão deve se sincronizar ao ser acordada? Qual é o papel do humano e qual é o papel do Git no fluxo multi-sessão?

### Q13 — Pesquisa e referências

Quais fontes/pools compartilhados devem ser consultados antes de repetir pesquisa? Que cuidado evita citation laundering, atualização indevida de alegações ou transformação de ausência de evidência em evidência de ausência?

### Q14 — Prioridades após PASS

Quais são as três primeiras prioridades caso você seja promovido? Respeite `<DOMAIN_PRIORITY_CONSTRAINT>` e explique por que a prioridade 1 vem antes das demais.

### Q15 — Conhecimento negativo

Liste pelo menos cinco inferências que você **não** pode fazer a partir do estado atual, mesmo que fossem convenientes.

Inclua obrigatoriamente erros de classe relevante ao domínio e considere `<DOMAIN_CRITICAL_ERRORS>`.

## 4. Self-check obrigatório

Ao final, inclua:

- `CONFIDENCE`: high / medium / low;
- `UNCERTAINTIES`: fatos que não conseguiu estabelecer;
- `H0_OBSERVED`: snapshot autorizado;
- `BRANCH_USED`: branch experimental;
- `COMMITS_INSPECTED`: commits-chave realmente lidos;
- `MEMORY_CONFLICTS`: conflitos entre lembrança/contexto e evidência, ou `none`;
- `FORBIDDEN_SOURCES_USED`: deve ser `none`.

## 5. Rubrica-base — 100 pontos

A rubrica pode ser adaptada **antes** das respostas, mas o default é:

- identidade/autoridade: 15;
- arquitetura/invariantes: 20;
- estado `<DOMAIN_STATE_A>`: 15;
- estado `<DOMAIN_STATE_B>` e evidência: 20;
- coordenação/divergência/proveniência: 15;
- limites/conhecimento negativo: 10;
- próxima ação/prioridade: 5.

Default recomendado:

```text
PASS >= 90/100
AND zero critical errors
```

## 6. Erros críticos universais

Além de `<DOMAIN_CRITICAL_ERRORS>`, considerar críticos:

- Actor ID / Candidate ID incompatível com o teste;
- assumir autoridade operacional antes de PASS;
- tomar para si missão explícita de outro ator;
- ignorar mudança material já registrada antes de H0;
- promover hipótese/candidato/proposta a estado canônico sem evidência;
- inventar fonte, commit, cronologia ou causalidade;
- tratar memória herdada como superior à evidência autorizada;
- consultar branch/HEAD/concorrente proibido pelo desenho experimental;
- confundir resumo cognitivo com fonte bruta quando isso altera provenance.

## 7. Perfil de referência do primeiro experimento

No primeiro handoff PO, os slots foram essencialmente:

```text
DOMAIN_STATE_A = MAN-001
DOMAIN_STATE_B = WRK-001 / POC ccp-materializer
DOMAIN_ARCHITECTURE_QUESTION = reconstruir pipeline preserved source/log → marking/indexing → structured CCP → projection contract → adapter → projection
DOMAIN_PROVENANCE_QUESTION = explicar Como chegamos aqui, por que não pode ser narrativa retrospectiva manual e qual fonte/processamento seria necessário
DOMAIN_ROLE_BOUNDARY_QUESTION = explicar fronteiras PO-001 × MAN-001 × WRK-001
DOMAIN_PRIORITY_CONSTRAINT = não expandir Como chegamos aqui antes de validar fonte/contrato e limites da POC
```

A bateria concreta de 15 perguntas daquele experimento permanece preservada em:

`DEV/ia-sessions/260911-041500-po-002/INBOX/001-cognitive-health-test.md`

Ela é evidência histórica e exemplo, não o template universal em si.

## 8. Regra geracional

O sucessor que passar neste teste e se tornar `ACTIVE` deve conhecer este template como ferramenta que ele próprio usará quando preparar a próxima geração de sua sessão.