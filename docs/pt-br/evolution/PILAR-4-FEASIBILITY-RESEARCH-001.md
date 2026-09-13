# Pesquisa de realizabilidade — Pilar 4: Progressividade governada

**Status:** Referência Experimental para fechamento do Pilar 4 do Manifesto FlowED.

## 1. Pergunta de realizabilidade

É tecnicamente plausível que uma capability/prática/processo FlowED comece em uma configuração mínima e aumente, mantenha, reduza ou reverta sua intensidade conforme contexto, risco, evidência e política, sem trocar o modelo mental central nem acoplar o FlowED a uma única implementação?

## 2. Conclusão preliminar

**Sim, com forte plausibilidade técnica.** A ideia não depende de uma tecnologia inédita. Há prior art científico e ferramentas maduras cobrindo quatro responsabilidades complementares:

1. **tailoring/variabilidade de processos** — selecionar e compor variantes conforme contexto;
2. **avaliação contextual por política** — decidir que configuração deve valer em determinado contexto;
3. **ativação progressiva e reversível** — aplicar mudança gradualmente, medir e promover/segurar/reverter;
4. **feedback e adaptação** — observar resultados e realimentar nova decisão.

A contribuição FlowED, se houver, não está em inventar qualquer uma dessas técnicas isoladamente, mas em compor suas propriedades sob um contrato horizontal comum aplicável a múltiplas capabilities de Engenharia de Software.

## 3. Prior art científico e técnico

### 3.1 Software Process Tailoring e Situational Method Engineering

A literatura de software process tailoring parte do fato de que processos genéricos frequentemente precisam ser adaptados ao contexto de uma organização ou projeto. Revisões sistemáticas tratam explicitamente da seleção/adaptação de processos conforme necessidades contextuais.

Isso sustenta a ideia de que uma prática/processo não precisa existir em uma única intensidade/configuração universal.

### 3.2 Software Process Lines (SPrL)

Software Process Lines fornecem um mecanismo sistemático para construir famílias de processos a partir de ativos comuns e pontos de variabilidade. Trabalhos aplicados ao V-Modell XT demonstram variantes de processo, operações explícitas de variabilidade, evolução do metamodelo e aplicação prática ao longo de anos.

Isso é especialmente relevante para FlowED porque mostra que largura/profundidade/configuração podem ser tratadas como variações controladas e deriváveis, em vez de forks manuais desconectados.

### 3.3 EPF / Method Composer

EPF/Method Composer materializou uma ferramenta concreta para selecionar, adaptar e montar processos a partir de blocos reutilizáveis e publicar variantes específicas para diferentes tipos de projeto.

É um exemplo histórico de tecnologia real capaz de materializar tailoring de processos.

### 3.4 OpenFeature / OFREP

OpenFeature define uma API vendor-neutral de avaliação de feature flags com **Evaluation Context**, providers substituíveis, hooks, eventos e requisitos de conformidade. OFREP adiciona um protocolo remoto vendor-neutral para que diferentes sistemas de feature flags implementem a mesma interface.

Propriedades relevantes para FlowED:

- decisão contextual;
- targeting por atributos;
- ativação/desativação sem alterar o consumidor;
- providers substituíveis;
- resposta com reason/variant/metadata;
- protocolo/conformidade verificável.

OpenFeature não resolve sozinho progressividade de processo, mas demonstra uma arquitetura madura para decidir configuração em função de contexto sem lock-in de provider.

### 3.5 Unleash / LaunchDarkly e progressive rollout

Ferramentas de feature management implementam estratégias graduais, percentuais, constraints, segmentos, variantes, schedule e coleta de métricas. A mudança pode ser aplicada a uma pequena população e ampliada depois.

Isso demonstra que progressão de intensidade/exposição baseada em contexto é uma capability executável hoje.

### 3.6 Argo Rollouts / Progressive Delivery

Argo Rollouts materializa progressão controlada com canary/blue-green, passos graduais, consultas a métricas, análise, promoção automática, pausa, julgamento manual e rollback automático quando critérios falham.

Propriedade importante para o Pilar 4: **progressão não precisa ser monotônica**. Um sistema real pode promover, pausar ou reverter com base em evidência observada.

### 3.7 Policy-as-Code — OPA e equivalentes

OPA separa decisão de política da aplicação da decisão. Recebe dados estruturados e políticas declarativas e retorna decisões. Isso fornece um mecanismo pronto para codificar regras como:

- se risco alto, exigir maior intensidade;
- se evidência insuficiente, limitar progressão;
- se custo exceder limiar e risco for baixo, permitir redução;
- se condição de gate não for satisfeita, manter ou reverter.

Cedar e outros policy engines mostram que há alternativas tecnológicas para a mesma classe de responsabilidade.

### 3.8 MAPE-K / Autonomic Computing

A arquitetura MAPE-K organiza adaptação em Monitor → Analyze → Plan → Execute sobre conhecimento compartilhado. Ela demonstra um padrão maduro para feedback adaptativo e uso de políticas para controlar mudanças.

O FlowED não precisa adotar MAPE-K como arquitetura obrigatória, mas ele é um antecedente forte para a ideia de usar observação + análise + política + ação + memória em ciclos de adaptação.

### 3.9 Software Process Improvement (SPI)

A literatura de SPI estuda avaliação de iniciativas de melhoria por métricas, contexto e comparação de resultados. Revisões mostram diversas estratégias de avaliação e também alertam para confounders e descrições contextuais insuficientes.

Isso reforça a necessidade de que qualquer promoção/redução FlowED carregue contexto e evidência, e não seja apenas um número de maturidade desconectado do uso.

