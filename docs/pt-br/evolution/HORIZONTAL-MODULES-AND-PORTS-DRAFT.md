# Draft — Contratos Públicos, Módulos Horizontais e Materializações no FlowED

**Status:** decisão conceitual provisória em simulação.

## 1. Correção arquitetural

O FlowED ocupa a esfera superior de conceito, filosofia, linguagem operacional e coordenação. Abaixo dele podem existir módulos horizontais pares, ferramentas e outras materializações práticas.

A fronteira conceitual do FlowED **não deve depender da arquitetura interna dessas implementações**. Em particular, `port`, `adapter`, provider, plugin, processo local, chamada remota ou outra técnica são decisões possíveis de materialização.

O objeto que o FlowED precisa conhecer é o **contrato público**.

Regra candidata:

> **O FlowED se orienta por contratos públicos e comportamento observável; não precisa conhecer como uma implementação satisfaz esse contrato.**

Isso reduz acoplamento não apenas entre implementações, mas também entre a teoria FlowED e uma arquitetura de software específica.

## 2. Contrato público como fronteira

Um contrato público descreve somente o que é necessário para que uma capability seja inteligível, interoperável e substituível no ecossistema FlowED.

O contrato deve declarar, conforme aplicável:

- significado/objetivo da capability;
- operações públicas;
- entradas aceitas;
- saídas e garantias observáveis;
- invariantes e constraints;
- erros/estados públicos relevantes;
- requisitos mínimos de rastreabilidade;
- versão e regras de compatibilidade;
- capabilities/limitações que precisam ser conhecidas pelo consumidor.

O contrato não deve declarar algoritmo, organização interna, tecnologia ou estrutura de artefatos que não sejam necessários para o consumidor.

## 3. Igualdade relevante

Substituição não exige que duas implementações produzam arquivos, textos, estruturas internas ou experiências idênticas.

A igualdade exigida é **igualdade em relação ao contrato**.

Dadas entradas equivalentes no escopo do contrato, dois implementadores compatíveis devem preservar as mesmas garantias públicas e fornecer saídas que satisfaçam o mesmo significado contratual, ainda que o resultado concreto tenha personalidade própria.

Assim, diferenças são permitidas quando pertencem à liberdade de materialização e não alteram aquilo que o contrato prometeu.

Se um consumidor depende de uma diferença que não está declarada no contrato, essa dependência é acoplamento fora da fronteira pública e não deve ser atribuída ao FlowED.

## 4. FlowED e implementação

A separação proposta passa a ser:

**FlowED conceitual → contrato público → implementação/materialização**

O lado de implementação pode optar por:

- ports e adapters;
- providers/plugins;
- chamadas locais ou remotas;
- APIs;
- CLIs;
- processos externos;
- serviços;
- bibliotecas;
- outras arquiteturas adequadas.

Ports continuam sendo uma excelente forma de realizar a separação na implementação, especialmente em arquiteturas hexagonais, mas **não são requisito conceitual do FlowED** enquanto o contrato público puder ser preservado.

## 5. Módulos horizontais

Os módulos horizontais representam áreas/capabilities pares que ampliam a cobertura prática do ecossistema FlowED.

Cada módulo pode implementar um ou mais contratos públicos e pode depender de outros contratos públicos. Essa dependência deve permanecer contratual, não baseada em conhecimento obrigatório de uma implementação específica.

O FlowED não precisa saber como o módulo está organizado internamente.

## 6. Exemplo conceitual

`ISO29110-lite` não deve ser acoplado ao `InitProj` nem tratado automaticamente como profile interno dele.

O FlowED deve primeiro identificar qual capability pública está sendo requerida e qual contrato a representa.

Se `ISO29110-lite` e outra ferramenta satisfazem esse contrato, qualquer uma pode atender a requisição no escopo declarado. Uma pode produzir documentos, nomenclaturas, estruturas e uma personalidade diferente da outra, desde que ambas preservem as garantias públicas exigidas.

Do mesmo modo, `InitProj` pode ser uma ferramenta/materialização de uma ou mais capabilities sem se tornar definição conceitual delas.

## 7. Consequência para a linguagem FlowED

A língua pública do FlowED continua comum. `flwd`, YAML, API, SDK, UI e agentes expressam a mesma semântica pública.

Essa língua deve falar em termos de operações e conceitos expostos pelos contratos, não em termos da arquitetura interna ou do nome de uma implementação concreta, salvo quando o usuário explicitamente exigir/restringir uma materialização.

Portanto:

**entrada FlowED → contrato público aplicável → materialização escolhida → resultado contratualmente válido**

A maneira como o resultado foi produzido é irrelevante para a semântica pública, exceto quando alguma propriedade interna tiver sido promovida explicitamente a requisito do contrato.

## 8. Consequência para determinismo

Determinismo público também deve ser definido na fronteira contratual.

FlowED não precisa impor que todas as implementações tenham a mesma arquitetura interna de planejamento, reconciliação, idempotência, hash, locks ou transações.

Ele precisa exigir as garantias observáveis que forem necessárias. Por exemplo, se determinada operação contratualmente precisa ser reexecutável sem duplicar efeito, o contrato exige esse comportamento; cada implementação decide como garanti-lo.

Mecanismos internos só sobem para o contrato quando seu efeito precisa ser prometido ao consumidor.

## 9. Implicação para o primeiro piloto

O primeiro piloto não deve começar por escolher uma tecnologia, módulo ou arquitetura interna.

Deve começar por escolher uma **capability pequena e real** e escrever apenas seu contrato público mínimo.

Depois, duas materializações diferentes devem tentar satisfazê-lo. O teste principal é verificar se o consumidor e a linguagem pública permanecem inalterados ao trocar a implementação e se as diferenças concretas permanecem legitimamente fora do contrato.

Esse teste é mais forte do que testar apenas ports, porque permite inclusive que implementações usem arquiteturas internas distintas.

## 10. Relação com arquitetura por ports

Ports e adapters permanecem como materialização técnica candidata e recomendável onde fizer sentido, mas ficam abaixo da fronteira conceitual do FlowED:

**Contrato público FlowED → (opcionalmente) Port → Adapter/Provider/Implementação**

Em outra implementação poderia existir:

**Contrato público FlowED → API remota**

ou:

**Contrato público FlowED → biblioteca local**

Desde que o comportamento público seja equivalente no escopo declarado, o FlowED não diferencia essas escolhas.

## 11. Gaps afetados

- GAP-M004: a unidade primária da linguagem pública se aproxima de operações definidas por contratos, não de implementações.
- GAP-M005: a fronteira de coordenação/soberania passa a ser explicitamente o contrato público.
- GAP-M015: liberdade governada passa a significar liberdade total abaixo do contrato, limitada pelas garantias públicas.
- GAP-M024: representação canônica precisa representar contratos públicos sem impor arquitetura interna.
- novo gap candidato: definir quando duas materializações podem ser consideradas equivalentes/compatíveis perante um contrato sem exigir resultados concretos idênticos.

## 12. Dogfood e correção de hipótese

A hipótese anterior elevava `port` a elemento conceitual central. O debate mostrou que isso ainda acoplava o FlowED a uma solução arquitetural específica.

A correção desta rodada eleva o **contrato público** à fronteira conceitual e rebaixa ports/adapters/providers a possíveis materializações.

A mudança preserva a intenção original de substituibilidade, mas aumenta a liberdade tecnológica e torna o FlowED menos dependente de uma arquitetura particular.
