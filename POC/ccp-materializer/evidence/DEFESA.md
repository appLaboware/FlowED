# P2.3 — DEFESA

**Status:** candidata em revisão. Não substitui a redação consolidada do manifesto até aprovação explícita.

Fonte: documento editorial preservado; não é transcrição integral do chat.

Autoridade registrada: candidata editorial da frente MAN-001; aprovação final não registrada nesta fonte

Compilação experimental de trechos existentes. Equivalência semântica não verificada automaticamente.

A proposição não afirma que contratos sejam novidade nem que já não possuam papel central em diversas práticas de Engenharia de Software. O ponto de partida é justamente reconhecer esse domínio conhecido e deslocar a discussão para outro nível: não apenas usar contratos para interfaces, responsabilidades ou integrações, mas fazer deles o principal lugar de preservação da coerência operacional que deve sobreviver às mudanças de materialização.

A camada EXPAND-MAX não é uma defesa adicional. Ela apenas explicita pré-requisitos de compreensão que leitores mais experientes podem inferir sozinhos: exemplos do que pode funcionar como contrato, uma glosa curta de coerência operacional e o sentido de concentrar nos contratos aquilo que deve sobreviver às trocas de materialização. Essas explicações podem ser removidas em projeções menos densas sem alterar a conclusão.

