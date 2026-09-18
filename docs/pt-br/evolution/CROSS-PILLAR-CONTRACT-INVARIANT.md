# Invariante transversal — rigidez contratual e liberdade de materialização

**Status:** decisão conceitual para orientar o fechamento do Manifesto FlowED.

## 1. Regra transversal

Os pilares do FlowED devem afirmar **o que precisa ser verdadeiro no comportamento público**, e não qual ferramenta deve existir para produzi-lo.

> **O FlowED é rígido no contrato e livre na materialização.**

O contrato pode ser preciso, versionado, testável e obrigatório para a capability correspondente. A tecnologia, produto, framework, provider, adapter, linguagem, banco, broker, classificador ou arquitetura interna usada para satisfazê-lo não é prescrita pelo FlowED.

## 2. Manifesto, contrato e produto

A arquitetura conceitual deve manter três responsabilidades separadas:

- **Manifesto FlowED:** afirma o que consideramos importante e por quê;
- **Contratos públicos FlowED:** tornam essas posições operacionalmente representáveis, testáveis e interoperáveis;
- **produto FlowED / `flwd`:** cliente/runtime oficial de referência que operacionaliza os contratos, acionando capabilities no hub horizontal e providers/adapters substituíveis.

O produto oficial pode possuir defaults, integrações, UX, adapters e materializações de referência. Isso não transforma esses elementos em obrigação normativa.

## 3. Conformidade não é qualidade do provider

Cumprir um contrato FlowED responde a uma pergunta de conformidade: **a implementação entrega o comportamento público prometido?**

Não responde, por si só, se aquela implementação é a melhor, mais confiável, mais precisa ou mais bem sustentada entre as disponíveis.

Essa distinção é constitutiva:

- **contrato/conformidade:** responsabilidade do FlowED;
- **qualidade, confiabilidade, precisão, validade ou utilidade da opinião produzida:** responsabilidade do provider/materializador e de sua própria sustentação;
- **escolha entre providers conformantes:** decisão livre e governada da organização adotante.

Logo, um provider pode ser plenamente conforme ao contrato e ainda possuir sustentação empírica fraca, baixa maturidade ou uma metodologia discutível. Isso não o torna automaticamente não-FlowED; torna sua qualidade uma propriedade que deve ser avaliada separadamente.

## 4. Atribuição de opiniões

Quando um provider produz score, ranking, recomendação, diagnóstico ou qualquer outra saída opinativa, o FlowED deve preservar sua autoria.

Exemplo conceitual correto:

> **segundo COR, a referência recebeu avaliação X.**

Isso não equivale a:

> **o FlowED avalia a referência como X.**

O FlowED pode definir como uma opinião é identificada, transportada, consultada e relacionada. O conteúdo, confiabilidade e metodologia da opinião continuam pertencendo ao provider.

## 5. Dogfood epistemológico dos providers

As próprias ferramentas e classificadores podem ser tratados como referências avaliáveis pelo Pilar 3.

Assim, a confiabilidade de um classificador não precisa ser embutida no contrato que ele implementa. Ela pode ser representada como sustentação do próprio provider: publicações, validações, benchmarks, histórico de uso, incidência de erro, cobertura, replicações e demais evidências aplicáveis.

Isso permite separar:

**conformidade contratual do provider**

 de

**força da evidência que sustenta o provider**.

A primeira pode ser determinística por testes de contrato; a segunda pode evoluir com evidência científica e operacional.

## 6. O que pertence ao contrato

Pertencem ao nível normativo/contratual:

- significado da capability;
- operações e conceitos públicos necessários;
- entradas, saídas, estados e erros observáveis;
- invariantes e garantias públicas;
- evidência/rastreabilidade mínima da execução quando necessária;
- regras de compatibilidade e versionamento;
- condições de conformidade;
- identidade/autoria do provider quando a saída carregar julgamento próprio;
- metadados necessários para interpretar corretamente uma saída.

O contrato pode exigir que uma ferramenta identifique metodologia, versão, escala ou inputs quando isso for indispensável à correta interpretação da saída. Isso não significa que o FlowED certifique a qualidade daquela metodologia.

## 7. O que não pertence ao contrato

Não pertencem ao nível normativo, salvo quando uma propriedade concreta for indispensável ao comportamento público:

