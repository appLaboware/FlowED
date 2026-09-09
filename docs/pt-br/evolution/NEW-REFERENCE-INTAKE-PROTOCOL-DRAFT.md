# Draft executável — Entrada de Novas Referências no FlowED

**Status:** Referência Experimental. Aplicação inicial autorizada para simulação documental e uso controlado.

## 1. Por que “referência” e não apenas “ideia”

A entrada do FlowED não deve pressupor invenção. O objeto recebido pode ser uma ideia nova, prática já existente, norma, paper, ferramenta, princípio, tecnologia, problema, hipótese, decisão ou composição.

Por isso, o nome de trabalho é **Nova Referência**. A origem pode ser interna ou externa.

## 2. Objetivo

Permitir que qualquer nova referência entre no FlowED com custo inicial baixo, sem ganhar autoridade prematura e sem perder a informação necessária para Discovery, comparação, simulação, validação e futura decisão.

O protocolo precisa ser simples o suficiente para uso cotidiano e forte o suficiente para impedir que opinião seja promovida silenciosamente a regra.

## 3. Regra de entrada mínima

Toda nova referência começa por uma **Ficha de Entrada**. Nesta etapa não é exigida pesquisa completa, score ou prova de eficácia.

Campos mínimos obrigatórios:

1. `id` — identificador estável;
2. `origem` — pessoa, fonte, documento, experiência, sistema ou referência externa de onde veio;
3. `enunciado_bruto` — a ideia/referência como chegou, sem reescrita que apague a origem;
4. `problema_ou_objetivo` — que problema tenta resolver ou que objetivo pretende atingir;
5. `contexto_inicial` — onde isso parece relevante;
6. `impacto_se_errada` — baixo, médio, alto ou crítico, com justificativa curta;
7. `estado_inicial` — sempre `CAPTURED`, salvo importação já acompanhada de evidência formal;
8. `responsavel_pela_triagem` — quem decide o próximo passo.

A ficha deve apontar para a fonte bruta quando existir.

## 4. Estado inicial e máquina mínima de estados

Estados de intake:

- `CAPTURED` — entrada preservada, ainda sem enquadramento suficiente;
- `FRAMED` — D0 suficiente: problema, contexto, risco e objetivo foram enquadrados;
- `DISCOVERY` — D1 em andamento;
- `ROUTED` — existe decisão de rota: ADOPT, ADAPT, COMPOSE, INVENT, HOLD ou REJECT;
- `EXPERIMENTAL` — referência autorizada para simulação/validação controlada;
- `ACTIVE` — referência adotada no escopo declarado;
- `SUSPENDED` — uso interrompido sem apagar histórico;
- `REJECTED` — não adotada no escopo atual;
- `SUPERSEDED` — substituída por referência posterior.

Esses estados não substituem realizabilidade, sustentação ou maturidade. São estados de fluxo operacional.

## 5. Fluxo executável

### I0 — Capturar

Registrar a Ficha de Entrada sem exigir que o originador já saiba provar, classificar ou defender cientificamente a referência.

Regra: **capturar primeiro; julgar depois**.

Saída: estado `CAPTURED`.

### I1 — Enquadrar (D0)

Responder somente o necessário:

- qual problema/objetivo existe?
- para quem/contexto?
- o que mudaria se adotássemos?
- qual o risco de estar errado?
- que claim estamos fazendo: existência, viabilidade, eficácia, superioridade, segurança, conformidade, outro?

Saída: estado `FRAMED`.

### I2 — Definir diligência

Escolher L0–L4 conforme impacto, irreversibilidade, risco, novidade e força do claim.

Regra prática inicial:

- baixo impacto + claim fraco → L0/L1;
- impacto médio ou dependência relevante → L1/L2;
- baseline central, claim forte ou decisão difícil de reverter → L2/L3;
- publicação científica/certificação/claim amplo → L3/L4.

A justificativa do nível escolhido é obrigatória; o nível pode ser elevado durante o processo.

### I3 — Discovery (D1)

Aplicar **ADOPT → ADAPT → COMPOSE → INVENT only proven residual**.

Produzir um mapa curto contendo:

- prior art encontrado;
- o que pode ser adotado diretamente;
- o que exige adaptação;
- o que pode ser composto;
- residual ainda não coberto;
- limite declarado da busca;
- evidência adversa relevante.

Saída: decisão de rota.

### I4 — Roteamento

Escolher explicitamente uma rota:

- `ADOPT` — referência externa resolve suficientemente o problema no contexto;
- `ADAPT` — referência existente resolve núcleo, exigindo mudanças declaradas;
- `COMPOSE` — combinação de referências cobre o problema;
- `INVENT` — residual relevante permaneceu após Discovery;
- `HOLD` — informação insuficiente ou momento inadequado;
- `REJECT` — inadequada, inviável, redundante ou risco não aceitável.

A rota não é um score; é uma decisão operacional rastreável.

Saída: estado `ROUTED`.

