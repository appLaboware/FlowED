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

```text
sessão predecessora
→ checkpoint / handoff package
→ sessão sucessora limpa
→ reconstrução pelo repositório
→ teste cognitivo
→ avaliação pela predecessora
→ correções, se necessárias
→ PASS
→ sucessora assume o ator
```

Durante a sobreposição, a predecessora permanece avaliadora e a sucessora permanece **candidata à continuidade**, sem emitir novas decisões operacionais fora do teste salvo autorização explícita.

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

## 8. Aprendizado para o protocolo

Cada transição é também um experimento. Registrar falhas de reconstrução, perguntas que não discriminam saúde real, informações que ficaram implícitas demais e passos manuais desnecessários. Só após ciclos suficientes essas observações devem ser propostas de volta ao InitProj como regra geral.
