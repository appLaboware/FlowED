# Manifesto FlowED — versão preliminar 001

**Status:** hipótese operacional em simulação. Não normativa. Não certificável. Sujeita ao protocolo de evolução e à revisão por evidência.

## Missão

O FlowED existe para permitir que todos os domínios da Engenharia de Software sejam expressos por uma linguagem operacional comum, compondo práticas, ferramentas, evidências e decisões sem aprisionar a organização a uma implementação única e sem transformar crescimento em burocracia proporcional.

## Tese central

Uma organização deve poder aumentar sua sofisticação, abrangência e maturidade de engenharia sem exigir crescimento proporcional da complexidade operacional percebida pelas pessoas.

Para isso, o FlowED separa intenção de materialização, preserva contratos e rastreabilidade, transforma experiência em aprendizado reutilizável e exige que referências relevantes exponham sua sustentação científica, normativa e empírica.

## Regra transversal — contrato rígido, materialização livre

O FlowED é normativo no nível do contrato público e deliberadamente livre no nível da materialização concreta.

O contrato pode ser rigoroso sobre o que deve existir, o significado das operações, entradas e saídas públicas, estados, garantias observáveis, rastreabilidade mínima, compatibilidade e demais propriedades necessárias à interoperabilidade e à governança. Ele não deve impor algoritmo, arquitetura interna, framework, produto, fornecedor ou tecnologia quando esses detalhes não fizerem parte da garantia pública.

Qualquer implementação capaz de cumprir integralmente o contrato aplicável é uma materialização válida daquela capability FlowED. Implementações de referência servem para demonstrar realizabilidade e oferecer caminhos prontos, mas não recebem autoridade normativa adicional.

Conformidade contratual não equivale a qualidade, confiabilidade ou preferência por uma implementação. Essas avaliações pertencem ao time, à organização e às políticas que adotarem, exceto quando uma propriedade estiver explicitamente incluída no próprio contrato.

## Fluxo fundamental

O FlowED entende evolução como um ciclo governado:

**esboço → debate → refinamento → versão preliminar → uso real → evidência → alteração de sustentação → revisão → novo ciclo**.

Uso não confirma automaticamente uma referência. Evidência pode fortalecê-la, mantê-la, enfraquecê-la, restringi-la a determinado contexto ou justificar seu abandono.

## Pilar 1 — Unidade operacional e liberdade governada

Todos os domínios da Engenharia de Software devem poder participar de uma linguagem operacional comum sem perder soberania interna e sem se tornarem presos a uma ferramenta, metodologia ou fornecedor.

Liberdade não significa ausência de controle. Múltiplas materializações são permitidas desde que cumpram os contratos públicos aplicáveis e permaneçam inteligíveis, rastreáveis, interoperáveis e substituíveis dentro das garantias contratadas.

O FlowED padroniza a expressão de intenção, a semântica pública e os contratos de interação; não obriga a padronização das tecnologias concretas. Artefatos permanecem nativos e utilizáveis fora do FlowED.

## Pilar 2 — Autoeducação e conhecimento vivo

Uma organização não deve apenas executar processos. Ela deve ser capaz de transformar execução em memória operacional estruturada e relacionável ao conhecimento que a motivou, permitindo que experiência, decisão e evidência retroalimentem conscientemente a evolução da forma de trabalhar.

O FlowED exige essa capacidade no nível contratual, não uma tecnologia específica de memória, logging, event stream, proveniência ou conhecimento. Diferentes materializações podem atender ao mesmo contrato.

O conhecimento consolidado não é o conhecimento inteiro. É uma projeção adequada a um interlocutor e a um objetivo. Racional, proveniência, alternativas, divergências, evidências e revisões devem poder permanecer acessíveis para aprendizagem, crítica e evolução.

EDT, CCP/CCC, MyTrues e composições de tecnologias de eventos, observabilidade e provenance permanecem referências e materializações candidatas, não requisitos tecnológicos do pilar.

## Pilar 3 — Sustentação científica e empírica explícita

Toda referência relevante deve tornar explícita sua relação com o conhecimento científico e normativo disponível e com a evidência empírica observada no contexto em que é usada.

O FlowED não transforma ciência em dogma, experiência local em verdade universal nem score em julgamento oficial. Ele defende que sustentação científica, normativa e empírica seja um fator importante e visível nas decisões técnicas e filosóficas de um time.

