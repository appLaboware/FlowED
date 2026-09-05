# FlowED — Plano de Controle Único e Independência por Materialização

**ID:** FLOWED-ARCH-UNIFIED-CONTROL-PLANE
**Versão:** 0.1-draft
**Status:** FUNDAMENTAL / DOGFOODING
**Domínio proprietário:** FlowED

---

## 1. Tese arquitetônica central

> **FlowED propõe um plano de controle único para engenharia e gestão organizacional, preservando soberania absoluta dos domínios, compondo ferramentas heterogêneas por contratos e materializando resultados portáveis que continuam utilizáveis sem dependência operacional do próprio FlowED.**

Esta afirmação é uma tese arquitetônica, industrial e acadêmica central do FlowED.

Ela não significa que o FlowED implemente internamente todos os domínios. O FlowED não é um monólito funcional e não deve absorver a soberania dos componentes que coordena. Seu papel é oferecer um plano de controle comum, contratual e automatizável sobre domínios independentes.

---

## 2. Consequências obrigatórias

A tese acima implica simultaneamente as seguintes propriedades.

### 2.1. Plano de controle único

Toda capability operacional oficialmente exposta pelo ecossistema FlowED deve possuir acesso pelo CLI `fled` ou por uma interface programática equivalente que preserve o mesmo contrato.

O `fled` é uma porta pública de orquestração. Ele não deve concentrar lógica de negócio pertencente aos bounded contexts dos componentes.

### 2.2. Soberania absoluta de domínio

A soberania de domínio é uma lei absoluta do FlowED.

Cada domínio:

- é responsável por seus próprios conceitos, invariantes, contratos e regras;
- publica explicitamente as capabilities que oferece;
- não pode ter sua implementação interna atravessada por consumidores externos;
- só pode ser consumido por meio de seu contrato público;
- pode trocar sua implementação interna sem obrigar consumidores a conhecer a mudança, desde que preserve seu contrato.

Um domínio consumidor deve enxergar apenas a dependência imediata que contratou.

### 2.3. Composição por contratos

O FlowED compõe capabilities, não implementações.

A integração de um componente ao ecossistema deve ser declarativa e estruturada o suficiente para permitir, no mínimo:

- identificação da capability;
- contrato de entrada;
- contrato de saída;
- validação;
- erros possíveis;
- efeitos esperados;
- pontos de especialização;
- defaults;
- propriedades bloqueáveis;
- evidências requeridas;
- dependências públicas.

Wizard, CLI interativo, web, GitHub App, IDE, prompt e agente são projeções desses contratos, nunca sua fonte de verdade.

### 2.4. Materialização independente

O FlowED deve privilegiar a produção de artefatos nativos, portáveis, auditáveis e utilizáveis fora dele.

Quando tecnicamente possível, um resultado produzido pelo FlowED deve continuar compreensível e operacional mesmo que o FlowED deixe de estar presente após a materialização.

Exemplos de artefatos esperados:

- repositórios Git;
- Markdown;
- YAML;
- JSON;
- scripts;
- configurações;
- pipelines;
- estruturas de diretórios;
- documentos;
- contratos;
- evidências;
- arquivos de regras.

O FlowED deve evitar criar dependência operacional desnecessária de runtime proprietário para manter funcionando algo que já poderia existir como artefato nativo.

---

## 3. Princípio de exitabilidade operacional

A materialização independente estabelece uma propriedade adicional:

> **Um sistema gerenciado pelo FlowED deve permanecer compreensível e, sempre que tecnicamente possível, operacional após a remoção do próprio FlowED.**

Essa propriedade será tratada como **Operational Exitability**.

A exitabilidade não exige que toda conveniência de orquestração continue disponível sem o FlowED. Ela exige que os artefatos, decisões, configurações e mecanismos materializados não sejam artificialmente aprisionados ao plano de controle.

O FlowED pode agregar valor continuamente sem possuir o resultado final.

---

## 4. Redução de carga cognitiva sem apagar os domínios

O FlowED busca reduzir o número de interfaces operacionais que uma pessoa precisa dominar para executar tarefas recorrentes em múltiplos domínios.

Isso não elimina a necessidade de conhecimento conceitual dos próprios domínios.

Portanto:

> **FlowED reduz carga operacional sem substituir conhecimento de domínio.**

O usuário pode executar uma intenção por meio de `fled`, mas os artefatos materializados devem permanecer transparentes e estudáveis nos termos dos domínios originais.

Isso permite simultaneamente:

- abstração para uso;
- transparência para estudo;
- rastreabilidade para auditoria;
- independência para continuidade.

---

## 5. Arquitetura de referência

```text
USUÁRIO / EMPRESA / PROJETO
            ↓
          fled
            ↓
   FLOWED CONTROL PLANE
            ↓
  CONTRACT / CAPABILITY LAYER
            ↓
 ┌──────────┼───────────┬───────────┐
 ↓          ↓           ↓           ↓
InitProj  ISO29110    Dec-B       outros
   ↓                                  
 internos soberanos e substituíveis
```

O FlowED orquestra a composição. Cada domínio preserva sua autoridade interna.

---

## 6. Hipóteses acadêmicas associadas

Esta arquitetura permite investigar formalmente, entre outras, as seguintes hipóteses.

### H1 — Unified Operational Language

Uma linguagem operacional uniforme sobre múltiplos domínios pode reduzir carga cognitiva e erros de integração quando comparada à operação direta de toolchains heterogêneas.

### H2 — Sovereign Domain Composition

Uma arquitetura baseada em contratos e soberania absoluta de domínio pode permitir substituição de componentes sem propagar dependências transitivas aos consumidores.

### H3 — Materialization Independence

Um plano de controle que materializa artefatos nativos e autossuficientes pode reduzir dependência operacional da própria plataforma e preservar continuidade após sua remoção.

### H4 — Progressive Determinism

A substituição progressiva de interpretação humana ou probabilística por contratos, validadores e automação determinística pode reduzir custo e variabilidade sem alterar a semântica do processo.

Estas hipóteses devem ser testadas; não devem ser apresentadas como comprovadas apenas por definição arquitetônica.

---

## 7. Critério de admissão de componentes

Nenhum componente deve ser tratado como integrante maduro do ecossistema FlowED sem declarar, em nível compatível com sua maturidade:

- boundary de domínio;
- capability catalog;
- contratos de entrada e saída;
- error contract;
- side-effect contract;
- specialization points;
- dependency contracts;
- interface automatizável;
- critérios de teste;
- formato de evidência;
- comportamento de materialização e exitabilidade quando aplicável.

---

## 8. Relação com os demais princípios do FlowED

Esta tese deve ser interpretada em conjunto com os princípios já documentados de:

- Contract First;
- Stable Contract and Adapter Boundary;
- Critical Adoption;
- Immediate Domain Visibility;
- Deterministic-First Execution;
- Verify Before Propagate;
- adoção antes de construção proprietária.

Nenhuma dessas regras autoriza o FlowED a ultrapassar a soberania de um domínio adotado.

---

## 9. Regra resumida

```text
ONE CONTROL PLANE
+ ABSOLUTE DOMAIN SOVEREIGNTY
+ CONTRACT-BASED COMPOSITION
+ PORTABLE MATERIALIZATION
+ OPERATIONAL EXITABILITY
= FLOWED ARCHITECTURAL THESIS
```

Esta formulação deve permanecer visível nas decisões arquitetônicas, no desenho do `fled`, na admissão de componentes, nos experimentos de dogfooding e na futura defesa acadêmica do FlowED.
