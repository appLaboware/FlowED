# FlowED — fronteira entre Manifesto, contratos e produto

**Status:** decisão conceitual para o fechamento do manifesto.

## 1. Motivação

As discussões dos pilares começaram a misturar três níveis diferentes: a filosofia defendida pelo Manifesto FlowED, os contratos públicos que tornam essa filosofia operacional e as ferramentas que materializam esses contratos.

Essa mistura deve ser evitada porque uma crítica ao algoritmo de uma ferramenta não é necessariamente uma crítica ao FlowED; da mesma forma, uma ferramenta tecnicamente boa não corrige um contrato conceitualmente insuficiente.

## 2. Três níveis

### 2.1 Manifesto FlowED

O manifesto declara **por que determinadas capacidades e propriedades são importantes** para uma Engenharia de Software coerente, rastreável, evolutiva e livre de aprisionamento tecnológico.

Ele defende valores, princípios e obrigações conceituais. Não escolhe ferramentas, algoritmos, fornecedores ou fórmulas particulares.

Exemplos:

- é importante que sustentação científica/empírica seja visível;
- é importante que execução possa gerar memória reutilizável;
- é importante que capacidades diferentes interoperem por contratos;
- é importante que a forma de trabalhar possa progredir ou regredir conscientemente conforme contexto e evidência.

### 2.2 Contratos públicos FlowED

Os contratos transformam as posições do manifesto em **obrigações observáveis e interoperáveis**.

O contrato define o que deve poder ser expresso, solicitado, recebido, relacionado, versionado, rastreado ou garantido para que uma capability participe do ecossistema FlowED.

Ele pode ser rigoroso em semântica, comportamento público, versionamento e conformidade, mas não prescreve a tecnologia interna quando ela não faz parte da garantia pública.

### 2.3 Produto FlowED / `flwd`

O produto executável de referência do FlowED é o cliente/runtime representado pelo **CLI `flwd`**.

Seu papel é tornar os contratos utilizáveis operacionalmente: receber comandos, convertê-los para a semântica pública adequada, descobrir/acionar capabilities e providers no hub horizontal ou através de adapters, validar as respostas contratuais e projetá-las de volta ao usuário.

O `flwd` pode oferecer implementações e integrações de referência, mas não deve adquirir autoridade para redefinir silenciosamente o contrato. A ferramenta executa e orquestra o ecossistema; o contrato continua sendo a autoridade normativa sobre o comportamento público.

## 3. Providers e ferramentas horizontais

Ferramentas especializadas vivem abaixo ou ao lado da fronteira contratual e podem ser substituídas.

Exemplos atuais de candidatos de materialização:

- COR para classificação/opinião de sustentação;
- MyTrues para memória decisória/cognitiva;
- futuras composições de memória operacional;
- materializações ISO 29110 e outras capabilities horizontais.

Esses produtos podem possuir filosofia própria, metodologia própria, pesquisas próprias e diferentes graus de confiabilidade. O FlowED não incorpora automaticamente essas opiniões como suas.

## 4. Atribuição de opinião

Quando uma capability produz uma avaliação, recomendação ou score, o FlowED deve preservar a autoria do provider.

Exemplo conceitual:

> segundo COR, Scrum possui avaliação 8,7/10 nesta versão e contexto.

Isso não significa:

> FlowED afirma que Scrum vale 8,7/10.

A diferença é constitutiva. O FlowED padroniza como a opinião pode ser identificada, transportada, consultada e relacionada; o provider responde pelo conteúdo da opinião.

Logo:

- discordar do cálculo do COR é criticar COR;
- trocar COR por outro classificador é liberdade do time;
- demonstrar que o contrato não consegue expressar uma informação necessária é criticar o contrato FlowED;
- demonstrar que o manifesto considera irrelevante algo que deveria ser constitutivo é criticar o próprio FlowED.

## 5. Relação com a analogia Agile Manifesto / Scrum

A analogia é útil para separar níveis, mas não é literal.

O **Manifesto Ágil** declara valores e princípios; **Scrum** é uma forma concreta de operacionalizar parte desse universo. De maneira semelhante, o Manifesto FlowED declara a filosofia e o produto FlowED torna essa filosofia operacional.

A diferença é que `flwd` é mais próximo de um **runtime/cliente oficial de referência de contratos FlowED** do que Scrum é do Manifesto Ágil. Scrum possui suas próprias prescrições de processo; `flwd` deve permanecer subordinado aos contratos públicos FlowED e permitir providers concorrentes.

Portanto, a analogia serve para compreender:

**filosofia != materialização**

mas não deve ser usada para afirmar identidade arquitetural entre Scrum e `flwd`.

## 6. Regra de auditoria dos pilares

Cada pilar deve ser revisado perguntando separadamente:

1. **Filosofia:** o que o FlowED defende e por que isso é importante?
2. **Contrato:** o que precisa ser publicamente representável/observável para cumprir essa defesa?
3. **Realizabilidade:** existem tecnologias ou composições plausíveis capazes de cumprir esse contrato?
4. **Produto:** quais implementações de referência podemos construir ou integrar sem torná-las obrigatórias?

Somente os itens 1 e 2 pertencem ao núcleo normativo do FlowED. O item 3 sustenta a verossimilhança do manifesto. O item 4 pertence ao ecossistema de produtos.

## 7. Regra transversal

> **FlowED defende o que importa, contrata o comportamento necessário e deixa livre quem e como materializa.**

O `flwd` é a ferramenta oficial que operacionaliza essa rede de contratos, mas não transforma suas dependências, defaults ou providers em verdade normativa do FlowED.