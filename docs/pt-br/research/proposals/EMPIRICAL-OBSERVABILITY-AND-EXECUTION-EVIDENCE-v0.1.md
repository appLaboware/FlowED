# Observabilidade Empírica e Evidência de Execução — Proposta de Pesquisa v0.1

**Status:** RESEARCH PROPOSAL / UNVALIDATED

## Pergunta central

É possível instrumentar execuções de engenharia de software de forma suficientemente estruturada para comparar custo, qualidade, variabilidade, intervenção humana, reprodutibilidade e cobertura entre diferentes cenários de execução, sem transformar telemetria operacional em coleta científica ou produto de dados por padrão?

## Motivação

O FlowED pretende permitir que a mesma intenção operacional seja executada por mecanismos diferentes, preservando contrato, critérios de aceitação e evidência. Isso cria a possibilidade de comparar cenários como:

- prompt-only;
- assisted;
- agent;
- deterministic;
- futuros cenários homologados.

A comparação só é cientificamente defensável se:

1. a semântica da capability permanecer comparável;
2. as métricas forem definidas antes da análise;
3. a coleta operacional for separada da finalidade de pesquisa;
4. a derivação dos dados possuir proveniência;
5. a autorização de uso for explícita;
6. o artefato produzido não depender da instrumentação.

## Hipótese candidata

> **Execuções de uma mesma capability, submetidas ao mesmo contrato, critérios de aceitação e política de evidência, podem ser comparadas empiricamente por telemetria estruturada, desde que os dados científicos sejam derivados sob protocolo explícito e separados da coleta operacional.**

Esta hipótese não constitui reivindicação de novidade.

## Variáveis candidatas

### Eficiência
- tempo total;
- tempo humano;
- tempo de modelo/runtime;
- custo estimado;
- tokens/contexto;
- número de chamadas de ferramentas;
- retries.

### Qualidade
- aceitação/rejeição;
- número de defeitos;
- rework;
- cobertura de evidência;
- resultados de validadores;
- estado de homologação.

### Variabilidade
- dispersão de tempo;
- dispersão de custo;
- dispersão de resultados;
- frequência de intervenção humana;
- frequência de escalonamento.

### Reprodutibilidade
- repetibilidade da execução;
- equivalência dos artefatos;
- estabilidade frente à repetição;
- dependência de inferência probabilística.

### Cobertura
Métrica candidata:

```text
coverage(processo) =
capabilities técnicas necessárias ao processo executáveis via FlowED
/
capabilities técnicas necessárias ao processo estudado
```

A cobertura deve ser definida para um processo ou escopo observado, nunca presumida como completude universal da Engenharia de Software.

Duas dimensões candidatas:
- **coverage breadth** — quantas capabilities necessárias são alcançadas;
- **coverage depth** — quanto de cada capability pode ser executado sem abandonar a porta operacional do FlowED.

## Unidade experimental candidata

Uma execução de capability sob:
- versão conhecida do contrato;
- cenário de execução conhecido;
- entradas controladas;
- critérios de aceitação conhecidos;
- evidência verificável.

## Desenho experimental inicial

```text
MESMA INTENÇÃO
     ↓
MESMO CONTRATO
     ↓
MESMAS ENTRADAS / CLASSES DE ENTRADA
     ↓
MESMOS CRITÉRIOS DE ACEITAÇÃO
     ↓
S0 / S1 / S2 / S3 / S4
     ↓
TELEMETRIA OPERACIONAL
     ↓ transformação governada
DADOS DE PESQUISA
     ↓
COMPARAÇÃO
```

## Critérios de falsificação

A linha de pesquisa deve ser enfraquecida ou rejeitada se, entre outros casos:
- os cenários não puderem ser comparados sem alterar materialmente a semântica da capability;
- as métricas estruturadas não capturarem diferenças relevantes observáveis;
- a coleta necessária exigir conteúdo excessivo ou incompatível com minimização e privacidade;
- o custo da instrumentação superar de modo injustificado o valor experimental;
- a variabilidade não puder ser atribuída com evidência suficiente ao cenário estudado.

## Separação obrigatória de domínios

Esta proposta depende do documento:
`docs/pt-br/architecture/TELEMETRY-RESEARCH-AND-DATA-PRODUCT-SEPARATION-v0.1.md`.

A pesquisa não recebe autoridade automática sobre logs operacionais, e resultados de pesquisa não se tornam produto de dados automaticamente.

## Próximo gate

Antes de qualquer alegação de contribuição científica, realizar busca de prior art em:
- empirical software engineering;
- software process telemetry;
- developer productivity measurement;
- AI-assisted software engineering evaluation;
- experiment instrumentation;
- provenance;
- reproducible software engineering experiments;
- process mining;
- observability applied to software engineering workflows.

Classificar o resultado como adoção, extensão, composição conhecida, residual potencial ou ausência de evidência suficiente.
