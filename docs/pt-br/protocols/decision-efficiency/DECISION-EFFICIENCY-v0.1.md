# Decision Efficiency Protocol — DEP 0.1

**ID:** FLOWED-DECISION-EFFICIENCY  
**Versão:** 0.1-draft  
**Status:** DOGFOODING  
**Owner de domínio:** FlowED  
**Escopo:** redução contínua de iterações, custo decisório, ambiguidade e trabalho cognitivo repetido em projetos conduzidos por humanos e agentes de IA.

## 1. Metaobjetivo

O FlowED deve perseguir continuamente a redução do número de interações necessárias para transformar intenção em resultado correto, verificável e reutilizável.

A eficiência não é apenas tempo de execução. Também inclui:

- tempo humano;
- número de iterações;
- tokens e custo de IA;
- necessidade de modelos mais caros;
- retrabalho;
- ambiguidade transferida entre atores;
- compute/energia e recursos consumidos sem ganho equivalente;
- perda de conhecimento por decisões repetidas que poderiam ter sido institucionalizadas.

Princípio:

```text
EVERY REPEATED CONVERSATION IS A CANDIDATE FOR A RULE.
EVERY STABLE RULE IS A CANDIDATE FOR A TEMPLATE OR CONTRACT.
EVERY REPEATABLE CONTRACT IS A CANDIDATE FOR VALIDATION.
EVERY DETERMINISTIC STEP IS A CANDIDATE FOR AUTOMATION.
```

## 2. Analogia de competição

O FlowED trata pequenas ineficiências como uma equipe de competição trata milésimos de segundo: melhorias pequenas, quando repetidas em toda a organização, acumulam valor relevante.

Nenhuma melhoria é pequena demais para ser registrada quando:

- reduz uma interação recorrente;
- elimina ambiguidade;
- evita uma decisão já tomada anteriormente;
- permite usar um executor mais barato;
- transforma julgamento repetitivo em comportamento determinístico;
- reduz retrabalho ou necessidade de escalonamento.

## 3. Escada de compressão decisória

Uma prática descoberta em conversa deve poder evoluir progressivamente por estes níveis:

```text
CONVERSATION
    ↓
DECISION
    ↓
RULE / POLICY
    ↓
POP / PROCEDURE
    ↓
TEMPLATE / PROMPT TEMPLATE / PROFILE
    ↓
CONTRACT / SCHEMA
    ↓
VALIDATOR / TEST
    ↓
AUTOMATION / CLI / TOOL
    ↓
MEASURED OPERATION
```

Nem todo item precisa chegar ao último nível. O objetivo é empurrar para níveis mais determinísticos tudo aquilo que já não exige julgamento humano ou inteligência de alto custo.

## 4. Economia de inteligência

A capacidade mais cara deve ser usada prioritariamente para decisões de maior incerteza, impacto ou abrangência.

```text
HIGH-COST INTELLIGENCE -> high-impact decisions
LOW-COST INTELLIGENCE  -> bounded interpretation and decomposition
DETERMINISTIC TOOLING   -> repeatable execution
```

O objetivo não é reduzir qualidade nem eliminar revisão. É impedir que inteligência cara seja consumida em execução que já pode ser especificada de forma determinística.

## 5. Autoridade por camada

A autonomia deve ser proporcional ao escopo decisório e à capacidade necessária.

### Product Owner

Responsável por decisões de produto, trade-offs, prioridade, bounded context, valor, risco e ambiguidades não resolvidas por política existente.

Recebe o menor volume possível de tarefas operacionais e concentra-se em decisões de maior impacto.

### Project/Product Manager

Recebe decisões já enquadradas por políticas e contratos do FlowED. Pode decompor, planejar, coordenar, verificar dependências e resolver ambiguidades dentro do mandato recebido.

Não deve reabrir decisões institucionais já materializadas sem evidência de conflito ou necessidade de mudança.

### Developer / Executor

Recebe uma unidade de trabalho estreita, verificável e com baixa liberdade interpretativa.

