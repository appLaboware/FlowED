# Algorithm and ownership boundary

## Unidade de propriedade

Cada técnico/equipe/fornecedor possui seu próprio MyTrues e pode manter:

- memória isolada;
- decisões aprovadas;
- histórico;
- preferências;
- dados privados.

Isso não significa que todos os algoritmos usados pelo fornecedor sejam proprietários.

## OPEN — conhecimento público

Devem permanecer na superfície aberta quando forem conhecimento público:

- protocolos;
- schemas;
- algoritmos científicos publicados;
- Case-Based Reasoning;
- MCDA/MCDM;
- regras/decision tables;
- métodos probabilísticos conhecidos;
- graph/vector/hybrid retrieval conhecidos;
- learning-to-rank publicado;
- calibração e abstention conhecidas;
- reference implementations;
- benchmarks;
- conformance;
- adapters genéricos.

## PRIVATE DATA — confidencialidade, não IP

Podem ser privados por segurança, contrato ou privacidade:

- secrets;
- dados de clientes;
- casos reais;
- memória de um fornecedor;
- preferências individuais;
- resultados internos;
- dados de benchmark não publicáveis.

Privacidade desses dados não transforma o algoritmo público que os processa em propriedade intelectual.

## CORE — somente delta original

`core/` só recebe implementação quando houver evidência de que:

1. a solução não é mera reprodução de método público;
2. baselines relevantes foram reproduzidas;
3. existe benchmark;
4. a melhoria é mensurável;
5. a hipótese é falsificável;
6. o protocolo aberto continua suficiente para interoperabilidade.

Até esse gate, o Core deve permanecer vazio de claims proprietários.

## Regra humana

Caso desconhecido não é auto-promovido a verdade operacional.

Fluxo aberto de referência:

`retrieve known -> decide`

ou:

`pause -> sanitize -> human sandbox -> explicit resolution -> retain -> resume`

LLMs podem auxiliar pesquisa e preparação de alternativas, mas não criam autoridade
operacional por si mesmas.
