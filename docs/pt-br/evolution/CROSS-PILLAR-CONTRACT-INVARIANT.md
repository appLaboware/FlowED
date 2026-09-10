# Invariante transversal — rigidez contratual e liberdade de materialização

**Status:** decisão conceitual para orientar o fechamento do Manifesto FlowED.

## 1. Regra transversal

Os pilares do FlowED devem afirmar **o que precisa ser verdadeiro no comportamento público**, e não qual ferramenta deve existir para produzi-lo.

> **O FlowED é rígido no contrato e livre na materialização.**

O contrato pode ser preciso, versionado, testável e obrigatório para a capability correspondente. A tecnologia, produto, framework, provider, adapter, linguagem, banco, broker, classificador ou arquitetura interna usada para satisfazê-lo não é prescrita pelo FlowED.

## 2. Conformidade não é qualidade do provider

Cumprir um contrato FlowED responde a uma pergunta de conformidade: **a implementação entrega o comportamento público prometido?**

Não responde, por si só, se aquela implementação é a melhor, mais confiável, mais precisa ou mais bem sustentada entre as disponíveis.

Essa distinção é constitutiva:

- **contrato/conformidade:** responsabilidade do FlowED;
- **qualidade, confiabilidade, precisão, validade ou utilidade da opinião produzida:** responsabilidade do provider/materializador e de sua própria sustentação;
- **escolha entre providers conformantes:** decisão livre e governada da organização adotante.

Logo, um provider pode ser plenamente conforme ao contrato e ainda possuir sustentação empírica fraca, baixa maturidade ou uma metodologia discutível. Isso não o torna automaticamente não-FlowED; torna sua qualidade uma propriedade que deve ser avaliada separadamente.

## 3. Dogfood epistemológico dos providers

As próprias ferramentas e classificadores podem ser tratados como referências avaliáveis pelo Pilar 3.

Assim, a confiabilidade de um classificador não precisa ser embutida no contrato que ele implementa. Ela pode ser representada como sustentação do próprio provider: publicações, validações, benchmarks, histórico de uso, incidência de erro, cobertura, replicações e demais evidências aplicáveis.

Isso permite separar:

**conformidade contratual do provider**

 de

**força da evidência que sustenta o provider**.

A primeira pode ser determinística por testes de contrato; a segunda pode evoluir com evidência científica e operacional.

## 4. O que pertence ao contrato

Pertencem ao nível normativo/contratual:

- significado da capability;
- operações e conceitos públicos necessários;
- entradas, saídas, estados e erros observáveis;
- invariantes e garantias públicas;
- evidência/rastreabilidade mínima da execução quando necessária;
- regras de compatibilidade e versionamento;
- condições de conformidade;
- metadados necessários para interpretar corretamente uma saída.

O contrato pode exigir que uma ferramenta identifique sua metodologia, versão, escala, inputs e provenance quando isso for necessário para interpretar sua saída. Isso não significa que o FlowED certifique a qualidade daquela metodologia.

## 5. O que não pertence ao contrato

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
- ranking normativo de qual provider é "melhor";
- confiabilidade científica ou empírica presumida de uma ferramenta apenas por ela ser referência do ecossistema.

## 6. Materialização de referência sem privilégio normativo

O ecossistema FlowED pode produzir ferramentas próprias por composição de tecnologias maduras para demonstrar realizabilidade, oferecer uma alternativa pronta, gerar dogfood/evidência operacional e acelerar adoção.

Entretanto, a ferramenta de referência é apenas **um provider possível**. Produto de terceiro, implementação interna ou ferramenta concorrente podem ocupar o mesmo papel se cumprirem o contrato público aplicável.

Uma implementação de referência pode emitir opiniões próprias — por exemplo um classificador composto de evidência — desde que essas opiniões sejam identificadas como pertencentes ao provider e não promovidas a verdade normativa do FlowED.

## 7. Full FlowED

Full FlowED nunca deve depender do uso de uma ferramenta oficial específica.

Uma materialização que satisfaz integralmente o contrato aplicável é conformante àquela capability independentemente de quem a produziu.

- ferramenta oficial que viola contrato -> não conforme;
- ferramenta de terceiro que cumpre contrato -> conforme;
- ferramenta própria do time que cumpre contrato -> conforme;
- provider conforme mas fracamente sustentado -> conforme, porém com sustentação própria baixa/indefinida;
- provider conforme e fortemente sustentado -> conforme e com sustentação própria alta.

A escolha entre providers conformantes permanece livre à organização e pode ser guiada por suas próprias políticas, evidências, custos, riscos e preferências.

## 8. Auditoria dos pilares sob este invariante

### Pilar 1

Alinhado: separa linguagem/contrato público de implementação substituível e passa a ser o guardião transversal deste invariante.

### Pilar 2

O contrato deve exigir as capacidades públicas de memória, correlação e reutilização necessárias ao aprendizado. MyTrues, CDEvents, OpenTelemetry, OCEL, Kafka e demais tecnologias são referências/materializações possíveis e provas de realizabilidade, não requisitos do pilar.

### Pilar 3

O contrato deve exigir representação identificável de sustentação, provenance, estado, observações e saída de avaliação quando a capability oferecida assim exigir. Não deve exigir o classificador FlowED/LaboWare nem certificar que sua opinião é "confiável".

A confiabilidade do classificador é problema do próprio classificador e pode, recursivamente, ser avaliada como referência pelo Pilar 3.

### Pilar 4

Deve ser desenhado desde o início sob a mesma regra: comportamento público rígido, materialização livre e providers substituíveis.

## 9. Consequência para o manifesto final

O manifesto final deve falar em **obrigações contratuais e comportamento público**, não em ferramentas específicas.

Estrutura:

**pilar -> obrigação pública -> contrato -> conformidade**

Materialização:

**contrato -> provider/materializador A | B | C | implementação própria**

Ferramentas de referência aparecem como evidência de realizabilidade e opções do ecossistema, nunca como condição ontológica do FlowED.
