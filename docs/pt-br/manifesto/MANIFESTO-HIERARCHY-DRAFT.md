# Esboço de hierarquia do Manifesto FlowED

**Status:** proposta de trabalho — não normativa, sujeita a debate e refinamento.

Este documento organiza o material histórico e conceitual atual do FlowED em níveis de importância. Ele não substitui o manifesto histórico nem congela terminologia. Sua função é permitir debate estruturado antes da versão preliminar do manifesto.

## 0. Missão

**Cobrir todos os domínios da Engenharia de Software por uma linguagem operacional comum e uma arquitetura modular capaz de crescer horizontalmente por domínios pares e verticalmente por materializadores/adapters, permitindo que a organização evolua sua própria forma de trabalhar sem perder rastreabilidade, conhecimento acumulado, liberdade tecnológica ou sustentabilidade.**

A missão é o nível superior. Pilares, princípios e mecanismos existem para realizá-la.

## 1. Tese central

O FlowED parte da hipótese de que a Engenharia de Software pode aumentar sua sofisticação, abrangência e maturidade sem exigir crescimento proporcional da complexidade operacional percebida pelas pessoas.

Para isso, separa intenção de materialização, preserva uma linguagem operacional comum, permite composição modular e transforma a experiência da organização em insumo rastreável para sua própria evolução.

## 2. Fluxo fundamental de evolução

O FlowED não trata uma referência adotada como conhecimento congelado. Sua forma de trabalhar deve evoluir por um fluxo explícito e recorrente:

**esboço → debate → refinamento → versão preliminar → uso real → evidência → alteração de sustentação/score → revisão → novo ciclo**.

Este fluxo é candidato a elemento central do manifesto, e não apenas ao processo usado para escrevê-lo. Ele representa como uma organização FlowED transforma hipótese em prática, prática em evidência e evidência em evolução consciente.

O ciclo não pressupõe que uso confirme uma regra. A experiência pode aumentar, manter ou reduzir sua sustentação; revelar inadequação contextual; produzir divergência; ou levar ao abandono da referência. O valor está em tornar a evolução observável, rastreável, criticável e reutilizável.

O próprio manifesto deve percorrer esse fluxo. Assim, sua versão preliminar não será apresentada como verdade final: será uma referência utilizável cuja sustentação deverá evoluir com aplicação, observação e crítica.

## 3. Quatro pilares propostos

Os pilares formam o primeiro nível de compreensão abaixo da missão e da tese central. Devem ser poucos, estáveis e suficientemente amplos para explicar o animal sem exigir que o interlocutor conheça seus mecanismos internos.

### Pilar 1 — Unidade operacional e liberdade governada

Todos os domínios da Engenharia de Software devem poder participar de uma mesma linguagem operacional sem perder sua soberania interna nem ficar presos a uma implementação concreta.

A liberdade de materialização não é liberdade caótica. Ela existe dentro de intenções explícitas, contratos públicos, rastreabilidade, regras de composição e capacidade de substituição controlada.

O crescimento ocorre em três dimensões:

- horizontalmente, pela inclusão de domínios/capabilities pares em um hub comum;
- verticalmente, por materializadores/adapters substituíveis;
- em intensidade, pelo grau de rigor e profundidade com que cada capability é aplicada em determinado contexto.

FlowED padroniza a expressão de intenção e os contratos públicos, não as tecnologias concretas. Artefatos permanecem nativos e utilizáveis fora do FlowED.

Este pilar absorve o problema histórico da fragmentação metodológica e estabelece a ideia de liberdade governada: múltiplas materializações são permitidas, mas precisam continuar inteligíveis, rastreáveis, comparáveis e substituíveis.

### Pilar 2 — Autoeducação e conhecimento vivo

A organização não deve apenas executar um processo; deve aprender com a própria execução e ser capaz de transformar esse aprendizado em evolução consciente de sua forma de trabalhar.

No modelo atual, esse eixo é operacionalizado principalmente pelo **Education-Driven Thinking (EDT)**. O **Creator's Cognitive Path / Caminho Cognitivo do Criador (CCP/CCC)** é tratado como pré-requisito metodológico pretendido do EDT para normalizar e tornar rastreável o percurso cognitivo relevante à criação de decisões, normas, práticas e conhecimento.

Decisões, razões, mudanças, resultados e aprendizados relevantes devem poder ser preservados e reutilizados. O conhecimento consolidado é uma projeção adequada a um interlocutor e objetivo, não o conhecimento inteiro.

