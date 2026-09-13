# Intent-first, aprendizagem e separação da materialização — rascunho

**Status:** hipótese conceitual para refinamento do Manifesto FlowED. Não normativa. Não declara ineditismo científico.

## 1. Meta-posicionamento do manifesto

O FlowED não precisa reivindicar ter inventado as ideias que sustenta. A hipótese é que muitas — possivelmente a maior parte — já existam na ciência, em RFCs, padrões, sistemas e boas práticas de engenharia.

A contribuição pretendida do manifesto é atribuir uma **ordem de importância** e uma **prioridade operacional transversal** a princípios que hoje aparecem distribuídos e muitas vezes confinados a domínios específicos.

Formulação de trabalho:

> **A engenharia já sabe separar intenção de implementação. O FlowED propõe tratar essa separação como uma prioridade operacional transversal da Engenharia de Software.**

O RFC 9315 é um ancestral particularmente forte: define intent como objetivos/resultados operacionais declarativos sem especificar como alcançá-los e defende que o sistema absorva detalhes de realização. O RFC 9316 complementa com intent user, policy, níveis de abstração, contexto, capabilities e constraints.

O FlowED deve apresentar esses antecedentes como sustentação, não como obstáculos à sua identidade: a proposta é dar a esses princípios uma centralidade maior na organização cotidiana da Engenharia de Software.

## 2. Primeira tese de valor: intenção estável, materialização volátil

A intenção deve ser a superfície operacional mais estável do sistema. Tecnologias, frameworks, providers, ferramentas e procedimentos podem mudar com frequência muito maior.

Quando a intenção continua válida, a mudança da tecnologia que a realiza não deveria, por si só, obrigar quem a expressa a reaprender como trabalhar.

Formulações candidatas curtas para manifesto:

> **Quando a intenção permanece, mudar a tecnologia não deveria exigir reaprender a operação.**

> **Quando a intenção permanece válida, a volatilidade tecnológica deve ser absorvida, sempre que possível, na fronteira de materialização.**

> **Aprender uma materialização melhor não deveria obrigar a organização a ensinar novamente uma intenção que continuou sendo a mesma.**

Consequência operacional:

> **Os materializadores é que devem aprender a língua da intenção.**

Efeito pretendido:

> **O custo de adaptação à mudança tecnológica deve, sempre que possível, ser transferido de todos os executores para a fronteira de materialização.**

Isso não significa impedir o aprendizado de tecnologias. Especialistas continuarão precisando conhecer profundamente os mecanismos sob sua responsabilidade. Significa evitar que detalhes incidentais de uma implementação se tornem pré-requisito universal para expressar um objetivo já compreendido.

## 3. Separar decisões, não necessariamente pessoas

FlowED não precisa impor cargos ou separação organizacional rígida. A distinção é entre **momentos e responsabilidades decisórias**.

Três esferas conceituais são úteis:

1. **Intenção** — qual resultado se deseja e quais restrições pertencem verdadeiramente ao resultado;
2. **Governança/política** — quais escolhas, limites, padrões, riscos e providers são permitidos ou preferidos naquele contexto;
3. **Materialização** — como uma implementação concreta realiza o resultado dentro do contrato e das políticas vigentes.

Uma única pessoa pode exercer as três responsabilidades em momentos diferentes. Em organizações maiores, elas podem pertencer a pessoas ou equipes diferentes.

A separação de policy e mechanism possui longa tradição em sistemas computacionais. O ponto do FlowED é aplicar uma separação análoga de maneira consciente ao ciclo operacional da Engenharia de Software, sem confundir a analogia com identidade conceitual perfeita.

## 4. Linguagem da intenção

A intenção não precisa ser uma frase pobre ou um verbo isolado. Pode conter parâmetros, qualificadores, restrições, escopo, critérios de resultado e relações com outras intenções.

A linguagem deve, porém, evitar elevar prematuramente detalhes contingentes da solução a componentes da intenção.

Exemplo conceitual:

- “quero uma linha estável entregue ao cliente, uma linha de desenvolvimento e uma linha isolada de validação” expressa um objetivo estrutural;
- “use três branches Git” pode ser uma política, uma restrição legítima ou apenas uma materialização, dependendo do motivo pelo qual a exigência existe.

A classificação é semântica e contextual, não lexical. `Java`, `Spring`, `PostgreSQL`, `branch`, `container` e outros termos podem ser intenção/restrição, policy ou materialização conforme o problema que representam.

## 5. Conhecimento conceitual e conhecimento incidental

O FlowED deve favorecer o aprendizado do significado conceitual de uma intenção antes de exigir domínio da ferramenta contingente que a materializa.

Isso encontra sustentação indireta em pesquisa sobre expertise. Estudos clássicos mostram que especialistas não possuem apenas mais informação: organizam o conhecimento em estruturas mais significativas e tendem a representar problemas por princípios/estruturas profundas, enquanto novatos tendem a apoiar-se mais em características superficiais. Pesquisas de Cognitive Load Theory mostram também que reduzir carga extrínseca pode tornar a aprendizagem de novatos mais eficiente.

Entretanto, o FlowED **não deve afirmar como fato** que o gap aprendiz→sênior é prioritariamente conhecimento de ferramenta. Essa hipótese é forte demais. Expertise envolve organização de conhecimento, julgamento contextual, reconhecimento de padrões, trade-offs, experiência, conhecimento tácito, comunicação e outras capacidades.

Hipótese mais defensável:

> **Separar intenção de materialização pode reduzir uma parcela incidental da carga de aprendizagem e da ruptura tecnológica, permitindo que o aprendiz invista mais atenção no significado, na estrutura do problema e na qualidade das decisões.**

