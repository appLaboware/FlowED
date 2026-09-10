# Pré-manifesto — princípios que o Manifesto FlowED deve refletir

**Status:** rascunho de trabalho. Não normativo. Serve para registrar, antes da reorganização dos pilares, quais princípios centrais o manifesto deve fazer um leitor compreender.

A intenção deste documento não é definir tecnologia, produto, provider ou implementação. Também não é reivindicar ineditismo filosófico. O FlowED parte de princípios já presentes em ciência, padrões e prática de engenharia e propõe dar a alguns deles prioridade transversal diferente.

## PR-M01 — Princípio da Separação entre Intenção e Materialização

### Frases nucleares

> **Separar intenção de materialização torna possível avaliar separadamente a qualidade do que foi decidido e a qualidade de como aquilo foi realizado.**

> **Quando o conhecimento conceitual é acumulado independentemente da ferramenta que o materializa, a evolução tecnológica tende a exigir menos readaptação.**

> **Quando intenção e materialização são tratadas como competências distintas, cada uma pode ser aprofundada segundo suas próprias demandas de decisão e conhecimento técnico, e suas excelências podem ser combinadas sem pressupor que coexistam na mesma pessoa ou no mesmo momento.**

> **Quando iniciantes e especialistas compartilham a mesma linguagem de intenção, ensino e aprendizagem podem se tornar mais cumulativos: cresce a profundidade, o vocabulário e a precisão sem exigir a substituição da linguagem operacional.**

> **Quando a primeira linguagem operacional aprendida permanece válida ao longo da evolução profissional, novos conhecimentos tendem a se acumular por extensão e refinamento, reduzindo a necessidade de substituir a base e favorecendo seu aprofundamento.**

### O que este princípio quer fazer o leitor compreender

A Engenharia de Software já conhece a separação entre intenção e implementação. O FlowED propõe elevar essa separação a uma prioridade operacional transversal.

A intenção deve ser tratada como a superfície operacional mais estável. Ferramentas, frameworks, plataformas, providers, adapters e outras materializações podem mudar com maior frequência sem obrigar quem expressa uma intenção ainda válida a reaprender como trabalhar.

Os materializadores devem adaptar-se à linguagem da intenção sempre que possível, em vez de obrigar todos os executores a reaprender a linguagem particular de cada materializador.

O custo de adaptação à mudança tecnológica deve, sempre que possível, concentrar-se na fronteira de materialização. Conhecimento especializado de materialização pode ser encapsulado e reutilizado, enquanto quem busca um resultado continua exprimindo a intenção e suas restrições conceituais.

Não se separam necessariamente pessoas. Separam-se decisões e momentos decisórios. Uma mesma pessoa pode, em momentos diferentes, definir intenção, estabelecer políticas e restrições, especializar uma materialização e executar uma intenção.

A separação também permite reconhecer que formular boas intenções e materializá-las bem envolvem competências parcialmente distintas. O primeiro trabalho tende a concentrar-se mais em objetivos, restrições, contexto, trade-offs e qualidade da decisão; o segundo, em conhecimento técnico profundo sobre mecanismos, tecnologias, limites e maneiras de realizar essas decisões. O FlowED não presume que isso corresponda a personalidades fixas ou a tipos cognitivos rígidos. A hipótese relevante é que separar os trabalhos permite aprofundá-los segundo suas demandas próprias e depois recombinar suas excelências.

Uma pessoa, equipe ou momento decisório pode ser forte em uma dimensão e menos forte em outra. O objetivo não é criar castas profissionais rígidas, mas permitir que competências de intenção e de materialização sejam desenvolvidas, avaliadas e combinadas separadamente.

A mudança de ferramenta pode continuar exigindo adaptação, aprendizado e especialização. O FlowED não propõe eliminar esse efeito. Propõe reduzir quanto dessa mudança precisa atingir quem continua expressando a mesma intenção ou trabalhando com o mesmo conhecimento conceitual.

Quando intenção e materialização são separadas, o aprendizado acumulado sobre objetivos, restrições, decisões e estruturas do problema pode sobreviver melhor à substituição de tecnologias concretas. A parte volátil da mudança pode concentrar-se, tanto quanto o domínio permitir, na fronteira de materialização.

A consequência desejada não é ausência de reaprendizado, mas **menor ruptura**: aquilo que continuou conceitualmente válido não deveria ser descartado apenas porque mudou a ferramenta que o realiza.

Compartilhar a mesma linguagem de intenção entre níveis de experiência não significa exigir a mesma profundidade, o mesmo repertório ou a mesma autonomia de um iniciante e de um especialista. Significa preservar uma base semântica comum sobre a qual a competência possa crescer. O iniciante pode operar com um vocabulário menor e com mais defaults e orientação; o especialista pode usar intenções mais compostas, parâmetros mais ricos, restrições mais precisas e maior consciência de trade-offs sem precisar migrar para outra linguagem operacional.

