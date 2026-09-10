# Pilar 3 — pesquisa de realizabilidade 001

**Pilar:** sustentação científica e empírica explícita.  
**Objetivo:** verificar se existe tecnologia e prior art suficientes para materializar futuramente um contrato FlowED capaz de relacionar referências, claims, evidências, proveniência, validação e políticas sem inventar toda a infraestrutura.

## Conclusão executiva

Há um horizonte tecnológico suficientemente forte para considerar o núcleo do Pilar 3 **realizável em nível de manifesto**.

Não existe uma única ferramenta que resolva toda a governança epistemológica pretendida. Porém, existe uma composição concreta de padrões, modelos, APIs e engines capazes de representar claims, referências, relações de evidência, proveniência, metadados acadêmicos, constraints, políticas e attestations.

A parte ainda não resolvida é científica/metodológica: como comparar e graduar de forma defensável evidências de naturezas diferentes e como transformar isso em score ou maturidade sem falsa precisão. Esse gap não invalida a realizabilidade do pilar, porque o pilar exige primeiro **explicitação, proveniência e possibilidade de avaliação**, não uma fórmula universal já pronta.

## 1. Base metodológica — Evidence-Based Software Engineering

Kitchenham, Dybå e Jørgensen (ICSE 2004) propõem Evidence-Based Software Engineering como adaptação do movimento evidence-based à Engenharia de Software e defendem integração de resultados de pesquisa para apoiar diferentes stakeholders, observando também limitações próprias da área.

Referência: Kitchenham, B. A.; Dybå, T.; Jørgensen, M. *Evidence-Based Software Engineering*. ICSE 2004. DOI: 10.1109/ICSE.2004.1317449.

Consequência para FlowED: a proposição de relacionar decisões/práticas a conhecimento científico disponível possui antecedente direto; o FlowED não precisa inventar o princípio de engenharia orientada por evidência.

## 2. Claims científicos granulares — Nanopublications

Nanopublications fornecem um formato Linked Data para publicar pequenos claims/assertions juntamente com proveniência e metadados de publicação. A literatura demonstra uso em escala de milhões de nanopublications e experimentos de publicação/revisão científica com semântica machine-interpretable.

Referências:
- Kuhn et al. *Nanopublications: A Growing Resource of Provenance-Centric Scientific Linked Data* (2018).
- Bucur et al. *Nanopublication-Based Semantic Publishing and Reviewing: A Field Study with Formalization Papers* (2022).

Consequência para FlowED: uma referência não precisa ser apenas um documento opaco. É tecnicamente possível representar claims discretos e anexar a cada um sua proveniência e metadados.

## 3. Pacotes reproduzíveis de evidência — RO-Crate

RO-Crate é um formato aberto e leve, baseado em JSON-LD/Schema.org, para empacotar artefatos de pesquisa, identificadores, metadados, relações, provenance e annotations em um objeto machine-readable.

Referência: Soiland-Reyes et al. *Packaging research artefacts with RO-Crate* (2021/2022).

Consequência para FlowED: conjuntos de evidência, experimentos, datasets, software e documentação podem ser representados como pacotes portáveis e relacionados, em vez de referências textuais soltas.

## 4. Proveniência — W3C PROV-O/PROV-DM

A família W3C PROV oferece modelo de dados e ontologia para representar Entity, Activity, Agent e relações de derivação, geração, uso e responsabilidade.

Referência: W3C Recommendation, *PROV-O: The PROV Ontology* e *PROV-DM* (2013).

Consequência para FlowED: origem e transformação de uma evidência podem ser representadas por padrão interoperável, inclusive ligando evidência científica e operacional.

## 5. Validação estrutural — RDF + SHACL

SHACL é uma Recommendation W3C para descrever e validar constraints em grafos RDF. Shapes podem declarar cardinalidade, tipos, relações e regras e produzir relatórios de conformidade. SHACL também é aplicável a integração de dados, geração de UI e code generation.

Consequência para FlowED: um futuro contrato epistemológico pode ser machine-verifiable. Por exemplo, determinada classe de referência pode exigir fonte, tipo de evidência, provenance, data, estado e relações obrigatórias, sem depender de validação manual de formato.

