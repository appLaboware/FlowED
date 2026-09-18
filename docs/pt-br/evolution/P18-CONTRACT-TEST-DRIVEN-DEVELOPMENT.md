# P18 — Linha de pesquisa: composição test-driven de contratos públicos

**Status:** candidato a artigo / linha de pesquisa aberta.  
**Nome:** **em aberto**.  
**Estado epistemológico:** conceito ainda não consolidado; não reivindicar novidade nem fixar nomenclatura antes de revisão de anterioridade.  
**Origem:** composição identificada durante o desenho test-first dos contratos públicos do `flwd`.

> Nota de linhagem: o nome provisório **Contract-Test-Driven Development (CTDD)** foi usado em uma rodada anterior apenas como rótulo de trabalho. Ele não deve ser tratado como nome definido do conceito. O arquivo preserva o nome legado no path apenas por rastreabilidade histórica.

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

## 2. Linha de pesquisa aberta

A existência de uma composição útil está registrada, mas **não há conceito ou nome consolidado**.

A revisão futura deverá determinar se essa composição:

- já existe integralmente sob um nome estabelecido;
- é apenas uma aplicação combinada de TDD + CDCT + CDD + conformance testing;
- possui um residual metodológico próprio;
- merece uma nova denominação;
- ou deve ser simplesmente adotada sem criação conceitual.

Portanto, esta linha permanece deliberadamente aberta.

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

A pesquisa deverá verificar se isso é apenas aplicação de conceitos existentes ou se há residual próprio.

## 5. Relação com Consumer-Driven Contract Testing

CDCT fornece o antecedente mais direto para consumidor + mock + contrato + provider verification.

O residual possível a investigar é ampliar o foco de compatibilidade consumidor-provider para um ciclo explícito de desenvolvimento guiado pelo contrato executável, incluindo desenho do consumidor antes do provider, contrato como artefato central de evolução, projeções múltiplas de interface sobre a mesma semântica, substituição de providers como requisito primário e versionamento/evolução contratual como parte do método.

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

Realizar revisão estruturada de TDD, Contract-Driven Development, contract-first/API-first development, Consumer-Driven Contract Testing, specification-based/conformance testing, executable specifications, behavioral contracts/interfaces, mock-driven/outside-in development e interface substitutability/refinement.

### POC/artefato

Implementar o ciclo em um caso pequeno com consumidor funcional contra mock, contrato executável versionado, pelo menos dois providers estruturalmente distintos, mesma suíte de conformidade e registros de mudanças de contrato/incompatibilidades.

### Avaliação

Comparar quantidade/tipo de incompatibilidades detectadas antes da integração, retrabalho provocado por mudanças de interface, acoplamento consumidor-provider, esforço de manutenção dos contratos, capacidade real de substituição e limitações semânticas dos exemplos/matchers.

## 9. Relação com FlowED

FlowED é inicialmente **caso de uso e dogfood**, não prova científica da proposta.

Se o método funcionar no `flwd`, isso produz evidência de realizabilidade e um caso inicial. Não demonstra validade geral.

O artigo pode existir independentemente do FlowED se o residual científico for confirmado. Se a revisão mostrar que conceitos existentes já cobrem suficientemente a composição, a decisão correta é **ADOPT/MERGE**, e não criar uma nova teoria.

## 10. Gate para virar paper

Estado atual: **CANDIDATE / OPEN CONCEPT / GO FOR PRIOR-ART REVIEW**.

Não promover para contribuição científica até existir revisão de anterioridade com boundary explícito, comparação formal com CDD/CDCT/TDD/conformance testing, definição clara do residual, hipótese falsificável, desenho de avaliação, ao menos uma materialização reproduzível e decisão final `GO / MERGE / ADOPT / DON'T GO`.