O contrato deve permitir representar, transportar, consultar e relacionar origem, reconhecimento, influência, estado, evidência operacional, lacunas e divergências de uma referência. A forma de classificar, ranquear, ponderar ou compor esses sinais pertence aos classificadores e às políticas escolhidas pelo adotante, não ao FlowED.

Uma referência pode ser usada com sustentação baixa ou inexistente quando isso for conscientemente necessário, desde que a condição permaneça explícita e rastreável. Diferentes ferramentas podem emitir avaliações ou opiniões distintas sobre a mesma evidência sem deixar de ser compatíveis com o FlowED, desde que cumpram o contrato aplicável.

## Pilar 4 — Progressividade governada

A forma de trabalhar deve poder variar e evoluir de maneira governada conforme contexto, risco, maturidade, necessidade e evidência, sem impor antecipadamente toda a complexidade possível.

O contrato FlowED deve tornar possível representar a configuração vigente, o contexto que a condiciona, a mudança proposta ou realizada, sua justificativa, autoridade, efeitos observáveis e possibilidade de manutenção, aumento, redução, pausa ou reversão.

O FlowED não deve impor a engine, algoritmo, policy system ou ferramenta que decide, recomenda ou executa essa progressão. Qualquer materialização que cumpra o contrato aplicável é aceitável.

Progressividade não é crescimento automático. Complexidade máxima não é sinônimo de maturidade; reduzir rigor ou capacidade pode ser uma decisão tão válida quanto aumentá-los quando o contexto e a evidência assim justificarem.

## Princípios preliminares

1. Uma intenção pode admitir muitas materializações governadas.
2. Uma linguagem comum pode coexistir com muitas tecnologias.
3. Domínios são pares e soberanos internamente, mas interoperam por contratos explícitos.
4. O FlowED é rígido no contrato e livre na materialização.
5. Cumprir o contrato não torna uma implementação automaticamente melhor que outra.
6. O conhecimento do time pode modificar conscientemente o modo de trabalho.
7. Aprendizado relevante deve deixar rastros reutilizáveis.
8. O consolidado é uma projeção do conhecimento, não o conhecimento inteiro.
9. A projeção normativa depende da intenção, do papel, do contexto e do objetivo do interlocutor.
10. A projeção deve fornecer somente a informação necessária, mas nunca menos que a necessária.
11. Divergir é permitido; esconder a divergência não.
12. Ausência de sustentação não invalida automaticamente uma decisão operacional.
13. Toda referência relevante deve declarar a sustentação disponível e suas lacunas.
14. O baseline é ponto de partida, não verdade nem destino obrigatório.
15. O FlowED deve poder ser superado por evidência melhor que a sua própria.
16. A sofisticação da engenharia deve poder crescer sem burocracia proporcional.
17. Experimentar uma prática deve ser mais barato que reconstruir a organização.
18. Artefatos nativos permanecem soberanos e portáveis.
19. O mesmo modelo mental deve poder acompanhar estudante, profissional, equipe e organização ao longo do crescimento.
20. O próprio FlowED deve explicar e registrar sua evolução usando os mecanismos que exige de seus usuários.
21. Uso produz evidência; não produz verdade automática.

## Documentação normativa dinâmica

Uma referência normativa não deve ser tratada apenas como um texto estático entregue igualmente a todos. Sua apresentação deve ser projetada a partir da intenção, do papel, do contexto e do objetivo do interlocutor.

O interlocutor não deve ser obrigado a escolher sozinho quanta informação precisa, pois pode desconhecer aquilo que deveria conhecer. O sistema deve determinar um mínimo informacional necessário, permitir aprofundamento e explicar por que determinada informação foi considerada necessária.

A referência canônica continua existindo para versionamento e auditoria, mas o consumo é uma projeção dinâmica do conhecimento disponível.

## Autoaplicação

Este manifesto é a primeira referência submetida ao próprio fluxo FlowED. Sua existência inicial vale como hipótese operacional, não como comprovação.

Seus gaps, ambiguidades, conflitos e falhas serão registrados como parte da própria evolução. O objetivo é produzir uma primeira simulação de memória epistemológica e decisória sem pressupor que uma materialização específica já esteja implementada.

## Critério de revisão

Esta versão deverá ser revisada sempre que o uso, a crítica, uma nova evidência, uma contradição interna ou um gap relevante justificar alteração de entendimento. Cada alteração relevante deve preservar o estado anterior, a razão da mudança, a evidência conhecida e o impacto esperado.