### I5 — Preparar experimento (D2–D3)

Somente para ADAPT, COMPOSE ou INVENT, e para ADOPT quando a adequação local ainda precisar ser testada.

Criar um `Experiment Brief` mínimo:

- objetivo;
- pergunta(s) GQM;
- hipótese/expectativa;
- critérios de sucesso e falha;
- contexto do teste;
- riscos;
- duração/limite;
- dados/observações a coletar;
- rollback/saída segura;
- gaps conhecidos.

Se houver artefato a construir, aplicar DSRM no nível necessário.

### I6 — Autorizar simulação (D4)

Antes do uso controlado, verificar gates:

- realizabilidade mínima para o escopo do teste;
- nenhum gap bloqueante não mitigado;
- sucesso/falha definidos antes da observação quando possível;
- risco aceitável;
- fonte e decisões preservadas;
- responsável explícito.

Saída: estado `EXPERIMENTAL`.

### I7 — Uso contextual (D5)

Aplicar em contexto real limitado quando fizer sentido. Registrar intervenção, contexto, alterações locais, resultados, efeitos adversos e ameaças à validade.

### I8 — Síntese e decisão (D6)

Atualizar separadamente:

- realizabilidade/maturidade;
- sustentação científica;
- sustentação empírica/operacional;
- adequação contextual;
- rastreabilidade;
- validação/replicação;
- gaps;
- decisão.

Decisão possível: `ACTIVE`, permanecer `EXPERIMENTAL`, voltar para `DISCOVERY`, `SUSPENDED`, `REJECTED` ou iniciar nova versão.

## 6. Ficha de Entrada — template mínimo

```yaml
reference_id: REF-YYYY-NNN
created_at: YYYY-MM-DD
origin:
raw_statement:
source_link_or_artifact:
problem_or_goal:
initial_context:
claim_type:
impact_if_wrong: low|medium|high|critical
impact_rationale:
intake_state: CAPTURED
triage_owner:
notes:
```

O bloco é uma representação de intercâmbio. A implementação concreta pode ser formulário, arquivo, banco, issue ou MyTrues.

## 7. Research/Reference Brief — depois de D0

```yaml
reference_id:
problem:
objective:
actors:
context:
constraints:
claim:
expected_change:
risk:
known_assumptions:
known_gaps:
discovery_diligence: L0|L1|L2|L3|L4
diligence_rationale:
```

## 8. Discovery Map — depois de D1

```yaml
reference_id:
search_boundary:
prior_art:
  - item:
    relation: adopt|adapt|compose|inspiration|adverse
residual:
adverse_evidence:
unknowns:
route: ADOPT|ADAPT|COMPOSE|INVENT|HOLD|REJECT
route_rationale:
```

## 9. Experiment Brief — quando houver teste

```yaml
reference_id:
version:
objective:
questions:
metrics_or_observations:
success_criteria:
failure_criteria:
context:
duration_or_limit:
risks:
rollback:
blocking_gaps:
expected_evidence:
authorized_by:
```

## 10. Regras para manter o processo adotável

1. Intake não exige paper, score ou experimento: exige captura fiel e contexto mínimo.
2. Rigor cresce com risco e força do claim, não com preferência burocrática.
3. A mesma referência não precisa executar todas as etapas se for rejeitada, adotada diretamente ou irrelevante.
4. Nenhuma etapa deve pedir informação que não mude uma decisão, um gate, uma medida ou a rastreabilidade.
5. Formulários podem ser progressivos: campos aparecem apenas quando o estado exige.
6. O originador da ideia não precisa ser o pesquisador que executará Discovery.
7. Evidência contrária deve ser preservada junto com evidência favorável.
8. A ausência de resposta fecha nada automaticamente; pode levar a HOLD.
9. Automatização pode sugerir classificação e rota, mas decisões com autoridade devem permanecer identificáveis.
10. Toda promoção deve preservar o estado anterior e o racional da transição.

## 11. Critério de sucesso deste próprio draft

Este protocolo só deve amadurecer se, aplicado a referências reais, conseguir:

- receber uma ideia em poucos minutos;
- não bloquear criatividade na captura;
- impedir promoção silenciosa a norma;
- encaminhar a diligência proporcional;
- encontrar/adotar prior art antes de inventar;
- produzir um experimento executável quando necessário;
- preservar origem, gaps, evidência e decisão;
- permitir abandono sem apagar aprendizado;
- ter custo percebido menor que o retrabalho evitado.

## 12. Estado epistemológico

Este documento é uma Referência Experimental em `R1 — realizável em princípio / escopo aberto`.

Ele compõe diretamente o `DISCOVERY-AND-PROGRESSIVE-VALIDATION-PROTOCOL.md` e o `THEORY-SIMULATION-PROTOCOL.md`.

A próxima ação correta não é promovê-lo a norma, mas usá-lo em pelo menos uma entrada real e registrar atrito, omissões, decisões desnecessárias e informação faltante.