Há também uma dimensão temporal: a linguagem encontrada no início da formação não precisa ser tratada como uma linguagem provisória destinada ao descarte. Quando continua semanticamente válida, ela pode servir de base para a progressão posterior. O crescimento desejado ocorre pela ampliação do repertório, pelo refinamento das intenções e pelo aumento da precisão, reduzindo a necessidade de substituir recorrentemente a base operacional.

Assim, a progressão de aprendizado desejada é por **ampliação e aprofundamento**, não por descarte sucessivo da linguagem anterior. A hipótese de que isso torne ensinar ou aprender efetivamente mais fácil, rápido ou eficiente deve ser validada empiricamente; o compromisso constitutivo é permitir continuidade semântica entre níveis de experiência e ao longo da trajetória.

### Consequências esperadas deste princípio

Estas consequências explicam as frases nucleares, mas não são ainda claims independentes do manifesto:

- preservar uma superfície operacional mais duradoura apesar da mudança tecnológica;
- reduzir reaprendizado de procedimentos incidentais quando a intenção continua válida;
- tornar mais claro se um resultado ruim decorreu da intenção, da política, da materialização ou da execução;
- permitir comparar múltiplas materializações de uma mesma intenção sem misturar automaticamente qualidade da intenção com qualidade da ferramenta;
- permitir que conhecimento especializado em materialização seja reaproveitado por muitos usuários através de fronteiras reutilizáveis;
- permitir que competências de intenção e de materialização sejam aprofundadas segundo demandas próprias e compostas sem exigir que a mesma pessoa domine ambas no mesmo grau;
- ampliar o espaço para especialistas predominantemente orientados à decisão e especialistas predominantemente orientados à materialização contribuírem no mesmo sistema;
- permitir crescimento progressivo do vocabulário de intenção sem exigir ruptura completa da forma de expressão a cada nova ferramenta;
- permitir continuidade semântica entre aprendizado inicial e prática especializada, com aumento de profundidade em vez de troca de linguagem;
- permitir que a primeira linguagem operacional continue útil como base de crescimento, reduzindo a necessidade de substituí-la quando seu significado permanece válido;
- facilitar continuidade entre aprendizado inicial e uso profissional de maior escala;
- reduzir o impacto da evolução tecnológica sobre conhecimento conceitual que permaneceu válido.

### Limites e hipóteses ainda abertas

O manifesto não deve afirmar, sem evidência própria, que esta separação automaticamente torna alguém sênior mais rápido, reduz universalmente carga cognitiva, melhora necessariamente a qualidade do software ou elimina a necessidade de especialistas conhecerem tecnologias concretas.

A hipótese de que especialização separada em intenção e materialização, quando bem coordenada, aumente a probabilidade de melhores resultados é plausível e testável, mas não deve ser promovida a verdade constitutiva antes de evidência. A separação também pode introduzir custos de coordenação, perda de contexto ou fronteiras mal desenhadas; esses efeitos precisam permanecer visíveis.

Também permanece aberta a hipótese de que os dois tipos de trabalho recrutem, em média, perfis cognitivos, preferências ou traços diferentes. O FlowED não precisa dessa hipótese psicológica para sustentar o princípio: basta reconhecer que as tarefas têm ênfases de competência diferentes e podem ser desenvolvidas separadamente.

A hipótese de que uma linguagem de intenção compartilhada entre iniciantes e especialistas torne ensino, aprendizagem ou progressão profissional mais rápidos ou eficientes também deve permanecer testável. O princípio pode exigir continuidade semântica sem antecipar a magnitude dos benefícios educacionais.

A permanência da primeira linguagem operacional também não é defendida por apego histórico. Ela só deve continuar como base enquanto seu significado permanecer adequado; quando a própria intenção evoluir ou se mostrar insuficiente, a linguagem deve poder evoluir de forma explícita e versionada.

Esses efeitos são hipóteses empiricamente testáveis e podem tornar-se linhas de pesquisa. O compromisso filosófico anterior a essas hipóteses é a separação entre qualidade da decisão intencional e qualidade de sua materialização, acompanhada da preservação do conhecimento conceitual diante da volatilidade tecnológica.

Também não se assume que intenção seja imutável. Novas intenções podem surgir e intenções existentes podem evoluir. A prioridade é preservar estabilidade relativa quando o significado da intenção permanece válido.

### Relação com o produto FlowED

`flwd` é apenas uma materialização de referência desta visão. Deve poder ser substituído por qualquer outro cliente ou produto que respeite os mesmos princípios e contratos.

