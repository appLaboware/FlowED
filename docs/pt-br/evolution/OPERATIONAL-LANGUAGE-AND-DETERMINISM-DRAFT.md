# Draft — Linguagem Operacional e Determinismo do FlowED

**Status:** Referência Experimental em `R1 — realizável em princípio / escopo aberto`.

**Reference ID:** `REF-2026-002`  
**Origem:** GAP-M004, GAP-M005 e GAP-M015; debate sobre comando, parâmetros, declaratividade e determinismo.  
**Diligência de Discovery:** L1 — exploratory/scoping.  
**Rota provisória:** `COMPOSE` — combinar padrões existentes antes de inventar sintaxe/semântica própria.

## 1. Pergunta

Qual deve ser a unidade primária da linguagem operacional do FlowED e como uma interface humana simples pode preservar comportamento determinístico, auditável e independente de tecnologia?

## 2. Decisão provisória

O FlowED **não deve fazer da string de comando sua unidade semântica primária**.

A hipótese atual é:

> **O núcleo recebe uma requisição operacional canônica, tipada e versionada. CLI, UI, API e linguagem natural são projeções/compiladores dessa requisição.**

A interface humana pode continuar usando verbos, parâmetros e opções. Porém, antes de qualquer efeito, a entrada deve ser normalizada para uma representação canônica, validada e versionada.

Isso permite manter uma linguagem agradável para humanos sem transformar particularidades de CLI, shell, agente ou ferramenta externa em semântica central do FlowED.

A requisição operacional possui três modos semânticos iniciais: observação, estado e ação. Apenas os dois últimos expressam intenção de mudança.

## 3. Prior art adotado na composição

### 3.1 Desired state + reconciliation — Kubernetes

Controllers Kubernetes operam por reconciliação entre estado desejado e estado atual. A lição adotada é que, para objetos persistentes, o usuário deve preferencialmente declarar **o resultado desejado**, e o sistema calcula como convergir.

### 3.2 Plan antes de Apply — Terraform

Terraform compara configuração/estado desejado com estado anterior e produz um plano de mudanças antes da aplicação. A lição adotada é separar **decisão semântica** de **execução efetiva**, tornando a mudança inspecionável e reproduzível.

### 3.3 Resource-oriented/declarative-friendly APIs — Google AIP

As AIPs favorecem recursos e métodos padronizados que funcionam em clientes declarativos, CLIs e UIs; recursos declarative-friendly usam controles como `etag`, e identificadores de requisição são usados para deduplicação, retries seguros e auditoria.

### 3.4 Hermeticity/reproducibility — Bazel

Bazel trata hermeticidade como dependência apenas de entradas conhecidas/declaradas e restringe fontes ambientais implícitas para favorecer reprodutibilidade.

### 3.5 Validation-first configuration — CUE

CUE trata validação e constraints como responsabilidade central da linguagem de configuração. A lição adotada é que uma requisição não deve ser apenas parseável; ela precisa satisfazer schema, constraints e policies antes de planejamento ou execução.

## 4. Três classes semânticas de requisição

Forçar toda Engenharia de Software a um único estilo — imperativo ou declarativo — produz distorções. A proposta é distinguir três classes.

### 4.1 Observe Request — observação/consulta

Expressa necessidade de informação sem intenção de produzir efeito no domínio.

Exemplos conceituais:

- obter estado atual;
- comparar estado desejado e atual;
- explicar por que uma policy se aplica;
- inspecionar plano;
- validar uma declaração sem executá-la.

O mecanismo preferencial é **read/derive → validate authorization → return view/explanation**, preservando proveniência da resposta quando relevante.

### 4.2 State Intent — intenção de estado

Expressa **como algo deve permanecer/terminar**, não a sequência exata de passos.

Exemplos conceituais:

- projeto deve possuir versionamento ativo;
- branch principal deve exigir determinada política;
- qualidade deve operar em determinada intensidade;
- ambiente deve possuir determinado conjunto de capabilities.

O mecanismo preferencial é **desired state → diff → plan → reconcile/apply**.

Reexecução da mesma intenção, sob o mesmo estado relevante, deve tender a `no-op`.

### 4.3 Action Intent — intenção de ação/evento

Expressa uma ação com significado temporal próprio, em que repetir pode significar fazer novamente.

Exemplos conceituais:

- publicar uma release;
- aprovar uma entrega;
- disparar um benchmark;
- registrar uma decisão;
- executar uma migração específica.

O mecanismo preferencial é **validate → plan/preconditions → invoke → receipt/result**.

Ações devem usar idempotency/request IDs quando repetição acidental não deve duplicar efeitos.

## 5. Unidade canônica proposta

Nome de trabalho: **Operational Request / Requisição Operacional**.