## 6. Descoberta e metadados científicos — Crossref, DataCite e OpenAlex

- Crossref expõe metadados bibliográficos por REST API, incluindo DOI, autores, licenças, financiadores, atualizações pós-publicação e outros identificadores.
- DataCite fornece DOI metadata, relações entre objetos, citations/references e provenance de metadados.
- OpenAlex mantém grafo aberto de works, authors, institutions, topics, funders e relações de citação, com API para navegar referências e citações.

Consequência para FlowED: uma materialização futura pode enriquecer automaticamente referências científicas e verificar identificadores/relações sem construir um índice acadêmico próprio.

## 7. Evidência operacional verificável — in-toto e SLSA

in-toto define metadata/attestations sobre passos executados, por quem, com quais materiais e produtos, permitindo verificar se uma cadeia ocorreu conforme esperado.

SLSA usa attestations e provenance para descrever como artefatos foram produzidos e permitir verificação de propriedades da cadeia de software.

Consequência para FlowED: a evidência operacional não precisa ser apenas um log informal. É tecnicamente possível produzir attestations machine-verifiable ligadas a artifacts e executions, que depois podem ser relacionadas a uma referência/claim.

## 8. Políticas e decisões determinísticas — Open Policy Agent

OPA é um policy engine geral, declarativo e domain-agnostic. Recebe dados estruturados e avalia políticas separadamente da aplicação que executa/enforce a decisão.

Consequência para FlowED: pisos, gates e regras organizacionais como “esta classe de decisão exige evidência de tipo X”, “divergência precisa de justificativa Y” ou “determinada referência não satisfaz política mínima” podem ser materializados por engines existentes sem embutir regras em cada ferramenta.

## 9. Composição tecnológica de referência

Uma futura materialização do Pilar 3 pode ser construída, por exemplo, pela composição:

**Crossref/DataCite/OpenAlex → referência científica identificada/enriquecida**

**Nanopublication/knowledge graph → claim e relações explícitas**

**RO-Crate → pacote de evidências e artefatos**

**W3C PROV → provenance**

**RDF/SHACL → estrutura e validação do contrato**

**eventos/attestations do Pilar 2 + in-toto/SLSA → evidência operacional verificável**

**OPA ou engine equivalente → políticas/gates determinísticos**

**MyTrues/EDT/CCP → decisão, racional, revisão e projeção de conhecimento quando amadurecidos**

Nenhum desses componentes deve se tornar obrigatório no conceito FlowED. O contrato público deve capturar as propriedades relevantes e permitir outras implementações.

## 10. O que já é tecnicamente plausível automatizar

- resolver e enriquecer referências por identificador;
- representar claims e evidências como objetos relacionados;
- preservar provenance;
- ligar evidência científica, normativa e operacional;
- validar presença/estrutura de metadados obrigatórios;
- executar políticas organizacionais explícitas;
- verificar attestations de determinadas classes de evidência;
- navegar relações de citação;
- produzir projeções/relatórios de fragilidade com base em regras declaradas.

## 11. O que permanece aberto

Não tratar como resolvido:

- fórmula universal de score epistemológico;
- equivalência entre qualidade de um paper e adequação contextual;
- comparação direta entre norma, revisão sistemática, benchmark, experiência operacional e opinião de especialista;
- pesos universais;
- inferência automática de causalidade a partir de correlação;
- alegação de que citation count mede qualidade;
- promoção automática de decisão organizacional a verdade.

Esses pontos pertencem principalmente às linhas P02/P03/P06 e precisam de pesquisa própria.

## 12. Estado para o manifesto

**Realizabilidade técnica do núcleo:** suficientemente estabelecida para avançar.

O futuro contrato ainda não existe, mas existe tecnologia concreta no horizonte capaz de representar, validar, consultar e governar os objetos necessários. O residual científico está sobretudo no modelo de avaliação e no significado dos scores, não na inexistência de infraestrutura para implementar o pilar.

Portanto, o Pilar 3 pode ser debatido agora em sua formulação constitutiva e, se não surgir contradição, atingir o mesmo gate de verossimilhança usado nos Pilares 1 e 2.
