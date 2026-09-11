# P2.3 — Coerência Operacional — Projeções cognitivas

**Status:** candidata em revisão. Não substitui a redação consolidada do manifesto até aprovação explícita.

Esta unidade registra EXPAND-MAX, BASE, níveis de redução, REDUCT-MAX e DEFESA como projeções da mesma unidade cognitiva. A redução deve preservar núcleo semântico, conclusão, autoridade, estado epistêmico e causalidade essencial. O aprofundamento deve acrescentar compreensão sem contradizer os níveis anteriores.

EXPAND-MAX é a projeção de maior densidade que ainda preserva a forma, a voz e a função de uma proposição do manifesto. Ela pode acrescentar pré-requisitos de compreensão, pequenas glosas e exemplos de categoria, mas ainda não entra em evidências, objeções, justificativas extensas ou demonstração; esses elementos pertencem à DEFESA.

## EXPAND-MAX — pré-requisitos de compreensão

Contratos — por exemplo, interfaces, esquemas, políticas ou declarações de configuração que explicitam condições a serem respeitadas — já são amplamente utilizados na Engenharia de Software, em diferentes níveis da arquitetura e da operação. Nossa proposta, porém, é que lhes seja atribuída a responsabilidade primária pela preservação da coerência operacional — aquilo que deve continuar reconhecível na forma de pensar e operar mesmo quando a tecnologia usada para realizá-la muda. Concentrar essa responsabilidade nos contratos significa manter neles a intenção e os invariantes que devem sobreviver às trocas de materialização. Portanto, quanto mais essa coerência reside nos contratos, menos depende da permanência das tecnologias que os materializam e maior tende a ser a liberdade para experimentá-las, substituí-las e fazê-las evoluir sem reconstruir o que continua válido. Ao deslocar a estabilidade para aquilo que se pretende preservar, a organização pode deixar mais livre para mudar justamente aquilo que mais tende a mudar.

## BASE

Contratos já são amplamente utilizados na Engenharia de Software. Nossa proposta, porém, é que lhes seja atribuída a responsabilidade primária pela preservação da coerência operacional, concentrando nos contratos aquilo que deve permanecer reconhecível mesmo quando as tecnologias mudam. Quanto mais essa coerência reside nos contratos, menos depende da permanência das tecnologias que os materializam e maior tende a ser a liberdade para experimentá-las, substituí-las e fazê-las evoluir. Ao deslocar a estabilidade para aquilo que se pretende preservar, a organização pode deixar mais livre para mudar justamente aquilo que mais tende a mudar.

## REDUÇÃO — Nível 1

Contratos já são amplamente utilizados na Engenharia de Software. Propomos que lhes seja atribuída a responsabilidade primária pela coerência operacional. Quanto mais essa coerência reside nos contratos, menos depende da permanência das tecnologias que os materializam e mais livres elas ficam para mudar.

## REDUÇÃO — Nível 2

Propomos atribuir aos contratos a responsabilidade primária pela coerência operacional. Quanto mais essa coerência reside neles, mais livre a tecnologia fica para mudar.

## REDUCT-MAX

Propomos fazer dos contratos a base primária da coerência operacional para que a tecnologia permaneça livre para mudar.

## DEFESA

### O que a proposição quer dizer

A proposição não afirma que contratos sejam novidade nem que já não possuam papel central em diversas práticas de Engenharia de Software. O ponto de partida é justamente reconhecer esse domínio conhecido e deslocar a discussão para outro nível: não apenas usar contratos para interfaces, responsabilidades ou integrações, mas fazer deles o principal lugar de preservação da coerência operacional que deve sobreviver às mudanças de materialização.

A camada EXPAND-MAX não é uma defesa adicional. Ela apenas explicita pré-requisitos de compreensão que leitores mais experientes podem inferir sozinhos: exemplos do que pode funcionar como contrato, uma glosa curta de coerência operacional e o sentido de concentrar nos contratos aquilo que deve sobreviver às trocas de materialização. Essas explicações podem ser removidas em projeções menos densas sem alterar a conclusão.

### Deslocamento proposto

O deslocamento é de centralidade. Em vez de deixar que identidade operacional, continuidade de práticas e invariantes relevantes fiquem excessivamente incorporados às tecnologias concretas usadas em cada momento, propõe-se concentrar essa responsabilidade nos princípios e contratos que definem como a organização pretende operar.

A tecnologia continua importante, especializada e sujeita a requisitos próprios de confiabilidade. Ela apenas deixa de ser o lugar primário onde a coerência organizacional precisa residir.

### Causalidade essencial

O encadeamento preservado pela proposição é:

`coerência operacional concentrada em contratos → menor dependência da permanência de tecnologias específicas → maior liberdade para experimentar, substituir e evoluir materializações`

A conclusão não é que tecnologia deixe de precisar de estabilidade operacional. O que se reduz é a necessidade de transformar uma tecnologia específica no suporte principal da identidade operacional da organização.

### Por que a formulação começa reconhecendo o óbvio

A primeira frase reconhece explicitamente que contratos já são amplamente utilizados. Isso evita reivindicar como novidade algo já conhecido pelo público técnico e estabelece o ponto exato de partida do raciocínio. A proposta começa depois desse reconhecimento: no grau de responsabilidade atribuído aos contratos pela coerência operacional.

### Relação com intenção e materialização

A proposição depende da separação entre intenção e materialização. Se tecnologias tendem a mudar em ritmos diferentes da intenção que realizam, concentrar a coerência em uma superfície mais estável permite que a mudança tecnológica permaneça mais localizada na borda de materialização.

Essa relação não significa que toda intenção permaneça imutável. Princípios e contratos também evoluem. A hipótese é apenas que, quando aquilo que deve permanecer é explicitado separadamente daquilo que o materializa, mudanças de implementação tendem a exigir menos reconstrução conceitual.

### Impacto estratégico esperado

O efeito estratégico pretendido é aumentar a capacidade de evolução tecnológica sem exigir que cada troca de ferramenta, framework, plataforma ou provider redefina a forma de trabalho que continua válida.

A materialização é frequentemente a parte mais visível da evolução de um sistema: novos frameworks, bibliotecas, plataformas e padrões alteram diretamente o artefato produzido. Quando a coerência operacional não depende da permanência dessas tecnologias, a organização tende a poder experimentar e substituí-las com menor impacto sobre sua identidade operacional.

### Limites

Esta proposição não afirma que:

- contratos devam conter toda decisão da organização;
- tecnologias concretas não precisem ser estabilizadas, governadas ou padronizadas;
- toda substituição tecnológica se torne barata ou simples;
- princípios e contratos sejam imutáveis;
- diversidade tecnológica seja sempre desejável;
- contratos eliminem conhecimento especializado sobre materializações.

A proposição trata apenas de onde se busca preservar prioritariamente a coerência operacional e da consequência esperada dessa escolha sobre a liberdade de evolução das materializações.

### Caminho cognitivo resumido

`tecnologias mudam e deixam marcas visíveis no artefato`

`↓`

`se a coerência operacional estiver incorporada à tecnologia, a mudança tecnológica arrasta parte da forma de trabalhar`

`↓`

`princípios e contratos podem carregar invariantes e intenção de forma separada da materialização`

`↓`

`deslocar para eles a responsabilidade primária pela coerência reduz a dependência da permanência tecnológica`

`↓`

`a estabilidade passa a proteger a liberdade de mudar`
