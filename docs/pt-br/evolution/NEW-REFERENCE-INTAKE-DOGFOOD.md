# Dogfood do Protocolo de Entrada e Progressão de Referências

**Status:** regra operacional experimental.

## 1. Decisão

O próprio protocolo usado para capturar, descobrir, testar, promover, restringir ou abandonar novas referências será o primeiro objeto permanente de dogfood desse mesmo protocolo.

Isso significa que o protocolo possui dois papéis simultâneos:

1. **instrumento de avaliação** — é usado para processar novas referências;
2. **objeto avaliado** — cada uso real produz evidência sobre clareza, custo, lacunas, excesso, ambiguidade e eficácia do próprio protocolo.

O protocolo não será considerado estável apenas porque foi escrito. Sua maturação ocorrerá por uso repetido, registro de atrito, comparação entre rodadas e revisão versionada.

## 2. Hipótese de dogfood

Hipótese operacional:

> Um protocolo de entrada e progressão de referências pode amadurecer de forma progressiva se cada execução real produzir, além da decisão sobre a referência processada, uma avaliação estruturada do próprio protocolo que a processou.

Estado inicial: `R1 — realizável em princípio / escopo aberto`.

## 3. Dupla saída obrigatória de cada execução

Toda execução real do intake deve produzir duas saídas distintas.

### Saída A — sobre a referência processada

- estado alcançado;
- Discovery realizado;
- rota escolhida;
- experimento, quando aplicável;
- evidência produzida;
- gaps da referência;
- decisão atual.

### Saída B — sobre o protocolo usado

- etapas realmente necessárias;
- etapas puladas e por quê;
- informação pedida cedo demais;
- informação que faltou quando necessária;
- decisões difíceis de classificar;
- termos ambíguos;
- tempo/custo de execução;
- retrabalho evitado ou criado;
- automações possíveis;
- risco de perda de rastreabilidade;
- pontos em que o usuário precisou improvisar fora do protocolo;
- alteração candidata para a próxima versão.

A execução não termina metodologicamente enquanto a Saída B não tiver sido registrada, ainda que possa ser mínima em casos triviais.

## 4. Ciclo de evolução do próprio protocolo

O ciclo de dogfood é:

**protocolo vigente → uso em referência real → observação do protocolo em uso → evidência/gaps → proposta de alteração → simulação da alteração → nova versão experimental → novo uso**.

Uma alteração no protocolo é tratada como nova referência vinculada à versão que a originou. Portanto, a evolução do protocolo também passa por captura, enquadramento, Discovery proporcional, decisão e teste.

Isso evita exceção autorreferente: o protocolo não pode exigir dos demais referências uma disciplina da qual ele próprio esteja isento.

## 5. Unidade de evidência de dogfood

Cada rodada gera uma evidência identificável, por exemplo `EVID-INTAKE-DOGFOOD-NNN`, contendo no mínimo:

- versão do protocolo usada;
- referência processada;
- contexto;
- duração aproximada;
- etapas percorridas;
- resultado da referência;
- fricções observadas;
- omissões observadas;
- alterações sugeridas;
- alterações efetivamente adotadas;
- limitações da rodada.

Uma única execução não demonstra eficácia geral. Ela apenas acrescenta evidência operacional contextual.

## 6. Critérios de evolução do protocolo

O protocolo pode ser fortalecido quando rodadas independentes mostrarem que ele:

- captura referências com baixo custo inicial;
- seleciona diligência de forma coerente;
- favorece ADOPT/ADAPT/COMPOSE antes de INVENT;
- produz testes executáveis quando necessários;
- evita promoção prematura de hipótese para regra;
- preserva origem, decisão, evidência e gaps;
- não exige trabalho que não altere decisão, gate, medida ou rastreabilidade;
- consegue ser aplicado por interlocutores diferentes sem depender de conhecimento tácito excessivo.

O protocolo deve ser enfraquecido, restringido ou revisado quando produzir burocracia sem valor, classificações instáveis, falsa precisão, perda de informação relevante, decisões opacas ou necessidade recorrente de contorná-lo.

## 7. Regra de atualização

Não atualizar o protocolo apenas porque uma execução foi desconfortável. Primeiro registrar o atrito e distinguir:

- falha do protocolo;
- caso excepcional;
- erro de uso;
- informação ainda ausente;
- necessidade real de nova regra;
- necessidade apenas de melhor projeção/documentação.

Quando a alteração for aceita, preservar:

**versão anterior → evidência que motivou mudança → gap → decisão → nova versão**.

## 8. Relação com MyTrues

Este dogfood é também uma simulação mínima de MyTrues. O repositório preserva a versão física; os artefatos de dogfood preservam a relação cognitiva e epistemológica entre uso, problema observado, evidência, decisão e revisão.

A intenção é que a futura materialização em MyTrues possa representar essa mesma cadeia sem depender de reconstrução manual posterior.

## 9. Primeira aplicação

O próprio `NEW-REFERENCE-INTAKE-PROTOCOL-DRAFT.md` é a primeira referência submetida permanentemente a este dogfood.

A partir de agora, referências reais processadas pelo intake devem servir simultaneamente para decidir sobre a referência e para testar o intake. Alterações do protocolo devem surgir de evidência registrada sempre que possível, e não apenas de preferência editorial.
