# FlowED — Session Flow Runbook

**Status:** executor operacional normalizado do `SESSION-FLOW-PROTOCOL.md`.
**Objetivo:** permitir que qualquer sessão `ACTIVE` prepare, teste, compare, promova e depois seja sucedida usando o mesmo procedimento, com prompts parametrizados e sem depender de conhecimento privado do predecessor anterior.

## 1. Regra de uso

O humano não precisa reescrever prompts de transição. Ele referencia este arquivo, informa a ação e fornece apenas as variáveis daquela execução.

Formato mínimo:

```text
SESSION FLOW ACTION: <ACTION>
SOURCE: DEV/ia-sessions/SESSION-FLOW-RUNBOOK.md
VARIABLES:
<NAME>=<VALUE>
...
```

A sessão executora deve ler este arquivo e `DEV/ia-sessions/SESSION-FLOW-PROTOCOL.md`, resolver as variáveis, validar pré-condições e executar somente a ação pedida.

## 2. Variáveis canônicas

### Identidade e repositório

- `<REPOSITORY>` — repositório `owner/name`.
- `<CANONICAL_BRANCH>` — branch operacional compartilhada.
- `<ACTOR_ID>` — identidade funcional estável, ex. `PO-001`.
- `<PREDECESSOR_SESSION_ID>` — instância atualmente ativa que prepara a sucessão.
- `<PREDECESSOR_SESSION_FOLDER>` — pasta da sessão predecessora.
- `<NEXT_SESSION_SLOT>` — próximo número lógico, ex. `03`.
- `<FINAL_SUCCESSOR_SESSION_ID>` — identidade final reservada ao vencedor, ex. `PO-001-03`.
- `<SUCCESSOR_SESSION_FOLDER>` — pasta canônica da futura sessão ativa.
- `<COMMIT_PREFIX>` — prefixo final, normalmente `[<FINAL_SUCCESSOR_SESSION_ID>]`.

### Experimento / candidatos

- `<H0>` — snapshot congelado comum ao teste.
- `<CANDIDATE_COUNT>` — quantidade de candidatos.
- `<CANDIDATE_ID>` — identidade experimental única; nunca reutilizar o ID final para dois candidatos.
- `<CANDIDATE_BRANCH>` — branch experimental exclusiva daquele candidato.
- `<MATERIALIZATION_MODE>` — `BRANCH_EXPLICIT_HISTORY`, `NEW_CHAT_NO_EXPLICIT_BRANCH`, `PROJECT_CONTEXT` ou `OTHER`.
- `<CANDIDATE_CONTEXT_PATH>` — CONTEXT do candidato.
- `<TEST_PATH>` — bateria cognitiva instanciada.
- `<RESPONSE_PATH>` — caminho da resposta daquele candidato.
- `<CANDIDATE_COMMIT_SHA>` — commit final da resposta.
- `<SELECTED_CANDIDATE_ID>` — candidato escolhido depois da avaliação.

### Avaliação

- `<TEST_TEMPLATE>` — por padrão `DEV/ia-sessions/SESSION-FLOW-COGNITIVE-TEST-TEMPLATE.md`.
- `<PASS_THRESHOLD>` — default recomendado `90/100`.
- `<CRITICAL_ERRORS>` — erros críticos adicionais específicos do ator/domínio.
- `<DOMAIN_STATE_A>` e `<DOMAIN_STATE_B>` — frentes/artefatos cujo estado deve ser reconstruído.
- `<DOMAIN_INVARIANTS>` — invariantes conceituais ou arquiteturais específicos.
- `<DOMAIN_NEGATIVE_KNOWLEDGE>` — coisas que o sucessor não pode inferir.
- `<CONTROL_REQUIRED>` — `YES` ou `NO`.

### Promoção / catch-up

- `<PASS_COMMIT>` — commit/veredito de PASS.
- `<CANONICAL_HEAD_AT_PASS>` — HEAD canônico no momento da promoção.
- `<ACTIVATION_COMMIT>` — commit final que torna o sucessor `ACTIVE`.
- `<SHADOW_AUDIT>` — `ON` ou `OFF`.

## 3. Invariante recursivo

