<!--
ARCHAEOLOGY COPY — NOT NORMATIVE
Source: Google Drive
Drive file id: 13CZAME99MCF8R412SjxgMqw7Gjy4scJb
Source URL: https://drive.google.com/file/d/13CZAME99MCF8R412SjxgMqw7Gjy4scJb/view?usp=drivesdk
Original title: true_structure.md
Reason preserved: 2025-06 MyTrues TRUE structure / neural knowledge model
-->

# 🧠 Sistema MyTrues: Rede Neural de Conhecimento

Este documento explica a estrutura, organização e funcionamento do sistema MyTrues, que implementa uma rede neural de conhecimento baseada em verdades validadas (TRUEs).

## 📋 Visão Geral

O sistema MyTrues é uma implementação prática da filosofia EDT (Education-Driven Think), criando uma base de conhecimento que:

1. **Preserva o contexto cognitivo** que levou a cada decisão ou verdade
2. **Organiza conhecimento em rede neural** com conexões verticais e horizontais
3. **Evolui organicamente** através de refinamentos e novas descobertas
4. **Mantém rastreabilidade** até a origem de cada conceito

## 🧩 Anatomia de uma TRUE

Uma TRUE (Traced Reliable Unified Essence) é a unidade fundamental de conhecimento no sistema:

```
TRUE
├── Identificador Único
├── Essência (conceito fundamental imutável)
├── Contexto (domínio de aplicação)
├── Manifestação (implementação atual)
├── Caminho Cognitivo do Criador (CCC)
├── Sinapses (conexões com outras TRUEs)
└── Metadados (tipo, domínios, confiabilidade, etc.)
```

### Exemplo de TRUE

```markdown
# TOOL-DEV-001 - Gerenciamento de Versões com ASDF

## Essência
Gerenciamento consistente de múltiplas versões de runtimes e ferramentas de desenvolvimento.

## Contexto
Desenvolvimento de software que requer múltiplas versões de linguagens e ferramentas.

## Manifestação
```json
{
  "currentImplementation": {
    "tool": "asdf",
    "version": "0.11.2",
    "installCommand": "asdf plugin add <nome-do-plugin>",
    "deprecatedCommands": ["asdf plugin-add <nome-do-plugin>"],
    "lastValidated": "2025-06-10",
    "omgDiaryOrigin": "8f7e6d5c-4b3a-2a1d-9e8f-7c6b5a4d3e2f"
  }
}
```

## Caminho Cognitivo do Criador (CCC)
1. **Problema Inicial**: Necessidade de gerenciar múltiplas versões de ferramentas
2. **Alternativas Consideradas**: nvm (específico para Node.js), pyenv (específico para Python)
3. **Critérios de Decisão**: Solução unificada, suporte a múltiplas linguagens, comunidade ativa
4. **Decisão**: ASDF como ferramenta de gestão de versões
5. **Evolução**: Migração do comando `plugin-add` para `plugin add` na versão 0.8.0 [OMGDiary: 8f7e6d5c]

## Metadados
- **Tipo**: Concrete
- **Domínios**: [desenvolvimento, tooling, ambiente]
- **Criado**: 2025-06-10
- **Última Validação**: 2025-06-10
- **Confiabilidade**: Alta
```

## 🔄 Tipos de TRUEs

O sistema MyTrues organiza o conhecimento em diferentes tipos de TRUEs:

### 1. TRUEs Abstratas (Conceituais)
- Princípios fundamentais e filosóficos
- Raramente mudam
- Base para outras TRUEs
- Exemplo: `ARCH-PRIN-001 - Princípio de Encapsulamento Matrioska`

### 2. TRUEs Concretas (Implementações)
- Implementações específicas de princípios abstratos
- Podem evoluir com o tempo
- Exemplo: `TOOL-DEV-001 - Gerenciamento de Versões com ASDF`

### 3. TRUEs Especializadas (Contextuais)
- Adaptações de TRUEs concretas para contextos específicos
- Herdam e sobrescrevem aspectos de TRUEs concretas
- Exemplo: `TOOL-DEV-001-FREMUX - Configuração ASDF para Fremux`

### 4. TRUEs Experienciais (Aprendizados)
- Baseadas em experiências práticas
- Documentam lições aprendidas
- Exemplo: `EXP-DEV-003 - Resolução de Problemas de Hidratação SSR/CSR`

## 🌐 Estrutura Neural

O sistema MyTrues organiza o conhecimento em uma rede neural com diferentes tipos de conexões:

### 1. Sinapses Verticais (Herança)
- **Relação**: Especialização/Generalização
- **Direção**: De conceitos abstratos para implementações concretas
- **Exemplo**: `ARCH-PRIN-001` (Princípio Matrioska) → `ARCH-IMPL-003` (Implementação em Nuxt)

### 2. Sinapses Horizontais (Variantes)
- **Relação**: Alternativas/Complementos
- **Direção**: Entre conceitos do mesmo nível de abstração
- **Exemplo**: `TOOL-DEV-001` (ASDF) ↔ `TOOL-DEV-002` (NVM) como alternativas

### 3. Sinapses Contextuais (Aplicações)
- **Relação**: Adaptação para contextos específicos
- **Direção**: De implementação genérica para uso específico
- **Exemplo**: `TOOL-DEV-001` (ASDF genérico) → `TOOL-DEV-001-FREMUX` (ASDF para Fremux)

### 4. Sinapses Cognitivas (Origem)
- **Relação**: Ligação com origem cognitiva
- **Direção**: De TRUE para entrada no OMGDiary
- **Exemplo**: `TOOL-DEV-001` → `OMGDiary:8f7e6d5c-4b3a-2a1d-9e8f-7c6b5a4d3e2f`

## 📂 Organização do Sistema

