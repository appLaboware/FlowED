# Meta-tese do Manifesto — prioridade da intenção sobre a volatilidade da materialização

**Status:** hipótese conceitual para revisão do Manifesto FlowED. Não normativa. Deve orientar a próxima reescrita do manifesto, mas ainda está em debate.

## 1. Ponto de partida

O Manifesto FlowED não deve ser apresentado como se estivesse inventando isoladamente conceitos como intenção declarativa, desired state, separação entre objetivo e mecanismo, policy versus mechanism, abstração, interoperabilidade ou automação orientada por intent.

Essas ideias possuem antecedentes fortes na engenharia e em sistemas reais. O valor candidato do manifesto está em **dar prioridade normativa, organizar e combinar essas ideias em torno de uma experiência operacional comum para a Engenharia de Software**.

A analogia de referência é o Manifesto Ágil: sua força não dependeu de afirmar que cada valor era inédito, mas de declarar explicitamente uma redistribuição de peso entre valores já conhecidos e levá-la a consequências práticas.

## 2. Formulação candidata da meta-tese

> **A intenção deve ser a superfície operacional mais estável do sistema; materializações podem mudar com muito maior frequência sem obrigar o usuário a reaprender a intenção.**

A proposta do FlowED não é congelar intenções para sempre. Novas intenções podem surgir e intenções existentes podem evoluir. A claim é relativa: **a linguagem da intenção deve ser mais estável que as tecnologias usadas para materializá-la**.

## 3. O problema que o manifesto pretende reponderar

Na prática da Engenharia de Software, troca de tecnologia frequentemente força troca de superfície operacional: novos CLIs, novas APIs, novos workflows, novos nomes, novas estruturas de projeto, novas formas de deployment e novas convenções.

Isso faz com que parte significativa do aprendizado seja consumida pela volatilidade da ferramenta, embora a intenção subjacente muitas vezes permaneça semelhante: iniciar projeto, executar teste, publicar software, implantar, observar, reverter, registrar decisão, criar artefato etc.

O manifesto deve propor uma mudança de peso:

- dar mais peso à **intenção** que à sintaxe da ferramenta;
- dar mais peso ao **significado público** que ao procedimento de uma implementação;
- dar mais peso ao **contrato interoperável** que ao domínio de uma ferramenta específica;
- permitir que conhecimento especializado sobre materialização seja concentrado em quem governa/configura a organização e em materializadores/adapters, sem obrigar todo executor a reaprender esse conhecimento incidental.

## 4. Ancestrais e evidência de realizabilidade

### 4.1 Intent-Based Systems

RFC 9315 define intent como objetivos operacionais e resultados declarados sem especificar como atingi-los. O mesmo trabalho enfatiza abstração de dados e de lógica de controle, permitindo que o usuário se concentre no resultado desejado enquanto o sistema resolve como alcançá-lo.

RFC 9316 descreve sistemas com interface para entrada de intent e engine para tradução/materialização. O documento também registra características recorrentes das abordagens de intent: natureza declarativa, independência de fornecedor, interface simplificada e resolução/gestão de conflitos.

Particularmente relevante para o FlowED, RFC 9316 reconhece que stakeholders diferentes exigem níveis diferentes de exposição técnica: alguns precisam de detalhes; outros devem ser protegidos de conceitos e tecnologias que não são pertinentes à sua função.

A abstração proposta no RFC 9316 por **Context + Capabilities + Constraints** é um antecedente importante para futuras discussões sobre granularidade da intenção FlowED, sem que deva ser copiada automaticamente como modelo final.

### 4.2 Sistemas declarativos

Kubernetes demonstra em escala industrial que uma API declarativa pode separar responsabilidade: o usuário declara estado desejado e controllers procuram reconciliar o estado atual com o desejado, podendo evoluir independentemente da interface declarativa.

Esse antecedente reforça que a estabilidade relativa da superfície desejada em relação aos mecanismos internos é tecnologicamente realizável.

## 5. Executor e governança — separação conceitual, não de cargo

A comparação informal entre "executor" e "legislador" ajuda a revelar duas responsabilidades, mas não deve necessariamente criar dois cargos ou papéis obrigatórios.

