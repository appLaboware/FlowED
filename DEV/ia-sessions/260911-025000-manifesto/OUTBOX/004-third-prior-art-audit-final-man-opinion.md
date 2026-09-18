# MAN-001 → PO-001 — parecer final sobre a terceira auditoria de anterioridade

**Origem:** interação direta `HUMAN_CHAT`, fora da tarefa ordinária pedida pelo PO.

## Síntese

A terceira auditoria é significativamente melhor que as duas anteriores porque adota uma matriz por claim e reconhece que antecedente próximo não implica identidade. Ainda assim, **não deve ser tratada como mapa validado nem como definição final do FlowED**.

Minha conclusão atual é:

> Os antecedentes reduzem fortemente qualquer pretensão de novidade dos ingredientes isolados do FlowED, mas ainda não demonstram equivalência com a composição/hierarquia atual dos três princípios. A maior ameaça não é "a ideia já existir", e sim descrevermos o FlowED com claims mais fortes do que o próprio manifesto realmente faz.

## 1. Correções importantes que a terceira auditoria acertou

- reconhece corretamente a existência de `Intent-based System Design and Operation` (Microsoft Research / arXiv 2502.05984, 2025);
- trata Simonyi/Intentional Programming, MDA/OMG, Cockburn, design rationale e lenses como antecedentes relevantes;
- substitui o julgamento binário de ineditismo por uma análise de grau de relação;
- abandona os rótulos anteriores de `polyhedral`, `FinOps routing`, áudio/fones etc. como se fossem invariantes do manifesto.

## 2. Problema central remanescente: os claims P1/P2/P3 ainda não correspondem fielmente ao manifesto

### P1

A auditoria formula P1 como:

`intenção = entidade primária, invariante e autoritativa; código = artefato derivado, descartável`.

Isso é mais forte do que o manifesto atual. P1 hoje afirma separação entre intenção e materialização, maior durabilidade relativa da intenção, linguagem orientada à intenção e menor custo de readaptação. Não afirma que toda intenção seja invariante, que ela seja sempre autoritativa nem que todo código seja descartável.

### P2

A auditoria formula P2 como transferência da garantia de funcionamento da fiscalização humana da sintaxe para contratos/políticas invariantes em runtime e como contenção de automações estocásticas.

O P2 atual trata de **coerência operacional organizacional**: identidade operacional podendo residir mais em princípios e contratos do que em tecnologias; liberdade local sem fragmentação; contratos como possível locus primário de coerência. Runtime, LLMs, safety gates e verificação de sintaxe são possíveis materializações/compromissos derivados, não o princípio filosófico atualmente escrito.

### P3

A auditoria formula P3 como `histórico cognitivo = ativo primário e permanente; códigos/documentos/diagramas = projeções derivadas não-autoritativas`.

O manifesto atual faz uma distinção mais sutil: o caminho cognitivo pode ter **primazia epistêmica** para compreender, criticar e evoluir, enquanto um consolidado congelado pode manter **autoridade normativa** para cumprimento. Portanto `source of truth`, `repositório normativo` e `projeções não-autoritativas` são formulações perigosas se usadas sem essa distinção.

## 3. Antecedentes que realmente pressionam o FlowED

### Intentional Programming — Simonyi, 1995

É antecedente forte, não apenas de AST. A própria Microsoft Research descreve intenção como mecanismo de abstração e software intencional como capaz de preservar significado independentemente da evolução de notação e técnicas de implementação. Portanto o residual do P1 não pode ser simplesmente `preservar intenção apesar da mudança tecnológica`.

### MDA — OMG/NIST, 2000–2001

É antecedente fortíssimo. OMG define PIM estável enquanto a tecnologia evolui e geração/mapeamento para PSM/implementação; NIST descreve a transição para um regime em que o modelo normativo tem precedência sobre outros artefatos. O argumento `preserve o que muda menos, regenere o que muda mais` já possui parentes próximos claros.

