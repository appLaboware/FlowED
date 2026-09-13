# Esboço de hierarquia do Manifesto FlowED

**Status:** proposta de trabalho — não normativa, sujeita a debate e refinamento.

Este documento organiza o material histórico e conceitual atual do FlowED em níveis de importância. Ele não substitui o manifesto histórico nem congela terminologia. Sua função é permitir debate estruturado antes da versão preliminar do manifesto.

## 0. Missão

**Cobrir todos os domínios da Engenharia de Software por uma linguagem operacional comum e uma arquitetura modular orientada por contratos públicos, permitindo que a organização evolua sua própria forma de trabalhar sem perder rastreabilidade, conhecimento acumulado, liberdade tecnológica ou sustentabilidade.**

A missão é o nível superior. Pilares, princípios e mecanismos existem para realizá-la.

## 1. Tese central

O FlowED parte da hipótese de que a Engenharia de Software pode aumentar sua sofisticação, abrangência e maturidade sem exigir crescimento proporcional da complexidade operacional percebida pelas pessoas.

Para isso, separa intenção de materialização, preserva uma linguagem operacional comum, permite composição modular e transforma a experiência da organização em insumo rastreável para sua própria evolução.

### Invariante transversal

O FlowED é **rígido no contrato e livre na materialização**.

Ele pode determinar com precisão o que uma capability deve significar, quais operações e garantias públicas precisa oferecer, que evidências e rastros precisam existir e quais regras de interoperabilidade e compatibilidade devem ser preservadas. Não determina algoritmo, framework, fornecedor, ferramenta ou arquitetura interna quando esses detalhes não forem parte da garantia pública.

Qualquer materializador/provider que cumpra integralmente o contrato aplicável é válido naquela capability FlowED. Uma implementação de referência serve para demonstrar realizabilidade e oferecer um caminho pronto, mas não possui autoridade normativa adicional.

Conformidade contratual não equivale a qualidade ou preferência. A avaliação de confiabilidade, metodologia, eficiência ou adequação de uma ferramenta pertence aos adotantes e às políticas escolhidas por eles, salvo propriedades explicitamente exigidas pelo contrato.

## 2. Fluxo fundamental de evolução

O FlowED não trata uma referência adotada como conhecimento congelado. Sua forma de trabalhar deve evoluir por um fluxo explícito e recorrente:

**esboço → debate → refinamento → versão preliminar → uso real → evidência → alteração de sustentação → revisão → novo ciclo**.

Este fluxo é candidato a elemento central do manifesto, e não apenas ao processo usado para escrevê-lo. Ele representa como uma organização FlowED transforma hipótese em prática, prática em evidência e evidência em evolução consciente.

O ciclo não pressupõe que uso confirme uma regra. A experiência pode aumentar, manter ou reduzir sua sustentação; revelar inadequação contextual; produzir divergência; ou levar ao abandono da referência. O valor está em tornar a evolução observável, rastreável, criticável e reutilizável.

O próprio manifesto deve percorrer esse fluxo. Assim, sua versão preliminar não será apresentada como verdade final: será uma referência utilizável cuja sustentação deverá evoluir com aplicação, observação e crítica.

## 3. Quatro pilares propostos

Os pilares formam o primeiro nível de compreensão abaixo da missão e da tese central. Devem descrever capacidades e compromissos contratuais do FlowED, não ferramentas preferidas de materialização.

### Pilar 1 — Unidade operacional e liberdade governada

Todos os domínios da Engenharia de Software devem poder participar de uma mesma linguagem operacional sem perder sua soberania interna nem ficar presos a uma implementação concreta.

A liberdade de materialização não é liberdade caótica. Ela existe dentro de intenções explícitas, contratos públicos, rastreabilidade, regras de composição e capacidade de substituição controlada.

FlowED padroniza a expressão de intenção, a semântica pública e os contratos, não as tecnologias concretas. Artefatos permanecem nativos e utilizáveis fora do FlowED.

Este pilar estabelece a regra transversal dos demais: **rigidez no contrato, liberdade na materialização**.

### Pilar 2 — Autoeducação e conhecimento vivo

A organização não deve apenas executar um processo; deve ser capaz de transformar execução em memória operacional estruturada e relacionável ao conhecimento que a motivou, permitindo que experiência, decisão e evidência retroalimentem conscientemente a evolução da forma de trabalhar.

O FlowED exige essa capacidade no nível contratual. Não exige Kafka, OpenTelemetry, MyTrues, EDT, CCP/CCC ou qualquer outra tecnologia específica. Esses elementos podem servir como referências, materializações ou implementações de referência.

Decisões, razões, mudanças, resultados e aprendizados relevantes devem poder ser preservados e reutilizados. O conhecimento consolidado é uma projeção adequada a um interlocutor e objetivo, não o conhecimento inteiro.

### Pilar 3 — Sustentação científica e empírica explícita

Toda referência relevante deve tornar explícita sua relação com o conhecimento científico e normativo disponível e com a evidência empírica observada em seu contexto de uso.

