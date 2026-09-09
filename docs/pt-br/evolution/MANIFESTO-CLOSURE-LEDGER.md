# Ledger de fechamento do Manifesto FlowED

**Status:** regra operacional de fechamento conceitual da fase atual.

## Regra de fechamento

O objetivo imediato é **terminar o manifesto**, não implementar todas as materializações nem fechar todas as linhas de pesquisa derivadas.

Para cada pilar ou afirmação estrutural do manifesto, a rodada deve responder somente o suficiente para estabelecer que:

1. o conceito é coerente com o animal FlowED;
2. não depende de uma implementação única;
3. existe pelo menos um caminho plausível/realizável de materialização;
4. gaps de implementação, formalização ou pesquisa podem ser deixados como linhas abertas para continuidade posterior;
5. uma linha aberta não bloqueia o manifesto quando sua realizabilidade conceitual já está suficientemente estabelecida.

A partir desse ponto, a discussão deve avançar para o próximo elemento do manifesto. O aprofundamento técnico fica para ciclos posteriores.

## Pilar 1 — Unidade operacional e liberdade governada

**Estado para fechamento do manifesto:** suficientemente realizável nesta fase.

A discussão estabeleceu que FlowED pode se orientar por uma linguagem pública comum e contratos públicos, mantendo implementações livres e substituíveis. `flwd`, YAML, API e outros clientes podem projetar a mesma semântica pública sem obrigar o FlowED a conhecer mecanismos internos.

Ports, adapters, providers, mocks, contract testing e demais mecanismos permanecem como possíveis materializações e linhas de continuidade, não como assuntos que precisem ser fechados antes do manifesto.

A linha de pesquisa derivada da composição test-driven/contract-driven permanece aberta e não bloqueia o manifesto.

## Pilar 2 — Autoeducação e conhecimento vivo

**Estado para fechamento do manifesto:** em aprofundamento; realizabilidade fortemente avançada, ainda aguardando decisão do princípio mínimo.

A primeira formulação — apenas registrar experiência e permitir que ela altere conscientemente a forma de trabalhar — foi considerada fraca. A rodada seguinte aprofundou o mecanismo de realizabilidade.

Há prior art suficiente para estruturar memória operacional sem inventar logging do zero: IEEE XES e Process Mining para event logs interoperáveis/analisáveis, W3C PROV para proveniência, OpenTelemetry para structured logs/events, CloudEvents para envelope interoperável e Event Sourcing quando histórico temporal completo for adequado.

Hipótese FlowED atual:

**contrato público → execução → evento estruturado derivado do contrato → memória operacional → ligação com decisão/referência/racional → análise/aprendizagem → possível revisão da forma de trabalhar.**

Duas memórias devem permanecer distinguíveis, porém correlacionáveis:

- **memória operacional** — o que ocorreu;
- **memória decisória/cognitiva** — por que foi feito, escolhido ou alterado.

O papel candidato do MyTrues é relacionar memória operacional com decisões, referências, evidências e linhagem cognitiva; ele não precisa ser o logger nem o executor. EDT/CCP permanecem referências para aprendizagem, racional e projeção do conhecimento.

Formulação candidata mais forte para o Pilar 2:

> **Toda execução relevante deve poder deixar uma memória operacional estruturada e relacionável às decisões, referências e evidências que a contextualizam. O FlowED deve permitir que essa memória seja reutilizada para compreender o que ocorreu, confrontar intenção com resultado e evoluir conscientemente a forma de trabalhar.**

A implementação específica — schema, banco, broker, OpenTelemetry/XES/CloudEvents concretos, MyTrues, algoritmos de análise — permanece aberta e não precisa ser fechada no manifesto.

Pendência para encerrar o Pilar 2: decidir o significado mínimo de **execução relevante** e se a correlação execução ↔ decisão/referência é constitutiva ou apenas materialização preferida.

Documento de aprofundamento: `PILAR-2-STRUCTURED-OPERATIONAL-MEMORY-DRAFT.md`.

## Próximo passo

Fechar a formulação mínima do Pilar 2 sem projetar ainda sua implementação. Depois avançar diretamente ao Pilar 3.
