# FlowED — Coordenação multiagente via repositório

**Status:** protocolo operacional experimental inspirado no InitProj.
**Escopo:** coordenação entre o chat original (PO), a branch paralela de revisão do manifesto e o worker de materialização do CCP.
**Autoridade filosófica final:** humano.
**Ciclo de vida das sessões:** `DEV/ia-sessions/SESSION-FLOW-PROTOCOL.md`.

## 1. Atores e instâncias de sessão

O **Actor ID** representa o cargo/continuidade funcional. O **Session Instance ID** identifica a materialização daquele ator em uma sessão específica de ChatGPT.

Exemplo:

```text
Actor ID:            PO-001
Session Instance ID: PO-001-01
sucessora:           PO-001-02
```

| Actor ID | Papel | Missão principal | Prefixo de commit enquanto a sessão atual estiver ativa |
|---|---|---|---|
| `PO-001` | PO / coordenador | coordenar as duas frentes, observar convergências, orientar CCP/materialização, criticar decisões e integrar aprendizados | usar o Session Instance ID, ex. `[PO-001-01]` |
| `MAN-001` | revisão do manifesto | continuar a revisão do Manifesto FlowED e operar o protocolo editorial de projeções cognitivas | migrar para Session Instance ID quando houver handoff, ex. `[MAN-001-01]` |
| `WRK-001` | Worker CCP/POC | construir a POC vertical do materializador CCP sem redefinir a filosofia nem revisar o manifesto | migrar para Session Instance ID quando houver handoff, ex. `[WRK-001-01]` |

Commits históricos que usam apenas `[PO-001]`, `[MAN-001]` ou `[WRK-001]` permanecem válidos. A granularidade por sessão começa com o protocolo de handoff.

O fato de todos usarem a mesma conexão GitHub torna o autor Git insuficiente para distinguir agentes e sessões. **O prefixo no assunto do commit é obrigatório.**

## 2. Canais de comunicação

A coordenação deve depender do repositório, não de cópia manual de mensagens pelo humano.

### MAN-001

`MAN-001` possui dois canais legítimos de entrada:

1. **chat com o humano** — instruções, decisões, críticas, novas ideias e mudanças de direção dadas diretamente durante a conversa;
2. **INBOX da sessão** — orientações e avaliações de `PO-001`.

`MAN-001` não precisa acessar a sessão privada de `PO-001`. A comunicação PO → MAN ocorre por `INBOX/`; MAN → PO ocorre por `OUTBOX/`, commits e arquivos de estado da própria sessão.

As entradas do humano e do PO são ambas autoritativas para o trabalho. Quando houver conflito explícito, a decisão direta do humano prevalece por ser ele a autoridade filosófica final, mas a divergência deve ser registrada para revisão crítica posterior do PO.

### WRK-001

`WRK-001` recebe orientação operacional por sua própria `INBOX/`, lê contratos e artefatos compartilhados e devolve dúvidas, resultados e blockers por `OUTBOX/` e commits.

## 3. Ciclo de trabalho comum

Cada ator, antes de iniciar um ciclo:

1. consulta o HEAD e commits recentes;
2. identifica commits dos demais atores pelo prefixo;
3. lê o próprio `INBOX/`;
4. abre alterações de outros atores somente quando tocarem seu domínio;
5. executa sua missão;
6. atualiza seu `session_resume.md` quando houver interação ou decisão relevante;
7. registra entrega, blocker, divergência ou estado útil no repositório;
8. faz commit com seu prefixo de sessão vigente.

Mensagens entre atores são arquivos. Não sobrescrever mensagens anteriores de `INBOX/` ou `OUTBOX/`.

## 4. Registro obrigatório de cognição da sessão

Cada sessão deve possuir `session_resume.md` como projeção cronológica estruturada do que ocorreu naquela sessão.

O objetivo não é transcrever todo o chat, mas impedir que decisões, mudanças de entendimento e ideias relevantes existam apenas na interface de conversa.

Para cada interação relevante, registrar pelo menos:

- origem: `HUMAN_CHAT`, `PO_INBOX`, `SELF_ANALYSIS` ou outro ator;
- o que foi proposto, decidido, criticado ou alterado;
- resposta/ação do ator;
- impacto sobre o trabalho em curso;
- arquivos e commits relacionados;
- divergências entre orientação anterior e nova decisão, quando existirem;
- pendências ou incertezas.

Entradas provenientes diretamente do humano merecem atenção especial de registro, pois o PO não vê o chat paralelo e deve conseguir reconstruir pelo repositório o que mudou e por quê.

`session_resume.md` é um resumo cognitivo da sessão, não substitui a fonte bruta quando ela estiver disponível.

## 5. Crítica do PO ao humano

A autoridade final do humano não transforma suas decisões em pressupostos de correção.

`PO-001` atua também como consultor crítico. Ao encontrar decisão, interpretação ou desvio do humano que pareça tecnicamente, cientificamente ou arquiteturalmente frágil, deve apontá-lo explicitamente, explicar o risco e propor alternativa melhor.

Sempre que a crítica depender de conhecimento externo relevante, o PO deve preferir evidência científica, padrões, literatura técnica ou dados verificáveis e registrar as referências reutilizáveis no pool comum.

## 6. Fronteiras de responsabilidade

### `PO-001`

- coordena o mecanismo de materialização do CCP;
- observa `MAN-001` pelo ângulo de CCP, projeções, layouts, adapters, cognição mínima, monotonicidade, proveniência e materialização;
- orienta e avalia `WRK-001`;
- critica decisões do humano quando houver fundamento para isso;
- não substitui o humano em decisões filosóficas finais;
- não reescreve proposições do manifesto que estão sob trabalho de `MAN-001`, salvo decisão explícita do humano.