FlowED não transforma ciência em dogma, experiência local em verdade universal nem score em julgamento oficial. O princípio é que sustentação científica, normativa e empírica seja um fator importante, visível e rastreável nas decisões técnicas e filosóficas de um time.

O contrato deve permitir representar, transportar, consultar e relacionar reconhecimento, influência, estado, evidência operacional, lacunas e divergências. A forma de classificar, ranquear, ponderar ou compor esses sinais pertence aos providers/classificadores escolhidos pelo adotante.

COR ou qualquer classificador futuro é materialização possível, não parte normativa do pilar. Ferramentas concorrentes que cumpram o mesmo contrato são igualmente admissíveis.

### Pilar 4 — Progressividade governada

A forma de trabalhar deve poder variar e evoluir conforme necessidade, contexto, risco, maturidade e evidência, sem impor antecipadamente toda a complexidade possível.

Progressividade é uma capacidade contratual: deve ser possível representar configuração vigente, contexto, mudança, justificativa, autoridade, resultado e eventual manutenção, aumento, redução, pausa ou reversão.

O FlowED não determina a engine, algoritmo, policy framework ou ferramenta responsável por recomendar, decidir ou executar essa progressão. A materialização permanece livre dentro do contrato.

Sustentabilidade, proporcionalidade e redução de burocracia são consequências esperadas de uma progressão bem governada. Complexidade máxima não é sinônimo de maturidade.

## 4. Princípios como aprofundamento progressivo dos pilares

Os princípios não competem com os pilares. Eles são o próximo nível de zoom: dissecam, explicam e tornam operacionalmente compreensíveis as ideias contidas nos pilares.

Essa relação também deve orientar a futura documentação dinâmica do manifesto:

**missão → tese → invariante transversal → fluxo fundamental → pilares → princípios → mecanismos → evidências/linhagem cognitiva**.

A progressividade de apresentação não significa que o interlocutor escolhe livremente qualquer profundidade e assume o risco de omitir informação necessária. A projeção deve ser governada pela intenção, papel, contexto e objetivo do interlocutor.

O sistema conceitual deve determinar qual é a informação mínima suficiente para que aquele interlocutor compreenda e execute corretamente o que precisa fazer, incluindo o racional necessário para interpretação e crítica. O interlocutor pode aprofundar além desse mínimo quando desejar, mas não deve poder omitir silenciosamente aquilo que o próprio contexto torna necessário.

Da mesma forma, o sistema não deve despejar automaticamente toda a informação disponível. O objetivo é fornecer **somente a informação necessária, mas nunca menos que a necessária**.

### Princípios candidatos

1. **Uma intenção, muitas materializações governadas.**
2. **Uma linguagem comum, muitas tecnologias.**
3. **Domínios são pares e soberanos internamente.**
4. **Rígido no contrato, livre na materialização.**
5. **Conformidade contratual não implica superioridade da implementação.**
6. **O conhecimento do time pode modificar conscientemente o modo de trabalho.**
7. **Aprendizado relevante deve deixar rastros reutilizáveis.**
8. **O consolidado é uma projeção do conhecimento, não o conhecimento inteiro.**
9. **A projeção normativa depende da intenção, do papel, do contexto e do objetivo do interlocutor.**
10. **A projeção deve fornecer somente a informação necessária, mas nunca menos que a necessária.**
11. **Divergir é permitido; esconder a divergência não.**
12. **Ausência de sustentação não invalida automaticamente uma decisão operacional.**
13. **Toda referência relevante deve declarar sua sustentação científica, normativa e/ou empírica disponível.**
14. **O baseline é ponto de partida, não verdade nem ponto final.**
15. **O FlowED deve poder ser superado por evidência melhor que a sua própria.**
16. **A sofisticação da engenharia pode crescer sem burocracia proporcional.**
17. **Experimentar uma nova prática deve ser mais barato que reconstruir a organização.**
18. **Artefatos nativos permanecem soberanos e portáveis.**
19. **O mesmo modelo mental deve poder acompanhar estudante, profissional, equipe e empresa ao longo do crescimento.**
20. **O próprio FlowED deve explicar sua evolução usando os mecanismos que exige de seus usuários.**
21. **Uma referência adotada deve permanecer aberta à evidência produzida por seu próprio uso.**
22. **Evidência pode confirmar, enfraquecer ou invalidar uma referência; uso não é confirmação automática.**

## 5. Mecanismos estruturais

Os mecanismos não são pilares nem obrigações tecnológicas; são formas possíveis de realizar os contratos e podem evoluir ou ser substituídos tecnicamente.

- clientes como CLI, API, SDK, UI ou agentes;
- providers/materializadores/adapters substituíveis;
- configuração de intensidade por contexto;
- linguagem operacional comum de intenções;
- contratos e governança de materialização;
- baseline versionado;
- referências com proveniência e estado de sustentação;
- classificadores/avaliações quando desejados pelos adotantes;
- perfis de comportamento e evolução;
- registro histórico de decisões e resultados;
- EDT/CCP/CCC como referências candidatas para autoeducação e caminho cognitivo;
- projeções dinâmicas orientadas por intenção, papel, contexto e objetivo;
- MyTrues como possível materialização de memória decisória/proveniência;
- stacks de eventos, observabilidade, evidência e policy como materializações possíveis, nunca obrigatórias por nome.

