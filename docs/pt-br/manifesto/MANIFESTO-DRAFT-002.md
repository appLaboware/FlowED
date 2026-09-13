# Manifesto FlowED — rascunho 002

**Status:** rascunho de consolidação. Não normativo. Ainda sujeito a crítica, simulação, uso e revisão.

## Por que o FlowED existe

A Engenharia de Software cresce continuamente em conhecimento, métodos, ferramentas, normas e especialidades. Esse crescimento não deveria obrigar pessoas e organizações a carregar uma complexidade operacional proporcional.

O FlowED existe para permitir que a engenharia cresça sem que cada novo domínio, prática ou ferramenta se transforme em mais uma ilha de linguagem, processo e operação.

Defendemos uma Engenharia de Software em que diferentes capacidades possam participar de uma linguagem operacional comum, preservar sua especialidade e continuar livres para evoluir por dentro.

Nossa hipótese central é simples:

> **a sofisticação da Engenharia de Software deve poder crescer sem exigir burocracia e complexidade operacional na mesma proporção.**

## O compromisso fundamental

O FlowED é **rígido no contrato e livre na materialização**.

O contrato define aquilo que precisa ser possível, seu significado público, as entradas e saídas relevantes, os estados e garantias observáveis, a rastreabilidade necessária, a compatibilidade e as condições de conformidade.

O contrato não determina algoritmo, linguagem, framework, fornecedor, banco, arquitetura interna ou produto quando esses elementos não forem parte da garantia pública.

> **Uma intenção pode admitir muitas materializações. Uma materialização não pode redefinir silenciosamente a intenção.**

Qualquer implementação que cumpra integralmente o contrato aplicável é uma implementação válida, independentemente de ter sido criada pelo projeto FlowED, por outra empresa, por uma comunidade ou pelo próprio time que a utiliza.

Conformidade não significa superioridade. Uma ferramenta pode cumprir perfeitamente um contrato e ainda não ser a preferência de um time. A escolha entre implementações conformantes permanece livre e governada por quem adota o FlowED.

## Pilar 1 — Unidade operacional e liberdade governada

A Engenharia de Software deve poder operar como um sistema composto, não como uma coleção de ilhas incompatíveis.

Domínios distintos podem manter conceitos, métodos, artefatos e tecnologias próprios, mas devem poder se relacionar por significados e contratos públicos explícitos.

O FlowED busca reduzir a quantidade de interfaces operacionais que uma pessoa precisa dominar sem reduzir o conhecimento conceitual necessário para exercer cada domínio.

A linguagem comum não elimina a especialidade. Ela cria uma fronteira compartilhada para que especialidades diferentes possam conversar, compor-se e ser substituídas sem transformar cada troca de tecnologia em reconstrução da organização.

Por isso:

- uma linguagem comum pode coexistir com muitas tecnologias;
- artefatos nativos permanecem soberanos e portáveis;
- implementações de referência não recebem privilégio normativo;
- interoperabilidade e substituição dependem do contrato, não da origem da ferramenta.

## Pilar 2 — Autoeducação e conhecimento vivo

Executar não basta. Uma organização deve poder aprender com aquilo que executa e usar esse aprendizado para modificar conscientemente sua própria forma de trabalhar.

> **O maior patrimônio de um projeto não é apenas o que ele entrega, mas o conhecimento acumulado durante a construção.**

A execução relevante deve poder deixar memória estruturada. Essa memória deve poder ser relacionada às decisões, referências, hipóteses, justificativas, resultados, divergências e evidências que deram contexto ao que aconteceu.

O FlowED não exige uma tecnologia específica de logging, eventos, proveniência, memória ou conhecimento. Exige que essas capacidades possam ser cumpridas por contrato e relacionadas de maneira interoperável.

O conhecimento consolidado não é o conhecimento inteiro. Ele é uma projeção adequada a uma intenção, papel, contexto e objetivo. O sistema deve fornecer somente a informação necessária, mas nunca menos que a necessária, preservando a possibilidade de retornar à origem, ao racional e à evidência.

A autoeducação se completa quando experiência preservada pode voltar a influenciar decisão, referência ou modo de trabalho.

## Pilar 3 — Sustentação explícita

Decisões técnicas e filosóficas não deveriam esconder aquilo que as sustenta.

O FlowED defende que a relação de uma referência com conhecimento científico, normativo e evidência empírica seja explícita, rastreável e disponível para decisão.

Isso não transforma ciência em dogma, experiência local em verdade universal ou popularidade em prova de correção.

