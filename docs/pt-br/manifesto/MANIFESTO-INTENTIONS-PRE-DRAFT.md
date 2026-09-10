# Pré-manifesto — princípios que o Manifesto FlowED deve refletir

**Status:** rascunho de trabalho. Não normativo. Serve para registrar, antes da reorganização dos pilares, quais princípios centrais o manifesto deve fazer um leitor compreender.

A intenção deste documento não é definir tecnologia, produto, provider ou implementação. Também não é reivindicar ineditismo filosófico. O FlowED parte de princípios já presentes em ciência, padrões e prática de engenharia e propõe dar a alguns deles prioridade transversal diferente.

## PR-M01 — Princípio da Separação entre Intenção e Materialização

### Frases nucleares

> **Separar intenção de materialização torna possível avaliar separadamente a qualidade do que foi decidido e a qualidade de como aquilo foi realizado.**

> **Quando o conhecimento conceitual é acumulado independentemente da ferramenta que o materializa, a evolução tecnológica tende a exigir menos readaptação.**

> **Separar intenção de materialização permite desenvolver e combinar excelência na decisão e excelência na realização sem pressupor que ambas coincidam na mesma pessoa ou no mesmo momento.**

### O que este princípio quer fazer o leitor compreender

A Engenharia de Software já conhece a separação entre intenção e implementação. O FlowED propõe elevar essa separação a uma prioridade operacional transversal.

A intenção deve ser tratada como a superfície operacional mais estável. Ferramentas, frameworks, plataformas, providers, adapters e outras materializações podem mudar com maior frequência sem obrigar quem expressa uma intenção ainda válida a reaprender como trabalhar.

Os materializadores devem adaptar-se à linguagem da intenção sempre que possível, em vez de obrigar todos os executores a reaprender a linguagem particular de cada materializador.

O custo de adaptação à mudança tecnológica deve, sempre que possível, concentrar-se na fronteira de materialização. Conhecimento especializado de materialização pode ser encapsulado e reutilizado, enquanto quem busca um resultado continua exprimindo a intenção e suas restrições conceituais.

Não se separam necessariamente pessoas. Separam-se decisões e momentos decisórios. Uma mesma pessoa pode, em momentos diferentes, definir intenção, estabelecer políticas e restrições, especializar uma materialização e executar uma intenção.

A separação também permite reconhecer que competência para formular boas intenções e competência para materializá-las bem não são necessariamente a mesma competência. Uma pessoa, equipe ou momento decisório pode ser forte em uma e fraco em outra. O objetivo não é criar castas profissionais rígidas, mas permitir que essas competências sejam desenvolvidas, avaliadas e combinadas separadamente.

A mudança de ferramenta pode continuar exigindo adaptação, aprendizado e especialização. O FlowED não propõe eliminar esse efeito. Propõe reduzir quanto dessa mudança precisa atingir quem continua expressando a mesma intenção ou trabalhando com o mesmo conhecimento conceitual.

Quando intenção e materialização são separadas, o aprendizado acumulado sobre objetivos, restrições, decisões e estruturas do problema pode sobreviver melhor à substituição de tecnologias concretas. A parte volátil da mudança pode concentrar-se, tanto quanto o domínio permitir, na fronteira de materialização.

A consequência desejada não é ausência de reaprendizado, mas **menor ruptura**: aquilo que continuou conceitualmente válido não deveria ser descartado apenas porque mudou a ferramenta que o realiza.

### Consequências esperadas deste princípio

Estas consequências explicam as frases nucleares, mas não são ainda claims independentes do manifesto:

- preservar uma superfície operacional mais duradoura apesar da mudança tecnológica;
- reduzir reaprendizado de procedimentos incidentais quando a intenção continua válida;
- tornar mais claro se um resultado ruim decorreu da intenção, da política, da materialização ou da execução;
- permitir comparar múltiplas materializações de uma mesma intenção sem misturar automaticamente qualidade da intenção com qualidade da ferramenta;
- permitir que conhecimento especializado em materialização seja reaproveitado por muitos usuários através de fronteiras reutilizáveis;
- permitir que competências de intenção e de materialização sejam especializadas e compostas sem exigir que a mesma pessoa domine ambas no mesmo grau;
- permitir crescimento progressivo do vocabulário de intenção sem exigir ruptura completa da forma de expressão a cada nova ferramenta;
- facilitar continuidade entre aprendizado inicial e uso profissional de maior escala;
- reduzir o impacto da evolução tecnológica sobre conhecimento conceitual que permaneceu válido.

### Limites e hipóteses ainda abertas

O manifesto não deve afirmar, sem evidência própria, que esta separação automaticamente torna alguém sênior mais rápido, reduz universalmente carga cognitiva, melhora necessariamente a qualidade do software ou elimina a necessidade de especialistas conhecerem tecnologias concretas.

A hipótese de que especialização separada em intenção e materialização, quando bem coordenada, aumente a probabilidade de melhores resultados é plausível e testável, mas não deve ser promovida a verdade constitutiva antes de evidência. A separação também pode introduzir custos de coordenação, perda de contexto ou fronteiras mal desenhadas; esses efeitos precisam permanecer visíveis.

Esses efeitos são hipóteses empiricamente testáveis e podem tornar-se linhas de pesquisa. O compromisso filosófico anterior a essas hipóteses é a separação entre qualidade da decisão intencional e qualidade de sua materialização, acompanhada da preservação do conhecimento conceitual diante da volatilidade tecnológica.

Também não se assume que intenção seja imutável. Novas intenções podem surgir e intenções existentes podem evoluir. A prioridade é preservar estabilidade relativa quando o significado da intenção permanece válido.

### Relação com o produto FlowED

`flwd` é apenas uma materialização de referência desta visão. Deve poder ser substituído por qualquer outro cliente ou produto que respeite os mesmos princípios e contratos.

O produto existe para demonstrar e facilitar a filosofia; não define a filosofia nem recebe privilégio normativo por ter sido produzido pelos autores do FlowED.

## Próximo princípio

O próximo princípio ainda não está consolidado. Deve ser discutido separadamente, evitando promover como novo princípio algo que seja apenas consequência, mecanismo ou hipótese derivada do PR-M01.
