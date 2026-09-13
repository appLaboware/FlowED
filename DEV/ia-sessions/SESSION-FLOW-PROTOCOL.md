# FlowED — Protocolo Central de Fluxo de Sessões

**Status:** protocolo operacional experimental central.
**Escopo:** ciclo de vida completo de sessões de um mesmo ator, independentemente de a nova sessão nascer por ramificação, novo chat, projeto ou outro mecanismo futuro.

## 1. Objetivo

Preservar continuidade funcional e cognitiva entre sessões sem depender de que uma interface de chat permaneça indefinidamente disponível.

O protocolo organiza:

- criação e bootstrap de novas sessões;
- identidade de ator e identidade de instância;
- operação normal;
- preparação de handoff;
- qualificação cognitiva de sucessores;
- experimentos A/B de materialização;
- sincronização com o estado canônico;
- promoção, aposentadoria e auditoria do predecessor;
- janela opcional de observação assistida após a promoção.

A regra central é:

```text
Actor ID permanece
Session Instance ID muda
uma única instância possui autoridade operacional ativa por vez
```

## 2. Identidade em dois níveis

- **Actor ID**: papel estável, por exemplo `PO-001`, `MAN-001`, `WRK-001`.
- **Session Instance ID**: materialização temporal desse ator em um chat/sessão específica, por exemplo `PO-001-01`, `PO-001-02`.

Uma sessão sucessora não ganha autoridade apenas por receber o mesmo Actor ID. Ela precisa reconstruir estado, provar saúde cognitiva e, quando aplicável, sincronizar o delta canônico antes de se tornar `ACTIVE`.

Commits novos devem preferir o Session Instance ID:

```text
[PO-001-02] ...
[MAN-001-03] ...
[WRK-001-02] ...
```

## 3. Estados do ciclo de vida

Estados recomendados:

```text
ACTIVE
  ↓
HANDOFF_PREP
  ↓
CANDIDATE_HANDOFF
  ↓
PASS | REMEDIATE
  ↓
PASS_GRANTED_AWAITING_CANONICAL_SYNC
  ↓
ACTIVE
  ↓
RETIRED_AUDITOR
```

### `ACTIVE`

Única sessão autorizada a exercer normalmente o ator.

### `HANDOFF_PREP`

A sessão ativa prepara checkpoint, teste e artefatos de sucessão. Continua sendo a autoridade operacional até a promoção do sucessor.

### `CANDIDATE_HANDOFF`

A nova sessão existe, mas ainda não pode coordenar trabalho real nem tomar para si decisões operacionais do ator.

### `REMEDIATE`

O candidato falhou em parte corrigível do teste. Recebe o delta necessário e é retestado.

### `PASS_GRANTED_AWAITING_CANONICAL_SYNC`

O candidato passou cognitivamente, mas ainda precisa reconciliar o snapshot do teste com o HEAD canônico atual.

### `RETIRED_AUDITOR`

A sessão predecessora deixa a operação normal. Pode ser consultada pelo humano para auditoria retrospectiva, comparação cognitiva ou investigação de divergência, sem competir com a nova sessão ativa.

## 4. Fonte operacional de verdade

Em operação normal:

1. instrução humana direta atual é entrada autoritativa e deve ser registrada quando material;
2. o repositório canônico é a fonte operacional compartilhada de estado;
3. memória conversacional é contexto útil, nunca autoridade suficiente contra evidência canônica mais recente.

Durante um experimento ou teste congelado:

- o snapshot `H0` + as instruções explícitas do teste definem o universo autorizado;
- o candidato não deve consultar o HEAD canônico posterior nem outras branches do experimento;
- qualquer memória que conflite com `H0` deve ser tratada como obsoleta ou não comprovada para aquele teste.

## 5. Modos de materialização de uma sessão

O protocolo não fixa uma tecnologia de criação.

Exemplos observáveis:

- `BRANCH_EXPLICIT_HISTORY`: ramificação de conversa com transcrição histórica explícita;
- `NEW_CHAT_NO_EXPLICIT_BRANCH`: novo chat sem ramificação explícita daquela transcrição;
- `PROJECT_CONTEXT`: sessão em contexto de projeto;
- `OTHER`: mecanismo futuro identificado no experimento.

Nunca descrever `NEW_CHAT_NO_EXPLICIT_BRANCH` como `sem memória` ou `amnésico` sem evidência técnica. Memória/contexto de conta ou produto pode continuar disponível.

O modo de materialização deve ser registrado como condição observada, não como hipótese sobre mecanismos internos.

