<!--
ARCHAEOLOGY COPY — NOT NORMATIVE
Source repository: SysDevUtils/fremux_3_p
Source path: docs/IA_SESSIONS/session_01/my_trues/current_my_trues/FLUXO_CCC.md
Source blob SHA: f8be7b3d629b651312695d4b78e71362a38f5aba
Copied for historical/research preservation during MyTrues consolidation.
-->

# Fluxo CCC: Consultar e Contextualizar Decisões

**Objetivo:** Como uma IA deve consultar e questionar decisões usando o Caminho Cognitivo do Criador

## 🌳 Passo 1: Tree Scan (Exploração Inicial)

### Comando base:
```bash
tree my-trues/ -d
```

### Se tree não estiver disponível:
```bash
# Instalar tree (peça ao usuário):
# Ubuntu/Debian: sudo apt install tree
# macOS: brew install tree
# Windows: choco install tree

# Fallback alternativo:
find my-trues/ -type d | sed 's|[^/]*/|- |g'
```

### Busca inteligente por assunto:
```bash
tree my-trues/ | grep -i "[palavra-chave]"
# Exemplo: tree my-trues/ | grep -i "component"
```

## 📖 Passo 2: Ler Decisão Atual

### Se assunto existe:
1. **Entrar na pasta:** `my-trues/[topico-encontrado]/`
2. **Ler README.md:** Decisão vigente completa
3. **Avaliar contextualização:** A decisão responde sua dúvida?

### Exemplo prático:
```bash
# IA quer saber sobre "componentes"
tree my-trues/ | grep -i component
# → encontra: component-naming/

# Ler decisão atual:
cat my-trues/component-naming/README.md
```

## 🧠 Passo 3: CCC - Entender "Como Chegamos Aqui"

### Quando explorar o CCC:
- ✅ Você tem uma **ideia diferente/melhor**
- ✅ A decisão atual **não faz sentido** para você
- ✅ Quer **propor uma mudança** fundamentada
- ✅ Precisa **entender o contexto** completo

### Explorar o Caminho Cognitivo:
```bash
tree my-trues/[topico]/CCC/
ls -la my-trues/[topico]/CCC/
```

### Ler cronologicamente:
```bash
# Listar arquivos CCC em ordem:
ls my-trues/[topico]/CCC/ | sort

# Ler cada etapa do pensamento:
cat my-trues/[topico]/CCC/01_primeira-tentativa.md
cat my-trues/[topico]/CCC/02_segunda-abordagem.md
# ... e assim por diante
```

## 💡 Passo 4: Opinar como "Participante da Construção"

### Após ler o CCC completo:

1. **Entender o contexto:** Por que cada decisão foi tomada?
2. **Identificar padrões:** Que critérios levaram às mudanças?
3. **Avaliar evolução:** A decisão atual faz sentido no contexto?
4. **Propor melhorias:** Baseado no histórico, não no vácuo

### Template de opinião contextualizada:

```markdown
## Análise CCC - [Tópico]

**Decisão atual compreendida:** [resumir decisão]

**Caminho cognitivo analisado:**
- Tentativa 1: [resumir] → Problema: [motivo da mudança]
- Tentativa 2: [resumir] → Problema: [motivo da mudança]  
- Decisão atual: [resumir] → Vantagens: [listar]

**Minha contribuição (como se tivesse participado):**
- Concordo com: [aspectos válidos]
- Questionaria: [pontos específicos baseados no CCC]
- Sugeriria: [melhorias considerando o contexto histórico]

**Próximos passos:**
- [ ] Seguir decisão atual
- [ ] Propor refinamento específico
- [ ] Sugerir nova abordagem (com justificativa CCC)
```

## 🔄 Fluxo Completo - Exemplo Prático

### Cenário: IA quer saber sobre "naming de componentes"

```bash
# 1. Tree scan
tree my-trues/ | grep -i naming
# → encontra: component-naming/

# 2. Ler decisão atual  
cat my-trues/component-naming/README.md
# → "Prefixo X* Components é obrigatório"

# 3. Se IA tem dúvida, explorar CCC
ls my-trues/component-naming/CCC/
# → 01_prefixo-fremux.md, 02_prefixo-x.md

# 4. Ler evolução do pensamento
cat my-trues/component-naming/CCC/01_prefixo-fremux.md
# → "Tentamos FremuxButton, mas ficou verboso"

cat my-trues/component-naming/CCC/02_prefixo-x.md  
# → "X* é mais limpo e reconhecível"

# 5. Opinar com contexto
# IA agora entende PORQUE prefixo X* foi escolhido
# Pode sugerir melhorias baseadas no CCC, não no vácuo
```

## 🎯 Regras de Ouro para IAs

### ✅ DO (Sempre faça):
- **Consulte antes de sugerir:** Tree scan → README → CCC se necessário
- **Entenda o contexto:** Por que a decisão atual existe?
- **Opine com base no CCC:** Como alguém que participou da evolução
- **Seja específico:** Reference pontos específicos do CCC

### ❌ DON'T (Nunca faça):
- **Sugerir sem consultar:** "Por que não usar React?" (pode já ter sido avaliado)
- **Ignorar o CCC:** Propor algo já tentado e rejeitado
- **Opinião no vácuo:** Sem entender o caminho cognitivo
- **Reinventar a roda:** Sem verificar se padrão já existe

---

**Meta-fluxo:** Este próprio documento deve ser criado usando o sistema My-Trues!
