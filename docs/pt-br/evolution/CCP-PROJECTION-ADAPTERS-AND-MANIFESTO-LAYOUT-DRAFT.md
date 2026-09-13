# CCP — Projection Adapters and Manifesto Layout — Draft

**Status:** hipótese arquitetural e editorial para investigação posterior. Não normativa.

## 1. Observação de origem

Durante a revisão frase por frase do Manifesto FlowED surgiu uma necessidade dupla:

1. dar às proposições uma voz autoral consistente e um potencial de descoberta/epifania;
2. preservar a cognição que sustenta cada proposição sem obrigar todo consumidor a receber a mesma forma de apresentação.

A hipótese resultante é que uma única base cognitiva estruturada possa gerar projeções distintas para consumidores distintos, sem multiplicar a origem do conhecimento.

## 2. Hipótese de layout para proposições reflexivas

Para ideias e textos reflexivos, investigar uma cadência recorrente semelhante a:

`domínio reconhecido → tratamento já conhecido → deslocamento proposto → consequência causal / epifania`

### 2.1 Domínio reconhecido

Começar reconhecendo explicitamente aquilo que o público competente já sabe, evitando sugerir descoberta artificial de práticas consolidadas.

Exemplo abstrato:

> Contratos são amplamente utilizados, estudados e tratados como parte importante da engenharia.

A função dessa etapa não é ensinar o óbvio, mas declarar ao leitor: **sabemos que você já sabe disso e nossa proposta não depende de fingir novidade onde ela não existe.**

### 2.2 Tratamento atual / ponto de partida

Explicitar, de maneira curta, como aquele conceito costuma participar do domínio ou qual posição normalmente ocupa no raciocínio que está sendo discutido.

Essa etapa funciona como âncora cognitiva e fornece o ponto a partir do qual o manifesto deslocará importância, prioridade ou relação.

### 2.3 Deslocamento proposto

Declarar com precisão o que o FlowED propõe valorizar, centralizar, separar ou reposicionar.

Estrutura candidata:

> Não propomos X; propomos Y.

A oposição não deve ser usada como ornamento retórico. Ela deve tornar visível a diferença entre o estado reconhecido e o deslocamento conceitual efetivamente proposto.

### 2.4 Consequência causal / epifania

Mostrar a consequência esperada sem fechar todo o raciocínio, deixando uma inferência curta e segura para o leitor completar.

A formulação deve buscar uma reação cognitiva equivalente a:

> “Isso já estava diante de mim; agora a relação ficou evidente.”

A expressão informal “como eu não pensei nisso antes?” pode ser usada internamente como heurística de projeto, mas **não como critério científico ou obrigatório de sucesso**. A validação deve observar compreensão, inferência, surpresa produtiva, retenção e ausência de obscuridade ou manipulação.

## 3. Uma fonte cognitiva, múltiplas projeções

A arquitetura candidata separa:

- **fonte cognitiva estruturada** — o conhecimento, relações, razões, alternativas, evidências, decisões, autoridade e proveniência;
- **projeção** — uma materialização orientada a um consumidor, tarefa e contexto;
- **adapter de projeção** — mecanismo que transforma a mesma fonte em uma representação adequada sem alterar seu conteúdo epistemicamente relevante.

Forma conceitual:

```text
                 CCP / base cognitiva estruturada
                             │
                 ┌───────────┴───────────┐
                 │                       │
          adapter humano             adapter IA
                 │                       │
        projeção orientada          projeção orientada
      à cognição humana            ao consumo por modelo
```

Essa arquitetura não cria duas verdades. Ela cria duas projeções do mesmo conhecimento.

## 4. Adapter para humanos

Uma projeção destinada a humanos pode otimizar, conforme a intenção:

- ordem de leitura;
- atenção e hierarquia visual;
- concisão;
- cadência retórica;
- descoberta/epifania;
- progressive disclosure;
- exemplos e analogias;
- visualizações mínimas de causalidade;
- profundidade compatível com papel, risco e tarefa.

O adapter humano pode esconder complexidade inicial para preservar clareza e impacto, desde que mantenha acesso progressivo às camadas necessárias e não oculte cognição obrigatória para aquele público.

## 5. Adapter para IA

Uma projeção destinada a IA pode priorizar características diferentes, por exemplo:

- semântica explícita;
- relações tipadas;
- identificação de autoridade;
- estado epistêmico;
- proveniência;
- premissas e conclusões separadas;
- alternativas aceitas, rejeitadas e superadas;
- restrições;
- causalidade declarada;
- identificadores estáveis;
- estrutura determinística e, quando útil, machine-readable;
- redução de ambiguidade e dependência de inferência implícita.

A projeção para IA não precisa reproduzir o estilo persuasivo ou epifânico destinado a humanos. Seu objetivo é permitir que o modelo receba a mesma base com a estrutura que melhor favoreça interpretação fiel, rastreabilidade e reutilização.

## 6. Regra de invariância entre adapters

Os adapters podem modificar forma, ordem, densidade, explicitação e affordances de navegação, mas não devem modificar silenciosamente:

- a conclusão;
- a autoridade;
- o estado epistêmico;
- a proveniência;
- as evidências relacionadas;
- as restrições relevantes;
- o sentido das relações causais;
- o histórico de supersessão quando necessário ao contexto.

Uma projeção pode omitir detalhes apenas quando o contrato daquele consumidor permitir essa omissão.

## 7. O CCP como base e os adapters como materialização

A hipótese aplica ao próprio conhecimento a separação FlowED entre intenção/contrato e materialização:

```text
conhecimento estruturado / contrato de projeção
                     ↓
               adapter de público
                     ↓
          materialização apropriada
```

Isso permite que a mesma empreitada possua uma base única e gere, por exemplo:

- manifesto para leitura humana;
- racional expandido para pesquisador;
- norma resumida para executor;
- trilha de auditoria para consultor;
- representação estruturada para IA;
- visualização causal mínima para aprendizagem.

## 8. Relação com EDT, CCP e FlowED

Hipótese de responsabilidade:

- **FlowED**: princípio de separação, primazia cognitiva e materializações substituíveis;
- **EDT**: investigação/metodologia sobre preservação e transmissão do caminho cognitivo;
- **CCP**: estrutura/contratos da base cognitiva e das projeções;
- **adapters de projeção**: materializações orientadas a públicos ou consumidores específicos.

Essa separação deve ser validada posteriormente e não deve ser tratada como arquitetura definitiva nesta fase.

## 9. Aplicação imediata ao Manifesto FlowED

Daqui para frente, durante a revisão frase por frase, usar provisoriamente como checklist:

1. Qual domínio já conhecido estamos reconhecendo?
2. Estamos deixando claro que não reivindicamos novidade artificial?
3. Qual deslocamento de importância o FlowED realmente propõe?
4. Qual consequência causal queremos tornar visível?
5. Qual inferência curta pode ficar para o leitor completar?
6. Qual reação cognitiva esperamos observar?
7. Qual parte do racional deve ficar na superfície e qual pode ser progressiva?
8. Como a mesma base seria projetada para um humano e para uma IA sem mudar o conhecimento?

Este checklist é experimental e deverá ser confrontado com pesquisa em psicologia cognitiva, comunicação, fatores humanos, design rationale, progressive disclosure e interação humano-IA antes de virar padrão normativo.