Assim, memória, continuidade e documentação normativa dinâmica são consequências necessárias deste pilar, e não um pilar separado.

### Pilar 3 — Sustentação científica e empírica explícita

Toda referência relevante deve tornar explícita sua relação com o conhecimento científico e normativo disponível e com a evidência empírica observada em seu contexto de uso.

FlowED não transforma ciência em dogma nem experiência local em verdade universal. O princípio é outro: uma decisão deve declarar o que a sustenta, o que a contradiz, o que ainda é desconhecido e qual parte de sua sustentação vem de ciência, norma, experimento, operação ou decisão contextual.

Quando não houver sustentação suficiente, a referência pode continuar operacionalmente adotada, mas sua fragilidade deve permanecer visível e refletida no estado de evidência/score correspondente.

O uso real participa desse pilar porque produz evidência. Testes, experimentos, resultados operacionais, falhas, replicações e observações podem aumentar, manter ou reduzir a sustentação de uma referência.

Assim, o FlowED exige **ligação explícita com evidência**, não obediência automática a uma fonte externa.

### Pilar 4 — Progressividade governada

A sofisticação da Engenharia de Software deve crescer conforme necessidade, contexto, risco, maturidade e evidência, sem impor antecipadamente toda a complexidade possível.

Progressividade é o princípio ativo deste pilar. Sustentabilidade, proporcionalidade e redução de burocracia são consequências esperadas de uma progressão bem governada.

Uma implantação pode começar mínima e aumentar largura, profundidade e intensidade à medida que o contexto justificar. O crescimento deve preservar rastreabilidade e capacidade futura de evolução, evitando tanto subengenharia persistente quanto complexidade prematura.

O FlowED preserva do manifesto histórico a prioridade dada ao crescimento do time, à sustentabilidade do projeto e à implantação progressiva, mas reorganiza esses elementos sob uma ideia mais concentrada: **crescer quando houver razão para crescer e saber por que cresceu**.

## 4. Princípios como aprofundamento progressivo dos pilares

Os princípios não competem com os pilares. Eles são o próximo nível de zoom: dissecam, explicam e tornam operacionalmente compreensíveis as ideias contidas nos pilares.

Essa relação também deve orientar a futura documentação dinâmica do manifesto:

**missão → tese → fluxo fundamental → pilares → princípios → mecanismos → evidências/linhagem cognitiva**.

A progressividade de apresentação não significa que o interlocutor escolhe livremente qualquer profundidade e assume o risco de omitir informação necessária. A projeção deve ser governada pela **intenção, papel, contexto e objetivo do interlocutor**.

O sistema conceitual deve determinar qual é a informação mínima suficiente para que aquele interlocutor compreenda e execute corretamente o que precisa fazer, incluindo o racional necessário para interpretação e crítica. O interlocutor pode aprofundar além desse mínimo quando desejar, mas não deve poder omitir silenciosamente aquilo que o próprio contexto torna necessário.

Da mesma forma, o sistema não deve despejar automaticamente toda a informação disponível. O objetivo é fornecer **somente a informação necessária, mas nunca menos que a necessária**.

Essa regra é central para a documentação normativa dinâmica defendida pelo EDT: a projeção depende do interlocutor, mas não é arbitrariamente escolhida por ele.

### Princípios candidatos

1. **Uma intenção, muitas materializações governadas.**
2. **Uma linguagem comum, muitas tecnologias.**
3. **Domínios são pares e soberanos internamente.**
4. **Liberdade de implementação exige rastreabilidade e contratos explícitos.**
5. **O conhecimento do time pode modificar conscientemente o modo de trabalho.**
6. **Aprendizado relevante deve deixar rastros reutilizáveis.**
7. **O consolidado é uma projeção do conhecimento, não o conhecimento inteiro.**
8. **A projeção normativa depende da intenção, do papel, do contexto e do objetivo do interlocutor.**
9. **A projeção deve fornecer somente a informação necessária, mas nunca menos que a necessária.**
10. **Divergir é permitido; esconder a divergência não.**
11. **Score zero não invalida uma decisão operacional.**
12. **Toda referência relevante deve declarar sua sustentação científica, normativa e/ou empírica disponível.**
13. **O baseline é ponto de partida, não verdade nem ponto final.**
14. **O FlowED deve poder ser superado por evidência melhor que a sua própria.**
15. **A sofisticação da engenharia pode crescer sem burocracia proporcional.**
16. **Experimentar uma nova prática deve ser mais barato que reconstruir a organização.**
17. **Artefatos nativos permanecem soberanos e portáveis.**
18. **O mesmo modelo mental deve poder acompanhar estudante, profissional, equipe e empresa ao longo do crescimento.**
19. **O próprio FlowED deve explicar sua evolução usando os mecanismos que exige de seus usuários.**
20. **Uma referência adotada deve permanecer aberta à evidência produzida por seu próprio uso.**
21. **Evidência pode confirmar, enfraquecer ou invalidar uma referência; uso não é confirmação automática.**