### `MAN-001`

- continua a revisão do manifesto;
- mantém autonomia editorial/conceitual dentro das decisões do humano;
- usa `BASELINE`, projeções de densidade e `DEFESA` segundo o protocolo vigente;
- conhece a existência futura de `Como chegamos aqui`, mas **não o produz manualmente nesta fase**;
- mantém `session_resume.md` atualizado para que decisões de chat, inclusive desvios determinados pelo humano, permaneçam visíveis ao PO;
- comunica por commit e `OUTBOX/` descobertas relevantes ao materializador CCP.

### `WRK-001`

- constrói uma POC vertical executável;
- ponto de partida: `fonte preservada → marcação → CCP estruturado → contrato de projeção → adapter → artefato compilado`;
- deve investigar posteriormente a geração dinâmica de `Como chegamos aqui` a partir de fonte bruta preservada e estruturação rastreável;
- prioriza execução mínima ponta a ponta antes de generalizar POP, DOC ou outros adapters;
- não altera o manifesto nem redefine o CCP por conta própria; dúvidas conceituais vão para o `INBOX/` do PO.

## 7. `Como chegamos aqui`

`Como chegamos aqui` é uma projeção prevista do CCP, mas não faz parte do trabalho manual corrente de `MAN-001`.

A hipótese de implementação é mais determinística:

```text
chat/log bruto preservado
→ marcação/indexação rastreável
→ estrutura cognitiva em armazenamento consultável
→ seleção atômica por assunto/unidade
→ projeção dinâmica "Como chegamos aqui"
```

O objetivo é evitar que um autor reconstrua retrospectivamente a história por memória ou narrativa livre. A POC de `WRK-001` deverá testar se o caminho pode ser derivado de registros preservados, mantendo proveniência e permitindo aprofundamento progressivo.

Até essa capacidade existir, `MAN-001` produz `DEFESA` e demais artefatos editoriais necessários, mas não simula manualmente uma história completa da criação.

## 8. Pool compartilhado de referências

Todo ator deve consultar `docs/research/REFERENCE-POOL.md` antes de iniciar pesquisa externa sobre tema já investigado.

Se o pool já contiver referência adequada e suficientemente atual para a alegação, ela pode ser reutilizada após conferência de pertinência. Se houver lacuna, o ator pesquisa novas fontes e acrescenta ao pool somente aquelas efetivamente consultadas.

Reutilização não significa autoridade automática: cada uso deve verificar se a referência realmente sustenta a nova alegação e se continua atual quando atualidade for relevante.

## 9. Propriedade de caminhos para reduzir conflitos

- `PO-001`: `DEV/ia-sessions/COORDINATION.md`, sua sessão, pool de referências e documentos de coordenação/arquitetura CCP que não pertençam à revisão do manifesto.
- `MAN-001`: arquivos do manifesto que já vinha revisando e sua própria sessão.
- `WRK-001`: sua sessão e a árvore da POC/materializador.

Antes de editar arquivo compartilhado fora dessas fronteiras, consultar o HEAD atual e registrar a necessidade quando houver risco de colisão.

## 10. Fluxo e handoff entre sessões do mesmo ator

O ciclo completo de uma sessão segue:

`DEV/ia-sessions/SESSION-FLOW-PROTOCOL.md`

A qualificação específica da passagem entre instâncias segue:

`DEV/ia-sessions/SESSION-HANDOFF-PROTOCOL.md`

Regra central:

```text
Actor ID permanece
Session Instance ID muda
uma única sessão fica ACTIVE por Actor ID
```

A sessão sucessora deve reconstruir o estado pelo repositório e passar por teste cognitivo antes de assumir integralmente o papel. Durante a sobreposição, a predecessora é avaliadora e a sucessora é candidata. Depois da promoção, a predecessora pode permanecer como `RETIRED_AUDITOR`, mas não como segunda autoridade operacional.

## 11. Tags de commit

Formato mínimo novo:

```text
[SESSION-INSTANCE-ID] tipo(escopo): resumo
```

Exemplos:

```text
[PO-001-01] chore(handoff): bootstrap PO successor
[PO-001-02] chore(handoff): answer cognitive health test
[MAN-001-01] docs(manifesto): refine proposition density protocol
[WRK-001-01] feat(ccp-poc): add source-to-projection vertical slice
```

Até cada ator realizar seu primeiro handoff formal, seus prefixos históricos simplificados continuam reconhecidos.

## 12. Estado histórico conhecido

O commit `1a9750491b7db1473190db94027c543e5d815e5e` foi produzido pela frente de revisão do manifesto antes da adoção das tags de ator e é tratado como trabalho de `MAN-001`.

O commit `40990f239712569addf97c5d4f366e564dbe1c71` contém a proposta de `MAN-001` para o fluxo `BASELINE / EXPAND-MAX / REDUCT-MAX / DEFESA` e também antecede sua efetiva adoção do prefixo `[MAN-001]`.

O commit `73ad98c53bcec3fa4eccb4b0ac636964f512d807` é a primeira entrega vertical observada de `WRK-001`, com a POC em `POC/ccp-materializer/`.

## 13. Fonte de regras

Este protocolo adapta o padrão de sessões do InitProj — sessões rastreáveis, `CONTEXT`, `INBOX`, `OUTBOX`, resumos e handoff por arquivo — ao experimento atual do FlowED.

`SESSION-FLOW-PROTOCOL.md` é a referência central para ciclo de vida de sessões; este arquivo permanece responsável por coordenação e fronteiras entre atores. Ambos são operacionais e devem evoluir com experiência real, sem transformar observações locais em regra geral antes de evidência suficiente.
