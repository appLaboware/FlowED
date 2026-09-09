# P18 — Contract-Test-Driven Development (CTDD)

**Status:** candidato a artigo / hipótese de contribuição residual.  
**Nome de trabalho:** **Contract-Test-Driven Development (CTDD)**.  
**Estado epistemológico:** não reivindicar novidade antes de revisão sistemática de anterioridade.  
**Origem:** composição identificada durante o desenho test-first dos contratos públicos do `flwd`.

## 1. Motivação

Durante o desenho do `flwd`, surgiu uma composição operacional em que:

1. o comportamento público esperado é especificado antes da implementação;
2. exemplos de comando/requisição e resposta funcionam como testes executáveis;
3. o consumidor pode ser desenvolvido contra um mock/fake compatível com o contrato;
4. o mesmo contrato é posteriormente usado para verificar um provider real;
5. múltiplos providers podem ser submetidos ao mesmo contrato;
6. a implementação interna permanece livre desde que o comportamento público seja contratualmente equivalente;
7. a mesma semântica pública pode ser projetada por CLI, YAML, API, SDK, UI ou agente.

Essa composição reúne elementos de **Test-Driven Development (TDD)**, **Consumer-Driven Contract Testing (CDCT)**, **contract/conformance testing**, **Design by Contract**, **behavioral substitutability** e **mocks/fakes**.

## 2. Por que não chamar simplesmente de Contract-Driven Development

`Contract-Driven Development (CDD)` já possui anterioridade científica, especialmente no trabalho de Bertrand Meyer e colaboradores, que combina Design by Contract, TDD, métodos formais e geração automática de testes a partir de contratos.

Portanto, o FlowED não deve reutilizar `CDD` como nome próprio de uma nova contribuição nem alegar que a combinação entre contratos e TDD é inédita.

O nome **CTDD** é apenas um rótulo de trabalho para investigar um residual mais específico: **desenvolvimento guiado por testes de contrato executáveis na fronteira consumidor-provider, com mock primeiro, verificação posterior de providers e substituição por equivalência pública**.

A revisão de anterioridade deverá decidir se o nome é preservado, alterado, absorvido por CDD/CDCT ou abandonado.

## 3. Hipótese de contribuição residual

A possível contribuição não está em TDD, CDCT, CDD, mocks ou conformance testing isoladamente.

O residual candidato é a composição de um ciclo de desenvolvimento em que o **contrato público executável é simultaneamente**:

- especificação de comportamento;
- oracle de teste do consumidor;
- base do mock/fake inicial;
- teste de conformidade do provider;
- critério de substituição entre providers;
- unidade de compatibilidade entre diferentes projeções da mesma linguagem operacional.

Ciclo candidato:

**comportamento desejado → exemplos executáveis → contrato público → consumidor contra mock → provider contra o mesmo contrato → substituição/conformidade → evolução versionada do contrato**.

No caso FlowED, `flwd` é apenas o primeiro consumidor de referência; a hipótese deve ser estudada de forma geral, não limitada ao produto FlowED.

## 4. Relação com TDD

O componente TDD é real: o comportamento verificável é definido antes da implementação e a implementação evolui até satisfazê-lo.

Entretanto, a unidade de pressão não é apenas uma função/classe e seu unit test. A unidade principal candidata é uma **fronteira pública contratual executável**, que pode atravessar processos, serviços, ferramentas ou módulos independentes.

Assim, o artigo deve investigar em que medida CTDD é:

- uma especialização de TDD;
- uma operacionalização de CDD;
- uma extensão de CDCT;
- uma composição sem novidade metodológica suficiente;
- ou uma contribuição residual própria.

## 5. Relação com Consumer-Driven Contract Testing

CDCT fornece o antecedente mais direto para consumidor + mock + contrato + provider verification.

O residual possível a investigar é ampliar o foco de compatibilidade consumidor-provider para um ciclo explícito de **desenvolvimento guiado pelo contrato executável**, incluindo:

