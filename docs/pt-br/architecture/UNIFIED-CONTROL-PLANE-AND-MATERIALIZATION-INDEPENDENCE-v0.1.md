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

## 6. Inspirações explícitas e princípio de adoção

O FlowED não deve reinventar mecanismos consolidados apenas para torná-los internos ao seu ecossistema. Deve estudar, adotar e compor capacidades existentes sempre que elas satisfizerem o contrato requerido.

As seguintes referências são inspirações arquitetônicas explícitas:

```text
Terraform / OpenTofu
   → Core + providers

Kubernetes
   → API declarativa + controllers/operators

Backstage
   → portal/plataforma + plugins/templates

GitLab
   → control plane integrado de SDLC

ServiceNow
   → control plane corporativo e workflows
```

O FlowED deve buscar utilizar, por adapters e contratos, tudo que essas referências ou soluções equivalentes já ofereçam de forma madura e adequada ao domínio, em vez de reimplementar a mesma capability.

Isto significa:

- Terraform/OpenTofu inspiram e podem fornecer capacidades de infraestrutura e o padrão de providers;
- Kubernetes inspira APIs declarativas, reconciliação e extensibilidade por controllers/operators;
- Backstage inspira catálogos, templates, descoberta e self-service orientado por contratos;
- GitLab inspira um plano de controle integrado para o ciclo de desenvolvimento;
- ServiceNow inspira workflows empresariais, gestão de processos e governança organizacional.

Essas referências não transferem soberania de domínio ao FlowED. O FlowED deve consumi-las através de adapters e preservar seus artefatos, formatos, contratos e expertise nativos sempre que possível.

### 6.1. Regra Adopt Before Build

> **Se uma capability necessária já existir de forma madura, sustentável, contratável e compatível com a soberania de domínio e a exitabilidade operacional, o FlowED deve adotá-la antes de considerar implementação proprietária.**

A existência de um adapter FlowED nunca justifica duplicar uma capability já consolidada.

### 6.2. Materialização no formato nativo do domínio

O FlowED não deve substituir o artefato final de um domínio por um artefato proprietário apenas para manter controle sobre ele.

Exemplos desejados:

```text
fled infra ...
   → pode materializar Terraform/OpenTofu/Pulumi/etc. nativo

fled repo ...
   → materializa Git e políticas compatíveis com o provider adotado

fled project ...
   → materializa arquivos, contratos, repositórios e estruturas nativas
```

O usuário experiente deve poder abandonar `fled` e continuar operando diretamente sobre o artefato nativo. O usuário que preferir o plano de controle pode continuar usando `fled` sobre o mesmo resultado por meio do adapter correspondente.

### 6.3. FlowED como camada acima, não como substituição

A abstração oferecida pelo FlowED deve reduzir carga operacional para iniciantes sem apagar ou sequestrar os domínios subjacentes.

```text
iniciante
   → aprende fled
   → opera múltiplos domínios por uma linguagem comum

especialista
   → inspeciona e opera diretamente Terraform/Git/Kubernetes/etc.

ambos
   → trabalham sobre os mesmos artefatos materiais
```

Essa propriedade diferencia orquestração de substituição de domínio.

---

## 7. Hipóteses acadêmicas associadas

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

## 8. Critério de admissão de componentes

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

## 9. Relação com os demais princípios do FlowED

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

## 10. Regra resumida

```text
ONE CONTROL PLANE
+ ABSOLUTE DOMAIN SOVEREIGNTY
+ CONTRACT-BASED COMPOSITION
+ ADOPT BEFORE BUILD
+ NATIVE ARTIFACT MATERIALIZATION
+ PORTABLE MATERIALIZATION
+ OPERATIONAL EXITABILITY
= FLOWED ARCHITECTURAL THESIS
```

Esta formulação deve permanecer visível nas decisões arquitetônicas, no desenho do `fled`, na admissão de componentes, nos experimentos de dogfooding e na futura defesa acadêmica do FlowED.
