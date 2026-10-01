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

## Coerência com a implementação de referência atual

A implementação em `reference/provider_server.py` é deliberadamente uma baseline
OPEN, não o futuro MyTrues Core.

Hoje ela faz:

1. procura uma decisão persistida por `failure_code` na memória SQLite do fornecedor;
2. se existir, materializa e devolve `200 decided`;
3. se não existir, cria um pedido pendente e devolve
   `202 awaiting-provider-decision`;
4. produz um `casePacket` sanitizado para o fornecedor;
5. aceita uma resolução explícita no endpoint provider-side;
6. persiste essa resolução somente na memória daquele fornecedor;
7. em ocorrência futura do mesmo failure code, reutiliza a decisão persistida.

O conformance v0.2 prova esse comportamento em Actions, inclusive após restart.

### O que essa referência NÃO faz

Ela não:

- gera uma nova decisão por LLM;
- promove similaridade vetorial a autoridade;
- escolhe autonomamente uma solução para caso desconhecido;
- implementa CBR completo, MCDA, Bayes, learning-to-rank ou outro algoritmo
  científico ainda não reproduzido;
- autentica hoje a operação provider-side;
- constitui propriedade intelectual proprietária.

### Seeds não são algoritmo

Decisões pré-carregadas para um fornecedor são **dados/memória de referência**.

Elas podem ser públicas no laboratório ou privadas em uma instância real, mas sua
existência não transforma o mecanismo simples de lookup em Core proprietário.

O futuro Core, se existir, fica atrás do protocolo aberto e precisa atravessar o
Science Frontier Gate antes de receber qualquer claim de superioridade.


## Storage boundary

The current reference implementation in `reference/provider_server.py` persists
provider state in SQLite through `MYTRUES_DB_PATH`.

That is the executable reference runtime proved by conformance.

Neo4j material under `memory/neo4j/` is historical/schema reference only after the
2026-10-01 license gate and is not a MyTrues runtime dependency.

## Seed loading boundary

`MYTRUES_SEED_MANIFEST` loads provider-specific decisions into the same SQLite
reference memory.

This is **data initialization**, not decision algorithm behavior:

- the provider receives only decisions explicitly assigned to its ID;
- absence of a decision still follows the normal unknown-case `202` path;
- the seed cannot manufacture a decision for the control case;
- seed-004 conformance run `36874885444` proves this behavior.
