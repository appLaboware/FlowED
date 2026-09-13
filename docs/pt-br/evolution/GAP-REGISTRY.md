# FlowED Gap Registry

**Status:** cadastro operacional preliminar para simulação do papel futuro de MyTrues.

Este arquivo não substitui issue tracker nem banco de conhecimento. Seu objetivo é normalizar gaps conceituais, científicos, empíricos e operacionais durante a evolução do Manifesto FlowED.

## Convenção de estados

- **OPEN** — gap reconhecido e não resolvido;
- **PARTIAL** — existe avanço relevante, mas condição de fechamento ainda não foi satisfeita;
- **BLOCKING** — impede evolução no escopo declarado;
- **CLOSED** — condição de fechamento satisfeita com evidência/racional registrado;
- **SUPERSEDED** — substituído por formulação posterior, preservando histórico.

## Cadastro atual

### GAP-M001 — Critério mínimo de pertencimento / Full FlowED

**Tipo:** conceitual / certificação  
**Estado:** OPEN  
**Impacto:** alto  
**Bloqueia manifesto:** não  
**Bloqueia certificação:** sim  
**Pergunta:** qual conjunto mínimo de comportamentos permite afirmar conformidade FlowED sem exigir alinhamento obrigatório ao baseline?  
**Fechamento:** definição operacional testável, com separação entre conformidade, alinhamento e sustentação.

### GAP-M002 — Modelo de score multidimensional

**Tipo:** mensuração  
**Estado:** OPEN  
**Impacto:** alto  
**Bloqueia manifesto:** não  
**Bloqueia certificação:** sim  
**Pergunta:** quais dimensões são medidas, como são calculadas e quais não devem ser reduzidas a um escalar único?  
**Fechamento:** modelo reproduzível com limites e decisões humanas explícitas.

### GAP-M003 — Mínimo informacional por interlocutor

**Tipo:** conceitual / operacional / EDT  
**Estado:** PARTIAL  
**Impacto:** alto  
**Bloqueia manifesto:** não  
**Pergunta:** como determinar informação suficiente sem paternalismo, omissão, sobrecarga ou opacidade?  
**Condições adicionais da rodada 001:** projeção deve ser explicável, contestável, auditável e permitir acesso à referência canônica e aprofundamento, salvo restrição legítima.  
**Fechamento:** protocolo/algoritmo conceitual capaz de justificar mínimo, permitir contestação e preservar fonte.

### GAP-M004 — Unidade primária da linguagem operacional

**Tipo:** conceitual / arquitetural  
**Estado:** OPEN  
**Impacto:** alto  
**Bloqueia manifesto:** não  
**Bloqueia especificação formal:** sim  
**Pergunta:** intenção, capability, ação, contrato ou composição é a unidade primária?  
**Fechamento:** ontologia mínima capaz de explicar comandos, contratos e materializações sem ambiguidade estrutural.

### GAP-M005 — Coordenação comum versus soberania dos domínios

**Tipo:** arquitetural  
**Estado:** OPEN  
**Impacto:** alto  
**Bloqueia manifesto:** não  
**Pergunta:** o que é governado centralmente e o que permanece soberano em cada domínio?  
**Fechamento:** fronteira pública definida e testada em pelo menos dois domínios distintos.

### GAP-M006 — Mínimo constitutivo de autoeducação

**Tipo:** conceitual / EDT  
**Estado:** OPEN  
**Impacto:** alto  
**Bloqueia identidade FlowED:** potencialmente  
**Pergunta:** registrar experiência basta ou é necessário reavaliar referências, produzir projeções, alterar modo de trabalho ou outro comportamento mínimo?  
**Fechamento:** definição mínima que diferencie autoeducação FlowED de simples logging/documentação.

### GAP-M007 — Necessidade do artigo-pai de síntese

**Tipo:** científico  
**Estado:** OPEN  
**Impacto:** alto  
**Bloqueia publicação conceitual definitiva:** sim  
**Pergunta:** existe teoria anterior que cubra suficientemente o animal ou será necessário construir síntese própria?  
**Fechamento:** revisão de anterioridade declarada.

### GAP-M008 — Formalização do CCP/CCC

**Tipo:** científico / conceitual / operacional  
**Estado:** OPEN  
**Impacto:** alto  
**Bloqueia EDT definitivo:** potencialmente  
**Pergunta:** como normalizar traços cognitivos externalizados sem afirmar captura de cognição privada?  
**Fechamento:** modelo/protocolo mínimo com fonte, interpretação, decisão, racional, evidência, alternativas e reprocessamento.

### GAP-M009 — Fronteiras entre classes de sustentação

**Tipo:** epistemológico / mensuração  
**Estado:** OPEN  
**Impacto:** alto  
**Pergunta:** como separar ciência, norma, padrão, experimento, evidência operacional, experiência contextual e decisão?  
**Fechamento:** taxonomia e regras de avaliação que evitem equivalência indevida entre classes.

### GAP-M010 — Independência e suficiência dos quatro pilares

**Tipo:** conceitual  
**Estado:** PARTIAL  
**Impacto:** alto  
**Evidência atual:** `EVID-MSIM-001` — análise documental encontrou funções conceituais distintas e nenhuma redundância obrigatória.  
**Limite:** ainda sem validação por uso real ou crítica externa.  
**Fechamento:** estabilidade após novas rodadas e teste em cenários de aplicação.