## 5. Mecanismos estruturais

Os mecanismos não são pilares; são formas de realizar os pilares e podem evoluir tecnicamente.

- hub horizontal de domínios/capabilities;
- adapters/providers/materializadores verticais;
- configuração de intensidade por contexto;
- linguagem operacional comum de intenções;
- contratos e governança de materialização;
- baseline versionado;
- referências com proveniência e estado de sustentação;
- score/avaliação determinística onde os dados permitirem;
- perfis de comportamento e evolução, incluindo o candidato Risco-FlowED;
- registro histórico de decisões e resultados;
- EDT como mecanismo de autoeducação e evolução do conhecimento;
- CCP/CCC como mecanismo de normalização do caminho cognitivo relevante;
- projeções dinâmicas orientadas por intenção, papel, contexto e objetivo;
- MyTrues como possível materialização de memória/proveniência.

## 6. Estados de evolução de uma hipótese ou referência

A evolução conceitual deve permitir trabalhar com algo ainda não plenamente comprovado sem tratá-lo como verdade e sem bloquear o desenvolvimento.

Proposta inicial de separação entre dois eixos:

### 6.1 Estado de realizabilidade

Exemplos provisórios:

- desconhecido;
- realizável em princípio / escopo aberto;
- realizabilidade parcialmente demonstrada;
- realizabilidade demonstrada no escopo declarado.

Este eixo responde: **é possível fazer?**

### 6.2 Sustentação / evidência

Parte de score zero quando ainda não há sustentação admissível suficiente. Uso controlado, experimentação, observação, evidência científica/normativa/operacional e replicação podem aumentar a sustentação conforme regras ainda a pesquisar e formalizar.

Este eixo responde: **quão sustentada está a referência?**

Não misturar inviabilidade, desconhecimento e ausência de evidência em um mesmo número.

## 7. Critério futuro de Full FlowED

Hipótese de trabalho: Full FlowED não deve significar "seguir o baseline". Deve significar cumprir um conjunto mínimo obrigatório de mecanismos de governança, rastreabilidade e evolução.

É plausível que uma futura definição de Full FlowED exija:

- conformidade mínima com o protocolo FlowED;
- rastreabilidade mínima das referências relevantes;
- tratamento explícito de divergências;
- preservação histórica suficiente;
- ligação explícita das referências relevantes com sustentação científica, normativa e/ou empírica disponível;
- critérios mínimos de realizabilidade quando uma hipótese sustenta mecanismos críticos;
- eventual piso de sustentação/evidência para determinadas classes de referência.

Os limiares não estão definidos e não devem ser inventados antes de pesquisa e uso prático.

## 8. O manifesto como primeira autoaplicação do fluxo

O manifesto deve obedecer ao fluxo fundamental que propõe:

**esboço → debate → refinamento → versão preliminar → uso real → evidência → alteração de sustentação/score → revisão**.

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

## 10. Questões para debate antes da versão preliminar

1. **Unidade operacional e liberdade governada** é o melhor nome para o Pilar 1 ou há termo mais preciso para liberdade não caótica, rastreável e contratual?
2. **Sustentação científica e empírica explícita** concentra corretamente o Pilar 3 ou ainda mistura evidência com governança?
3. **Progressividade governada** representa melhor o Pilar 4, com sustentabilidade e proporcionalidade como consequências?
4. O fluxo fundamental de evolução deve ficar acima dos pilares, como comportamento transversal do FlowED, ou ser apresentado dentro do pilar de autoeducação?
5. Quais princípios pertencem prioritariamente a cada pilar, admitindo relações secundárias entre eles?
6. Qual é o conjunto mínimo obrigatório para alguém se declarar Full FlowED?
7. Como definir o primeiro estado utilizável de "realizável em princípio" sem fingir validação?
8. Como formalizar futuramente a determinação da projeção normativa mínima suficiente sem criar paternalismo, opacidade ou perda de autonomia do interlocutor?
