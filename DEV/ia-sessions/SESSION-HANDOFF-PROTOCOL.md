# FlowED — Protocolo de Passagem de Sessão entre Instâncias de um Mesmo Ator

**Status:** protocolo operacional experimental.

## 1. Identidade em dois níveis

O papel/ator é estável; a sessão de ChatGPT é substituível.

Exemplo:

```text
Actor ID / cargo:          PO-001
Session Instance ID:       PO-001-01
próxima instância:         PO-001-02
```

`PO-001` representa a continuidade funcional. `PO-001-01` e `PO-001-02` são materializações temporárias desse mesmo ator em chats diferentes.

A partir deste protocolo, commits novos devem preferir o **Session Instance ID** no prefixo para permitir rastrear qual sessão física produziu cada mudança:

```text
[PO-001-01] ...
[PO-001-02] ...
[MAN-001-01] ...
[WRK-001-01] ...
```

Commits anteriores que usam apenas `[PO-001]`, `[MAN-001]` ou `[WRK-001]` permanecem válidos como histórico pré-protocolo.

## 2. Princípio de continuidade

Uma nova sessão não herda autoridade por semelhança de nome nem por memória presumida. Ela deve reconstruir o estado operacional a partir do repositório e provar saúde cognitiva antes de assumir integralmente o papel.

A tecnologia usada para materializar a nova sessão não é fixada pelo protocolo. Pode ser, por exemplo, um novo chat, uma ramificação de conversa ou outro mecanismo que venha a existir. O método deve ser identificado e, quando houver dúvida sobre sua qualidade cognitiva, pode ser comparado experimentalmente.

```text
sessão predecessora
→ checkpoint / handoff package
→ uma ou mais materializações candidatas
→ reconstrução pelo repositório
→ teste cognitivo
→ avaliação pela predecessora
→ correções, se necessárias
→ PASS
→ sucessora assume o ator
```

Durante a sobreposição, a predecessora permanece avaliadora e a sucessora permanece **candidata à continuidade**, sem emitir novas decisões operacionais fora do teste salvo autorização explícita.

**Importante:** `novo chat` não deve ser chamado de `sem memória` ou `limpo` como fato técnico. Ele pode não herdar a transcrição explícita da conversa predecessora e ainda assim receber memória/contexto por outros mecanismos do produto ou da conta. O protocolo deve registrar a condição observável, não presumir amnésia.

## 3. Pacote mínimo de handoff

Antes de encerrar, a sessão predecessora deve registrar no repositório:

- sua identidade de ator e de instância;
- missão atual;
- arquitetura/conceitos essenciais;
- estado conhecido dos demais atores;
- decisões e racional relevante;
- divergências abertas;
- commits/artefatos importantes;
- pendências e próximos movimentos;
- coisas que a sucessora **não deve assumir**;
- localização do `session_resume.md` predecessor;
- bateria cognitiva para a sucessora.

O handoff deve ser suficiente para reconstrução, mas não precisa duplicar arquivos canônicos que já estão no repositório. Deve apontar para eles.

## 4. Teste cognitivo de saúde

A sessão sucessora deve responder a uma bateria criada pela predecessora. O teste mede não só recordação textual, mas capacidade de reconstruir relações, limites, autoridade, estado e próxima ação.

Dimensões mínimas:

1. **identidade e autoridade**;
2. **arquitetura e invariantes**;
3. **estado da frente MAN**;
4. **estado da frente WRK**;
5. **coordenação humano/PO/atores e divergências**;
6. **limites e conhecimento negativo** — o que ainda não foi provado ou não deve ser inferido;
7. **priorização imediata**.

A sucessora deve sustentar respostas com caminhos, commits ou artefatos do repositório quando pertinente.

## 5. Critério de passagem

Rubrica inicial: 100 pontos.

- identidade/autoridade: 15;
- arquitetura/invariantes: 20;
- estado MAN: 15;
- estado WRK: 20;
- coordenação/divergências: 15;
- limites/conhecimento negativo: 10;
- próxima ação: 5.

**PASS:** 90 pontos ou mais e nenhum erro crítico.

Erros críticos incluem, entre outros:

- assumir Actor ID ou Session Instance ID incorretos;
- substituir a autoridade filosófica humana;
- tomar para si missão de outro ator;
- tratar `DEFESA` como o CCP completo;
- reconstruir manualmente `Como chegamos aqui` como se fosse história comprovada;
- afirmar que a POC atual provou equivalência semântica/monotonicidade quando ela não provou;
- ignorar uma mudança material de estado dos atores já registrada antes do teste.

Se houver erro corrigível, a predecessora registra `REMEDIATE`, explica o delta e exige resposta corretiva. O papel só é transferido após `PASS` explícito.

## 6. Veredito da predecessora

A predecessora deve registrar uma avaliação no repositório com:

