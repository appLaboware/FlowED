# Exemplo 001 — Autoaplicação do Intake de Nova Referência

**Referência testada:** protocolo executável para entrada de novas referências no FlowED.

## I0 — Captura

- `reference_id`: REF-2026-001
- `origin`: discussão de evolução do Manifesto FlowED
- `raw_statement`: precisamos de uma forma prática, verossímil, adotável e executável para uma nova ideia/referência entrar no próprio protocolo FlowED
- `problem_or_goal`: transformar o protocolo científico amplo D0–D6 em uma rotina cotidiana que não bloqueie a entrada de ideias e ainda preserve rigor progressivo
- `initial_context`: evolução conceitual e futura operação de projetos FlowED
- `claim_type`: viabilidade operacional / desenho de processo
- `impact_if_wrong`: médio
- `intake_state`: CAPTURED

## I1 — Enquadramento

Problema: D0–D6 é metodologicamente defensável, mas ainda abstrato para uma pessoa registrar uma nova referência durante o trabalho normal.

Objetivo: criar uma porta de entrada mínima que preserve origem e contexto e encaminhe rigor apenas quando necessário.

Mudança esperada: uma nova referência pode ser capturada rapidamente e depois entrar em Discovery, simulação e validação sem precisar nascer como uma pesquisa completa.

Risco principal: burocratizar a criação ou, no extremo oposto, permitir que intake superficial seja confundido com validação.

Estado: `FRAMED`.

## I2 — Diligência

Diligência inicial: **L1 — exploratory/scoping**.

Justificativa: o draft deriva diretamente de protocolos já compostos a partir de EBSE, DSRM, TTM, GQM e métodos de validação contextual. Neste momento o claim é apenas de plausibilidade operacional e teste interno, não de validade científica geral.

Uma promoção futura para baseline do FlowED exigirá diligência maior e uso real.

## I3 — Discovery

Prior art interno já adotado:

- `DISCOVERY-AND-PROGRESSIVE-VALIDATION-PROTOCOL.md` — fornece D0–D6, L0–L4, gates e Adapt First;
- `THEORY-SIMULATION-PROTOCOL.md` — fornece Referência Experimental, gaps, evidências e decisão;
- `GAP-REGISTRY.md` — fornece persistência manual de lacunas.

Residual identificado: **porta de entrada cotidiana e progressiva**, incluindo captura mínima, estado operacional e roteamento para ADOPT/ADAPT/COMPOSE/INVENT/HOLD/REJECT.

Rota: `COMPOSE`.

Racional: não há necessidade atual de inventar um novo método científico; o residual é de integração operacional entre métodos já escolhidos.

## I4 — Roteamento

Decisão: `COMPOSE`.

Composição:

1. captura de origem e contexto;
2. D0–D1 do protocolo de Discovery;
3. Adapt First para roteamento;
4. Experiment Brief do protocolo de simulação;
5. D4–D6 para teste e síntese;
6. estados operacionais separados de realizabilidade e sustentação.

Estado: `ROUTED`.

## I5 — Experimento

Objetivo: verificar se o draft permite receber e encaminhar uma referência real sem burocracia excessiva.

Perguntas:

- a captura inicial consegue ser feita sem pesquisa prévia?
- os campos mínimos mudam decisões reais ou há campos inúteis?
- a rota ADOPT/ADAPT/COMPOSE/INVENT/HOLD/REJECT é suficiente?
- é possível distinguir estado operacional de maturidade e evidência?
- o usuário sabe qual é o próximo passo?

Observações iniciais:

- o draft é executável documentalmente;
- a autoaplicação conseguiu chegar a uma rota sem exigir score fictício;
- a separação `CAPTURED`/`FRAMED`/`DISCOVERY`/`ROUTED` parece útil;
- ainda não há evidência de custo real, tempo de preenchimento ou comportamento sob volume.

Critérios de falha futura:

- intake demorar mais do que a utilidade percebida;
- originadores deixarem de registrar ideias por excesso de campos;
- decisões de diligência serem arbitrárias;
- referências pularem Discovery e ganharem autoridade indevida;
- estado operacional ser confundido com score epistemológico.

Rollback: manter apenas captura bruta + D0 e redesenhar demais estados caso o fluxo se mostre excessivo.

Estado: `EXPERIMENTAL`.

## Evidência produzida

`EVID-INTAKE-001`

Classe: operacional/documental.

Força: muito baixa.

Suporta: o draft é executável como artefato manual e consegue processar ao menos uma referência sem contradição estrutural imediata.

Não suporta: eficiência, usabilidade, escalabilidade, adequação organizacional, superioridade a processos existentes ou validade científica do protocolo.

## Gaps abertos

### GAP-I001 — Tempo máximo aceitável de intake

Pergunta: quanto tempo uma entrada cotidiana pode exigir antes de começar a desestimular registro?

### GAP-I002 — Seleção de diligência reproduzível

Pergunta: como transformar risco, impacto, novidade, irreversibilidade e força do claim em uma escolha L0–L4 suficientemente consistente sem inventar falsa precisão?

### GAP-I003 — Cardinalidade de referências

Pergunta: quando uma entrada contém várias hipóteses ou decisões acopladas, deve ser dividida em várias referências ou preservada como composição?

### GAP-I004 — Autoridade de roteamento

Pergunta: quem pode decidir ADOPT/ADAPT/COMPOSE/INVENT/HOLD/REJECT em diferentes contextos e riscos?

### GAP-I005 — Automatização segura

Pergunta: quais campos e classificações podem ser sugeridos automaticamente sem substituir decisão humana ou promover inferência a fato?

## Decisão desta rodada

Manter o draft em **R1 — realizável em princípio / escopo aberto** e estado operacional `EXPERIMENTAL`.

Próximo teste recomendado: usar o intake em uma nova ideia concreta que não seja sobre o próprio FlowED, medir tempo, campos ignorados, dúvidas e retrabalho e então revisar o protocolo.