Uma organização pode adotar uma referência ainda não sustentada cientificamente, contrariar um baseline ou manter uma prática baseada principalmente em experiência operacional. O que não deve acontecer é essa condição desaparecer da decisão.

O FlowED não mede verdade, não ranqueia referências e não emite uma opinião epistemológica própria. Ele define contratos capazes de representar e transportar sustentação, proveniência, lacunas, divergências e avaliações produzidas por terceiros.

Quando uma ferramenta afirma que algo possui determinada relevância, score, ranking ou nível de sustentação, o FlowED deve ser capaz de responder também **quem produziu essa avaliação** e sob qual contrato ela foi apresentada.

> **A opinião pertence a quem mede. A responsabilidade do FlowED é tornar essa opinião identificável, interoperável e criticável.**

Trocar o avaliador não deve exigir trocar a filosofia, o restante do ecossistema ou o histórico da organização.

## Pilar 4 — Progressividade governada

Mais não é automaticamente melhor.

A forma de trabalhar deve poder variar conforme contexto, risco, necessidade, maturidade e evidência sem que toda a complexidade possível seja imposta antecipadamente.

Uma capacidade pode ser introduzida, ampliada, mantida, reduzida, pausada ou revertida. Cada uma dessas decisões pode ser correta dependendo do contexto.

O FlowED deve tornar essa progressão explícita e rastreável por contrato, sem impor o mecanismo, algoritmo ou ferramenta que recomenda, decide ou executa a mudança.

> **Maturidade não é acumular permanentemente mais processo. É saber quanto processo, rigor e capacidade fazem sentido agora — e poder justificar a mudança depois.**

A progressividade permite que o mesmo modelo mental acompanhe estudante, profissional, equipe pequena e organização complexa sem exigir que todos operem desde o início com a mesma intensidade.

## Evolução como comportamento, não como promessa

O FlowED não considera uma referência verdadeira apenas porque foi adotada nem melhor apenas porque foi usada por muito tempo.

Toda referência deve poder evoluir por um ciclo rastreável:

**captura ou adoção → debate → refinamento → uso → evidência → crítica → revisão → nova versão, manutenção ou abandono.**

Uso produz evidência. Evidência pode fortalecer, manter, enfraquecer, restringir ou invalidar uma referência.

O baseline é um ponto de partida, não uma verdade nem um destino obrigatório.

Divergir é permitido. Esconder a divergência não.

O FlowED deve ser capaz de registrar inclusive a evidência que demonstra que uma recomendação anterior do próprio FlowED deveria ser superada.

## O que significa ser FlowED

Ser FlowED não significa utilizar uma ferramenta oficial.

Uma organização pode não executar uma única linha de código produzida pelo ecossistema de referência e ainda assim ser integralmente conformante, desde que cumpra os contratos e obrigações públicas aplicáveis.

Da mesma forma, instalar todo o software oficial não produz conformidade se os contratos forem violados.

> **Conformidade pertence ao comportamento público; não à marca da implementação.**

O ecossistema FlowED pode oferecer clientes, hubs, adapters, providers e outras implementações de referência. Essas ferramentas existem para demonstrar realizabilidade, reduzir o custo de adoção e oferecer uma composição pronta segundo a visão de seus autores.

Elas não são a única maneira legítima de materializar o manifesto.

Ferramentas concorrentes são bem-vindas. Implementações internas são bem-vindas. Novas abordagens são bem-vindas. Quando cumprem o contrato, participam do mesmo ecossistema de interoperabilidade.

## O FlowED que defendemos

Defendemos uma Engenharia de Software em que:

1. **contratos comuns permitam liberdade tecnológica sem perder organização;**
2. **execução gere memória capaz de alimentar aprendizagem;**
3. **sustentação e incerteza sejam visíveis em vez de presumidas;**
4. **processo e rigor possam crescer ou diminuir de forma governada;**
5. **ferramentas sejam substituíveis sem destruir o conhecimento acumulado;**
6. **a academia, a indústria e o aprendizado individual possam compartilhar uma mesma linguagem sem exigir a mesma escala;**
7. **nenhuma implementação, inclusive a nossa, esteja acima do contrato;**
8. **nenhuma versão do próprio FlowED esteja acima da crítica e da evidência.**

O FlowED não pretende escolher todas as respostas para uma organização.

Pretende garantir que essas respostas possam ser expressas, executadas, relacionadas, substituídas, justificadas e revistas dentro de uma linguagem comum.

> **Organização sem aprisionamento. Liberdade sem perda de sentido. Evolução sem perda de memória.**