A `Operational Intent / Intenção Operacional` permanece como subtipo de requisição que pretende alterar estado ou produzir ação. Essa distinção evita chamar consultas e explicações de “intenção de mudança”.

Não é ainda terminologia consolidada. A unidade deve carregar, no mínimo:

- `schema_version` — versão semântica da declaração;
- `request_id` — identidade estável da requisição/tentativa;
- `mode` — `observe`, `state` ou `action`;
- `domain` — domínio/capability responsável;
- `operation` — operação semântica padronizada;
- `target` — objeto/escopo afetado ou consultado;
- `desired` ou `arguments` — conteúdo declarado;
- `constraints` — limites obrigatórios;
- `policy_refs` — políticas/baselines aplicáveis e respectivas versões;
- `context_refs` — contexto que influencia legitimamente a resolução;
- `adapter_constraints` — requisitos de materialização quando existirem;
- `state_revision`/equivalente — proteção contra executar sobre estado diferente do planejado;
- `provenance` — quem/o que originou a requisição;
- `rationale_ref` — vínculo opcional/obrigatório conforme risco com decisão e racional.

A representação concreta pode ser JSON, YAML, CUE, Protobuf ou outro formato. O princípio é semântico, não sintático.

## 6. CLI como projeção humana

A CLI pode usar uma gramática convencional e previsível:

**`flow <domain> <verb> [target] [named options]`**

Exemplos apenas ilustrativos:

- `flow quality ensure projeto --level standard`
- `flow release publish v1.4.0 --channel stable`
- `flow project plan --profile enterprise`

A CLI não executa a string diretamente. Ela a compila para uma `Operational Request` canônica.

### 6.1 Verbos

Verbos são úteis para a interface humana, mas não devem criar semânticas arbitrárias por domínio.

Preferência atual:

- pequeno vocabulário transversal de observação/controle (`get`, `diff`, `plan`, `explain`, `validate`, `apply`);
- operações de estado com semântica declarativa (`ensure`, `set` ou equivalente a definir após teste);
- verbos de ação/evento somente quando o domínio realmente expressa evento (`publish`, `approve`, `run`, etc.).

O vocabulário final deve ser pesquisado/testado antes de normalização.

### 6.2 Parâmetros posicionais

Usar poucos parâmetros posicionais e somente quando sua semântica é inequívoca e estável — tipicamente o alvo principal ou identidade do recurso.

Todos os demais dados semânticos devem ser nomeados no modelo canônico.

### 6.3 Opções/flags

Flags servem como ergonomia. Antes de planejar, devem ser resolvidas para campos explícitos.

Regra proposta: **não existe default oculto no plano final**.

Um perfil como `--profile enterprise` pode ser conveniente, mas o planner deve expandi-lo para os valores concretos e versões que realmente participarão da execução.

## 7. Declarativo ou imperativo?

A proposta não escolhe um lado para tudo.

- **estado persistente:** declarativo por padrão;
- **consulta/explicação:** observacional;
- **evento temporal:** imperativo explícito;
- **CLI:** pode continuar verbal/imperativa por ergonomia;
- **núcleo:** trabalha com semântica tipada, não com interpretação ad hoc da frase de comando.

Assim, a escolha entre verbo imperativo e declaração de estado deixa de ser estética e passa a depender da natureza semântica da operação.

## 8. Determinismo: definição operacional proposta

Determinismo no FlowED não deve significar que o mundo externo nunca falha ou muda. Deve significar que a **decisão do sistema é reproduzível quando seus inputs legítimos são os mesmos**.

Proposta de contrato:

> `Plan = F(CanonicalRequest, StateSnapshot, PolicySet, CapabilitySet, AdapterSet)`

onde todos os argumentos relevantes são identificados e versionados.

Se essas entradas forem semanticamente idênticas, o planner determinístico deve produzir o mesmo plano canônico e o mesmo `plan_hash`.

A execução pode encontrar falhas externas; essas falhas não devem alterar silenciosamente a decisão original. Devem produzir estado/receipt observável e, para State Intents, nova reconciliação explícita.

## 9. Camadas de determinismo

### 9.1 Determinismo de interpretação

Mesma requisição canônica e mesma versão de schema produzem a mesma interpretação.

Linguagem natural/IA nunca é entrada autoritativa direta do executor: precisa primeiro ser compilada e validada em requisição canônica.

### 9.2 Determinismo de planejamento

Mesma requisição + mesmo snapshot + mesmas policies/capabilities/adapters versionados produzem mesmo plano.

### 9.3 Determinismo de execução possível

Quando o domínio permite, ações devem ser idempotentes, retry-safe, transacionais ou compensáveis.

Quando não permitem, a não determinabilidade deve ser declarada em contrato e tratada por preconditions, receipts, locks, compensation ou reconciliação.

### 9.4 Reprodutibilidade de artefatos

