# FlowED — Abstração Operacional e Conhecimento de Domínio

**ID:** `FLOWED-PHIL-OPERATIONAL-ABSTRACTION-DOMAIN-KNOWLEDGE`  
**Versão:** `0.1-draft`  
**Status:** `FUNDAMENTAL / DOGFOODING`  
**Domínio proprietário:** `FlowED`

---

## 1. Princípio fundamental

> **Para operar o ecossistema, o usuário pode aprender uma única linguagem operacional. Para compreender profundamente um domínio, o conhecimento daquele domínio continua integralmente válido, acessível e soberano.**

O FlowED reduz a necessidade de dominar múltiplas interfaces operacionais para executar tarefas recorrentes, mas não substitui, empobrece, redefine nem aprisiona o conhecimento dos domínios subjacentes.

A abstração existe para facilitar a operação. O domínio continua existindo por inteiro na ponta.

---

## 2. Uma linguagem operacional não significa um único domínio conceitual

O FlowED pode oferecer uma única porta operacional por meio de `fled`, API ou outra projeção equivalente do mesmo contrato.

Isso não significa que Git, Terraform, OpenTofu, Kubernetes, documentação, qualidade, testes, infraestrutura ou qualquer outro domínio deixem de possuir seus próprios conceitos, regras, artefatos, práticas e conhecimentos especializados.

```text
UMA LINGUAGEM OPERACIONAL
        ↓
MÚLTIPLOS DOMÍNIOS SOBERANOS
        ↓
ARTEFATOS NATIVOS REAIS
```

O FlowED unifica a forma de pedir, validar, orquestrar e materializar operações. Ele não tenta transformar os domínios em um único modelo conceitual proprietário.

---

## 3. Conhecimento de domínio permanece válido

O conhecimento profundo de um domínio não é invalidado pela existência da abstração FlowED.

Ao contrário, ele permanece útil em pelo menos quatro situações:

- compreensão profunda do que foi materializado;
- avaliação crítica de decisões, defaults e políticas;
- tratamento de exceções e casos não cobertos pela abstração;
- operação direta do artefato nativo quando desejado.

O usuário pode começar sem dominar o domínio e evoluir progressivamente até compreendê-lo profundamente.

```text
INICIANTE
  ↓
opera pela abstração
  ↓
observa artefatos nativos
  ↓
compreende decisões e conceitos
  ↓
especializa-se no domínio
  ↓
pode operar diretamente a tecnologia nativa
```

A abstração não deve bloquear esse caminho.

---

## 4. O domínio permanece intacto no resultado

O FlowED não deve esconder o domínio atrás de uma representação proprietária permanente.

Se o destino for Git, o resultado deve continuar sendo Git.

Se o destino for Terraform ou OpenTofu, os artefatos devem continuar sendo Terraform ou OpenTofu.

Se o destino for Kubernetes, os manifests devem permanecer Kubernetes.

Se o destino for documentação, o resultado deve permanecer um documento nativo, legível e operável fora do FlowED.

Portanto:

> **O FlowED não interfere no conhecimento do domínio porque o próprio domínio permanece intacto no produto materializado.**

---

## 5. Abstração progressiva, liberdade progressiva

O FlowED deve permitir que usuários com diferentes níveis de experiência operem sobre o mesmo processo e o mesmo resultado.

Um iniciante pode consumir defaults e guardrails maduros.

Um usuário intermediário pode compreender e substituir opções permitidas.

Um especialista pode inspecionar, discutir, alterar ou operar diretamente o domínio nativo.

```text
JÚNIOR
→ usa defaults e guardrails

PLENO
→ entende opções e especializa pontos permitidos

SÊNIOR
→ avalia criticamente decisões e pode operar o domínio diretamente
```

Nenhum desses níveis deve exigir a criação de um produto final conceitualmente diferente.

---

## 6. Princípio de transparência para aprendizagem

> **ABSTRAÇÃO PARA USO + TRANSPARÊNCIA PARA APRENDIZAGEM.**

A facilidade operacional não pode ser obtida ao custo de tornar o conhecimento real inacessível.

O FlowED deve, sempre que tecnicamente adequado:

- permitir inspeção dos artefatos nativos produzidos;
- preservar provenance suficiente para explicar como o resultado foi obtido;
- permitir rastrear defaults, regras, contratos e decisões aplicadas;
- não exigir conhecimento de formatos proprietários para compreender o produto final;
- permitir que o usuário abandone progressivamente a abstração conforme aumenta seu domínio técnico.

---

## 7. Não é simplificação do domínio

O FlowED não simplifica o domínio de destino no sentido de produzir uma versão inferior, pedagógica ou descartável.

Ele simplifica a operação sobre decisões que já puderam ser consolidadas com segurança.

```text
SIMPLIFICAR A OPERAÇÃO
≠
SIMPLIFICAR O RESULTADO
```

A meta é que o usuário possa executar menos decisões instrumentais sem reduzir a qualidade, a transparência ou a legitimidade industrial do artefato produzido.

---

## 8. Regra filosófica resumida

> **Aprender FlowED pode ser suficiente para operar o ecossistema. Aprender profundamente um domínio continua sendo o caminho para compreendê-lo, criticá-lo e operá-lo diretamente.**

Em forma ainda mais curta:

> **Uma linguagem para operar. Todos os domínios permanecem para aprender.**

E, como consequência:

> **O FlowED abstrai a operação; nunca apaga o conhecimento do domínio.**
