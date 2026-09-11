# CCP — Captura de insights da branch paralela sobre projeção e layout

**Status:** registro de convergências e hipóteses para investigação. Não normativo.

**Origem:** branch paralela de revisão do Manifesto FlowED, registrada no commit `391fbe07290a50a348630e9b29eb4e8a84432ebd`, especialmente em `docs/pt-br/evolution/CCP-PROJECTION-ADAPTERS-AND-MANIFESTO-LAYOUT-DRAFT.md`.

Este arquivo captura **somente** o que pertence ao domínio desta frente: estruturação cognitiva, layouts, projeções, adapters, público/consumidor e documentação estruturada. Ele não replica a revisão textual do manifesto.

## 1. Confirmação arquitetural trazida pela branch

A branch paralela chegou independentemente à mesma direção desta frente: o problema não é criar documentos diferentes como fontes independentes, mas manter uma **base cognitiva única** e gerar projeções adequadas a consumidores distintos.

Forma convergente:

```text
fonte / conhecimento de origem
        ↓
CCP estruturado
        ↓
adapter de projeção
        ↓
materialização orientada ao consumidor
```

Isso reforça a hipótese de que o domínio em estudo é maior que “layout de documento”. Trata-se de uma **arquitetura de projeção do conhecimento**.

## 2. Documentação estruturada, não apenas documentação normativa

A expressão “documentação normativa” é estreita demais para o domínio que está surgindo.

A projeção final pode ser:

- norma;
- POP;
- DOC;
- manifesto;
- backlog para humano;
- backlog para IA;
- treinamento;
- relatório;
- material científico;
- instrução de segurança;
- placa ou aviso;
- prompt/contrato operacional;
- visualização causal;
- artefato de auditoria.

A categoria de trabalho deve, portanto, ser tratada provisoriamente como **documentação estruturada** ou, de modo ainda mais geral, **projeção estruturada do conhecimento**.

Mesmo quando existe um consolidado, ele não precisa ser uma fonte estática. Ele pode ser uma projeção dinâmica derivada de uma base cognitiva mais rica, mantendo CCP e proveniência relacionados.

## 3. Adapters por consumidor

A branch paralela reforça que uma mesma base pode produzir projeções distintas sem criar verdades distintas.

### 3.1 Adapter humano

Pode otimizar:

- ordem de leitura;
- ritmo e cadência;
- hierarquia visual;
- progressive disclosure;
- exemplos e analogias;
- descoberta/epifania;
- visualização causal;
- profundidade adequada ao papel e à responsabilidade.

### 3.2 Adapter IA

Pode otimizar:

- semântica explícita;
- relações tipadas;
- autoridade;
- estado epistêmico;
- proveniência;
- premissas e conclusões separadas;
- alternativas rejeitadas ou superadas;
- restrições;
- causalidade declarada;
- identificadores estáveis;
- formato machine-readable quando pertinente;
- redução de inferência implícita.

O adapter IA não precisa reproduzir a retórica do adapter humano. Ambos, porém, devem derivar da mesma base cognitiva.

## 4. Regra de invariância entre projeções

A branch paralela oferece uma regra importante para esta frente:

**Adapters podem alterar forma, ordem, densidade, explicitação e navegação; não podem alterar silenciosamente o conteúdo epistemicamente relevante.**

Devem permanecer invariantes, conforme o contrato da projeção:

- significado;
- conclusão;
- autoridade;
- estado epistêmico;
- evidência;
- proveniência;
- restrições relevantes;
- relações causais;
- histórico de supersessão quando pertinente.

Omissão só pode ocorrer quando autorizada pelo contrato do consumidor.

## 5. Relação com a autonomia do leitor já discutida nesta frente

A branch fortalece a separação entre:

- **base cognitiva**;
- **contrato de projeção**;
- **adapter**;
- **consumidor**.

Isso converge com a hipótese já registrada nesta frente de que o leitor pode ter liberdade para aprofundar, mas quem publica precisa definir uma cognição mínima obrigatória quando papel, autoridade, risco ou ação esperada assim exigirem.

Assim, um adapter não serve apenas para “embelezar” ou resumir. Ele aplica um contrato que deve declarar o que pode ser omitido, o que deve permanecer visível e qual profundidade mínima é obrigatória para aquele consumidor.

