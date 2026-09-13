# TDD e CDCT no piloto do `flwd`

**Status:** clarificação conceitual e terminológica para o piloto `FLWD-CONTRACT-BY-EXAMPLE-PILOT.md`.

## 1. Correção

TDD — Test-Driven Development — existe, é uma prática consolidada e é diretamente relevante para a ideia do piloto do `flwd`.

A correção anterior não deveria ser lida como substituição de TDD por Consumer-Driven Contract Testing (CDCT). As duas referências atuam em níveis diferentes e podem ser compostas.

## 2. O que TDD sustenta no piloto

A ideia central de TDD é usar testes para guiar o desenvolvimento da funcionalidade antes de a implementação estar pronta. A sequência clássica é escrever um teste para o próximo comportamento desejado, observar a falha, implementar o mínimo necessário para fazê-lo passar e então refatorar mantendo o comportamento.

No piloto do `flwd`, isso sustenta diretamente a direção de trabalho:

**comportamento esperado primeiro -> teste executável -> implementação depois**.

Assim, ao definir primeiro um comando, uma requisição esperada e uma resposta válida/erro válido, e ao fazer o `flwd` passar nesses testes antes do provider real existir, estamos usando um raciocínio autenticamente test-driven.

## 3. O que CDCT acrescenta

Quando existe uma fronteira entre consumidor e provider independente, o problema deixa de ser apenas "desenvolver uma unidade guiada por testes" e passa também a ser "garantir que dois componentes independentes concordem sobre o contrato público".

É aí que Consumer-Driven Contract Testing e contract testing acrescentam algo específico:

- o consumidor explicita as expectativas que possui do provider;
- mocks/fakes permitem desenvolver e testar o consumidor antes do provider real;
- o contrato resultante pode ser executado posteriormente contra o provider real;
- providers diferentes podem demonstrar compatibilidade contra o mesmo contrato.

Portanto, no FlowED:

- **TDD** sustenta a estratégia geral de desenvolver a partir do comportamento/teste esperado;
- **CDCT/contract testing** sustenta a verificação da fronteira consumidor-provider e da substituição de providers;
- **specification/conformance testing** sustenta a ideia de que uma implementação concreta pode ser verificada contra uma especificação executável independente.

## 4. Formulação recomendada

O piloto do `flwd` pode ser descrito corretamente como uma composição:

> **test-driven, contract-first e consumer-driven**.

Não há necessidade de escolher uma única dessas tradições como se fossem mutuamente excludentes.

O aspecto mais próximo do TDD é: definir o comportamento esperado antes da implementação e fazer a implementação evoluir até satisfazer o teste.

O aspecto mais próximo de CDCT é: o `flwd` age como consumidor de referência e o provider real precisa satisfazer o contrato público que o consumidor usa.

## 5. Relação com a proposta específica do FlowED

A sequência proposta fica:

**experiência/comportamento público desejado -> exemplos de comando e resposta -> testes executáveis -> `flwd` contra mock -> provider real contra o mesmo contrato -> substituição por outro provider -> refinamento do contrato**.

Essa sequência não é reivindicada como invenção metodológica do FlowED. O FlowED compõe práticas existentes e as aplica à construção da sua língua pública e de seus contratos.

## 6. Limite epistemológico

A existência e consolidação de TDD não prova automaticamente que o método composto será suficiente para todos os contratos FlowED. A aplicação multi-domínio, a equivalência semântica entre diferentes interfaces e a substituição geral de providers continuam hipóteses experimentais do FlowED.

## 7. Referências de apoio

- Kent Beck — *Test-Driven Development: By Example*; referência clássica de TDD e do desenvolvimento guiado pelo comportamento esperado/teste.
- Martin Fowler — descrição moderna de TDD como ciclo de escrever teste para o próximo comportamento, implementar até passar e refatorar.
- Schwarz, Quast & Riehle (2025) — Consumer-Driven Contract Testing para interoperabilidade sintática e verificação isolada de contratos entre consumidor e provider.
- Heckel & Lohmann (2005) — contract-based testing e simulação de componentes requeridos a partir de contratos comportamentais.
- Tretmans (1999) — conformance testing derivado de especificações.

## 8. Decisão

Não substituir TDD por CDCT no discurso do piloto. Usar ambos onde cada conceito realmente se aplica.

Formulação curta recomendada:

> **O `flwd` é desenvolvido de forma test-driven a partir de contratos públicos executáveis; quando o contrato atravessa a fronteira consumidor-provider, usa princípios de consumer-driven contract testing e conformance testing.**