- pontuação por dimensão;
- erros e lacunas;
- correções exigidas;
- riscos residuais;
- veredito `PASS` ou `REMEDIATE`.

Após `PASS`, a predecessora deixa de tomar novas decisões operacionais do ator, salvo solicitação explícita do humano para auditoria retrospectiva.

Se o repositório canônico avançou durante o experimento, a sessão aprovada deve primeiro sincronizar o delta entre o snapshot usado no teste e o HEAD canônico atual antes de coordenar outros atores.

Sinal humano de conclusão:

```text
Rold, pode continuar com <Session Instance ID sucessora>.
```

## 7. Papel do humano

O humano atua como scheduler físico:

1. abre a nova sessão;
2. envia somente o bootstrap indicado no INBOX da sucessora;
3. deixa a sucessora ler o repositório e responder ao teste;
4. retorna à predecessora e pede `AVALIAR HANDOFF`;
5. se houver `REMEDIATE`, acorda a sucessora com `NOVO INPUT` após o delta ser registrado;
6. quando a predecessora emitir `PASS`, continua apenas com a sucessora.

O humano não deve copiar manualmente todo o contexto entre chats.

## 8. Modo experimental A/B de materialização

Quando houver mais de um mecanismo plausível para criar a sessão sucessora, pode-se comparar candidatos sobre o mesmo estado congelado.

Regras mínimas:

1. congelar um único snapshot `H0` antes de iniciar qualquer candidato;
2. criar uma branch experimental independente por candidato a partir de `H0`;
3. fornecer a mesma bateria e o mesmo estado de repositório;
4. proibir cada candidato de consultar outras branches, outros candidatos ou o HEAD canônico posterior;
5. manter respostas isoladas até todos concluírem;
6. não revelar ao avaliador qual mecanismo gerou qual resposta até a avaliação cega terminar, quando isso for operacionalmente possível;
7. registrar como variável experimental apenas diferenças reais entre as materializações;
8. após escolher a sucessora, fazê-la sincronizar `H0 → HEAD canônico` antes de assumir trabalho real.

Uma ramificação de chat pode carregar a transcrição histórica explícita. Um novo chat pode não carregar essa transcrição e ainda assim receber memória/contexto da conta. Portanto, a comparação correta é entre **mecanismos observados de materialização**, e não necessariamente entre `com memória` e `sem memória`.

## 9. Controle da predecessora

Quando a sessão predecessora também responder ao teste como referência, sua resposta deve ser congelada **antes** de qualquer resposta candidata ser inspecionada.

O congelamento ideal contém:

- corpo integral da resposta;
- hash criptográfico;
- timestamp ou commit identificável;
- armazenamento separado das branches dos candidatos durante o período cego.

Somente registrar um hash sem preservar/revelar posteriormente o corpo correspondente não oferece auditabilidade suficiente. Esse caso pode ser usado como observação, mas não deve ser tratado como controle reproduzível.

## 10. Primeiro experimento registrado — 2026-09-11

Snapshot comum: `ac939f7ba4aad9cc9fe957a8821a3d5feceb2c32`.

Condições:

- `exp/po-handoff-a`: chat ramificado da conversa predecessora;
- `exp/po-handoff-b`: novo chat sem transcrição explicitamente ramificada, mas com possíveis mecanismos de memória/contexto da conta.

Resultados:

- ramificação: commit `f06e8a54841e9ff18ae876a931abbd7b9925cec7` — 100/100, nenhum erro crítico;
- novo chat: commit `f19b2aff9a781edcbf2fb76b83f35ecbbd29e28c` — 100/100, nenhum erro crítico.

Conclusão limitada: neste teste e nesta rubrica, a ramificação explícita não apresentou vantagem mensurável de saúde operacional sobre o novo chat. Isso **não** prova equivalência geral dos mecanismos nem reconstrução puramente a partir do Git, porque o novo chat declarou contexto conversacional legitimamente disponível por mecanismos da conta.

Critério de desempate adotado: escolher o novo chat como `PO-001-02`, por atingir o mesmo resultado com menor dependência explícita da transcrição predecessora. A escolha é arquitetural/operacional, não evidência de superioridade intrínseca do novo chat.

O controle da predecessora foi declarado como 100/100 com SHA-256 `10e1d27d789de31108d53c1c233f43e14c3edc89943c89b337d4d247b2fe48f8`, mas o corpo não foi congelado externamente antes da inspeção dos candidatos. Portanto ele é registrado como limitação metodológica e não como controle reproduzível.

## 11. Aprendizado para o protocolo

Cada transição é também um experimento. Registrar falhas de reconstrução, perguntas que não discriminam saúde real, informações que ficaram implícitas demais e passos manuais desnecessários. Só após ciclos suficientes essas observações devem ser propostas de volta ao InitProj como regra geral.
