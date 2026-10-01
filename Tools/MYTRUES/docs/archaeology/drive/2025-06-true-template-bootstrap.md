<!--
ARCHAEOLOGY COPY — NOT NORMATIVE
Source: Google Drive
Drive file id: 18K79MItOnUdZspeOoCdr75wMB2v1uiJD
Source URL: https://drive.google.com/file/d/18K79MItOnUdZspeOoCdr75wMB2v1uiJD/view?usp=drivesdk
Original title: true_template_bootstrap.md
Reason preserved: 2025-06 TRUE bootstrap template
-->

# TRUE Template e Demonstração Bootstrap

Este documento demonstra a criação de TRUEs usando o exemplo do ASDF, aplicando os conceitos EDT na prática.

## Estrutura Base de uma TRUE

```markdown
# TRUE-{DOMINIO}-{SEQ} - {Título da TRUE}

## Essência (Imutável)
[Conceito fundamental que não muda independente da implementação]

## Contexto de Aplicação
- **Domínio**: [Área de conhecimento]
- **Escopo**: [Abrangência da aplicação]
- **Variáveis**: [Contextos substituíveis como {{projeto}}]

## Manifestação Atual
[Como esta TRUE se manifesta na prática hoje]

## Sinapses (Conexões Neurais)
- **Verticais (Herança)**: 
  - Pai: [TRUE mais abstrata que esta herda]
  - Filhos: [TRUEs mais específicas derivadas desta]
- **Horizontais (Variantes)**: [Alternativas no mesmo nível]
- **Contextuais**: [Aplicações específicas em contextos]

## Caminho Cognitivo do Criador (CCC)
[Referência ao(s) OMGDiary(s) que originaram esta TRUE]

## Metadados
- **Tipo**: [Abstrata|Concreta|Especializada|Experiencial]
- **Confiabilidade**: [Alta|Média|Baixa]
- **Última Validação**: [Data]
- **Versão**: [Número da versão]
```

## Exemplo Prático: Hierarquia ASDF

### TRUE Abstrata (Pai)
```markdown
# TRUE-TOOL-001 - Gestão de Ambientes de Desenvolvimento

## Essência
Necessidade de gerenciar múltiplas versões de linguagens e ferramentas de desenvolvimento de forma consistente e isolada.

## Contexto de Aplicação
- **Domínio**: Desenvolvimento de Software
- **Escopo**: Gestão de Ambiente
- **Variáveis**: {{linguagem}}, {{ferramenta}}, {{equipe}}

## Manifestação Atual
Uso de ferramentas de versionamento que permitem:
- Isolamento de versões por projeto
- Troca rápida entre versões
- Configuração declarativa via arquivos
- Suporte a múltiplas linguagens

## Sinapses
- **Verticais**: 
  - Pai: TRUE-ARCH-002 (Princípios de Isolamento)
  - Filhos: TRUE-TOOL-002 (ASDF Específico)
- **Horizontais**: 
  - TRUE-TOOL-003 (Docker para Isolamento)
  - TRUE-TOOL-004 (Máquinas Virtuais)

## CCC
OMGDiary: 1a2b3c4d-development-environment-chaos-2024

## Metadados
- **Tipo**: Abstrata
- **Confiabilidade**: Alta
- **Versão**: 1.0.0
```

