# Protocolo Canônico de Evolução de Ferramentas

## 1. Objetivo

Levar cada ferramenta ao limite prático da ciência, dos padrões e das implementações
públicas conhecidas antes de criar comportamento proprietário.

Este protocolo vale para Porter/CNAB, MyTrues, bancos de memória, provedores cloud,
protocolos, motores de decisão e futuras ferramentas.

## 2. Escada obrigatória

### E0 — DISCOVER

Pesquisar:

- especificação oficial;
- documentação atual;
- implementações maduras;
- extensões oficiais;
- literatura científica;
- benchmarks;
- limitações conhecidas;
- licenças e riscos de lock-in.

Saída obrigatória: dossiê versionado com fontes e data da revisão.

### E1 — ADOPT

Usar a ferramenta como foi projetada, sem wrapper próprio quando não necessário.

Critério de saída:

- capacidade executada de verdade;
- resultado reproduzível;
- versão e configuração registradas;
- limite observado separado de erro de configuração.

### E2 — EXHAUST CONFIGURATION

Antes de código novo, esgotar:

- configuração nativa;
- CLI/API nativa;
- plugins/mixins/providers;
- schemas;
- lifecycle;
- storage oficial;
- mecanismos de composição;
- extensões publicadas.

Critério de saída: tabela `capability -> native mechanism -> evidence`.

### E3 — COMPOSE / PERSONALIZE

Compor ferramentas existentes ou escrever apenas adapters nos extension points
previstos pelos projetos upstream.

Regras:

- aplicação de ponta não deve depender do wrapper;
- o adapter deve poder ser removido/substituído;
- protocolo externo deve continuar aberto;
- a personalização não pode duplicar capacidade upstream.

### E4 — FORK

Fork é exceção.

Só é permitido quando:

1. a limitação é reproduzível;
2. não há configuração/extensão upstream suficiente;
3. a mudança upstream foi considerada;
4. manter o fork tem custo aceitável;
5. existe teste de compatibilidade com upstream.

Preferência: contribuir upstream antes de manter divergência privada.

### E5 — REPRODUCE STATE OF THE ART

Para domínios científicos, implementar ou integrar baselines representativos do
estado da arte conhecido.

Exemplos para decisão:

- regras/DMN;
- Case-Based Reasoning;
- MCDA/MCDM;
- decisão probabilística/Bayesiana;
- graph retrieval;
- vector retrieval;
- learning-to-rank;
- calibração/abstenção;
- human-in-the-loop.

Nenhum desses métodos é "core proprietário" apenas por ter sido implementado aqui.

### E6 — SCIENCE FRONTIER GATE

Uma lacuna só pode ser candidata a invenção quando houver evidência de que:

- os métodos públicos relevantes foram catalogados;
- pelo menos as baselines adequadas foram reproduzidas;
- existe benchmark representativo;
- a lacuna persiste sob comparação justa;
- os modos de falha são conhecidos;
- o ganho pretendido é mensurável;
- não existe solução pública razoavelmente equivalente.

Artefato obrigatório: `FRONTIER-CLAIM.md` com fontes, experimento, benchmark e
hipótese falsificável.

### E7 — INVENT

Implementar somente o delta que atravessou E6.

O código novo deve responder:

- qual baseline pública ele supera;
- por qual métrica;
- em quais condições;
- com qual custo;
- onde falha;
- como pode ser substituído.

## 3. Gates transversais

Cada estágio deve avaliar:

### Interoperabilidade
O consumidor consegue trocar a implementação sem reescrever a aplicação?

### Segurança
Secrets, identidades e dados reais estão fora de relatórios e casos sintéticos?

### Proveniência
É possível reconstruir quem decidiu, com quais evidências e qual resultado?

### Observabilidade
Falha, decisão, retry, fallback e resultado possuem trace/correlation ID?

### Reprodutibilidade
O experimento pode ser repetido por workflow limpo?

### Reversibilidade
O experimento sabe destruir apenas os recursos que criou?

### Custo operacional
Há medição de tempo, API calls, recursos, quotas e interação humana?

## 4. Classes de evidência

- **EVIDENCE-A** — execução real em infraestrutura externa.
- **EVIDENCE-B** — conformance/integration test reproduzível.
- **EVIDENCE-C** — teste unitário/sintético.
- **EVIDENCE-D** — documentação/hipótese ainda não executada.

Claims de capacidade do produto exigem A ou B.

## 5. Registro mínimo por ferramenta

Todo dossiê deve manter:

- versão/data observada;
- função no sistema;
- estágio E0–E7;
- capacidades nativas já exploradas;
- capacidades nativas ainda não exploradas;
- extensões oficiais;
- limites confirmados;
- limites apenas suspeitos;
- experimentos;
- upstreams relacionados;
- decisão de adoção/fork;
- próximo gate.

## 6. Regra open/core

### OPEN

Deve permanecer aberto:

- padrões;
- protocolos;
- ciência publicada;
- algoritmos conhecidos;
- reference implementations;
- conformance suites;
- adapters genéricos;
- baseline heuristics.

### PRIVATE DATA

Pode ser privado sem ser propriedade intelectual:

- secrets;
- dados de clientes;
- memória de casos de um técnico;
- preferências privadas;
- contratos;
- métricas internas.

### CORE

Só entra no Core:

- algoritmo/método original;
- não trivial;
- não equivalente a conhecimento público encontrado;
- validado contra baseline aberta;
- com ganho reproduzível.

## 7. Política de revisão

Cada dossiê deve ser revisitado quando ocorrer qualquer um:

- release major/minor relevante;
- depreciação upstream;
- novo padrão formal;
- experimento que contradiga claim anterior;
- fork local;
- nova baseline científica relevante.