[Fonte de meaning](https://github.com/appLaboware/FlowED/blob/a22a6ad841f3ab6e87eb89ffef43e9bfcd45e4ba/docs/pt-br/manifesto/P2.3-COERENCIA-OPERACIONAL-PROJECTIONS.md#L33-L35)

O deslocamento é de centralidade. Em vez de deixar que identidade operacional, continuidade de práticas e invariantes relevantes fiquem excessivamente incorporados às tecnologias concretas usadas em cada momento, propõe-se concentrar essa responsabilidade nos princípios e contratos que definem como a organização pretende operar.

A tecnologia continua importante, especializada e sujeita a requisitos próprios de confiabilidade. Ela apenas deixa de ser o lugar primário onde a coerência organizacional precisa residir.

[Fonte de shift](https://github.com/appLaboware/FlowED/blob/a22a6ad841f3ab6e87eb89ffef43e9bfcd45e4ba/docs/pt-br/manifesto/P2.3-COERENCIA-OPERACIONAL-PROJECTIONS.md#L39-L41)

O encadeamento preservado pela proposição é:

`coerência operacional concentrada em contratos → menor dependência da permanência de tecnologias específicas → maior liberdade para experimentar, substituir e evoluir materializações`

A conclusão não é que tecnologia deixe de precisar de estabilidade operacional. O que se reduz é a necessidade de transformar uma tecnologia específica no suporte principal da identidade operacional da organização.

[Fonte de causality](https://github.com/appLaboware/FlowED/blob/a22a6ad841f3ab6e87eb89ffef43e9bfcd45e4ba/docs/pt-br/manifesto/P2.3-COERENCIA-OPERACIONAL-PROJECTIONS.md#L45-L49)

A primeira frase reconhece explicitamente que contratos já são amplamente utilizados. Isso evita reivindicar como novidade algo já conhecido pelo público técnico e estabelece o ponto exato de partida do raciocínio. A proposta começa depois desse reconhecimento: no grau de responsabilidade atribuído aos contratos pela coerência operacional.

[Fonte de recognition](https://github.com/appLaboware/FlowED/blob/a22a6ad841f3ab6e87eb89ffef43e9bfcd45e4ba/docs/pt-br/manifesto/P2.3-COERENCIA-OPERACIONAL-PROJECTIONS.md#L53-L53)

A proposição depende da separação entre intenção e materialização. Se tecnologias tendem a mudar em ritmos diferentes da intenção que realizam, concentrar a coerência em uma superfície mais estável permite que a mudança tecnológica permaneça mais localizada na borda de materialização.

Essa relação não significa que toda intenção permaneça imutável. Princípios e contratos também evoluem. A hipótese é apenas que, quando aquilo que deve permanecer é explicitado separadamente daquilo que o materializa, mudanças de implementação tendem a exigir menos reconstrução conceitual.

[Fonte de intent](https://github.com/appLaboware/FlowED/blob/a22a6ad841f3ab6e87eb89ffef43e9bfcd45e4ba/docs/pt-br/manifesto/P2.3-COERENCIA-OPERACIONAL-PROJECTIONS.md#L57-L59)

O efeito estratégico pretendido é aumentar a capacidade de evolução tecnológica sem exigir que cada troca de ferramenta, framework, plataforma ou provider redefina a forma de trabalho que continua válida.

A materialização é frequentemente a parte mais visível da evolução de um sistema: novos frameworks, bibliotecas, plataformas e padrões alteram diretamente o artefato produzido. Quando a coerência operacional não depende da permanência dessas tecnologias, a organização tende a poder experimentar e substituí-las com menor impacto sobre sua identidade operacional.

[Fonte de impact](https://github.com/appLaboware/FlowED/blob/a22a6ad841f3ab6e87eb89ffef43e9bfcd45e4ba/docs/pt-br/manifesto/P2.3-COERENCIA-OPERACIONAL-PROJECTIONS.md#L63-L65)

Esta proposição não afirma que:

- contratos devam conter toda decisão da organização;
- tecnologias concretas não precisem ser estabilizadas, governadas ou padronizadas;
- toda substituição tecnológica se torne barata ou simples;
- princípios e contratos sejam imutáveis;
- diversidade tecnológica seja sempre desejável;
- contratos eliminem conhecimento especializado sobre materializações.

A proposição trata apenas de onde se busca preservar prioritariamente a coerência operacional e da consequência esperada dessa escolha sobre a liberdade de evolução das materializações.

[Fonte de limits](https://github.com/appLaboware/FlowED/blob/a22a6ad841f3ab6e87eb89ffef43e9bfcd45e4ba/docs/pt-br/manifesto/P2.3-COERENCIA-OPERACIONAL-PROJECTIONS.md#L69-L78)

`tecnologias mudam e deixam marcas visíveis no artefato`

`↓`

`se a coerência operacional estiver incorporada à tecnologia, a mudança tecnológica arrasta parte da forma de trabalhar`

`↓`

`princípios e contratos podem carregar invariantes e intenção de forma separada da materialização`

`↓`

`deslocar para eles a responsabilidade primária pela coerência reduz a dependência da permanência tecnológica`

`↓`

`a estabilidade passa a proteger a liberdade de mudar`

[Fonte de argument-path](https://github.com/appLaboware/FlowED/blob/a22a6ad841f3ab6e87eb89ffef43e9bfcd45e4ba/docs/pt-br/manifesto/P2.3-COERENCIA-OPERACIONAL-PROJECTIONS.md#L82-L98)

## Núcleo preservado e proveniência

O JSON desta projeção contém integralmente os elementos abaixo, inclusive os que não estão na superfície de leitura.

- [state](https://github.com/appLaboware/FlowED/blob/a22a6ad841f3ab6e87eb89ffef43e9bfcd45e4ba/docs/pt-br/manifesto/P2.3-COERENCIA-OPERACIONAL-PROJECTIONS.md#L3-L3)

- [base](https://github.com/appLaboware/FlowED/blob/a22a6ad841f3ab6e87eb89ffef43e9bfcd45e4ba/docs/pt-br/manifesto/P2.3-COERENCIA-OPERACIONAL-PROJECTIONS.md#L15-L15)

- [causality](https://github.com/appLaboware/FlowED/blob/a22a6ad841f3ab6e87eb89ffef43e9bfcd45e4ba/docs/pt-br/manifesto/P2.3-COERENCIA-OPERACIONAL-PROJECTIONS.md#L45-L49)

- [limits](https://github.com/appLaboware/FlowED/blob/a22a6ad841f3ab6e87eb89ffef43e9bfcd45e4ba/docs/pt-br/manifesto/P2.3-COERENCIA-OPERACIONAL-PROJECTIONS.md#L69-L78)

[Projeção estruturada](DEFESA.json)

Omissões autorizadas neste contrato: expand, reduction-1, reduction-2, reduct