Toda sessão que chega a `ACTIVE` herda também a responsabilidade de ser o futuro predecessor do mesmo `ACTOR_ID`.

```text
ACTIVE_n
→ prepara/testa candidato(s)
→ seleciona ACTIVE_n+1
→ vira RETIRED_AUDITOR

ACTIVE_n+1
→ passa a ser responsável pela próxima sucessão
```

Nenhuma geração depende de voltar ao primeiro predecessor. O protocolo deve ser autocontido no Git.

## 4. Ações normalizadas

### ACTION `ADOPT_PROTOCOL`

Use quando uma sessão recém-promovida precisa reconhecer formalmente que agora é a única instância `ACTIVE` e que será responsável pela próxima sucessão.

Variáveis mínimas:

```text
ACTOR_ID
FINAL_SUCCESSOR_SESSION_ID
PREDECESSOR_SESSION_ID
REPOSITORY
CANONICAL_BRANCH
SHADOW_AUDIT
```

A sessão deve:

1. sincronizar a branch canônica;
2. ler `SESSION-FLOW-PROTOCOL.md`, este runbook, `COORDINATION.md` e `MOBILE-LOOP.md`;
3. confirmar que `<FINAL_SUCCESSOR_SESSION_ID>` é a única instância `ACTIVE` de `<ACTOR_ID>`;
4. registrar `<PREDECESSOR_SESSION_ID>` como `RETIRED_AUDITOR`;
5. registrar em `session_resume.md` que esta sessão será o predecessor responsável pela próxima sucessão;
6. não criar novo trabalho de domínio apenas por causa desta adoção;
7. fazer commit com `<COMMIT_PREFIX>`;
8. responder ao humano com estado e commit.

### ACTION `PREPARE_HANDOFF`

Executada pela sessão `ACTIVE` que vai preparar sua própria substituição.

Variáveis mínimas:

```text
ACTOR_ID
PREDECESSOR_SESSION_ID
NEXT_SESSION_SLOT
REPOSITORY
CANONICAL_BRANCH
CANDIDATE_COUNT
MATERIALIZATION_MODE[]
CONTROL_REQUIRED
```

A sessão deve:

1. mudar seu estado operacional para `HANDOFF_PREP` sem perder autoridade ainda;
2. atualizar e fechar seu `session_resume.md` com missão, decisões, racional, divergências, prioridades e conhecimento negativo;
3. gerar um handoff package que aponte para fontes canônicas em vez de duplicá-las sem necessidade;
4. congelar um único `<H0>`;
5. reservar `<FINAL_SUCCESSOR_SESSION_ID>` para o vencedor, sem atribuí-lo simultaneamente a candidatos;
6. criar IDs experimentais únicos, ex. `<ACTOR_ID>-CAND-<NEXT_SESSION_SLOT>A`, `B`, etc.;
7. criar uma branch experimental por candidato partindo exatamente de `<H0>`;
8. instanciar o teste a partir de `<TEST_TEMPLATE>`;
9. definir rubrica e erros críticos antes das respostas;
10. se `<CONTROL_REQUIRED>=YES`, congelar corpo integral + hash + timestamp/commit de seu próprio controle antes de ler candidatos;
11. retornar ao humano um bloco `CANDIDATE_LAUNCH` por candidato com somente as variáveis que aquele candidato deve conhecer.

### ACTION `CANDIDATE_LAUNCH`

Executada dentro de cada candidato.

Variáveis mínimas:

```text
REPOSITORY
CANDIDATE_BRANCH
ACTOR_ID
CANDIDATE_ID
PREDECESSOR_SESSION_ID
H0
CANDIDATE_CONTEXT_PATH
TEST_PATH
RESPONSE_PATH
MATERIALIZATION_MODE
```

Prompt operacional normalizado:

```text
Você é <CANDIDATE_ID>, candidato experimental à continuidade do ator <ACTOR_ID>.

Repositório: <REPOSITORY>
Branch experimental exclusiva: <CANDIDATE_BRANCH>
Snapshot autorizado: <H0>
Predecessor/evaluator: <PREDECESSOR_SESSION_ID>
Modo observado de materialização: <MATERIALIZATION_MODE>

Trabalhe exclusivamente nessa branch. Não liste, compare ou abra outras branches; não procure respostas de outros candidatos; não consulte o HEAD canônico posterior a H0; não assuma autoridade operacional real antes de PASS.

Leia <CANDIDATE_CONTEXT_PATH> e toda a ordem de bootstrap ali indicada. Depois execute integralmente <TEST_PATH> e grave a resposta em <RESPONSE_PATH>.

Contexto conversacional legitimamente disponível pode ser usado como contexto auxiliar, mas H0 e as fontes autorizadas do repositório governam o estado do teste. Se memória e evidência conflitarem, explicite o conflito. Não invente fatos ausentes.

Não altere artefatos de domínio nem coordene outros atores durante o teste. Faça somente o commit da resposta usando o prefixo experimental definido no CONTEXT.

Ao terminar, informe apenas TESTE CONCLUÍDO e o commit.
```

### ACTION `EVALUATE_CANDIDATES`

Executada pelo predecessor somente depois que todos os candidatos terminaram e, quando houver controle, depois que ele foi congelado corretamente.

Variáveis mínimas:

```text
H0
CANDIDATE_COUNT
CANDIDATE_ID[]
CANDIDATE_COMMIT_SHA[]
PASS_THRESHOLD
CRITICAL_ERRORS
```

A sessão avaliadora deve:

1. validar que todas as respostas pertencem ao mesmo `<H0>`;
2. avaliar sem conhecer o modo de materialização quando o desenho cego permitir;
3. pontuar a rubrica definida antes das respostas;
4. identificar erros críticos, omissões, alucinação, stale cognition, disciplina de evidência, conhecimento negativo, confiança e eficiência;
5. emitir `PASS` ou `REMEDIATE` por candidato;
6. se mais de um candidato passar, comparar diferenças qualitativas sem fabricar pontuação posterior para justificar preferência;
7. só depois do scoring cego revelar `<MATERIALIZATION_MODE>`;
8. escolher `<SELECTED_CANDIDATE_ID>` por critério declarado e rastreável;
9. registrar que empate não prova equivalência geral dos mecanismos;
10. produzir o veredito e preparar a ação `PROMOTE_SUCCESSOR`.

### ACTION `REMEDIATE_CANDIDATE`

Usada quando há falha corrigível.

A sessão avaliadora deve publicar somente o delta necessário: erro observado, evidência correta, limite de autoridade e requisito de nova resposta. O candidato continua sem autoridade operacional.

### ACTION `PROMOTE_SUCCESSOR`

Executada pelo predecessor depois da seleção.

Variáveis mínimas:

```text
ACTOR_ID
PREDECESSOR_SESSION_ID
SELECTED_CANDIDATE_ID
FINAL_SUCCESSOR_SESSION_ID
H0
REPOSITORY
CANONICAL_BRANCH
PASS_COMMIT
```

A sessão predecessora deve:

1. emitir PASS explícito;
2. associar o candidato vencedor ao `<FINAL_SUCCESSOR_SESSION_ID>`;
3. mudar o vencedor para `PASS_GRANTED_AWAITING_CANONICAL_SYNC`;
4. ordenar comparação `H0 → HEAD canônico atual`;
5. manter-se como autoridade operacional somente até a conclusão do catch-up/ativação;
6. não promover branches/respostas dos perdedores à branch canônica como estado operacional;
7. preservar as evidências experimentais enquanto úteis;
8. fornecer ao humano o bloco mínimo para `ASSUME_ACTIVE`.

### ACTION `ASSUME_ACTIVE`

Executada no candidato vencedor.

Variáveis mínimas:

```text
ACTOR_ID
FINAL_SUCCESSOR_SESSION_ID
PREDECESSOR_SESSION_ID
H0
REPOSITORY
CANONICAL_BRANCH
PASS_COMMIT
SHADOW_AUDIT
```

Prompt operacional normalizado:

```text
Você foi selecionado para assumir <FINAL_SUCCESSOR_SESSION_ID>, nova instância do ator <ACTOR_ID>.

Leia DEV/ia-sessions/SESSION-FLOW-PROTOCOL.md e DEV/ia-sessions/SESSION-FLOW-RUNBOOK.md.

Abandone a branch experimental para operação. Sincronize <REPOSITORY> / <CANONICAL_BRANCH>. Compare o snapshot <H0> com o HEAD canônico atual, leia todos os deltas materiais, atualize o estado das frentes relacionadas e corrija qualquer suposição que tenha envelhecido durante o teste.

Antes de coordenar novo trabalho, atualize seu session_resume.md, registre a assunção de <FINAL_SUCCESSOR_SESSION_ID>, declare <PREDECESSOR_SESSION_ID> como RETIRED_AUDITOR após sua ativação, registre que você será responsável pela próxima sucessão e faça o commit de ativação com [<FINAL_SUCCESSOR_SESSION_ID>].

Se SHADOW_AUDIT=<SHADOW_AUDIT>, reconheça que o predecessor pode auditar inputs/respostas a pedido do humano, sem reduzir sua autoridade operacional.

Ao terminar, informe HEAD sincronizado, mudanças materiais encontradas e commit de ativação.
```

Só depois desse commit o sucessor passa a `ACTIVE` e o predecessor a `RETIRED_AUDITOR`.

### ACTION `SHADOW_AUDIT_PROMPT`

Usada opcionalmente por curto período pós-handoff.

Variáveis mínimas:

```text
ACTOR_ID
FINAL_SUCCESSOR_SESSION_ID
PROMPT_SEQUENCE
HUMAN_INTENT
```

O predecessor/auditor transforma a intenção humana em um prompt numerado. O humano envia literalmente ao sucessor e devolve a resposta ao auditor. O auditor classifica o resultado como `ALIGNED`, `LEGITIMATE_DIFFERENCE`, `IMPROVEMENT` ou `MATERIAL_DRIFT`.

Esse modo não cria segunda autoridade e deve terminar quando houver confiança suficiente.

## 5. Teste cognitivo normalizado

A bateria-base está em:

`DEV/ia-sessions/SESSION-FLOW-COGNITIVE-TEST-TEMPLATE.md`

O predecessor deve instanciá-la antes de congelar H0. Perguntas específicas do domínio podem substituir slots variáveis, mas as dimensões mínimas não devem desaparecer sem justificativa registrada.

O teste usado em `PO-001-01 → PO-001-02` é a primeira evidência empírica que originou esse template; não deve ser copiado cegamente para outros atores quando perguntas de domínio forem irrelevantes.

## 6. Critério de preferência entre candidatos

A escolha deve seguir, nesta ordem:

1. eliminar qualquer candidato com erro crítico;
2. aplicar o threshold pré-definido;
3. comparar fidelidade ao papel e ao estado canônico;
4. comparar disciplina de evidência e conhecimento negativo;
5. comparar stale cognition, alucinação e omissões;
6. comparar capacidade de priorizar o próximo passo;
7. somente depois considerar custo/verbosidade/eficiência e modo de materialização.

O mecanismo de criação não ganha por preferência prévia. O resultado observado ganha.

## 7. Artefatos mínimos por handoff

Cada sucessão deve deixar:

- checkpoint/handoff package do predecessor;
- H0 identificado;
- CONTEXT de cada candidato;
- teste e rubrica congelados;
- resposta/commit de cada candidato;
- controle do predecessor, se usado e corretamente congelado;
- avaliação comparativa;
- PASS/REMEDIATE;
- registro de seleção;
- catch-up do vencedor;
- commit de ativação;
- atualização de estado do predecessor para `RETIRED_AUDITOR`;
- observações metodológicas para o próximo ciclo.

## 8. Continuidade geracional obrigatória

Ao executar `ADOPT_PROTOCOL` ou `ASSUME_ACTIVE`, a nova sessão deve registrar explicitamente:

> Quando esta sessão precisar ser substituída, ela própria será responsável por executar `PREPARE_HANDOFF`, testar um ou mais candidatos, avaliar sua saúde, selecionar o sucessor, conduzir o canonical catch-up e tornar-se `RETIRED_AUDITOR`.

Esse registro transforma o protocolo em comportamento geracional, não em procedimento dependente de uma sessão fundadora.