Quando relevante, versões, dependências, timestamps, seeds, environment variables, network inputs e demais fontes de variação devem ser declaradas, fixadas ou registradas. O objetivo é reduzir estado ambiental implícito.

## 10. Pipeline canônico

Entrada humana/máquina → parse/compile → canonicalize → validate constraints → resolve explicit context/policies → snapshot state → plan/derive → explain/diff → authorize quando houver efeito → apply/reconcile/invoke → receipt/result → observe → evidence/history.

Para operações de baixo risco, algumas etapas podem ser agrupadas na UX, mas devem continuar existindo conceitualmente e ser recuperáveis para auditoria.

Para operações de alto risco, `plan` e `apply` devem ser separáveis e a autorização deve apontar para o hash exato do plano aprovado.

## 11. Regras contra não determinismo acidental

1. nenhum efeito antes de validação/canonicalização;
2. defaults resolvidos e registrados antes do plano;
3. contexto ambiental só influencia se declarado como input legítimo;
4. adapters/providers e policies relevantes são versionados;
5. estado usado no planejamento recebe revisão/hash/etag equivalente;
6. apply de plano antigo deve falhar ou exigir replanejamento quando preconditions mudarem;
7. request IDs/idempotency keys evitam duplicação acidental onde necessário;
8. plano recebe identidade/hash imutável;
9. resultado produz receipt observável;
10. IA pode interpretar/sugerir, mas não introduzir silenciosamente campos ou autoridade no executor.

## 12. Consequência para o Pilar 1

`Liberdade governada` ganha uma definição operacional mais concreta:

> O domínio é livre para materializar uma intenção por implementações diferentes, desde que preserve o contrato semântico, declare capacidades e limitações, aceite inputs explícitos, produza plano/resultado rastreável e não altere silenciosamente a intenção recebida.

Assim, o núcleo governa **semântica, contratos, validação, políticas, planejamento e rastreabilidade**; o domínio conserva soberania sobre sua implementação interna dentro do contrato declarado.

## 13. Estado dos gaps após esta rodada

### GAP-M004 — Unidade primária da linguagem operacional

Avança de `OPEN` para `PARTIAL`.

Hipótese atual: `Operational Request` é envelope semântico primário; `Operational Intent` é o subtipo de mudança. Comando é projeção. Ainda falta provar suficiência em domínios distintos e estabilizar ontologia/nome.

### GAP-M005 — Coordenação comum versus soberania dos domínios

Avança para `PARTIAL`.

Fronteira candidata: núcleo governa representação canônica, contratos, validation/policies, planning e provenance; domínio governa implementação/materialização interna. Precisa teste em pelo menos dois domínios.

### GAP-M015 — Liberdade governada

Avança para `PARTIAL`.

Propriedades mínimas candidatas: contrato semântico, inputs explícitos, constraints, rastreabilidade, versionamento de materializadores/policies, plan/receipt, idempotência/reconciliação conforme natureza da operação.

## 14. Novos gaps

### GAP-M021 — Suficiência da taxonomia Observe × State × Action

Validar se três modos cobrem operações reais de domínios distintos sem criar exceções artificiais.

### GAP-M022 — Vocabulário operacional transversal

Definir conjunto mínimo de verbos padronizados e separar verbos de controle do runtime de operações próprias dos domínios.

### GAP-M023 — Contrato formal de determinismo

Definir exatamente quais inputs entram no hash/planejamento, equivalência semântica, canonicalização e tratamento de nondeterminism declarado.

### GAP-M024 — Representação canônica e linguagem de schema

Escolher ou compor formato/schema (JSON Schema, CUE, Protobuf, outro) somente depois de POC comparativo; não inventar DSL antes de demonstrar residual.

## 15. Dogfood desta referência

Esta proposta entrou como `REF-2026-002` e foi submetida ao intake atual.

- `CAPTURED`: questão sobre comando/parâmetros/opções e determinismo;
- `FRAMED`: unidade semântica precisa ser comum a domínios e não depender de materializador;
- diligência: L1;
- prior art: reconciliation/desired state, plan/apply, resource-oriented declarative-friendly APIs, hermeticity e validation-first;
- rota: `COMPOSE`;
- residual atual: composição específica para linguagem horizontal de Engenharia de Software e vínculo com governança epistemológica FlowED;
- estado: `EXPERIMENTAL` conceitualmente, ainda sem implementação.

O próprio refinamento desta rodada encontrou uma terceira classe necessária para evitar chamar consultas de “intenção de mudança”: `observe`. Isso é evidência documental de que o dogfood já está corrigindo o modelo antes de implementação.

O próximo teste não deve discutir sintaxe abstratamente. Deve escolher dois domínios de natureza diferente — por exemplo Versionamento e Qualidade — e verificar se ambos podem expressar operações reais usando o mesmo envelope de requisição sem perder semântica.
