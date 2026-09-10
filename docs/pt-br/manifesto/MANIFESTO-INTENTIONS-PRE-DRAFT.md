# Pré-manifesto — intenções que o Manifesto FlowED deve refletir

**Status:** rascunho de trabalho. Não normativo. Serve para registrar, antes da reorganização dos pilares, quais conclusões centrais o manifesto deve fazer um leitor compreender.

A intenção deste documento não é definir tecnologia, produto, provider ou implementação. Também não é reivindicar ineditismo filosófico. O FlowED parte de princípios já presentes em ciência, padrões e prática de engenharia e propõe dar a alguns deles prioridade transversal diferente.

## INT-M01 — Separar intenção de materialização

### Frase nuclear

> **Separar intenção de materialização torna possível avaliar separadamente a qualidade do que foi decidido e a qualidade de como aquilo foi realizado.**

### O que esta intenção quer fazer o leitor compreender

A Engenharia de Software já conhece a separação entre intenção e implementação. O FlowED propõe elevar essa separação a uma prioridade operacional transversal.

A intenção deve ser tratada como a superfície operacional mais estável. Ferramentas, frameworks, plataformas, providers, adapters e outras materializações podem mudar com maior frequência sem obrigar quem expressa uma intenção ainda válida a reaprender como trabalhar.

Os materializadores devem adaptar-se à linguagem da intenção sempre que possível, em vez de obrigar todos os executores a reaprender a linguagem particular de cada materializador.

O custo de adaptação à mudança tecnológica deve, sempre que possível, concentrar-se na fronteira de materialização. Conhecimento especializado de materialização pode ser encapsulado e reutilizado, enquanto quem busca um resultado continua exprimindo a intenção e suas restrições conceituais.

Não se separam necessariamente pessoas. Separam-se decisões e momentos decisórios. Uma mesma pessoa pode, em momentos diferentes, definir intenção, estabelecer políticas e restrições, especializar uma materialização e executar uma intenção.

### Consequências esperadas desta intenção

Estas consequências explicam a frase nuclear, mas não são ainda claims independentes do manifesto:

- preservar uma superfície operacional mais duradoura apesar da mudança tecnológica;
- reduzir reaprendizado de procedimentos incidentais quando a intenção continua válida;
- tornar mais claro se um resultado ruim decorreu da intenção, da política, da materialização ou da execução;
- permitir comparar múltiplas materializações de uma mesma intenção sem misturar automaticamente qualidade da intenção com qualidade da ferramenta;
- permitir que conhecimento especializado em materialização seja reaproveitado por muitos usuários através de fronteiras reutilizáveis;
- permitir crescimento progressivo do vocabulário de intenção sem exigir ruptura completa da forma de expressão a cada nova ferramenta;
- facilitar continuidade entre aprendizado inicial e uso profissional de maior escala.

### Limites e hipóteses ainda abertas

O manifesto não deve afirmar, sem evidência própria, que esta separação automaticamente torna alguém sênior mais rápido, reduz universalmente carga cognitiva, melhora necessariamente a qualidade do software ou elimina a necessidade de especialistas conhecerem tecnologias concretas.

Esses efeitos são hipóteses empiricamente testáveis e podem tornar-se linhas de pesquisa. O compromisso filosófico anterior a essas hipóteses é a separação entre qualidade da decisão intencional e qualidade de sua materialização.

Também não se assume que intenção seja imutável. Novas intenções podem surgir e intenções existentes podem evoluir. A prioridade é preservar estabilidade relativa quando o significado da intenção permanece válido.

### Relação com o produto FlowED

`flwd` é apenas uma materialização de referência desta visão. Deve poder ser substituído por qualquer outro cliente ou produto que respeite os mesmos princípios e contratos.

O produto existe para demonstrar e facilitar a filosofia; não define a filosofia nem recebe privilégio normativo por ter sido produzido pelos autores do FlowED.

## INT-M02 — Preservar conhecimento diante da evolução tecnológica

### Frase nuclear

> **Quando o conhecimento conceitual é acumulado independentemente da ferramenta que o materializa, a evolução tecnológica tende a exigir menos readaptação.**

### O que esta intenção quer fazer o leitor compreender

A mudança de ferramenta pode continuar exigindo adaptação, aprendizado e especialização. O FlowED não propõe eliminar esse efeito. Propõe reduzir quanto dessa mudança precisa atingir quem continua expressando a mesma intenção ou trabalhando com o mesmo conhecimento conceitual.

Quando intenção e materialização são separadas, o aprendizado acumulado sobre objetivos, restrições, decisões e estruturas do problema pode sobreviver melhor à substituição de tecnologias concretas. A parte volátil da mudança pode concentrar-se, tanto quanto o domínio permitir, na fronteira de materialização.

A consequência desejada não é ausência de reaprendizado, mas **menor ruptura**: aquilo que continuou conceitualmente válido não deveria ser descartado apenas porque mudou a ferramenta que o realiza.

Essa formulação também evita uma claim absoluta. O manifesto não afirma que evolução tecnológica deixará de exigir readaptação; afirma que separar conhecimento conceitual de materialização pode reduzir o impacto da mudança sobre o conhecimento já acumulado.

## Próxima intenção

A próxima intenção ainda não está consolidada. Deve ser discutida separadamente, evitando promover como novo princípio algo que seja apenas consequência, mecanismo ou hipótese derivada das intenções anteriores.