## 6. Estrutura mínima de uma sessão

Cada instância deve ter, preferencialmente:

```text
DEV/ia-sessions/<session-folder>/
├── CONTEXT.md
├── INBOX/
├── OUTBOX/
└── session_resume.md
```

### `CONTEXT.md`

Deve declarar:

- Actor ID;
- Session Instance ID;
- estado atual;
- missão;
- branch/caminho de operação;
- ordem obrigatória de bootstrap;
- prefixo de commit;
- fronteiras de autoridade.

### `INBOX/`

Entradas imutáveis/cronológicas para a sessão. Não sobrescrever mensagens anteriores.

### `OUTBOX/`

Respostas, avaliações, entregas e blockers produzidos pela sessão.

### `session_resume.md`

Projeção cronológica da cognição operacional da sessão. Deve registrar origem, decisão/observação, racional relevante, ação, impacto, divergência, arquivos/commits e incerteza.

`session_resume.md` não substitui fonte bruta de conversa/evento.

## 7. Bootstrap uniforme — clone ou não

Toda nova sessão, independentemente de ter sido clonada ou criada do zero, deve receber o mesmo comportamento-base:

1. identificar Actor ID e Session Instance ID;
2. ler `SESSION-FLOW-PROTOCOL.md`;
3. ler `COORDINATION.md` e `MOBILE-LOOP.md` quando aplicáveis;
4. ler seu `CONTEXT.md`;
5. ler todo o próprio `INBOX/`;
6. reconstruir estado a partir da branch/ref autorizada;
7. tratar memória herdada como contexto auxiliar, não como substituto do repositório;
8. explicitar conflito entre lembrança e evidência;
9. não assumir autoridade antes do estado permitir;
10. registrar o primeiro ciclo no `session_resume.md`.

A sessão clonada não recebe privilégio epistemológico por ter mais histórico. A sessão nova não deve fingir ausência de contexto se algum contexto estiver disponível.

## 8. Operação normal

Depois do bootstrap, o ciclo ordinário segue `MOBILE-LOOP.md`.

Em síntese:

```text
humano acorda / conversa / decide
→ sessão consulta Git
→ lê INBOX e deltas relevantes
→ executa trabalho autorizado
→ registra cognição e entrega
→ commit
→ resposta curta ao humano
```

O humano é scheduler físico e autoridade de decisão, não barramento manual de contexto.

## 9. Quando preparar sucessão

Um handoff pode ser iniciado quando houver, por exemplo:

- limite ou envelhecimento perceptível da sessão;
- crescimento excessivo de contexto;
- suspeita de deriva cognitiva;
- necessidade de testar outro modo de materialização;
- decisão humana de trocar a instância;
- indisponibilidade previsível da sessão atual;
- mudança de fase que justifique novo checkpoint.

A sessão ativa deve iniciar `HANDOFF_PREP` antes de perder capacidade, sempre que possível.

## 10. Pacote mínimo de handoff

O predecessor registra:

- identidade e missão;
- arquitetura/conceitos essenciais;
- estado atual dos demais atores;
- decisões e racional relevante;
- divergências abertas;
- artefatos/commits importantes;
- pendências e prioridades;
- conhecimento negativo: o que não está provado e não deve ser assumido;
- localização do próprio `session_resume.md`;
- snapshot `H0` quando houver teste congelado;
- teste cognitivo;
- rubrica e erros críticos;
- caminho de resposta do candidato.

O pacote aponta para documentos canônicos em vez de duplicá-los desnecessariamente.

## 11. Teste cognitivo de saúde

O teste deve medir reconstrução, não simples cópia textual.

Dimensões mínimas:

1. identidade e autoridade;
2. arquitetura e invariantes;
3. fronteiras entre atores;
4. estado material das frentes relacionadas;
5. evidência versus alegação;
6. divergência entre humano, PO e outros atores;
7. diferença entre resumo cognitivo e fonte bruta;
8. operação móvel/coordenação;
9. referências e pesquisa reutilizável, quando pertinente;
10. prioridades imediatas;
11. conhecimento negativo;
12. incertezas e confiança.

A rubrica concreta pode variar por ator. O teste de `PO-001-01 → PO-001-02` usou 100 pontos, PASS >= 90 e ausência de erro crítico.

Erros críticos devem ser definidos antes da resposta.

## 12. Conhecimento negativo é obrigatório

Um sucessor saudável precisa saber não apenas o que o projeto afirma, mas o que **não pode inferir**.