## 4. O que o contrato FlowED provavelmente precisará representar

Não fechar sintaxe nesta fase. O horizonte contratual mínimo pode ser descrito semanticamente por:

- **subject/capability/reference** — o que está sendo configurado/progredido;
- **current configuration/state** — configuração/intensidade atual;
- **candidate/target configuration** — configuração proposta;
- **context** — fatos relevantes do projeto/organização/execução;
- **policy/rule set** — regras versionadas que governam a decisão;
- **evidence/metrics** — sinais usados na avaliação;
- **decision** — increase / maintain / reduce / pause / rollback / not-applicable, ou semântica equivalente;
- **scope** — onde/a quem a mudança se aplica;
- **transition strategy** — imediata, gradual, experimental, staged, manual etc.;
- **guards/constraints** — condições que não podem ser violadas;
- **rollback/reversibility information** quando aplicável;
- **reason/decision trace** — por que a decisão foi produzida;
- **effective time/version** — quando e sob qual versão da regra a decisão vale;
- **observed outcome** — resultado posteriormente observado, relacionado à memória operacional do Pilar 2.

O contrato não precisa impor níveis universais como 1–5. Cada capability pode possuir suas próprias configurações/intensidades, desde que a linguagem comum consiga representar estado, contexto, política, decisão e transição.

## 5. Pipeline conceitual de referência

**configuração atual + contexto + evidência + políticas versionadas → decisão de progressão → aplicação limitada/gradual → observação → manter/promover/reduzir/reverter → nova evidência**.

Esse pipeline pode ser materializado hoje por composição de tecnologias existentes.

Uma implementação de referência poderia, por exemplo, usar:

- um modelo de variabilidade/process line para variantes de processo;
- OPA ou outro policy engine para decisão;
- OpenFeature/OFREP ou mecanismo equivalente para resolução contextual e provider substituível;
- Argo Rollouts/feature-management quando houver aplicação gradual mensurável;
- memória operacional do Pilar 2 para observação e evidência;
- MyTrues/EDT/CCP quando amadurecidos para decisão, racional e revisão.

Nenhuma ferramenta sobe como dependência conceitual obrigatória.

## 6. Compatibilidade com os pilares anteriores

O Pilar 4 não pode violar o Pilar 1: progressão deve ser expressa por contrato e permitir providers/materializações substituíveis.

O Pilar 4 usa o Pilar 2: mudanças precisam produzir memória operacional e resultados observáveis para que o ciclo seja realimentado.

O Pilar 4 usa o Pilar 3: decisões de aumentar/manter/reduzir devem poder consumir evidência e regras explícitas, sem confundir score com verdade.

Assim, a progressividade é **cumulativa com os pilares anteriores**, não um mecanismo paralelo que os contorna.

## 7. O que é e o que não é progressividade FlowED

Progressividade FlowED não deve significar uma escada universal de maturidade na qual mais é sempre melhor.

Ela deve significar que a configuração aplicada a uma capability pode variar conscientemente com o contexto e ser alterada por regras explícitas e evidência. Isso inclui redução de intensidade quando o contexto justificar.

Portanto:

- mais rigor não é automaticamente melhor;
- menos rigor não é automaticamente imaturidade;
- progressão não é obrigatoriamente monotônica;
- a decisão precisa ser contextual, rastreável e reversível quando aplicável.

## 8. Formulação candidata para o manifesto

> **O FlowED permite que a forma de trabalhar varie e evolua de maneira governada conforme contexto, risco, evidência e necessidade. Aumentar, manter, reduzir ou reverter intensidade deve ser uma decisão explícita e rastreável, sem transformar complexidade máxima em sinônimo de maturidade.**

## 9. Avaliação pelo gate de realizabilidade

### Coerência conceitual

Alta. O pilar operacionaliza a promessa histórica de crescimento progressivo sem burocracia proporcional.

### Prior art

Forte: process tailoring, Situational Method Engineering, Software Process Lines, Software Process Improvement, autonomic/self-adaptive systems e progressive delivery.

### Tecnologia no horizonte

Forte: EPF/Method Composer e V-Modell XT como exemplos de tailoring/process variants; OpenFeature/OFREP e feature-management systems para resolução contextual e progressão; OPA/Cedar para policy decisions; Argo Rollouts e equivalentes para aplicação gradual/rollback; observabilidade e memória do Pilar 2 para feedback.

### Contrato previsível

Sim. Já é possível prever semanticamente estado/configuração atual, contexto, políticas, evidência, decisão, transição, guards, rollback e resultado sem escolher sintaxe definitiva.

### Risco residual

O principal residual não é viabilidade tecnológica, mas governança e modelagem:

- como definir intensidade por capability sem impor escala artificial;
- quais sinais autorizam increase/reduce;
- como tratar conflitos entre políticas;
- como distinguir recomendação automática de decisão autorizada;
- como avaliar custo/benefício da progressão;
- quando rollback é tecnicamente impossível ou semanticamente inadequado.

Esses gaps podem permanecer como pesquisa posterior se o manifesto limitar sua claim à progressão governável e rastreável.

## 10. Estado

**Realizabilidade:** fortemente plausível / suficiente para debate de fechamento do manifesto.

**Rota:** ADOPT/COMPOSE. Não inventar tailoring, feature evaluation, policy-as-code, progressive rollout ou adaptive feedback. O eventual residual FlowED está na linguagem/contrato transversal que permite aplicar essas propriedades a capabilities heterogêneas de Engenharia de Software.
