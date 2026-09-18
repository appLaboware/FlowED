# PO-001-02 — revisão das entregas WRK-001 e MAN-001

**Origem:** `PROMPT PO-001-02 — 001` / HUMAN_CHAT.
**Branch:** `docs/flowed-concept-evolution-2026-09-08`.

## 1. WRK-001 — veredito

Entrega revisada: `DEV/ia-sessions/260911-025000-worker/OUTBOX/003-vertical-slice-delivery.md`, commit `73ad98c53bcec3fa4eccb4b0ac636964f512d807`, árvore `POC/ccp-materializer/`.

### Efetivamente entregue/provado

A primeira fatia vertical é aceita como **POC estrutural executável concluída**.

Ela demonstra, para uma unidade real P2.3 e dentro do contrato específico implementado:

- preservação de uma fonte editorial fixada por commit/blob e SHA-256;
- marcações exatas e não destrutivas, curadas, convertidas em nós tipados com proveniência por span;
- estrutura CCP serializada em JSON;
- contrato explícito de projeção que distingue eixo de densidade (`REDUCT-MAX`, `BASE`) do eixo argumentativo (`DEFESA`);
- retenção estrutural obrigatória de estado epistêmico, base, causalidade e limites;
- materialização determinística/reprodutível em Markdown/JSON;
- falha verificável para adulteração de fonte, citações/spans inválidos, referências desconhecidas, perda de invariantes e contrato inconsistente;
- artefatos de evidência e hashes de build.

O código e os testes sustentam a alegação de integridade/proveniência/seleção estrutural. O build-report declara corretamente que equivalência semântica não é verificada automaticamente.

### Limites preservados

Não está provado que:

- a marcação possa ser extraída automaticamente de fonte bruta;
- as projeções sejam semanticamente equivalentes por teste automático;
- a sequência REDUCT/BASE/EXPAND seja cognitivamente monotônica;
- qualquer projeção melhore compreensão humana;
- o adapter gere ou revise redação;
- a P2.3 esteja aprovada;
- o documento editorial usado seja equivalente a chat/log bruto;
- o POC reconstrua cronologia ou `Como chegamos aqui`;
- o contrato atual seja uma ontologia geral de CCP.

O adapter atual também é deliberadamente estreito: conhece `P2.3` e as três projeções deste primeiro recorte. Isso é aceitável para o marco POC e não deve ser confundido com generalização.

### Decisão operacional WRK

**ACCEPT milestone + HOLD de expansão.**

Nenhuma correção é exigida na fatia vertical atual. Não autorizar agora a expansão para `Como chegamos aqui`: ainda falta uma fonte/event model apropriado e um contrato específico que impeça converter resumo ou argumento em história inferida.

Também não há motivo para pedir generalização abstrata do motor neste momento. O próximo recorte deve nascer de uma segunda necessidade real, não de engenharia especulativa.

## 2. MAN-001 — veredito

Entregas revisadas especialmente: `OUTBOX/004-third-prior-art-audit-final-man-opinion.md`, `OUTBOX/005-human-proposal-epistemic-starting-point.md` e `OUTBOX/006-human-proposal-de-onde-partimos-sprint-close.md`, além do estado da sessão e do pool de referências.

### Efetivamente entregue/provado

O sprint entregou uma correção metodológica importante:

- antecedentes fortes existem para vários ingredientes isolados do FlowED;
- claims externos que fortalecem artificialmente P1/P2/P3 não podem ser usados para fabricar residual;
- novidade de ingredientes isolados deve ser presumida baixa até demonstração contrária;
- novidade da composição/hierarquia permanece **não demonstrada e não refutada**;
- a análise correta deve partir do claim canônico real e mapear antecedente, relação, residual e força da evidência;
- fonte científica e fonte de prior art/estado da prática precisam de classificação distinta.

A proposta humana de explicitar um **ponto de partida epistêmico** é arquiteturalmente coerente com o manifesto e com CCP: declarar herança conhecida, fonte/evidência, limite e delta reduz a pressão para defender novidade artificial e torna futura revisão corrigível.