- desenho do consumidor antes do provider;
- contrato como artefato central de evolução;
- projeções múltiplas de interface sobre a mesma semântica;
- substituição de providers como requisito primário;
- versionamento e evolução contratual como parte do método.

Nada disso deve ser tratado como novo sem revisão sistemática.

## 6. Referências-base já identificadas

- Beck — Test-Driven Development / test-first development.
- Meyer et al. — Contract-Driven Development e Design by Contract.
- Schwarz, Quast & Riehle (2025) — Consumer-Driven Contract Testing.
- Ayas et al. (2022) — evidência empírica de CDCT em sistemas de microservices.
- Heckel & Lohmann (2005) — contract-based testing e simulação de componentes.
- Tretmans (1999) — specification-based conformance testing.
- de Alfaro & Henzinger (2001) — behavioral interfaces / Interface Automata.
- Liskov & Wing (1994) — substituição comportamental.
- Freeman et al. (2004) e Spadini et al. (2019) — mocks como técnica de desenvolvimento/teste.

Documento de sustentação relacionado: `SCIENTIFIC-BASIS-FLWD-CONTRACT-BY-EXAMPLE.md`.

## 7. Perguntas de pesquisa candidatas

1. Existe anterioridade que já cubra integralmente esse ciclo sob outro nome?
2. Contratos executáveis definidos antes da implementação reduzem incompatibilidades e retrabalho em comparação com desenvolvimento code-first ou contract-last?
3. O desenvolvimento do consumidor contra mock baseado no contrato melhora independência temporal entre consumidor e provider?
4. O mesmo conjunto de testes pode servir de forma eficaz para validar mock, Provider A e Provider B sem acoplamento a detalhes internos?
5. Como definir equivalência contratual suficientemente forte sem exigir igualdade estrutural ou byte a byte?
6. Quais classes de comportamento não são bem capturadas por request/response examples simples — estado, tempo, concorrência, efeitos humanos, segurança, performance?
7. Como versionamento e evolução de contrato afetam compatibilidade e custo de manutenção?
8. A abordagem permanece útil fora de APIs HTTP e microservices?

## 8. Desenho metodológico inicial

A linha deve seguir Adapt First.

### Discovery

Realizar revisão estruturada de:

- Test-Driven Development;
- Contract-Driven Development;
- contract-first/API-first development;
- Consumer-Driven Contract Testing;
- specification-based/conformance testing;
- executable specifications;
- behavioral contracts/interfaces;
- mock-driven/outside-in development;
- interface substitutability/refinement.

### POC/artefato

Implementar o ciclo em um caso pequeno com:

- consumidor funcional contra mock;
- contrato executável versionado;
- pelo menos dois providers estruturalmente distintos;
- mesma suíte de conformidade;
- registros de mudanças de contrato e incompatibilidades encontradas.

### Avaliação

Comparar pelo menos:

- quantidade/tipo de incompatibilidades detectadas antes da integração;
- retrabalho provocado por mudanças de interface;
- acoplamento consumidor-provider;
- esforço de manutenção dos contratos;
- capacidade real de substituição;
- limitações semânticas dos exemplos/matchers.

## 9. Relação com FlowED

FlowED é inicialmente **caso de uso e dogfood**, não prova científica da proposta.

Se o método funcionar no `flwd`, isso produz evidência de realizabilidade e um caso inicial. Não demonstra validade geral.

O artigo pode existir independentemente do FlowED se o residual científico for confirmado. Se a revisão mostrar que CDD/CDCT já cobre suficientemente a composição, a decisão correta é **ADOPT/MERGE**, e não criar uma nova teoria.

## 10. Gate para virar paper

Estado atual: **CANDIDATE / GO FOR PRIOR-ART REVIEW**.

Não promover para contribuição científica até existir:

1. revisão de anterioridade com boundary explícito;
2. comparação formal com CDD, CDCT, TDD e conformance testing;
3. definição clara do residual;
4. hipótese falsificável;
5. desenho de avaliação;
6. pelo menos uma materialização reproduzível;
7. decisão final `GO / MERGE / ADOPT / DON'T GO`.