Essa hipótese é candidata a validação empírica futura; não deve ser promovida a verdade do manifesto sem evidência específica.

## 6. Continuidade aprendiz → especialista

O FlowED pode defender continuidade sem afirmar equivalência entre aprendiz e sênior.

O aprendiz e o especialista podem expressar a mesma classe de intenção porque compartilham a mesma linguagem operacional. O crescimento passa a ocorrer por maior vocabulário, melhores restrições, melhor composição de intenções, melhor leitura de contexto e melhor julgamento — não obrigatoriamente por ruptura completa da superfície operacional a cada mudança tecnológica.

Formulação candidata:

> **Quando a linguagem da intenção permanece, o crescimento de competência pode ser acumulativo em vez de repetidamente reiniciado pela troca de ferramenta.**

Isso é compatível com a ideia de conhecimento progressivo: a frase curta permanece compreensível; contexto, racional, políticas, evidências e detalhes podem ser aprofundados conforme papel, necessidade e maturidade.

## 7. Materializadores como concentração de conhecimento técnico

Um adapter/provider pode encapsular experiência técnica acumulada sobre como materializar uma classe de intenção em determinada tecnologia e contexto.

Isso permite que o conhecimento de um especialista seja reutilizado por muitos executores sem exigir que todos tenham o mesmo nível de especialização na ferramenta concreta.

O especialista em materialização continua tomando decisões técnicas dentro de seu espaço de responsabilidade. Portanto, a frase “quem materializa não precisa tomar boas decisões” deve ser rejeitada. O correto é:

> **quem materializa não precisa decidir novamente a intenção do usuário; deve tomar boas decisões de implementação dentro dos limites da intenção, do contrato e das políticas.**

## 8. Separação melhora observabilidade do erro, mas não produz causalidade perfeita

Manter uma intenção constante e variar materializadores cria um desenho muito melhor para comparação, conformance, benchmarking e aprendizagem.

Conceitualmente:

**mesma intenção + mesmo contexto relevante + políticas controladas → materializador A | B | C → resultados comparáveis**

Isso ajuda a distinguir falhas de intenção de falhas de materialização e pode tornar oportunidades de melhoria mais observáveis.

Entretanto, não se deve afirmar que a separação identifica automaticamente “a culpa”. Há interações entre intenção, contexto, policy, capabilities e provider. A separação aumenta a capacidade de diagnóstico e controle experimental; não elimina causalidade complexa.

A ideia de executar a mesma intenção contra múltiplos materializadores é uma hipótese particularmente promissora para experimentação futura e dogfood do FlowED.

## 9. Limite do determinismo

A materialização deve ser sistemática e previsível na maior extensão possível, mas “todo materializador é determinístico” seria uma promessa excessiva.

O que o contrato pode exigir com mais segurança é determinismo da resolução quando aplicável:

**mesma intenção canônica + mesmos parâmetros/restrições + mesmo contexto relevante + mesmas políticas/versionamento + mesmas capabilities declaradas → mesma interpretação e mesma decisão de resolução**, quando a capability declarar comportamento determinístico.

Falhas externas, ambientes mutáveis, concorrência e operações inerentemente não determinísticas podem alterar resultados físicos sem tornar a linguagem de intenção ambígua.

Quando julgamento humano especializado ainda for necessário, o sistema deve escalar essa necessidade em vez de inventar silenciosamente uma decisão.

## 10. Papel do produto FlowED / `flwd`

O produto oficial não é a filosofia.

`flwd` é uma implementação de referência da linguagem e dos contratos defendidos pelo manifesto. Deve servir para provar realizabilidade, dogfood e oferecer um ponto de partida prático, mas é totalmente substituível por qualquer cliente ou ecossistema que cumpra os mesmos princípios e contratos.

A ferramenta existe para exemplificar o manifesto; o manifesto não existe para justificar a ferramenta.

## 11. Relação com os pilares atuais

Esta tese parece estar acima da distribuição atual em quatro pilares e deverá orientar uma futura redistribuição:

- o atual Pilar 1 fornece a linguagem comum, contratos e liberdade de materialização;
- o atual Pilar 2 permite aprender com os resultados sem exigir reensinar a intenção;
- o atual Pilar 3 torna visível a sustentação das decisões e opiniões usadas;
- o atual Pilar 4 permite trocar políticas, intensidade e materializadores sem romper a superfície intencional.

Portanto, a estabilidade da intenção pode ser causa estrutural da redução de complexidade operacional pretendida pelo FlowED, não apenas mais uma propriedade lateral.

## 12. Linguagem de causa e efeito para o manifesto

Evitar copiar a fórmula “valorizamos X mais que Y” do Manifesto Ágil. Preferir afirmações compactas do tipo condição → consequência desejada.

Candidatas:

> **Quando a intenção permanece, mudar a tecnologia não deveria exigir reaprender a operação.**

> **Quando intenção e materialização são decididas separadamente, a evolução da tecnologia pode ocorrer sem apagar o conhecimento operacional já adquirido.**

> **Quando especialistas concentram conhecimento de materialização em providers substituíveis, mais pessoas podem executar uma intenção sem repetir o mesmo custo de especialização.**

> **Quando o mesmo pedido pode ser materializado por tecnologias diferentes, comparar resultados e localizar fragilidades torna-se mais fácil.**

> **Quando o aprendizado altera a materialização e não a intenção, quem executa pode continuar trabalhando enquanto a organização evolui por baixo da mesma linguagem.**

Essas frases são hipóteses normativas/causais do manifesto e deverão ser refinadas e sustentadas individualmente antes da versão definitiva.