### GAP-M011 — Abrangência pretendida versus cobertura implementada

**Tipo:** conceitual / escopo  
**Estado:** OPEN  
**Impacto:** médio-alto  
**Origem:** simulação 001  
**Pergunta:** como dizer “todos os domínios da Engenharia de Software” sem prometer cobertura concreta imediata?  
**Fechamento:** distinção explícita entre abertura arquitetural de escopo e capabilities efetivamente disponíveis por versão.

### GAP-M012 — Complexidade operacional percebida

**Tipo:** mensuração / tese  
**Estado:** OPEN  
**Impacto:** alto  
**Origem:** simulação 001  
**Pergunta:** a tese central usa um constructo mensurável, proxies ou conceito apenas qualitativo?  
**Fechamento:** operacionalização observável suficiente para teste ou reformulação da tese para não fingir mensurabilidade.

### GAP-M013 — Adapt First no manifesto

**Tipo:** conceitual / metodológico  
**Estado:** OPEN  
**Impacto:** alto  
**Origem:** simulação 001  
**Pergunta:** adotar → adaptar → compor → inventar deve ser princípio constitutivo explícito ou regra metodológica subordinada?  
**Fechamento:** posição hierárquica definida e refletida no fluxo fundamental.

### GAP-M014 — Portas de entrada do fluxo fundamental

**Tipo:** conceitual / processo  
**Estado:** OPEN  
**Impacto:** alto  
**Origem:** simulação 001  
**Pergunta:** como o fluxo representa referência criada internamente, adotada, adaptada ou composta sem obrigar tudo a nascer como esboço?  
**Fechamento:** fluxo geral com entradas normalizadas e trajetória epistemológica posterior comum.

### GAP-M015 — Significado operacional de “liberdade governada”

**Tipo:** conceitual / arquitetural  
**Estado:** OPEN  
**Impacto:** médio-alto  
**Origem:** simulação 001  
**Pergunta:** quais propriedades são obrigatoriamente governadas para que diversidade não se torne caos?  
**Fechamento:** conjunto mínimo de governança definido: candidatos atuais incluem intenção, contrato, composição, interoperabilidade, rastreabilidade e substituição.

### GAP-M016 — Formulação final do Pilar 3

**Tipo:** terminológico / epistemológico  
**Estado:** OPEN  
**Impacto:** alto  
**Origem:** simulação 001  
**Pergunta:** “sustentação científica e empírica explícita” comunica prioridade sem excluir normas, padrões, legislação, operação e decisão contextual?  
**Fechamento:** nome e enunciado coerentes com a taxonomia de sustentação.

### GAP-M017 — Fronteira mínima de busca de evidência

**Tipo:** científico / protocolo  
**Estado:** OPEN  
**Impacto:** alto  
**Origem:** simulação 001  
**Pergunta:** quando é legítimo declarar que uma referência possui ou não sustentação externa suficiente?  
**Fechamento:** protocolo com escopo de busca declarado, data, fontes/bases, critérios de inclusão e nível de diligência apropriado ao risco.

### GAP-M018 — Progressividade bidirecional e gatilhos de intensidade

**Tipo:** conceitual / operacional  
**Estado:** OPEN  
**Impacto:** alto  
**Origem:** simulação 001  
**Pergunta:** quando aumentar, manter ou reduzir rigor/intensidade e quem decide?  
**Decisão provisória:** progressividade é movimento governado de adequação, não crescimento unidirecional.  
**Fechamento:** gatilhos e autoridade definidos e testáveis.

### GAP-M019 — Rastreabilidade pilar → princípio

**Tipo:** documental / conceitual  
**Estado:** OPEN  
**Impacto:** médio  
**Origem:** simulação 001  
**Pergunta:** como princípios deixam de ser lista plana e passam a ser projeções de aprofundamento dos pilares?  
**Fechamento:** cada princípio com pilar primário, relações secundárias e racional consultável.

### GAP-M020 — Princípios constitutivos versus hipóteses de benefício

**Tipo:** epistemológico / manifesto  
**Estado:** OPEN  
**Impacto:** alto  
**Origem:** simulação 001  
**Pergunta:** quais enunciados definem FlowED e quais apenas expressam efeitos esperados ainda a validar?  
**Exemplo:** acompanhar estudante → profissional → equipe → organização é hoje hipótese forte, não resultado demonstrado.  
**Fechamento:** classificação explícita de cada princípio e benefício esperado.

## Evidências ligadas ao cadastro

### EVID-MSIM-001

**Descrição:** primeira aplicação manual do protocolo de simulação ao Manifesto FlowED 001.  
**Classe:** operacional/documental.  
**Força provisória:** baixa.  
**Suporta:** utilizabilidade inicial do protocolo para organizar crítica e gaps; suporte conceitual inicial à independência dos quatro pilares.  
**Não suporta:** eficácia geral do FlowED, validade científica do manifesto, eficácia do EDT/CCP, scoring, MyTrues ou documentação dinâmica em produção.  
**Fonte:** `MANIFESTO-SIMULATION-ROUND-001.md`.

## Regra de atualização

Nenhum gap deve ser apagado quando resolvido. Deve mudar de estado e preservar a referência da decisão/evidência que motivou a transição. Um gap dividido em vários deve ser marcado como `SUPERSEDED` e apontar para seus sucessores.
