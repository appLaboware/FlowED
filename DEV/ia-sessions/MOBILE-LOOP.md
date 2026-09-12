# FlowED — Mobile Human Orchestration Loop

**Status:** protocolo operacional experimental para coordenação de múltiplas sessões de ChatGPT a partir de celular.
**Ciclo de vida das sessões:** `DEV/ia-sessions/SESSION-FLOW-PROTOCOL.md`.

## Objetivo

Reduzir o trabalho manual do humano ao mínimo. O humano apenas alterna entre sessões e as desperta; contexto, orientação, estado e entrega permanecem no repositório.

## Comando humano mínimo

Depois do bootstrap inicial, o humano pode enviar apenas:

```text
NOVO INPUT
```

A sessão deve tratar essa expressão como comando operacional do protocolo, não como conteúdo de domínio.

## Comportamento ao receber `NOVO INPUT`

Cada ator deve:

1. identificar seu `Actor ID` e caminho de sessão pelo `CONTEXT.md`;
2. consultar HEAD e commits recentes da branch compartilhada;
3. identificar commits posteriores ao último ciclo tratado pelos prefixos de ator;
4. reler `DEV/ia-sessions/COORDINATION.md` quando houver alteração;
5. ler novos arquivos do próprio `INBOX/`;
6. abrir alterações dos demais atores apenas quando tocarem seu domínio;
7. executar todo trabalho pendente autorizado para seu papel;
8. atualizar `session_resume.md` com interação, decisão, mudança de entendimento ou desvio relevante;
9. registrar resultado, blocker ou estado útil no repositório;
10. fazer commit com seu prefixo obrigatório;
11. responder ao humano de forma curta, informando estado final e commit quando houver.

O humano não deve precisar copiar instruções entre sessões.

## Bootstrap único por sessão

Uma sessão que ainda não conheça este protocolo deve receber uma única instrução humana:

```text
Sincronize pelo repositório: leia DEV/ia-sessions/SESSION-FLOW-PROTOCOL.md, DEV/ia-sessions/MOBILE-LOOP.md, DEV/ia-sessions/COORDINATION.md, seu CONTEXT.md e seu INBOX. Adote seu Actor ID e respeite o estado da sua Session Instance ID. Depois disso, trate “NOVO INPUT” como comando para sincronizar, executar o trabalho pendente autorizado do seu papel, atualizar seu session_resume.md e registrar tudo no Git.
```

Esse bootstrap vale para sessão clonada, novo chat ou outro mecanismo de materialização. Contexto conversacional herdado é auxiliar; o estado operacional vem da fonte autorizada pelo protocolo.

Depois desse bootstrap, usar somente `NOVO INPUT` nos ciclos ordinários, salvo quando o humano quiser deliberadamente conversar ou mudar uma decisão naquele chat.

## Conversa humana direta

Quando o humano conversar normalmente com uma sessão, essa conversa pode alterar, ampliar ou divergir de orientação anterior do PO.

A sessão deve:

- responder normalmente ao humano;
- tratar a decisão humana como entrada autoritativa;
- registrar no `session_resume.md` a cognição relevante, não apenas a conclusão;
- deixar explícito quando a nova decisão mudou ou contrariou orientação anterior;
- permitir que `PO-001` descubra posteriormente pelo repositório o que mudou e por quê.

Assim, o humano não precisa copiar a conversa paralela para o PO.

## Papel do PO-001 no fluxo humano

`PO-001` coordena também a navegação do humano entre sessões. Ao final de uma decisão de coordenação, quando houver trabalho a disparar, deve indicar explicitamente qual sessão abrir em seguida e fornecer apenas o comando mínimo necessário.

Exemplo:

```text
AGORA → WRK-001
NOVO INPUT
```

Quando houver dois trabalhos independentes, o PO pode mandar o humano disparar ambos em sequência e voltar ao chat original.

## Monitoramento

Não existe monitoramento em background entre mensagens do humano. Sempre que o humano retornar ao PO e pedir continuidade, estado ou monitoramento, `PO-001` deve consultar o repositório antes de concluir sobre o progresso dos demais atores.

O histórico de commits, `session_resume.md` e `OUTBOX/` são as fontes de estado entre sessões.

## Princípio de esforço humano mínimo

O humano deve atuar como **scheduler físico e autoridade de decisão**, não como barramento de informação.

```text
humano: conversa / decide / acorda / alterna sessões
Git: transporta contexto, orientação, cognição resumida, estado e entrega
atores: leem, trabalham, resumem e registram
PO: coordena, critica, pesquisa quando necessário e orienta o próximo movimento humano
```

O protocolo deve ser refinado pelo uso real no celular; qualquer passo que exija cópia recorrente de conteúdo entre chats é candidato a eliminação.
