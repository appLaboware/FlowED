# PR-M02 — Exploração de frases para o Princípio da Coerência Operacional

**Status:** rascunho exploratório. Não normativo. As duas primeiras frases já foram aceitas para o princípio; as demais são candidatas para discussão antes de eventual incorporação ao pré-manifesto.

## Frases já aceitas

> **Quando decisões, práticas e ferramentas de diferentes domínios compartilham princípios e contratos transversais, a forma de trabalhar da organização tende a se tornar mais coerente e reconhecível.**

> **Uma organização pode preservar uma identidade operacional reconhecível mesmo quando suas ferramentas mudam, quando essa identidade reside nos princípios, intenções e contratos que governam seu uso, e não nas implementações específicas.**

## Frases candidatas em exploração

### Candidata A — autonomia sem fragmentação

> **Quando decisões locais permanecem livres dentro de princípios e contratos comuns, autonomia entre equipes e domínios pode crescer sem necessariamente fragmentar a forma de trabalhar da organização.**

Intenção: distinguir coerência de uniformidade. O princípio não busca centralizar toda decisão, mas permitir diversidade local dentro de invariantes transversais reconhecíveis.

### Candidata B — divergência visível

> **Quando decisões de diferentes domínios são expressas sobre uma base comum, divergências entre elas tendem a se tornar mais visíveis, comparáveis e discutíveis.**

Intenção: mostrar que a coerência operacional não serve apenas para identidade percebida; ela também cria uma superfície onde inconsistências, exceções e conflitos deixam de ficar escondidos dentro de ferramentas e práticas locais.

### Candidata C — composição entre domínios

> **Quando diferentes capacidades compartilham uma base operacional comum, combiná-las tende a exigir menos tradução entre linguagens, práticas e critérios locais.**

Intenção: explorar a hipótese de que coerência transversal reduz custo de composição entre domínios sem exigir que suas materializações internas sejam iguais.

### Candidata D — mudança local sem ruptura global

> **Quando a identidade operacional está nos princípios e contratos compartilhados, uma mudança local de tecnologia pode permanecer local sem obrigar a organização inteira a redefinir como trabalha.**

Intenção: complementar a segunda frase aceita com uma consequência organizacional mais concreta: mudanças de materialização podem ser contidas no domínio afetado quando a identidade não depende da ferramenta.

### Candidata E — identidade técnica percebida pela coerência transversal

> **Quando escolhas locais de diferentes domínios são orientadas por critérios transversais comuns e seus fundamentos permanecem visíveis, a diversidade tecnológica pode expressar uma mesma identidade operacional, em vez de fragmentá-la.**

Intenção: explicitar a transversalidade do princípio. A identidade técnica percebida de uma organização não nasce apenas de uma escolha isolada de linguagem, framework, ferramenta ou método, mas da recorrência de critérios reconhecíveis atravessando diferentes domínios. Se segurança, estabilidade, auditabilidade, reversibilidade, evidência ou qualquer outro valor organizacional relevante orienta escolhas locais distintas, essas escolhas podem continuar diferentes entre si e ainda assim serem percebidas como manifestações de uma mesma forma de pensar.

A coerência desejada não pressupõe que todas as áreas escolham tecnologias equivalentes nem que um valor transversal determine sozinho cada decisão. O ponto é que escolhas locais possam ser justificadas por uma base filosófica e contratual comum, tornando a personalidade operacional da organização mais legível para dentro e para fora.

Esta candidata pertence mais naturalmente ao PR-M02 do que ao PR-M01. O PR-M01 explica por que intenção e materialização podem evoluir separadamente. A candidata E trata de como decisões heterogêneas, quando orientadas por critérios transversais comuns, podem compor uma identidade organizacional reconhecível.

A analogia com projetos fortemente associados a uma linha técnica consistente pode ajudar a explicar a ideia: mudanças concretas de tecnologia podem alterar a implementação sem apagar necessariamente a percepção de uma maneira estável de decidir. A analogia é apenas ilustrativa; o princípio não depende de uma pessoa centralizadora nem de liderança personalista.

### Candidata F — identidade legível por uma superfície intencional comum

> **Quando escolhas de engenharia convergem para uma superfície intencional comum, a identidade técnica da organização tende a ser mais legível do que quando precisa ser inferida da soma das ferramentas que utiliza.**

