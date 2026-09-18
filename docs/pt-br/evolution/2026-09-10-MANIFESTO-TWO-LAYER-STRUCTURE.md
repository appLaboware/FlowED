# Manifesto FlowED — hipótese de estrutura em duas camadas

**Status:** exploração conceitual. Não normativa.

## Intuição desta rodada

Os três princípios atualmente em formação parecem ocupar um nível filosófico mais fundamental do que vários elementos dos manifestos preliminares anteriores.

1. **Separação entre Intenção e Materialização** — questiona o acoplamento entre o que se quer e a forma contingente de realizá-lo.
2. **Coerência Operacional** — questiona a fragmentação da forma de trabalhar entre domínios e ferramentas sem exigir uniformidade tecnológica.
3. **Foco no Caminho Cognitivo** — questiona a primazia do consolidado sobre o racional estruturado que produz, explica e permite revisar decisões.

Esses três princípios podem ser apresentados menos como ordens e mais como **proposições filosóficas abertas à reflexão**. O manifesto poderia deixar explícito que suas frases condensam perguntas recorrentes observadas na prática, no ensino e no estudo da Engenharia de Software, sem alegar criação de ideias inéditas.

Formulação introdutória candidata:

> **Este manifesto nasce de perguntas recorrentes sobre como a Engenharia de Software trabalha, aprende e evolui. As proposições a seguir não pretendem encerrar o raciocínio; condensam questões que convidam o leitor a examiná-las, contestá-las e desenvolvê-las.**

Outra formulação candidata:

> **Não reivindicamos ter criado os princípios que seguem. Propomos reconsiderar a ordem de importância que damos a ideias já presentes na ciência, nos padrões e na prática da engenharia.**

## Segunda camada: o que defendemos por causa desses princípios

Vários elementos dos manifestos 001/002 parecem mais fortes quando tratados não como novas filosofias independentes, mas como **compromissos derivados** dos três princípios.

A estrutura sugerida é:

**proposições filosóficas → portanto → compromissos FlowED → contratos públicos → materializações substituíveis**

Isso explicita o racional do próprio manifesto: os compromissos de baixo não surgem como lista arbitrária de funcionalidades; decorrem das posições filosóficas de cima.

### Memória operacional e aprendizagem pela execução

A capacidade de registrar execução não precisa ser um quarto princípio filosófico. Ela pode ser uma consequência do Foco no Caminho Cognitivo quando a experiência operacional passa a integrar o caminho de revisão do conhecimento: decisão → execução → resultado → evidência → revisão.

A filosofia é: conhecimento decisório deve poder continuar e evoluir.

O compromisso derivado é: experiências relevantes devem poder ser relacionadas às decisões que as motivaram, para que resultados posteriores realimentem conscientemente o caminho cognitivo.

A materialização concreta — eventos, logs, provenance, OpenTelemetry, CDEvents, event stores etc. — pertence ao produto/ecossistema, não ao princípio filosófico.

### Sustentação explícita

Razões, evidências, alternativas, divergências, incertezas e autoria das avaliações são componentes naturais do caminho cognitivo decisório. Assim, a exigência de sustentação explícita pode ser apresentada como compromisso derivado do terceiro princípio, em vez de princípio filosófico independente.

A filosofia é: uma determinação deve poder mostrar o racional que a sustenta.

O compromisso derivado é: referências e decisões relevantes devem poder tornar visíveis as evidências e lacunas que participam de seu racional, preservando autoria e sem confundir avaliação com verdade.

O scoring, ranking e os providers que materializam essa visibilidade continuam fora da filosofia.

### Progressividade governada

Progressividade também parece melhor como compromisso derivado. Ela resulta da combinação dos três princípios: se intenção e materialização são separáveis, se a organização pode preservar coerência sem uniformidade e se decisões podem ser compreendidas e revistas por seu caminho cognitivo, então mudar intensidade, rigor ou materialização conforme contexto pode ser tratado como decisão explícita e revisável.

A filosofia não precisa afirmar uma mecânica de progressão. O compromisso FlowED pode afirmar que a forma de trabalhar deve poder mudar conscientemente, com contexto, razão e rastreabilidade, sem tratar complexidade máxima como maturidade.

## Distinção importante: derivado não significa produto

Os antigos pilares não precisam ser classificados simplesmente como "produto". Há uma camada intermediária mais precisa:

- **filosofia:** por que algo importa;
- **compromissos derivados do manifesto:** o que o FlowED passa a defender por causa da filosofia;
- **contratos públicos:** o comportamento/capacidade que torna o compromisso verificável;
- **produto/materialização:** uma maneira concreta de cumprir o contrato.

Isso evita tanto transformar o manifesto em catálogo de funcionalidades quanto empurrar todo compromisso para o executável `flwd`.

## Ciência como exemplo do caminho cognitivo

A ciência oferece forte analogia para o terceiro princípio porque artigos, revisões, replicações, críticas e novos trabalhos tornam razões e evidências discutíveis e cumulativas. Porém, não convém descrevê-la como uma sucessão linear em que cada nível acadêmico corresponde a uma etapa fixa do caminho cognitivo; isso varia entre áreas e sistemas educacionais. O ponto aproveitável é mais geral: conhecimento científico se fortalece quando afirmações podem ser relacionadas a método, evidência, crítica, revisão e trabalhos anteriores.

## Possível fechamento autoaplicável

A ideia proposta para o encerramento é forte porque transforma criticabilidade em teste do próprio manifesto.

Formulações candidatas:

> **Se o FlowED estiver errado, ele próprio deve ajudar a demonstrá-lo.**

> **Se a crítica e a evidência mostrarem que este manifesto está errado, no todo ou em parte, seus próprios princípios exigem que ele seja revisto.**

A primeira é mais memorável e levemente provocativa. A segunda explicita a consequência. Elas podem aparecer juntas, uma como frase de fechamento e outra como explicação.

## Hipótese estrutural para próxima consolidação

Uma forma possível para o Manifesto FlowED passa a ser:

1. introdução — origem nas perguntas recorrentes, ausência de reivindicação de ineditismo e convite à crítica;
2. três proposições/princípios filosóficos;
3. transição explícita — **"Por isso, defendemos que..."**;
4. compromissos derivados: contrato/materialização, memória/aprendizagem, sustentação, progressividade, substituibilidade, criticabilidade e autoaplicação;
5. fechamento autoaplicável — o próprio FlowED deve poder ser contestado e superado pelos mecanismos que defende.

Esta estrutura ainda precisa de revisão antes de substituir o pré-manifesto atual.