## 6. Layout reflexivo como caso particular, não regra geral

A branch paralela propõe para textos reflexivos uma cadência experimental:

```text
domínio reconhecido
→ tratamento conhecido
→ deslocamento proposto
→ consequência causal / epifania
```

Para esta frente, o ponto importante não é adotar essa cadência como padrão universal, mas reconhecer que ela é um **adapter de projeção específico para um tipo de informação e uma intenção comunicativa**.

Logo:

- manifesto/reflexão pode priorizar epifania;
- POP pode priorizar sequência operacional e causalidade;
- DOC pode priorizar experiência acumulada e evolução;
- IA pode priorizar estrutura explícita e rastreabilidade;
- auditor pode priorizar proveniência e histórico;
- executor pode priorizar decisão vigente e cognição mínima obrigatória.

## 7. Consequência para o modelo bruto → marcado → estruturado → projetado

A convergência com a branch reforça a arquitetura discutida nesta frente:

```text
FONTE / LOG preservado
        ↓
MARCAÇÃO / indexação sem reescrita da origem
        ↓
CCP ESTRUTURADO
        ↓
CONTRATO DE PROJEÇÃO
        ↓
ADAPTER
        ↓
PROJEÇÃO / documentação estruturada
```

A fonte original não deve ser destruída pela normalização. A estruturação do CCP deve manter proveniência até os trechos de origem. O adapter trabalha sobre a base estruturada, não reinterpreta livremente uma fonte sem rastreabilidade.

Essa separação permite corrigir uma interpretação sem reescrever a história e permite gerar novas projeções futuras a partir da mesma base.

## 8. Hipótese de adapters especializados pelo próprio materializador

A branch converge também com a ideia de que um consumidor técnico — por exemplo, uma determinada família de LLM — pode possuir um contrato de projeção próprio.

No futuro, o fornecedor, criador ou mantenedor de um materializador poderia declarar características relevantes de consumo, permitindo um adapter especializado sem alterar o CCP.

Exemplo conceitual:

```text
CCP
 ├── adapter humano-dev
 ├── adapter auditor
 ├── adapter pesquisador
 ├── adapter LLM-A
 └── adapter LLM-B
```

Essa hipótese deve ser objeto de estudo empírico: comparar a eficiência de uma projeção genérica com projeções adaptadas ao consumidor mantendo constante a mesma base cognitiva.

## 9. Hipótese experimental para artigo/pesquisa

A branch paralela torna mais clara uma pergunta testável:

> A projeção de uma mesma base cognitiva por adapters específicos ao consumidor melhora compreensão ou execução sem alterar o conhecimento de origem?

Possíveis comparações:

- projeção genérica vs. projeção adaptada;
- humano iniciante vs. especialista;
- humano vs. IA;
- LLM A vs. LLM B;
- representação retórica vs. representação semântica explícita.

Possíveis medidas:

- acerto;
- omissões;
- tempo;
- retrabalho;
- pedidos de esclarecimento;
- desvio de intenção;
- retenção;
- consumo de tokens;
- capacidade de justificar a resposta a partir da proveniência.

## 10. Síntese provisória desta frente

A convergência entre esta frente e sua branch paralela pode ser resumida provisoriamente assim:

> **Preservamos a fonte, estruturamos o caminho, contratamos a projeção e adaptamos a materialização ao consumidor.**

Essa frase é apenas uma síntese de trabalho, não uma proposição aprovada do manifesto ou do CCP.

## 11. Regra para futuras capturas da branch paralela

Sempre que a branch paralela produzir novas ideias, esta frente deve importar apenas o que diga respeito a:

- fonte e log;
- marcação e proveniência;
- estruturação do CCP;
- contratos de projeção;
- adapters;
- layouts por tipo de informação;
- público/consumidor;
- cognição mínima obrigatória;
- progressive disclosure;
- invariância semântica entre projeções;
- documentação estruturada e materializações derivadas.

Discussões puramente editoriais sobre a redação das proposições do manifesto permanecem na branch paralela, exceto quando revelarem uma regra geral de projeção útil a este domínio.
