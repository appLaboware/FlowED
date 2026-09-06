# Telemetria Operacional, Pesquisa e Produtos de Dados — Separação de Domínios v0.1

**Status:** BLUEPRINT / ASPIRATIONAL

## Princípio

O FlowED deve tratar como domínios distintos:

1. **Telemetria Operacional** — evidência necessária para compreender, verificar, operar e melhorar execuções.
2. **Dados de Pesquisa** — dados derivados ou selecionados para responder perguntas científicas sob protocolo explícito.
3. **Produtos de Dados** — métricas, benchmarks ou agregações destinados a uso externo, comercial ou institucional.

Esses domínios podem compartilhar uma origem factual, mas **não compartilham automaticamente finalidade, autoridade, retenção, acesso ou permissão de uso**.

> **Instrumentar não autoriza pesquisar. Pesquisar não autoriza publicar. Publicar não autoriza comercializar.**

## Lei arquitetural

Nenhum dado coletado para uma finalidade pode migrar para outra finalidade sem uma transformação e uma autorização explicitamente governadas.

```text
EXECUÇÃO
   ↓
telemetria operacional
   ↓ autorização + transformação
conjunto de pesquisa
   ↓ autorização + agregação / anonimização adequada
produto de dados
```

A existência de um estágio anterior nunca implica autorização automática para o estágio seguinte.

## 1. Telemetria Operacional

Finalidade primária:
- rastreabilidade;
- evidência de execução;
- depuração;
- auditoria;
- homologação;
- análise de custo e eficiência operacional;
- detecção de falhas, drift e regressões.

Exemplos de campos possíveis:
- `execution_id`;
- `session_id`;
- `capability_id`;
- `execution_scenario`;
- modelo/runtime utilizado;
- toolset;
- duração;
- custo;
- tokens/contexto quando aplicável;
- chamadas de ferramentas;
- retries;
- intervenção humana;
- resultados de validadores;
- evidências produzidas;
- estado de homologação.

A telemetria operacional deve ser suficiente para responder **o que aconteceu**, **como aconteceu**, **quanto custou**, **com quais evidências** e **qual foi o resultado operacional**.

## 2. Dados de Pesquisa

Dados de pesquisa não são sinônimo de logs operacionais.

A pesquisa deve possuir, no mínimo:
- pergunta ou hipótese;
- protocolo;
- variáveis;
- unidade de análise;
- critérios de inclusão/exclusão;
- transformação da fonte operacional;
- política de minimização;
- autorização apropriada;
- retenção;
- critérios de publicação/reprodutibilidade.

Uma observação científica pode ser derivada da telemetria, mas deve ser materializada como artefato próprio e possuir proveniência até a evidência operacional de origem.

## 3. Produtos de Dados

Produtos de dados constituem um terceiro domínio.

Exemplos:
- benchmarks agregados;
- séries históricas de custo/qualidade;
- índices de cobertura;
- distribuições estatísticas;
- comparações de cenários de execução;
- métricas de produtividade ou confiabilidade.

Regra padrão:

> **Produtos de dados devem preferir métricas agregadas e irreversíveis a conversas, prompts, código-fonte, documentos ou eventos individuais.**

Conteúdo bruto de sessões não deve ser tratado como produto comercial por simples remoção de identificadores.

## 4. Níveis de uso

### Nível 0 — Operacional
Uso local ou organizacional para executar, validar, auditar e melhorar o sistema.

### Nível 1 — Pesquisa
Uso científico explicitamente autorizado, minimizado e governado por protocolo.

### Nível 2 — Produto de Dados
Uso estatístico, institucional ou comercial com política própria de agregação, publicação e acesso.

A passagem entre níveis é uma **mudança de finalidade**, não uma simples cópia de dados.

## 5. Separação física e lógica

A implementação futura deve permitir separar:
- schemas;
- stores;
- políticas de retenção;
- chaves de acesso;
- pipelines;
- permissões;
- identidades de consumidores;
- exportações;
- trilhas de auditoria.

Mesmo quando uma infraestrutura compartilhada for utilizada, as fronteiras lógicas devem permanecer explícitas e verificáveis.

## 6. Proveniência

Todo dado derivado deve permitir reconstruir sua linhagem:

```text
EXECUTION EVENT
   ↓
OPERATIONAL RECORD
   ↓ transformation_id
RESEARCH OBSERVATION
   ↓ aggregation_id
DATA PRODUCT METRIC
```

A derivação deve registrar, quando aplicável:
- fonte;
- transformação;
- versão do schema;
- versão do código de transformação;
- momento;
- autorização;
- finalidade.

## 7. Privacidade e minimização

O FlowED deve buscar:

> **Instrumentar tudo que seja útil; coletar nada que seja desnecessário; compartilhar nada sem autorização explícita.**

A capacidade de medir uma execução não cria obrigação de armazenar todo seu conteúdo.

Devem ser preferidas métricas estruturadas sobre captura indiscriminada de texto bruto.

## 8. Independência arquitetural

A telemetria não pode tornar-se dependência necessária do artefato final.

O produto materializado pelo FlowED deve continuar nativo e operável mesmo se toda a infraestrutura de telemetria, pesquisa e produtos de dados for removida.

> **Evidência pode acompanhar o processo; dependência não pode contaminar o produto.**

## 9. Relação com pesquisa empírica

A separação proposta permite que o FlowED funcione simultaneamente como:
- sistema operacional de engenharia;
- infraestrutura experimental;
- objeto de estudo;
- fonte potencial de métricas agregadas.

Essas funções permanecem soberanas entre si.

O mesmo conjunto de capabilities pode ser executado em cenários diferentes (`prompt-only`, `assisted`, `agent`, `deterministic`, ou outros futuros) e comparado mediante métricas homogêneas, desde que a coleta de pesquisa seja explicitamente autorizada e separada da finalidade operacional.

## 10. Artefatos iniciais

Esta versão introduz três contratos iniciais independentes:
- `schemas/telemetry/operational-event.schema.json`
- `schemas/research/research-observation.schema.json`
- `schemas/data-products/aggregate-metric.schema.json`

Eles são artefatos de blueprint e não constituem compromisso com tecnologia de armazenamento, transporte ou implementação.

## Regra final

> **Telemetria operacional prova a execução. Dados de pesquisa respondem perguntas científicas. Produtos de dados comunicam métricas derivadas. Nenhum dos três recebe automaticamente a autoridade dos outros dois.**
