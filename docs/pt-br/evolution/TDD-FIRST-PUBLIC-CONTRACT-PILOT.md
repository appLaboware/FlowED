# Primeiro piloto de contrato público — TDD / contrato por exemplo

**Status:** `SUPERSEDED` como formulação principal. Preservado para linhagem histórica.

## Correção

A formulação anterior interpretou “TDD” como Test-Driven Development usado como domínio/prática piloto do FlowED.

O debate posterior esclareceu que a intenção correta é outra: usar **test-driven design do próprio contrato público de `flwd`**, criando primeiro comandos, requisições e respostas válidas mockadas; testar o cliente contra esses mocks; e somente depois construir providers reais que precisam satisfazer exatamente o mesmo contrato observável.

Essa abordagem se aproxima de prior art já estabelecido em contract-first/API-first design, contract testing, consumer-driven contracts e contract by example. Portanto, pela regra Adapt First, o FlowED deve compor esses conceitos em vez de tratar a abordagem como método próprio já novo.

A referência operacional atual passa a ser:

`FLWD-CONTRACT-BY-EXAMPLE-PILOT.md`

## O que permanece válido deste documento

Permanece válida a motivação de usar um piloto pequeno para pressionar:

- linguagem pública;
- independência de implementação;
- substituição por contrato;
- respostas/erros observáveis;
- equivalência CLI/YAML/API;
- dogfood antes de fechar o baseline inicial do FlowED.

O que deixa de ser hipótese principal é usar o conceito metodológico de Test-Driven Development como o domínio dessa prova.

## Linhagem da correção

A sequência foi:

1. InitProj/ISO29110-lite considerados como pilotos;
2. identificado risco de acoplamento entre módulos;
3. TDD sugerido como prática menor;
4. esclarecido que o objetivo real era projetar **o próprio contrato do `flwd` por testes e mocks**;
5. piloto reenquadrado como contrato por exemplo / consumer-driven contract testing.

Essa correção é evidência de dogfood do processo de evolução conceitual do FlowED.