Intenção: distinguir uma organização que apenas enumera tecnologias, métodos e ferramentas adotados de uma organização que consegue expressar essas escolhas como manifestações de uma mesma forma de decidir. Uma lista como linguagem, banco, método ágil, estratégia de versionamento e ferramentas de infraestrutura pode revelar partes da prática, mas não necessariamente torna explícita a identidade que atravessa essas escolhas. Uma superfície intencional comum pode funcionar como projeção mais direta dessa identidade.

Esta candidata não exige que a organização adote um pacote monolítico de ferramentas nem que use qualquer produto específico. A unidade está na superfície intencional compartilhada, não na obrigatoriedade de uma implementação única.

#### Refinamento — uma superfície intencional, muitas materializações

O benefício não está simplesmente em trocar cinquenta ferramentas por uma ferramenta única. Uma ferramenta monolítica poderia apenas concentrar dependências e esconder decisões. O ganho pretendido é concentrar **a expressão da intenção** numa superfície transversal comum, mantendo livres e substituíveis as materializações de cada domínio.

> **Uma superfície intencional comum pode unificar a expressão da forma de pensar da organização sem unificar as ferramentas que a realizam.**

Uma formulação alternativa, mais explícita quanto à relação entre unidade e pluralidade, é:

> **Quando múltiplas decisões de engenharia são expressas por uma mesma superfície intencional, a organização pode apresentar uma linha de pensamento reconhecível sem impor uma única linha de materialização.**

Assim, uma organização pode defender, explicar e discutir de maneira unificada a lógica que orienta suas decisões, enquanto versionamento, banco de dados, construção, testes, implantação ou qualquer outro domínio continuam podendo usar materializadores distintos. A superfície comum funciona como lugar de expressão da identidade; adapters e providers permanecem como escolhas de realização.

Esta estrutura também torna mais claro um tipo de crítica que hoje costuma ficar misturado: alguém pode concordar com a intenção ou com o critério organizacional e discordar da materialização escolhida para realizá-lo. Essa decomposição pertence conceitualmente ao PR-M01, mas fortalece o PR-M02 ao permitir que a identidade intencional da organização permaneça legível mesmo quando uma escolha tecnológica específica é contestada ou substituída.

O mesmo vale para a permanência temporal: se a organização troca Git por outro sistema de versionamento, ou um framework por outro, sua identidade operacional não precisa ser redefinida se a intenção, os critérios e os contratos que governavam aquela capacidade continuam válidos. A mudança pode atingir a materialização sem apagar a personalidade intencional que a precede.

#### Ponte explícita com o PR-M01

> **A unidade operacional não precisa implicar adesão tecnológica monolítica quando a superfície comum expressa intenção e contratos, e não um pacote obrigatório de implementações.**

Essa ponte é importante para evitar uma leitura equivocada do PR-M02. Um produto de referência pode materializar uma determinada filosofia de forma integrada, mas a coerência organizacional não depende de usar esse produto inteiro. Uma organização pode construir outra superfície comum, adotar materializadores diferentes ou substituir todos eles, inclusive por soluções que expressem valores distintos dos do FlowED, e ainda assim obter o benefício estrutural de tornar sua identidade técnica mais explícita e duradoura.

A ligação entre os princípios fica assim: o PR-M02 explica por que uma superfície comum pode tornar a identidade organizacional mais coerente e legível; o PR-M01 impede que essa unidade seja confundida com acoplamento às materializações. A mesma identidade intencional pode sobreviver à troca de tecnologias porque a superfície que a expressa está acima delas.

## Distinções a preservar

- coerência não é uniformidade;
- identidade operacional não é padronização tecnológica;
- identidade técnica percebida não exige uma pessoa centralizadora;
- transversalidade significa critérios compartilhados atravessando decisões locais, não resultados locais idênticos;
- uma superfície intencional comum não significa pacote tecnológico obrigatório;
- unificar a expressão da intenção não significa unificar as materializações;
- uma implementação integrada pode expressar uma filosofia, mas não possui monopólio sobre ela;
- autonomia local não significa ausência de invariantes comuns;
- uma base comum deve tornar diferenças visíveis, não apagá-las;
- o PR-M02 trata da organização como sistema coerente, enquanto o PR-M01 garante que essa coerência possa permanecer separada das materializações concretas.
