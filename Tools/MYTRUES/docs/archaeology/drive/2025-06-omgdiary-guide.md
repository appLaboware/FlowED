<!--
ARCHAEOLOGY COPY — NOT NORMATIVE
Source: Google Drive
Drive file id: 1i5SacdxRVZY_vi9p5Y3ekTu-eY0bAn9K
Source URL: https://drive.google.com/file/d/1i5SacdxRVZY_vi9p5Y3ekTu-eY0bAn9K/view?usp=drivesdk
Original title: omgdiary_guide.md
Reason preserved: 2025-06 OMGDiary cognitive capture guide
-->

# 📔 OMGDiary: Guia de Captura Cognitiva

Este documento explica o conceito, estrutura e processo do OMGDiary como ferramenta fundamental de captura cognitiva no ecossistema EDT-TICA.

## 🌟 O que é o OMGDiary?

O OMGDiary (Oh My God Diary) é um sistema de registro cronológico e emocional de cognições, insights e decisões que ocorrem durante o desenvolvimento de um projeto. Seu nome faz referência ao momento "Eureka!" ou "Oh My God!" quando uma pessoa tem um insight significativo.

### Princípios Fundamentais

1. **Captura Emocional**: Registra não apenas o que foi decidido, mas como o criador se sentiu
2. **Cronologia Preservada**: Mantém a sequência temporal de descobertas e decisões
3. **Contexto Completo**: Documenta o ambiente, problemas e gatilhos que levaram à cognição
4. **Rastreabilidade**: Cada entrada recebe um UUID para referência permanente
5. **Honestidade Cognitiva**: Valoriza o registro do processo mental, incluindo erros e confusões

## 📝 Anatomia de uma Entrada OMGDiary

Cada entrada no OMGDiary segue uma estrutura consistente:

```markdown
# OMGDiary: [UUID]

## Metadata
- **Data**: YYYY-MM-DD
- **Autor**: [Nome/Agente]
- **Contexto**: [Projeto/Situação]
- **Estado Emocional**: [Frustração/Eureka/Dúvida/etc]

## Cognição
[Descrição detalhada da cognição, decisão ou insight]

## Gatilhos
- [Evento ou problema que desencadeou esta cognição]
- [Limitação ou desafio enfrentado]

## Referências
- **TRUEs Relacionadas**: [Lista de TRUEs existentes consultadas]
- **Documentos**: [Links para documentos relevantes]
- **Experiências Anteriores**: [UUIDs de OMGDiaries relacionados]

## Resultado
- **Decisão Tomada**: [Descrição da decisão]
- **Impacto Esperado**: [O que se espera desta decisão]
- **TRUE Gerada/Modificada**: [TRUE-ID ou "Nenhuma"]

## OMG Factor (0-10)
[Nível de epifania/insight - 0: decisão rotineira, 10: completa mudança de paradigma]
```

### Exemplo Real

```markdown
# OMGDiary: 8f7e6d5c-4b3a-2a1d-9e8f-7c6b5a4d3e2f

## Metadata
- **Data**: 2025-06-10
- **Autor**: Desenvolvedor X
- **Contexto**: Configuração de ambiente para Fremux
- **Estado Emocional**: Frustração → Alívio

## Cognição
Tentei usar o comando `asdf plugin-add nodejs` conforme documentação antiga que encontrei, mas recebi erro. Após pesquisa, descobri que o comando correto agora é `asdf plugin add nodejs`. A sintaxe mudou na versão 0.8.0 do ASDF, removendo o hífen.

## Gatilhos
- Erro ao executar comando conforme documentação desatualizada
- Inconsistência entre diferentes fontes de documentação

## Referências
- **TRUEs Relacionadas**: [TOOL-ENV-002] Configuração de Ambiente de Desenvolvimento
- **Documentos**: https://asdf-vm.com/guide/getting-started.html
- **Experiências Anteriores**: 1a2b3c4d-5e6f-7g8h-9i0j-1k2l3m4n5o6p

## Resultado
- **Decisão Tomada**: Atualizar nossa documentação e práticas para usar `asdf plugin add` em vez de `asdf plugin-add`
- **Impacto Esperado**: Evitar erros de configuração para novos desenvolvedores
- **TRUE Gerada/Modificada**: TOOL-DEV-001

## OMG Factor (0-10)
3 - Insight moderado que corrige um problema recorrente
```

## 🔄 O Ciclo EDT e o OMGDiary

O OMGDiary é a primeira etapa do ciclo EDT (Education-Driven Think), servindo como registro primário de experiências cognitivas:

```
┌─────────────────┐
│                 │
│  Experiência    │
│                 │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│                 │
│    Registro     │ ◄── OMGDiary
│                 │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│                 │
│    Reflexão     │ ◄── Análise de padrões
│                 │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│                 │
│  Consolidação   │ ◄── MyTrues
│                 │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│                 │
│    Aplicação    │
│                 │
└─────────────────┘
```

## 📊 Classificação de Entradas por OMG Factor

O "OMG Factor" é uma métrica subjetiva que indica o nível de impacto ou importância de uma cognição:

| Nível | Descrição | Exemplo |
|-------|-----------|---------|
| **0-2** | Rotineiro | Correção de um bug simples |
| **3-4** | Insight Útil | Descoberta de um padrão de solução |
| **5-6** | Significativo | Nova abordagem para um problema recorrente |
| **7-8** | Transformador | Mudança fundamental em uma implementação |
| **9-10** | Revolucionário | Completa mudança de paradigma ou abordagem |