Exemplo de forma desejada:

```text
CREATE file X
USING template Y
WITH variables Z
RUN validator V
REPEAT UNTIL PASS or explicit blocker
RETURN report R
```

O executor não precisa reinterpretar diretamente toda a filosofia de engenharia do ecossistema quando essa filosofia já estiver incorporada em templates, contratos, validators e ferramentas.

## 6. Bounded authority, não confiança implícita

A redução de autonomia operacional deve ser implementada por escopo explícito, não por suposição sobre competência.

Cada missão deve responder:

```text
WHAT MAY BE DECIDED HERE?
WHAT IS ALREADY DECIDED?
WHAT MUST NOT BE REINTERPRETED?
WHAT REQUIRES ESCALATION?
WHAT IS THE ACCEPTANCE CONDITION?
```

Quando um executor encontra algo fora da autoridade recebida, deve escalar em vez de inventar uma decisão local.

## 7. Referências de engenharia adotadas

O FlowED deve encapsular progressivamente as referências de engenharia adotadas pela organização, para que elas apareçam como comportamento executável e não apenas como recomendações textuais.

Referências iniciais declaradas:

- Domain-Driven Design — para limites de domínio, linguagem e ownership;
- Clean Code — para legibilidade, simplicidade e responsabilidade local;
- Test-Driven Development — para especificação/validação orientada por testes quando aplicável;
- Arquitetura Hexagonal — para separar domínio de adapters, fornecedores e mecanismos de execução.

Essas referências não devem permanecer apenas como instruções genéricas do tipo “siga DDD”. O FlowED deve, sempre que possível, traduzi-las em:

- regras;
- checklists;
- templates;
- arquitetura de referência;
- contratos;
- validators;
- testes;
- geradores;
- ferramentas determinísticas.

## 8. Composição com o ecossistema appLaboware

A decisão concreta pertence a quem possui autoridade sobre seu conteúdo. Produtos adotados podem controlar como ela é processada, documentada, versionada, comunicada ou executada sem se tornarem donos da decisão.

Exemplo:

```text
LABOWARE DECIDES
"Todos os projetos devem usar determinado POP."
        ↓
FlowED
orquestra o processo e a adoção da decisão
        ↓
ISO29110-Lite
fornece o modelo documental POP/DOC adotado
        ↓
Dec-B
fornece o modelo de versionamento/SCM adotado
        ↓
InterMembers
pode transportar demandas, decisões, resultados e escalonamentos
        ↓
PROJECT
executa a política concreta
```

Portanto:

```text
DECISION OWNER != PROCESS OWNER != DOCUMENT MODEL OWNER
!= VERSIONING MODEL OWNER != COMMUNICATION MODEL OWNER
```

## 9. Instância não altera produto automaticamente

Experiência de um projeto concreto não modifica diretamente o produto/framework adotado.

Fluxo:

```text
INSTANCE EXPERIENCE
        ↓
CLASSIFY
        ↓
LOCAL DECISION? ------> solve locally
        |
        +-- GENERIC DOMAIN DEFICIENCY
                    ↓
               CHANGE REQUEST
                    ↓
               PRODUCT OWNER
                    ↓
          ACCEPT / REFRAME / DEFER / REJECT
```

Usar um POP do ISO29110-Lite em um projeto não significa desenvolver ISO29110-Lite. O produto só deve receber uma mudança quando a experiência revelar deficiência genérica pertencente ao domínio documental dele.

A mesma regra vale para FlowED, Dec-B, InterMembers e demais produtos appLaboware.

## 10. Fonte operacional atual

Para o ecossistema em desenvolvimento da LaboWare, os repositórios `appLaboware/*` são as fontes operacionais utilizadas.

Origem histórica externa não deve ser tratada por agentes como autoridade corrente, restrição de compatibilidade ou destino automático de sincronização.

Qualquer contribuição futura a outra origem/upstream é uma missão separada, explícita e posterior à maturidade comprovada do ecossistema atual.