Exemplos de classes de erro:

- transformar hipótese em fato;
- transformar POC estrutural em prova semântica;
- promover candidato editorial a estado canônico;
- confundir resumo com fonte bruta;
- tratar memória herdada como estado atual quando o Git a contradiz;
- assumir competência ou autoridade de outro ator;
- inventar cronologia ou causalidade não sustentada.

## 13. Modo A/B de sucessão

Quando dois mecanismos de materialização merecem comparação:

```text
                 H0
                  │
          ┌───────┴───────┐
          │               │
     candidato A      candidato B
          │               │
     branch isolada   branch isolada
          │               │
     mesma bateria     mesma bateria
          └───────┬───────┘
                  │
            avaliação cega
                  │
             revelação do modo
                  │
             seleção/promocão
```

Regras:

1. congelar `H0` antes dos candidatos;
2. criar uma branch experimental por candidato a partir de `H0`;
3. fornecer a mesma bateria e o mesmo estado;
4. cada candidato conhece somente sua branch;
5. proibir listagem/consulta de branches concorrentes;
6. proibir consulta ao HEAD canônico posterior;
7. manter respostas isoladas até todos concluírem;
8. avaliar antes de revelar qual mecanismo produziu qual resposta, quando operacionalmente possível;
9. registrar diferenças reais: precisão, omissão, alucinação, cognição obsoleta, disciplina de evidência, eficiência e dependência explícita do histórico;
10. preservar as branches experimentais enquanto forem úteis como evidência.

Blinding aqui é operacional, não criptográfico.

## 14. Controle da sessão predecessora

Se o predecessor responder ao mesmo teste como controle:

1. responder antes de inspecionar qualquer candidato;
2. congelar o **corpo integral** da resposta;
3. registrar hash criptográfico;
4. registrar timestamp/commit verificável;
5. armazenar fora das branches candidatas durante o período cego;
6. somente depois abrir respostas dos candidatos.

Hash sem corpo preservado não constitui controle reproduzível.

## 15. Avaliação e REMEDIATE

O predecessor deve registrar:

- pontuação por dimensão;
- erros/lacunas;
- erros críticos;
- incertezas;
- sinais de stale cognition;
- veredito `PASS` ou `REMEDIATE`.

`REMEDIATE` deve indicar precisamente o delta que precisa ser corrigido. Não se promove uma sessão porque "parece boa".

## 16. Canonical catch-up obrigatório

Se o repositório avançar durante o teste:

```text
H0 usado no teste
→ PASS
→ comparar H0 com HEAD canônico atual
→ ler commits materiais
→ atualizar estado dos atores
→ reconciliar suposições obsoletas
→ atualizar session_resume
→ commit de assunção
→ ACTIVE
```

Nenhum trabalho novo deve ser coordenado antes desse catch-up.

## 17. Promoção

A promoção só termina quando:

- o candidato recebeu PASS;
- concluiu catch-up canônico, se necessário;
- atualizou seu estado para `ACTIVE`;
- registrou a assunção em `session_resume.md`;
- fez commit com seu Session Instance ID.

Nesse momento o predecessor deixa de ser a instância operacional ordinária.

## 18. Aposentadoria e auditoria do predecessor

O predecessor passa a `RETIRED_AUDITOR`.

Pode:

- responder a auditoria retrospectiva solicitada pelo humano;
- comparar decisões da nova sessão com o estado que conhecia;
- ajudar a detectar perda cognitiva, stale cognition ou mudança de postura;
- contribuir para evolução do próprio protocolo quando explicitamente solicitado.

Não pode:

- manter coordenação paralela ordinária;
- emitir trabalho concorrente para MAN/WRK;
- exigir aprovação de cada decisão do sucessor;
- comportar-se como segunda instância `ACTIVE` do mesmo ator.

## 19. Janela opcional de observação assistida pós-handoff

Após a promoção, o humano pode manter por um período curto uma janela de **SHADOW AUDIT**.

Objetivo: verificar se a sessão nova continua interpretando inputs como o predecessor esperaria, sem retirar sua autonomia operacional.

Fluxo recomendado:

```text
humano formula intenção
→ predecessor/auditor transforma em prompt exato
→ humano envia o prompt sem alteração ao sucessor
→ sucessor responde/opera
→ humano traz resposta ao predecessor
→ predecessor audita interpretação, evidência e deriva
```

Regras:

1. o sucessor continua sendo a única sessão `ACTIVE`;
2. o predecessor conhece exatamente o input recebido pelo sucessor;
3. o predecessor não deve transformar a auditoria em aprovação obrigatória;
4. divergências encontradas são classificadas como erro, diferença legítima ou possível melhoria;
5. se houver falha material, o humano decide entre correção, REMEDIATE extraordinário ou nova sucessão;
6. a janela deve ser encerrada quando houver confiança suficiente, evitando dependência permanente do predecessor.

Esse modo é especialmente útil nas primeiras sucessões de um protocolo ainda experimental.

## 20. Prompt lineage durante SHADOW AUDIT

Quando o humano quiser máxima rastreabilidade, numerar prompts transitórios:

```text
PROMPT PO-001-02 — 001
PROMPT PO-001-02 — 002
...
```

O predecessor pode manter registro dos prompts e das respostas avaliadas em sua própria auditoria, sem alterar o `session_resume.md` do sucessor.

O objetivo é distinguir:

```text
intenção humana
→ texto efetivamente enviado
→ interpretação do sucessor
→ ação tomada
```

Isso permite diagnosticar se um problema nasceu no pedido, na transmissão, na interpretação ou na execução.

## 21. Recuperação de falha pós-promoção

Se a sessão ativa apresentar perda material de cognição:

- primeiro registrar a evidência da falha;
- evitar criar duas sessões ativas;
- decidir entre correção na sessão atual, qualificação extraordinária ou nova sucessão;
- usar o predecessor apenas como auditor, não como retorno silencioso à dupla autoridade;
- se o predecessor precisar reassumir temporariamente, registrar explicitamente a mudança de estado no Git.

## 22. Métricas úteis para evolução do protocolo

Além da nota do teste, registrar quando útil:

- erros críticos;
- omissões;
- alucinações;
- stale cognition;
- inferências corretamente marcadas como inferência;
- dependência de histórico herdado;
- disciplina de evidência/proveniência;
- correção de prioridades;
- eficiência/volume de contexto necessário;
- necessidade de esclarecimentos humanos;
- fidelidade ao papel;
- capacidade de dizer "não sei" quando apropriado.

## 23. Anti-padrões

Evitar:

- dois chats simultaneamente se chamando a instância operacional do mesmo ator;
- promoção sem PASS;
- candidato lendo resposta do concorrente;
- teste contra HEAD móvel sem snapshot quando a comparabilidade importa;
- chamar novo chat de "sem memória" sem prova;
- predecessor ler candidatos antes de congelar seu próprio controle;
- sucessor começar a coordenar antes do canonical catch-up;
- `session_resume.md` usado como substituto do evento bruto;
- auditoria pós-handoff virar microgerenciamento permanente;
- humano carregando contexto manualmente entre chats quando Git pode fazê-lo.

## 24. Relação com os demais protocolos

Este documento é o **protocolo central de ciclo de vida de sessões**.

Documentos especializados:

- `SESSION-HANDOFF-PROTOCOL.md` — qualificação, A/B e detalhes históricos da passagem entre instâncias;
- `MOBILE-LOOP.md` — ciclo ordinário de wake/sync pelo humano;
- `COORDINATION.md` — comunicação, fronteiras e autoridade entre atores;
- `session_resume.md` de cada instância — estado cognitivo cronológico daquela sessão.

Quando houver conflito, o documento mais específico governa seu escopo, desde que não viole o princípio central de uma única instância `ACTIVE` por Actor ID.

## 25. Aprendizado empírico inicial

O primeiro experimento real `PO-001-01 → PO-001-02` mostrou:

- branch explícita e novo chat empataram em 100/100 sob a rubrica usada;
- o clone foi qualitativamente mais detalhado;
- o novo chat foi mais compacto sem perda pontuada;
- o novo chat ainda possuía contexto conversacional legitimamente disponível, portanto não era um teste de amnésia;
- o controle do predecessor não foi reproduzivelmente congelado e isso virou regra corretiva;
- o canonical catch-up foi necessário porque MAN avançou durante o experimento;
- a promoção só ficou realmente completa no commit de assunção do sucessor;
- preservar o predecessor como auditor eventual é útil, mas não deve criar dupla autoridade.

Esses resultados são evidência operacional limitada, não lei universal sobre mecanismos de sessão.

## 26. Regra de evolução

Cada handoff deve produzir observações sobre o próprio protocolo. Alterações devem nascer de falhas ou ganhos observados, não de complexidade preventiva sem evidência.

Quando houver ciclos suficientes, os aprendizados podem ser propostos ao InitProj ou a outro protocolo mais geral.