## 6. Estados de evolução de uma hipótese ou referência

A evolução conceitual deve permitir trabalhar com algo ainda não plenamente comprovado sem tratá-lo como verdade e sem bloquear o desenvolvimento.

### 6.1 Estado de realizabilidade

Exemplos provisórios:

- desconhecido;
- realizável em princípio / escopo aberto;
- realizabilidade parcialmente demonstrada;
- realizabilidade demonstrada no escopo declarado.

Este eixo responde: **é possível fazer?**

### 6.2 Sustentação / evidência

A referência pode iniciar sem sustentação admissível suficiente. Uso controlado, experimentação, observação, evidência científica/normativa/operacional e replicação podem modificar sua sustentação conforme regras ainda a pesquisar e formalizar.

Este eixo responde: **quão sustentada está a referência e por quais sinais?**

Não misturar inviabilidade, desconhecimento e ausência de evidência em um mesmo número.

## 7. Critério futuro de Full FlowED

Hipótese de trabalho: Full FlowED não deve significar seguir o baseline nem utilizar ferramentas oficiais. Deve significar cumprir o conjunto de contratos constitutivos e obrigações públicas aplicáveis.

É plausível que uma futura definição de Full FlowED exija:

- conformidade com os contratos constitutivos aplicáveis;
- rastreabilidade mínima das referências relevantes;
- tratamento explícito de divergências;
- preservação histórica suficiente;
- capacidade de expor sustentação científica, normativa e/ou empírica disponível;
- critérios mínimos de realizabilidade quando uma hipótese sustenta mecanismos críticos;
- progressão e mudança governadas quando aplicáveis.

Os limiares não estão definidos e não devem ser inventados antes de pesquisa e uso prático.

O provider concreto usado para cumprir cada contrato permanece livre. Um materializador oficial, educacional, empresarial, open source, proprietário ou desenvolvido internamente pode satisfazer Full FlowED desde que cumpra as obrigações contratuais correspondentes.

## 8. O manifesto como primeira autoaplicação do fluxo

O manifesto deve obedecer ao fluxo fundamental que propõe:

**esboço → debate → refinamento → versão preliminar → uso real → evidência → alteração de sustentação → revisão**.

A prática não transforma automaticamente uma regra em verdade. Ela produz evidência operacional que pode aumentar, manter ou reduzir sua sustentação quando houver exposição, resultado e rastreabilidade suficientes.

O manifesto definitivo não deve existir apenas como texto estático. Sua publicação deve demonstrar a própria tese de documentação normativa dinâmica:

- existir uma referência canônica/versionada;
- preservar a linhagem cognitiva e decisória relevante;
- determinar projeções diferentes segundo intenção, papel, contexto e objetivo do interlocutor;
- assegurar um mínimo informacional obrigatório quando o contexto o exigir;
- permitir aprofundamento progressivo do "o quê" até o "por quê";
- permitir crítica e evolução rastreáveis;
- manter a projeção curta sem apagar a cadeia que a sustenta.

Um site do manifesto é candidato natural para materializar essa experiência, mas a tecnologia concreta não faz parte do princípio.

## 9. Linhagem científica pretendida

A hipótese atual é que não exista um único ancestral já conhecido que cubra toda a combinação do FlowED. Portanto, o cenário de trabalho mais provável é:

**ancestrais científicos/normativos diversos → artigo-pai de síntese do FlowED → FlowED como materialização operacional.**

EDT deve ser tratado como ancestral principal do eixo de autoeducação. CCP/CCC precede EDT como hipótese metodológica de normalização da trajetória cognitiva.

Essa hipótese não elimina a busca de anterioridade: o artigo-pai só deve ser declarado necessário depois que a revisão confirmar que nenhum trabalho existente cobre adequadamente o animal completo.

## 10. Questões para debate antes da consolidação

1. **Unidade operacional e liberdade governada** é o melhor nome para o Pilar 1?
2. **Sustentação científica e empírica explícita** concentra corretamente o Pilar 3 sem sugerir que FlowED seja o julgador?
3. **Progressividade governada** representa melhor o Pilar 4, com sustentabilidade e proporcionalidade como consequências?
4. O fluxo fundamental deve permanecer acima dos pilares como comportamento transversal?
5. Quais princípios pertencem prioritariamente a cada pilar, admitindo relações secundárias entre eles?
6. Qual é o conjunto mínimo de contratos constitutivos para alguém se declarar Full FlowED?
7. Como formalizar futuramente a determinação da projeção normativa mínima suficiente sem opacidade ou perda de autonomia do interlocutor?
8. Como assegurar em cada novo domínio que o contrato não promova acidentalmente uma implementação de referência a requisito do FlowED?
