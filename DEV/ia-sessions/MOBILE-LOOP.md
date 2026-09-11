# FlowED — Mobile Human Orchestration Loop

**Status:** protocolo operacional experimental para coordenação de múltiplas sessões de ChatGPT a partir de celular.

## Objetivo

Reduzir o trabalho manual do humano ao mínimo. O humano apenas alterna entre sessões e as desperta; todo contexto, orientação, estado e entrega permanecem no repositório.

## Comando humano mínimo

Depois do bootstrap inicial, o humano pode enviar apenas:

```text
NOVO INPUT
```

A sessão deve tratar essa expressão como um comando operacional do protocolo, não como conteúdo de domínio.

## Comportamento ao receber `NOVO INPUT`

Cada ator deve:

1. identificar seu próprio `Actor ID` e caminho de sessão pelo `CONTEXT.md`;
2. consultar o HEAD e os commits recentes da branch compartilhada;
3. identificar commits posteriores ao último ciclo tratado, usando os prefixos de ator;
4. ler `DEV/ia-sessions/COORDINATION.md` quando houver alteração nele;
5. ler novos arquivos do próprio `INBOX/`;
6. abrir alterações dos demais atores somente quando tocarem seu domínio;
7. executar todo trabalho pendente autorizado para seu papel;
8. registrar resultado, blocker ou estado útil no repositório;
9. fazer commit com seu prefixo obrigatório de ator;
10. responder ao humano de forma curta, informando apenas estado final e commit quando houver.

O humano não deve precisar copiar instruções entre sessões.

## Bootstrap único por sessão

Uma sessão que ainda não conheça este protocolo deve receber uma única instrução humana:

```text
Sincronize pelo repositório: leia DEV/ia-sessions/MOBILE-LOOP.md, DEV/ia-sessions/COORDINATION.md, seu CONTEXT.md e seu INBOX. Adote seu Actor ID. Depois disso, trate “NOVO INPUT” como comando para sincronizar, executar o trabalho pendente do seu papel e registrar tudo no Git.
```

Depois desse bootstrap, usar somente `NOVO INPUT` para novos ciclos ordinários.

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

O histórico de commits e os `OUTBOX/` são a fonte de estado entre sessões.

## Princípio de esforço humano mínimo

O humano deve atuar como **scheduler físico** das sessões, não como barramento de informação.

```text
humano: acorda / alterna sessões
Git: transporta contexto, instrução, estado e entrega
atores: leem, trabalham e registram
PO: coordena prioridades e próximo movimento humano
```

O protocolo deve ser refinado a partir do uso real no celular; qualquer passo que exija cópia recorrente de conteúdo entre chats é candidato a eliminação.
