# CCP — hipótese de realizabilidade e fronteira de dependência

**Status:** hipótese operacional de trabalho — não normativa

## Decisão atual

O FlowED e o EDT podem prosseguir assumindo que é **realizável em algum grau** transformar registros brutos de criação (conversas, decisões, alternativas, rejeições, justificativas, evidências e mudanças) em uma representação estruturada e rastreável do caminho cognitivo do criador.

Essa realizabilidade **não é considerada comprovada em 100%**, nem o projeto depende, neste momento, de resolver completamente o problema.

A regra prática é:

1. verificar se já existem conceitos, métodos e ferramentas de anterioridade capazes de capturar e representar rationale, decisões, alternativas, argumentos, dependências e histórico de projeto;
2. adotar o máximo possível dessas soluções;
3. identificar o resíduo necessário para aproximar o conceito de CCP/CCC;
4. continuar FlowED/EDT enquanto existir uma trajetória tecnicamente plausível para esse resíduo;
5. não bloquear o manifesto do FlowED esperando a formalização completa do CCP;
6. se a pesquisa futura mostrar que uma parte do CCP é inviável, reduzir a ambição do CCP ao subconjunto realizável sem invalidar automaticamente EDT ou FlowED.

## Evidência preliminar de realizabilidade

Uma busca exploratória já encontrou uma tradição consolidada em **design rationale / rationale-based software engineering** que registra decisões, alternativas consideradas e rejeitadas, argumentos, intenções, dependências e histórico do processo de design.

Isso não prova que o CCP, tal como imaginado, já exista nem que toda cognição possa ser normalizada. Porém demonstra que uma parte central do problema — capturar e estruturar o raciocínio associado a decisões de engenharia — possui anterioridade prática e científica suficiente para tornar a hipótese de realizabilidade plausível.

Foram encontrados, entre outros antecedentes, trabalhos sobre:

- rationale-based software engineering;
- architecture design rationale;
- argumentation-based design rationale;
- representação e captura de design knowledge e design rationale;
- abordagens generativas em que explicações são reconstruídas a partir de conhecimento capturado durante o design, em vez de apenas reproduzir notas históricas.

## Fronteira importante

CCP não deve ser definido como "captura integral da cognição humana".

A hipótese mais defensável é capturar e normalizar o **traço cognitivo externalizável e relevante para a criação**, por exemplo:

- problema percebido;
- hipótese;
- alternativa;
- argumento;
- critério;
- decisão;
- rejeição;
- evidência;
- mudança de posição;
- dependência;
- racional;
- contexto;
- incerteza;
- resultado observado.

O nome e a ontologia final ainda dependem de pesquisa de anterioridade.

## Consequência para EDT

EDT pode assumir que existe um mecanismo de captura suficientemente estruturado para permitir que a trajetória de criação seja reutilizada em documentação, aprendizagem e evolução normativa.

Se CCP acabar sendo apenas uma composição de técnicas existentes de design rationale, argumentation e provenance, isso é aceitável: deve-se **adotar antes de inventar**.

## Consequência para FlowED

FlowED não precisa esperar a formalização total do CCP para fechar seu manifesto. No manifesto, basta assumir o princípio de que a autoeducação deve ser apoiada por trajetória de decisão/racional rastreável e reutilizável. A tecnologia/protocolo exato que realiza isso pode amadurecer em CCP/EDT antes da publicação pública do FlowED.

## Estado de pesquisa

Hipótese atual: **REALIZÁVEL EM PRINCÍPIO, ESCOPO AINDA ABERTO**.

A próxima pesquisa específica de CCP deverá determinar:

- quanto do conceito já é coberto por design rationale e áreas correlatas;
- qual o menor resíduo realmente novo;
- quais elementos podem ser capturados automaticamente de chats e logs;
- quais exigem confirmação humana;
- quais não podem ser inferidos com segurança;
- qual estrutura mínima é suficiente para EDT funcionar sem caos documental.