Entradas com OMG Factor alto (7+) frequentemente geram novas TRUEs abstratas ou provocam revisões significativas em TRUEs existentes.

## 🧠 Caminho Cognitivo do Criador (CCC)

O conjunto de entradas OMGDiary relacionadas a um tema ou decisão forma o Caminho Cognitivo do Criador (CCC), que documenta a jornada completa desde o problema inicial até a solução final.

### Exemplo de CCC para Escolha de Ferramenta

```
OMGDiary:1a2b3c -> Identificação da necessidade de gerenciar versões
     │
     ▼
OMGDiary:4d5e6f -> Comparação entre alternativas (nvm, pyenv, asdf)
     │
     ▼
OMGDiary:7g8h9i -> Decisão inicial de usar asdf
     │
     ▼
OMGDiary:0j1k2l -> Problema com documentação desatualizada
     │
     ▼
OMGDiary:8f7e6d -> Descoberta da sintaxe correta
```

Este CCC completo é então condensado na TRUE resultante, preservando os marcos principais da jornada cognitiva.

## 📝 Práticas de Registro Eficaz

### Para Humanos

1. **Registre em Tempo Real**
   - Capture cognições enquanto estão frescas
   - Não espere para "limpar" ou "organizar" o pensamento
   - Preserve a emoção e o contexto do momento

2. **Seja Honesto e Detalhado**
   - Inclua erros, confusões e becos sem saída
   - Documente o que você estava pensando, não apenas o resultado
   - Registre seu estado emocional (frustração, empolgação, etc.)

3. **Estabeleça Conexões**
   - Referencie TRUEs consultadas
   - Vincule a entradas anteriores relacionadas
   - Identifique documentos ou recursos externos relevantes

4. **Avalie o Impacto**
   - Atribua um OMG Factor honesto
   - Considere as implicações da cognição
   - Identifique potenciais TRUEs a serem criadas ou modificadas

### Para IAs

1. **Observe Padrões Cognitivos**
   - Identifique momentos de insight durante interações
   - Reconheça quando uma solução representa um padrão reutilizável
   - Detecte inconsistências entre prática e documentação

2. **Sugira Registro**
   - Proponha entradas OMGDiary quando apropriado
   - Forneça estrutura para a cognição observada
   - Sugira conexões com conhecimento existente

3. **Ajude na Reflexão**
   - Faça perguntas que estimulem aprofundamento
   - Sugira implicações não óbvias
   - Ajude a avaliar o OMG Factor adequado

## 🛠️ Ferramentas e Integração

### EDT-Agent

O EDT-Agent é um componente especializado que:

1. **Facilita o registro** de entradas OMGDiary
2. **Analisa padrões** entre múltiplas entradas
3. **Sugere conexões** com conhecimento existente
4. **Propõe TRUEs** baseadas em cognições significativas

### Integração com MyTrues

O OMGDiary alimenta o sistema MyTrues através de:

1. **Extração de Essência**: Identificação do conceito fundamental
2. **Mapeamento de CCC**: Documentação da jornada cognitiva
3. **Estabelecimento de Sinapses**: Conexão com conhecimento relacionado
4. **Validação de Confiabilidade**: Avaliação da robustez da cognição

## 🌱 Começando com OMGDiary

### Primeiros Passos

1. **Crie sua primeira entrada**
   - Escolha uma decisão ou insight recente
   - Siga o template fornecido
   - Seja detalhado e honesto

2. **Revise periodicamente**
   - Releia entradas antigas
   - Identifique padrões emergentes
   - Conecte cognições relacionadas

3. **Compartilhe quando apropriado**
   - Use UUIDs para referenciar entradas específicas
   - Discuta cognições com colegas para enriquecimento
   - Contribua para o conhecimento coletivo

### Dicas para Registro Eficaz

- **Use linguagem natural e pessoal** - O OMGDiary não é documentação formal
- **Inclua exemplos concretos** - Código, comandos, resultados
- **Registre o "por quê"** - Não apenas o "o quê" e o "como"
- **Documente alternativas consideradas** - Mesmo as rejeitadas
- **Capture momentos de confusão** - São valiosos para aprendizado futuro

## 📈 Evolução do OMGDiary

O sistema OMGDiary evolui continuamente:

### Fase Atual
- Registro manual em arquivos markdown
- Organização cronológica
- Indexação básica por metadados

### Próximos Passos
- Ferramenta dedicada para captura em tempo real
- Análise semântica automatizada
- Visualização de CCCs e conexões
- Sugestão proativa de TRUEs potenciais

### Visão Futura
- Captura cognitiva contínua e passiva
- Detecção automática de padrões emergentes
- Integração com fluxos de trabalho de desenvolvimento
- Síntese assistida por IA de novas TRUEs

## 🤝 OMGDiary na Colaboração Humano-IA

O OMGDiary serve como ponte entre cognição humana e processamento de IA:

1. **Humanos capturam** experiências ricas em contexto e emoção
2. **IAs analisam** padrões e conexões em escala
3. **Humanos validam** insights e priorizam conhecimento
4. **IAs aplicam** conhecimento validado em novos contextos

Esta simbiose cria um ciclo virtuoso onde:
- Experiência humana alimenta modelos de IA
- Análise de IA amplia capacidade humana
- Validação humana refina modelos de IA
- Aplicação de IA libera criatividade humana

---

*Este documento evolui continuamente conforme nossa compreensão e prática do OMGDiary se aprofunda. Última atualização: 2025-06-14*