## 11. Processo de melhoria de interação

Sempre que uma interação produzir aprendizado reutilizável:

1. Registrar a fricção observada.
2. Identificar quantas iterações foram necessárias e por quê.
3. Separar erro local de deficiência recorrente.
4. Identificar o domínio responsável.
5. Materializar a decisão no nível mais apropriado: policy, POP, DOC, template, prompt, profile, contract ou test.
6. Definir variáveis explícitas; usar `UNKNOWN` em vez de inferência silenciosa.
7. Criar critério de aceitação verificável.
8. Se a execução já for determinística, automatizá-la ou preparar sua automação.
9. Dogfoodar no próximo caso real.
10. Comparar número de interações/retrabalho antes e depois.
11. Promover, revisar ou descartar com evidência.

## 12. Regra de prompt reutilizável

Quando uma missão recorrente puder ser parametrizada:

```text
PROMPT TEMPLATE + VARIABLE TABLE = EXECUTION REQUEST
```

O executor deve receber preferencialmente uma referência estável ao template e somente as variáveis da execução atual.

Toda variável necessária deve possuir valor explícito ou `UNKNOWN`.

O prompt deve distinguir:

- decisões já tomadas;
- ações automatizáveis;
- manual gates;
- condições de parada;
- saída obrigatória;
- próximo ator.

## 13. Escalonamento como mecanismo de economia

Escalonar não é falha quando a decisão ultrapassa o mandato do ator.

É mais eficiente escalar uma ambiguidade real uma vez do que permitir que vários executores tomem decisões divergentes e produzam retrabalho.

Princípio:

```text
ESCALATE UNCERTAINTY.
AUTOMATE CERTAINTY.
DO NOT PAY TWICE FOR THE SAME DECISION.
```

## 14. Métricas candidatas

O FlowED deve evoluir métricas para observar eficiência decisória. Inicialmente:

```text
ITERATIONS_PER_ACCEPTED_RESULT
HUMAN_INTERVENTIONS_PER_WORK_UNIT
MODEL_ESCALATIONS_PER_WORK_UNIT
REWORK_RATE
DECISION_REUSE_RATE
TEMPLATE_REUSE_RATE
DETERMINISTIC_EXECUTION_RATIO
BLOCKERS_CAUSED_BY_MISSING_CONTEXT
TOKENS_PER_ACCEPTED_RESULT          # quando mensurável
COST_PER_ACCEPTED_RESULT            # quando mensurável
```

Métricas não devem incentivar atalhos que reduzam qualidade, evidência ou segurança.

## 15. Relação com Project Genesis

Project Genesis governa como um projeto nasce até poder receber autoridade local. Este protocolo governa como o conhecimento produzido nesse nascimento deve ser comprimido e reutilizado.

Dogfooding ideal:

```text
REAL PROJECT FRICTION
        ↓
FLOWED LEARNS
        ↓
RULE/TEMPLATE/VALIDATOR IMPROVES
        ↓
NEXT PROJECT NEEDS FEWER INTERACTIONS
```

O bootstrap atual do InterMembers é um espécime explícito deste ciclo.

## 16. Relação com documentação e versionamento

Quando o FlowED exigir um artefato concreto, pode adotar:

- formato POP/DOC do ISO29110-Lite para documentação;
- regras do Dec-B para versionamento;
- InterMembers para comunicação;
- adapters/ferramentas adequadas para execução.

Isso é composição de capacidades. A autoridade sobre o conteúdo permanece no domínio que tomou a decisão.

## 17. Regra final

```text
DECIDE ONCE.
MATERIALIZE THE DECISION.
REUSE IT.
VALIDATE IT.
AUTOMATE WHAT BECOMES DETERMINISTIC.
USE EXPENSIVE INTELLIGENCE FOR DECISIONS,
NOT FOR REPETITIVE EXECUTION.
MEASURE HOW MANY INTERACTIONS THE NEXT CASE SAVES.
```