### TRUE Concreta (Implementação)
```markdown
# TRUE-TOOL-002 - ASDF como Gestor de Versões

## Essência
ASDF como solução unificada para gestão de múltiplas linguagens e ferramentas.

## Contexto de Aplicação
- **Domínio**: Desenvolvimento de Software
- **Escopo**: Implementação de Gestão de Ambiente
- **Variáveis**: {{projeto}}, {{linguagem_primaria}}

## Manifestação Atual
```json
{
  "tool": "asdf",
  "version": "0.11.2+",
  "instalacao": {
    "comando_correto": "asdf plugin add <nome>",
    "comando_obsoleto": "asdf plugin-add <nome>",
    "mudanca_versao": "0.8.0"
  },
  "configuracao": {
    "arquivo_global": "~/.tool-versions",
    "arquivo_projeto": ".tool-versions"
  }
}
```

## Sinapses
- **Verticais**:
  - Pai: TRUE-TOOL-001 (Gestão de Ambientes)
  - Filhos: TRUE-TOOL-002-{{projeto}} (Especializações)
- **Horizontais**:
  - TRUE-TOOL-005 (NVM para Node)
  - TRUE-TOOL-006 (Pyenv para Python)

## CCC
OMGDiary: 8f7e6d5c-asdf-command-syntax-discovery-2025

## Metadados
- **Tipo**: Concreta
- **Confiabilidade**: Alta
- **Versão**: 2.1.0
```

### TRUE Especializada (Contexto Específico)
```markdown
# TRUE-TOOL-002-FREMUX - ASDF no Projeto Fremux

## Essência
Aplicação específica do ASDF para as necessidades do projeto Fremux.

## Contexto de Aplicação
- **Domínio**: Fremux Development
- **Escopo**: Configuração específica do projeto
- **Variáveis**: {substituídas por valores concretos}

## Manifestação Atual
```json
{
  "projeto": "fremux",
  "linguagens_requeridas": ["nodejs", "python"],
  "ferramentas_adicionais": ["pnpm"],
  "configuracao_especifica": {
    "nodejs": "20.10.0",
    "python": "3.11.5",
    "pnpm": "8.10.0"
  },
  "arquivo_tool_versions": "já criado no projeto"
}
```

## Sinapses
- **Verticais**:
  - Pai: TRUE-TOOL-002 (ASDF Genérico)
  - Filhos: Nenhum (especialização final)
- **Contextuais**:
  - TRUE-FREMUX-ENV-001 (Ambiente Fremux)
  - TRUE-FREMUX-DEPS-001 (Dependências Fremux)

## CCC
OMGDiary: 7f8e9d0a-fremux-environment-setup-2025

## Metadados
- **Tipo**: Especializada
- **Confiabilidade**: Alta
- **Versão**: 1.0.0
- **Contexto**: fremux
```

## Estrutura Neural Demonstrada

```
TRUE-ARCH-002 (Isolamento)
    ↓ (sinapse vertical)
TRUE-TOOL-001 (Gestão de Ambientes)
    ↓ (sinapse vertical)
TRUE-TOOL-002 (ASDF) ↔ (sinapses horizontais) → TRUE-TOOL-005 (NVM)
    ↓ (sinapse contextual)                        TRUE-TOOL-006 (Pyenv)
TRUE-TOOL-002-FREMUX (ASDF no Fremux)
```

## Como Usar Este Sistema

### 1. Identificar Necessidade
Quando surge uma decisão ou insight, pergunte:
- Já existe uma TRUE para isso?
- Preciso criar uma nova ou especializar uma existente?

### 2. Criar/Especializar TRUE
```bash
# Para nova TRUE
cp template_true.md TRUE-{DOMINIO}-{SEQ}-{nome}.md

# Para especialização
cp TRUE-{DOMINIO}-{SEQ}.md TRUE-{DOMINIO}-{SEQ}-{{contexto}}.md
```

### 3. Estabelecer Sinapses
- Identificar TRUE pai (herança)
- Identificar alternativas (horizontais)
- Criar especializações quando necessário

### 4. Registrar CCC
- Vincular com OMGDiary que originou a decisão
- Documentar processo de pensamento

## Próximos Passos para Implementação

1. **Criar estrutura de diretórios** para as TRUEs
2. **Implementar sistema de variáveis** {{projeto}}
3. **Desenvolver ferramentas** para navegação neural
4. **Automatizar criação** de especializações
5. **Implementar busca semântica** por sinapses

---

*Este documento demonstra o bootstrap cognitivo em ação: usando conceitos EDT para criar o próprio sistema EDT*