- produto específico;
- implementation stack;
- framework;
- banco de dados;
- message broker;
- linguagem de programação;
- algoritmo interno;
- dashboard específico;
- provider oficial;
- adapter específico;
- topologia interna da solução;
- fórmula de score de um classificador;
- ranking normativo de qual provider é "melhor";
- confiabilidade científica ou empírica presumida de uma ferramenta apenas por ela ser referência do ecossistema.

## 8. Materialização de referência sem privilégio normativo

O ecossistema FlowED pode produzir ferramentas próprias por composição de tecnologias maduras para demonstrar realizabilidade, oferecer uma alternativa pronta, gerar dogfood/evidência operacional e acelerar adoção.

Entretanto, a ferramenta de referência é apenas **um provider possível**. Produto de terceiro, implementação interna ou ferramenta concorrente podem ocupar o mesmo papel se cumprirem o contrato público aplicável.

O `flwd` é o cliente/runtime oficial de referência que torna a rede de contratos utilizável. Ele não elimina a liberdade das materializações que aciona.

## 9. Full FlowED

**Full FlowED é uma condição de conformidade, não uma condição de uso de software.**

Uma organização ou ecossistema pode ser Full FlowED sem usar uma única linha de código, CLI, adapter, hub ou provider produzido pela LaboWare, desde que cumpra integralmente os contratos constitutivos aplicáveis.

Consequências:

- ferramenta oficial que viola contrato -> não conforme;
- ferramenta de terceiro que cumpre contrato -> conforme;
- ferramenta própria do time que cumpre contrato -> conforme;
- ecossistema inteiramente independente que cumpre todos os contratos constitutivos -> elegível a Full FlowED;
- uso integral da stack oficial sem cumprimento contratual -> não é Full FlowED apenas por usar produtos oficiais.

A escolha entre providers conformantes permanece livre à organização e pode ser guiada por suas próprias políticas, evidências, custos, riscos e preferências.

## 10. Auditoria dos pilares sob este invariante

### Pilar 1 — alinhado

É o guardião da separação entre linguagem/contrato público e implementação substituível. Linguagem comum não significa tecnologia comum.

### Pilar 2 — alinhado após correção

O pilar defende a capacidade de transformar execução e conhecimento em memória reutilizável e relacionável. O contrato deve expressar somente as capacidades públicas necessárias de memória, correlação, provenance e recuperação.

MyTrues, CDEvents, OpenTelemetry, OCEL, Kafka e tecnologias semelhantes são referências/materializações candidatas e provas de realizabilidade, não requisitos do pilar.

### Pilar 3 — alinhado após correção

O pilar defende que sustentação científica, normativa e empírica seja informação relevante e visível nas decisões.

O contrato deve permitir representar, transportar e consultar evidências e opiniões atribuídas. **O FlowED não ranqueia, não mede e não julga por conta própria.** COR e classificadores concorrentes respondem por suas fórmulas, rankings, percentis, pesos e metodologias.

### Pilar 4 — alinhado por princípio, ainda em fechamento

O pilar deve defender progressividade contextual e governada. O contrato deve representar as informações e decisões necessárias à progressão, manutenção, redução, pausa ou reversão.

OPA, OpenFeature, Argo, engines próprias ou outros mecanismos são apenas provas de realizabilidade e materializações possíveis.

## 11. Regra de crítica

A separação organiza as críticas futuras:

- **"isso não deveria ser importante"** -> crítica ao Manifesto FlowED;
- **"o contrato não consegue expressar/garantir X"** -> crítica ao contrato FlowED;
- **"a ferramenta calcula/implementa mal X"** -> crítica ao provider/materializador;
- **"o `flwd` não orquestra/valida/projeta corretamente"** -> crítica ao produto de referência.

## 12. Consequência para naming

A ambiguidade entre `FlowED` como filosofia/ecossistema e `flwd` como produto executável deve ser tratada explicitamente. A recomendação provisória é manter a marca-raiz FlowED para o manifesto e os contratos e reservar `flwd`/distribuição LaboWare para a materialização oficial.

Documento relacionado: `FLOWED-NAMING-AND-CONFORMANCE-SEPARATION-DRAFT.md`.

## 13. Consequência para o manifesto final

O manifesto final deve falar em **obrigações filosóficas, contratuais e comportamento público**, não em ferramentas específicas.

Estrutura:

**pilar -> obrigação pública -> contrato -> conformidade**

Materialização:

**contrato -> provider/materializador A | B | C | implementação própria**

Ferramentas de referência aparecem como evidência de realizabilidade e opções do ecossistema, nunca como condição ontológica do FlowED.