O produto existe para demonstrar e facilitar a filosofia; não define a filosofia nem recebe privilégio normativo por ter sido produzido pelos autores do FlowED.

## PR-M02 — Princípio da Coerência Operacional

**Nome provisório.** A expressão "identidade operacional" é tratada aqui como efeito percebido da coerência, e não como obrigação de uniformidade.

### Frases nucleares candidatas

> **Quando decisões, práticas e ferramentas de diferentes domínios compartilham princípios e contratos transversais, a forma de trabalhar da organização tende a se tornar mais coerente e reconhecível.**

> **Uma organização pode preservar uma identidade operacional reconhecível mesmo quando suas ferramentas mudam, quando essa identidade reside nos princípios, intenções e contratos que governam seu uso, e não nas implementações específicas.**

> **Quando identidade intencional e materialização permanecem separadas, cada uma pode ser apresentada, avaliada e modificada em seu próprio momento.**

> **Trocar uma tecnologia não precisa significar abandonar a forma de pensar; mudar a forma de pensar não precisa exigir trocar toda tecnologia que ainda a satisfaz.**

### O que este princípio quer fazer o leitor compreender

Escolhas locais podem ser tecnicamente excelentes e ainda assim produzir, em conjunto, uma experiência organizacional fragmentada. Quando cada domínio adota sua própria linguagem, seus próprios critérios de decisão e sua própria forma de interação sem uma camada transversal comum, torna-se mais difícil perceber "como esta organização trabalha" como um todo.

O FlowED não propõe uniformizar internamente todos os domínios nem obrigar todas as ferramentas a partilhar a mesma arquitetura, tecnologia ou método. A coerência desejada ocorre na superfície pública: princípios, intenções, contratos, rastreabilidade e regras de composição podem ser comuns, enquanto cada domínio continua soberano em sua materialização.

Nesse sentido, identidade operacional não significa usar as mesmas ferramentas. Significa que escolhas diferentes continuam reconhecíveis como parte de uma mesma forma de trabalhar porque obedecem a compromissos transversais compartilhados.

Uma consequência esperada é que a organização possa substituir ferramentas, providers ou materializadores sem perder necessariamente a continuidade daquilo que a caracteriza operacionalmente. A identidade pode sobreviver à troca de tecnologia quando não está acoplada a ela.

Uma superfície intencional comum pode unificar a expressão da forma de pensar da organização sem unificar as ferramentas que a realizam. Isso permite que intenção e materialização sejam apresentadas e julgadas separadamente e que cada uma evolua em seu próprio momento, desde que permaneçam compatíveis com os contratos aplicáveis.

### Distinção em relação ao PR-M01

O PR-M01 trata da separação entre intenção e materialização e dos efeitos dessa separação sobre avaliação, aprendizagem, especialização e adaptação tecnológica.

O PR-M02 trata de outra propriedade: **a coerência transversal entre decisões locais de diferentes domínios**. Ele pergunta se uma organização consegue manter uma forma de trabalhar reconhecível mesmo quando suas capacidades são materializadas por ferramentas distintas.

## PR-M03 — Princípio do Foco no Caminho Cognitivo

**Nome provisoriamente adotado.** Pode ser substituído se surgir formulação mais precisa e igualmente direta.

### Frases nucleares — aceitas

> **O caminho cognitivo estruturado deve constituir a base primária do conhecimento normativo. Todo consolidado deve ser tratado como uma projeção contextual dessa base.**

> **O consolidado estabiliza uma decisão; o caminho cognitivo preserva o conhecimento que permite compreendê-la, retomá-la e fazê-la evoluir.**

### O que este princípio quer fazer o leitor compreender

O conhecimento normativo não deve ter como centro apenas sua formulação consolidada. O caminho cognitivo estruturado que produziu essa formulação deve ocupar a posição de base primária; normas, resumos, explicações e outras formas consolidadas são projeções de acesso, leitura e ação.

O consolidado continua útil por reduzir a quantidade de informação apresentada, mas sua conveniência não deve transformá-lo na própria fonte do conhecimento. O caminho cognitivo não deve aparecer apenas como anexo da norma; a norma deve ser tratada como projeção compacta e contextual da base cognitiva que a sustenta.

As consequências ainda estão em exploração. Entre elas estão a retenção de conhecimento produzido por pessoas que depois deixam uma organização, a continuidade de artefatos por novos mantenedores, a redução da dependência de uma única capacidade de síntese e a distinção entre a cognição de origem e interpretações produzidas posteriormente sobre seus consolidados.

Uma consequência já identificada é que, quando o caminho cognitivo é estruturado, consolidados podem tornar-se dinâmicos: diferentes contextos podem receber diferentes sínteses sem transformar cada síntese em uma nova fonte independente de conhecimento.