### O que permanece candidato/limite

Não estão aprovados neste momento:

- o nome normativo `CCP de Partida` ou `CCP de Fundação Epistêmica`;
- a inserção de `De onde partimos` no manifesto principal;
- `D0.1–D0.4` como BASELINE consolidada;
- qualquer claim de originalidade científica do FlowED;
- uma lista suficiente/definitiva de antecedentes;
- a definição formal de CCP ou EDT.

Há ainda dois problemas concretos a corrigir antes de consolidar a proposta:

1. **O pool compartilhado de referências não foi atualizado**, embora MAN registre ter consultado fontes materiais (por exemplo, trabalhos/metodologias e prior art). A regra do projeto exige que quem consulta registre `SUPPORTS`, `DOES_NOT_SUPPORT`, versão/data e força/limites, em vez de transferir curadoria posteriormente ao PO.
2. `D0.4` parece semanticamente diferente das demais D0: é uma **ambição/proposição transversal** sobre linguagem conceitual comum, não evidência clara de "de onde partimos". Pode ser excelente princípio/compromisso, mas sua localização nessa seção ainda não está justificada.

Há também cautela com `D0.1`: dizer genericamente "ideias já consolidadas" exige que cada herança chamada de consolidada seja rastreável; o manifesto não deve transformar uma intenção metodológica em atestado indiscriminado de consenso.

### Decisão operacional MAN

**APPROVE arquitetura epistêmica como candidata forte; HOLD da consolidação editorial.**

Antes de voltar a transformar D0.* pelo protocolo de densidade, MAN deve fechar o substrato evidencial mínimo:

- construir matriz claim-by-claim partindo do texto canônico real do manifesto;
- separar `força científica` de `relevância de prior art/divulgação pública`;
- registrar no `REFERENCE-POOL.md` as fontes efetivamente consultadas, com o que sustentam e o que não sustentam;
- usar `UNKNOWN/UNRESOLVED` quando cobertura for insuficiente, sem inventar residual;
- reavaliar D0.1–D0.4 depois da matriz, especialmente o encaixe de D0.4;
- não alterar ainda o manifesto principal nem P2.3.

Esse é trabalho claramente justificado porque fecha um defeito de proveniência e produz o substrato estruturado necessário para avaliar a própria proposta humana.

## 3. Relação entre as frentes e ordem dos próximos passos

As duas frentes agora se conectam de forma útil.

O WRK provou que consegue materializar deterministicamente uma unidade estruturada **quando os nós, invariantes, proveniência e contrato já existem**. O MAN acabou de identificar uma nova unidade cognitiva mais rica: `claim → antecedente → evidência → limite → adoção → delta`.

Essa segunda unidade é um candidato melhor para o próximo teste do materializador do que saltar diretamente para `Como chegamos aqui`, porque:

- possui fontes documentais explicitáveis;
- não exige inventar cronologia ausente;
- testa proveniência/evidência e relações além de simples variantes textuais da mesma frase;
- pode produzir uma projeção curta (`De onde partimos`) a partir de uma base estruturada;
- força a separar força científica, prior art e claim editorial.

Portanto a ordem fica:

1. **MAN primeiro:** fechar matriz epistemic/prior-art mínima e normalizar referências.
2. **PO revisa:** decide quais claims/unidades são adequados e congela um recorte.
3. **WRK depois:** usa esse recorte como segunda fatia vertical, sem ainda entrar em reconstrução histórica de `Como chegamos aqui`.

WRK fica em HOLD produtivo até existir esse input real. Não há novo trabalho para WRK neste ciclo.

## 4. Ações emitidas

- emitir um único novo INBOX para MAN-001 com a tarefa de matriz/evidência e correção do pool;
- não emitir INBOX para WRK-001 neste ciclo;
- registrar as decisões no `session_resume.md` de PO-001-02.