A terceira auditoria também exagera ao descrever MDA como obrigatoriamente dependente de UML: OMG informa que UML é comum, mas não requisito; MOF é a fundação obrigatória.

### GitHub Spec Kit / SDD — antecedente recente muito próximo e omitido nesta terceira matriz

A documentação atual do Spec Kit diz explicitamente:

- especificações tornam-se artefato primário/source of truth;
- código serve à especificação e pode ser regenerado;
- intenção fica no centro;
- princípios organizacionais/guardrails condicionam geração;
- implementações paralelas podem partir da mesma especificação;
- feedback de produção pode voltar para refinamento da especificação.

Para P1 e para o loop `intenção/especificação → implementação → evidência → revisão`, este antecedente é hoje mais próximo do que vários itens presentes na matriz e deve obrigatoriamente entrar em qualquer auditoria séria.

## 4. Outras qualificações técnicas

- Ports & Adapters não deve ser descrito simplesmente como `adaptadores estáticos`; o artigo original admite múltiplos adapters por porta. O padrão apenas não especifica, por si, service discovery/capability routing dinâmico.
- ADRs/IBIS não são apenas `atas estáticas`; o contraste defensável é que design rationale tradicional registra/estrutura racional, enquanto o FlowED está explorando uma base cognitiva capaz de alimentar projeções e materializações. Ainda precisa ser demonstrado que essa hierarquia/composição é distintiva.
- Lenses/view-update são antecedentes formais de sincronização entre fonte e view. Dizer que o FlowED `resolve` o problema porque projeções são descartáveis é excessivo. Se projeções puderem receber alterações/feedback, o problema de consistência reaparece. Além disso, algumas projeções podem ser normativamente autoritativas mesmo sem serem fonte epistêmica.

## 5. Rejeição da tese final proposta pela consultoria

Não aceito como definição atual do FlowED:

`arquitetura de governança epistemológica para desenvolvimento assistido por agentes` + `código como efeito colateral` + `contenção contratual contra não-determinismo de LLMs`.

Esses itens podem vir a ser compromissos derivados ou propriedades de uma implementação, mas **não são a formulação canônica dos três princípios filosóficos atuais** e estreitariam indevidamente FlowED a agentes/LLMs.

O manifesto deve continuar válido mesmo quando a materialização não usa IA generativa.

## 6. Parecer de posicionamento

Estado atual mais defensável:

- **novidade dos ingredientes isolados:** baixa;
- **relevância/timing:** alta, porque indústria e pesquisa convergem fortemente para intent/spec-driven development;
- **novidade da composição/hierarquia:** ainda não demonstrada nem refutada;
- **risco principal:** confundir implementação contingente com filosofia e criar claims artificiais só para fabricar residual;
- **candidato de residual:** a reponderação conjunta de (a) intenção como superfície operacional durável, (b) contratos como locus primário de coerência operacional organizacional e (c) caminho cognitivo como fonte epistêmica capaz de gerar projeções com autoridade separada da primazia epistemológica.

Esse residual precisa ser comparado claim a claim com MDA, Intentional Programming, Spec Kit/SDD, design rationale, MDE/lenses, policy-as-code e sistemas intent-based antes de qualquer alegação de ineditismo.

## 7. Recomendação operacional

Não alterar o manifesto com base nesta auditoria externa. Primeiro construir uma matriz canônica **a partir do texto real do manifesto**, e só depois procurar o antecedente mais próximo de cada claim.

Formato recomendado:

`claim canônico do manifesto → fonte do claim → antecedente → relação (equivalência / sobreposição / analogia / diferença) → residual real → força da evidência → implicação editorial`

A auditoria externa fez o inverso em alguns pontos: inventou uma versão mais forte do claim e depois encontrou um residual para ela. Isso deve ser evitado.

## 8. Estado da frente MAN-001

Esta auditoria foi iniciada diretamente pelo humano e continua explicitamente fora da tarefa ordinária do PO. P2.3 não foi alterada. Após este parecer, MAN-001 pode retornar ao trabalho do manifesto, salvo nova orientação humana/PO.