O sistema MyTrues é organizado em uma estrutura que facilita a navegação e evolução:

```
/private/docs/MY_TRUES/
├── _neural/                       # Sistema neural de TRUEs
│   ├── nodes/                     # Nós de conhecimento (TRUEs)
│   │   ├── abstract/              # TRUEs abstratas (conceituais)
│   │   ├── concrete/              # TRUEs concretas (implementações)
│   │   └── specialized/           # TRUEs especializadas (contextuais)
│   ├── synapses/                  # Conexões entre TRUEs
│   │   ├── vertical.json          # Relações de herança
│   │   ├── horizontal.json        # Relações de variantes
│   │   └── contextual.json        # Aplicações contextuais
│   └── contexts/                  # Contextos de aplicação
│       ├── {{project}}/           # Variáveis de projeto (substituíveis)
│       └── _variables.json        # Definição de variáveis de contexto
├── _omgdiary/                     # Registros cronológicos de cognições
│   ├── YYYY-MM/                   # Organizados por ano-mês
│   └── _index.json                # Índice temporal e emocional
├── _ccc/                          # Caminhos Cognitivos do Criador
│   ├── paths/                     # Caminhos específicos
│   └── insights/                  # OMGs (epifanias) registrados
└── domains/                       # Organização por domínios
    ├── development/               # TRUEs de desenvolvimento
    ├── architecture/              # TRUEs de arquitetura
    └── operations/                # TRUEs de operações
```

## 🌱 Ciclo de Vida de uma TRUE

### 1. Nascimento
- Originada de uma ou mais entradas no OMGDiary
- Criada pelo EDT-Agent ou proposta por humano/IA
- Recebe identificador único e classificação

### 2. Validação
- Verificação de consistência com TRUEs existentes
- Confirmação de utilidade e aplicabilidade
- Aprovação pelo Humano Orchestrator

### 3. Integração
- Estabelecimento de sinapses com outras TRUEs
- Indexação em domínios relevantes
- Disponibilização para consulta e uso

### 4. Evolução
- Refinamento baseado em novas experiências
- Especialização para contextos específicos
- Possível elevação para TRUE mais abstrata (OMG-Insight)

### 5. Obsolescência (raro)
- Marcação como histórica/obsoleta
- Manutenção para referência e aprendizado
- Substituição por TRUE mais atual

## 🔍 Como Consultar TRUEs

O sistema MyTrues oferece múltiplas formas de acesso ao conhecimento:

### 1. Navegação Taxonômica
- Por tipo (abstrata, concreta, especializada)
- Por domínio (desenvolvimento, arquitetura, etc.)
- Por projeto/contexto

### 2. Busca Semântica
- Por conceitos relacionados
- Por palavras-chave
- Por problemas ou necessidades

### 3. Exploração Neural
- Seguindo sinapses a partir de uma TRUE conhecida
- Explorando o Caminho Cognitivo do Criador
- Navegando de abstrações para implementações

### 4. Consulta Contextual
- Baseada no contexto atual de trabalho
- Filtrada por relevância para a tarefa
- Adaptada ao nível de especialização necessário

## 💡 Contribuindo para o Sistema MyTrues

### Para Humanos

1. **Identificar Oportunidade**
   - Reconhecer um insight valioso
   - Detectar um padrão recorrente
   - Encontrar uma solução para problema comum

2. **Registrar no OMGDiary**
   - Documentar o contexto e a cognição
   - Incluir estado emocional e gatilhos
   - Atribuir um "OMG Factor" (0-10)

3. **Propor TRUE**
   - Formatar seguindo o template padrão
   - Estabelecer conexões com TRUEs existentes
   - Submeter para revisão

### Para IAs

1. **Detectar Padrão**
   - Identificar conhecimento recorrente
   - Reconhecer inconsistências ou gaps
   - Observar soluções eficazes

2. **Validar contra TRUEs Existentes**
   - Verificar se já existe TRUE relacionada
   - Identificar possíveis conflitos
   - Determinar nível de novidade

3. **Sugerir Registro ou Atualização**
   - Propor entrada no OMGDiary
   - Sugerir nova TRUE ou refinamento
   - Fornecer justificativa e evidências

## 🧪 Implementação Técnica

O sistema MyTrues é implementado usando:

### 1. Armazenamento
- Arquivos Markdown para conteúdo legível por humanos
- JSON para metadados e sinapses
- Banco vetorial para busca semântica

### 2. Indexação
- Embeddings para representação semântica
- Grafos para representação de sinapses
- Taxonomia para classificação hierárquica

### 3. Acesso
- API REST para consultas programáticas
- Interface de busca para humanos
- Integração direta com agentes IA

## 📊 Métricas de Saúde do Sistema

O sistema MyTrues monitora sua própria saúde através de:

1. **Cobertura**: Percentual de domínios com TRUEs validadas
2. **Coesão**: Densidade e qualidade das sinapses
3. **Atualidade**: Tempo desde última validação das TRUEs
4. **Utilização**: Frequência de consulta e aplicação
5. **Evolução**: Taxa de refinamento e criação de novas TRUEs

## 🔮 Visão Futura

O sistema MyTrues continuará evoluindo para:

1. **Autoorganização**: TRUEs que se reorganizam baseadas em padrões de uso
2. **Inferência Proativa**: Sugestão de TRUEs relevantes antes mesmo da consulta
3. **Detecção de Contradições**: Identificação automática de inconsistências
4. **Síntese de Conhecimento**: Geração de novas TRUEs a partir de padrões emergentes
5. **Adaptação Dinâmica**: Especialização automática para novos contextos

---

*Este documento evolui continuamente conforme nosso entendimento do sistema MyTrues se aprofunda. Última atualização: 2025-06-14*
