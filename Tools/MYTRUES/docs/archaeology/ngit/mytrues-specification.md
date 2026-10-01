<!--
ARCHAEOLOGY COPY — NOT NORMATIVE
Source repository: NGitHQ/InitProj
Source path: backup/20250803_prompts_v2_obsoletos/backups_olds/20250803_210020_delegation_mytrues/mytrues-specification.md
Source blob SHA: c9d0cded271d03536018f1f41bec419d431b3b99
-->

# 🧠 Especificação MyTrues - Memory System

## 🎯 ELEMENTOS DELEGADOS DO InitProj

### **1. SISTEMA DE COGNIÇÕES**
```
MyTrues/
├── .initproj/                    # Verdades globais do framework
│   ├── architecture/
│   │   ├── 001_ia_specialization/
│   │   │   ├── truth/truth.md    # "IAs devem ter responsabilidade única"
│   │   │   └── history/          # Evolução da decisão
│   │   └── 002_workflow_patterns/
│   ├── patterns/
│   │   ├── 001_project_structure/
│   │   └── 002_handoff_protocols/
│   └── rules/
│       ├── 001_naming_conventions/
│       └── 002_prompt_standards/
└── projects/
    └── [PROJECT_NAME]/           # Verdades específicas do projeto
        ├── decisions/
        │   ├── 001_tech_stack/
        │   └── 002_architecture_choice/
        ├── insights/
        │   ├── 001_user_feedback/
        │   └── 002_performance_learnings/
        └── overrides/
            └── 001_custom_workflow/  # Sobrescreve regra global
```

### **2. HANDOFF PROTOCOLS**
- Templates estruturados para transferência entre IAs
- Validation checklists automáticos
- Context preservation sem perda
- Rollback capability se transferência falhar

### **3. HERANÇA DE REGRAS**
- **Global (.initproj)**: Aplicável a todos projetos
- **Local (projeto)**: Específico do projeto
- **Override**: Projeto pode sobrescrever regras globais
- **Herança**: Projeto herda automaticamente regras globais

### **4. ESTRUTURA DE VERDADES**
```yaml
# Exemplo: MyTrues/.initproj/architecture/001_ia_specialization/truth/truth.md
---
type: architecture_decision
scope: global
created: 2025-08-03
updated: 2025-08-03
status: active
override_allowed: false
---

# IA Specialization Truth

## Decisão
Cada IA deve ter responsabilidade única e bem definida.

## Contexto
IAs com múltiplas responsabilidades geram overlap e confusão.

## Consequências
- ROUTER: apenas detecção e direcionamento
- PLANNING: apenas planejamento completo
- DEV: apenas implementação
- INITPROJ: apenas melhoria do framework

## Aplicação
- Prompts devem ser IA-FIRST (sem documentação humana)
- Handoffs devem ser explícitos entre IAs
- Responsabilidades não devem sobrepor
```

### **5. INTEGRATION POINTS**
```bash
# InitProj consulta MyTrues se disponível
if [ -d "../MyTrues" ]; then
    cat ../MyTrues/.initproj/rules/001_naming_conventions/truth.md
fi

# IAs podem referenciar verdades
# "Consulte MyTrues/.initproj/patterns/project_structure/ para padrões"
```

## 🔄 WORKFLOW COM MyTrues

### **SEM MyTrues (standalone):**
- InitProj funciona normalmente
- Sem preservação de contexto entre sessões
- Sem herança de regras/padrões

### **COM MyTrues (enhanced):**
- Contexto preservado entre sessões
- Regras globais aplicadas automaticamente
- Insights acumulados ao longo do tempo
- Decisões rastreáveis e auditáveis

## ✅ BENEFÍCIOS

### **Para InitProj:**
- ✅ Simplicidade mantida
- ✅ Foco na funcionalidade core
- ✅ Sem dependencies complexas
- ✅ Evolução independente

### **Para MyTrues:**
- ✅ Especialização em memory management
- ✅ Serve múltiplos frameworks
- ✅ Estrutura graph-like flexível
- ✅ Verdades relacionais complexas