A mesma pessoa pode exercer ambas em equipes pequenas.

Conceitualmente:

- **execução:** expressa a intenção e os parâmetros/contextos que realmente pertencem ao seu objetivo;
- **governança:** define políticas, restrições, defaults, materializadores permitidos, requisitos de segurança, risco e organização;
- **sistema FlowED:** resolve intenção + contexto + políticas + contratos;
- **materialização:** executa a solução concreta por meio de uma tecnologia conformante.

## 6. Limite importante: abstração não é ignorância forçada

O manifesto não deve afirmar que profissionais nunca precisam aprender ferramentas ou mecanismos.

Conhecimento de implementação continua necessário quando é semanticamente relevante para a função, para segurança, para diagnóstico, para arquitetura, para custo, para performance, para compliance ou para governança.

A claim mais defensável é:

> **um usuário não deve ser obrigado a reaprender a superfície operacional apenas porque mudou um detalhe de materialização que não altera a intenção nem as garantias relevantes para sua responsabilidade.**

O FlowED procura esconder **volatilidade incidental**, não conhecimento conceitual necessário.

## 7. Determinismo — formulação cautelosa

A tradução de uma intenção deve ser governada e rastreável.

Quando o contrato declarar comportamento determinístico, a mesma intenção canônica, com o mesmo contexto relevante, políticas, versões e capabilities, deve produzir a mesma interpretação e decisão de materialização.

O manifesto não deve prometer determinismo físico universal: providers podem falhar, dependências externas podem mudar e algumas decisões podem ser legitimamente não determinísticas.

O princípio geral deve ser **resolução governada, explicável e reproduzível dentro das garantias declaradas pelo contrato**.

## 8. Hipótese de contribuição do Manifesto FlowED

A contribuição pretendida não é "inventar intent".

A hipótese de contribuição é mais próxima de:

> **elevar a intenção a principal superfície operacional da Engenharia de Software, tratá-la como vocabulário relativamente estável entre domínios e maturidades e exigir que materializações concorrentes se adaptem a contratos públicos comuns, em vez de exigir que cada profissional reaprenda a linguagem de cada materialização.**

Essa hipótese ainda precisa de revisão de anterioridade antes de qualquer reivindicação científica de novidade.

## 9. Consequência editorial para o manifesto

O manifesto deve demonstrar humildade de origem e firmeza de prioridade.

Uma formulação candidata para o preâmbulo:

> **Muitas das ideias que sustentam o FlowED já existem na ciência, nos padrões e na prática da engenharia. Não reivindicamos tê-las inventado. Propomos atribuir a elas uma ordem de importância: a intenção deve permanecer mais estável que sua materialização; contratos comuns devem pesar mais que dependência de ferramenta; aprendizado acumulado deve sobreviver à troca tecnológica; e a evolução da forma de trabalhar deve ser governada por contexto e evidência.**

A força do manifesto deve vir dessa distribuição de peso e de suas consequências operacionais, não de uma narrativa artificial de ruptura com todo o conhecimento anterior.

## 10. Impacto nos pilares

Se essa meta-tese sobreviver à crítica, os quatro pilares podem ser lidos como consequências:

1. **Unidade operacional e liberdade governada** — a intenção e o contrato permanecem estáveis; materializações variam.
2. **Autoeducação e conhecimento vivo** — o conhecimento acumulado não deve morrer quando a materialização muda.
3. **Sustentação explícita** — escolhas de intenção, política e materialização devem poder carregar sua sustentação e autoria de avaliações.
4. **Progressividade governada** — contexto e maturidade podem alterar a materialização e o rigor sem exigir nova linguagem operacional para a mesma intenção.

## 11. Gap principal a seguir

Antes de promover a meta-tese ao manifesto, deve-se testar a **granularidade da intenção**:

- o que pertence à intenção;
- o que pertence ao contexto;
- o que pertence a constraints;
- o que pertence à política organizacional;
- o que é apenas preferência de materialização.

Exemplo a investigar futuramente: em "criar projeto Java com Spring Boot e PostgreSQL", quais elementos representam intenção estável e quais representam contexto, constraint, política ou escolha de materializador?
