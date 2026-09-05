# FlowED — Plano de Controle Único e Independência por Materialização

**ID:** FLOWED-ARCH-UNIFIED-CONTROL-PLANE
**Versão:** 0.1-draft
**Status:** FUNDAMENTAL / DOGFOODING
**Domínio proprietário:** FlowED

---

## 1. Teses arquitetônicas centrais

> **FlowED propõe um plano de controle único para engenharia e gestão organizacional, preservando soberania absoluta dos domínios, compondo ferramentas heterogêneas por contratos e materializando resultados portáveis que continuam utilizáveis sem dependência operacional do próprio FlowED.**

> **FlowED busca reduzir a carga cognitiva sem eliminar a pluralidade metodológica nem centralizar a soberania dos domínios.**

Estas afirmações constituem teses arquitetônicas, industriais e acadêmicas centrais do FlowED.

Elas não significam que o FlowED implemente internamente todos os domínios. O FlowED não é um monólito funcional e não deve absorver a soberania dos componentes que coordena. Seu papel é oferecer um plano de controle comum, contratual e automatizável sobre domínios independentes.

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

O FlowED deve produzir, na ponta, artefatos nativos dos domínios e das tecnologias escolhidas, portáveis, auditáveis e utilizáveis sem o FlowED.

O FlowED não deve substituir um artefato nativo por um formato proprietário apenas para manter controle sobre o resultado.

Exemplos:

- Git permanece Git;
- um container permanece um container compatível com a tecnologia escolhida;
- Terraform/OpenTofu permanece Terraform/OpenTofu;
- manifests Kubernetes permanecem manifests Kubernetes;
- documentos, scripts, pipelines e configurações devem permanecer em formatos nativos ou abertos adequados ao domínio.

---

## 3. Lei absoluta de não aprisionamento

> **Nada materializado pelo FlowED, nem por qualquer cadeia de capacidades acionada por ele, pode exigir o FlowED para continuar existindo, sendo compreendido ou sendo operado no domínio de destino.**

O FlowED é uma ferramenta de conforto e orquestração, não uma dependência obrigatória do resultado.

Depois da materialização, o usuário deve poder remover completamente FlowED e `fled` e continuar trabalhando diretamente com os artefatos e ferramentas de destino.

A remoção do FlowED pode eliminar conveniências adicionais de automação, validação, reconciliação ou governança oferecidas pelo plano de controle, mas não pode invalidar artificialmente o resultado materializado.

### 3.1. Homologação não é aprisionamento

Se um usuário modificar diretamente um artefato nativo depois da materialização, ele continua dono e operador legítimo desse artefato.

A modificação pode tornar o estado incompatível com o contrato anteriormente homologado pelo FlowED. Nesse caso, a consequência correta é:

```text
ARTEFATO NATIVO ALTERADO
        ↓
VALIDAÇÃO PELO CONTRATO
        ↓
COMPATÍVEL?
  ├─ SIM → permanece homologado
  └─ NÃO → deixa de estar homologado para aquela automação
           mas continua válido e operável no domínio nativo
```

Portanto:

> **O FlowED pode negar homologação futura; nunca pode negar a propriedade, portabilidade ou operabilidade nativa do artefato materializado.**

---

## 4. Redução de carga cognitiva sem apagar os domínios

O FlowED busca reduzir o número de interfaces operacionais que uma pessoa precisa dominar para executar tarefas recorrentes em múltiplos domínios.

> **Reduzir a carga cognitiva sem eliminar a pluralidade metodológica nem centralizar a soberania dos domínios.**

Isso não elimina a necessidade de conhecimento conceitual dos próprios domínios.

O usuário iniciante pode operar por `fled`; o especialista pode operar diretamente sobre os mesmos artefatos nativos. Ambos devem encontrar o mesmo estado materializado, e não uma representação proprietária escondida atrás do FlowED.

Isso permite simultaneamente:

- uma linguagem operacional comum para quem deseja abstração;
- pluralidade de metodologias e tecnologias;
- transparência para estudo;
- acesso direto para especialistas;
- rastreabilidade para auditoria;
- independência para continuidade;
- possibilidade de abandonar o FlowED sem reconstruir o projeto.

---

## 5. Ponte entre aprendizagem e indústria

Uma hipótese acadêmica essencial do FlowED é reduzir o gap entre ambientes educacionais simplificados e ambientes industriais reais.

O objetivo não é ensinar uma ferramenta didática que precise ser descartada quando o aluno chega à produção. O objetivo é permitir que a mesma linguagem operacional acompanhe o usuário enquanto os mecanismos materializados evoluem para tecnologias industriais reais.

O iniciante pode receber abstração e automação. O resultado, porém, deve continuar sendo um artefato industrial nativo, que um profissional experiente reconhece e pode operar diretamente.

Portanto:

> **A abstração educacional do FlowED deve terminar em artefatos industriais reais, e não em substitutos pedagógicos incompatíveis com produção.**

Essa hipótese deve ser avaliada empiricamente; não é considerada comprovada apenas por definição arquitetônica.

---

## 6. Arquitetura de referência

```text
USUÁRIO / EMPRESA / PROJETO
            ↓
          fled
            ↓
   FLOWED CONTROL PLANE
            ↓
  CONTRACT / CAPABILITY LAYER
            ↓
        ADAPTERS
            ↓
 DOMÍNIOS / TECNOLOGIAS SOBERANAS
            ↓
      ARTEFATOS NATIVOS
```

O FlowED orquestra a composição. Cada domínio preserva sua autoridade interna e o resultado permanece no domínio de destino.

---

## 7. Inspirações explícitas e princípio de adoção

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

Essas referências não transferem soberania de domínio ao FlowED. O FlowED deve consumi-las por contratos e preservar seus artefatos, formatos, contratos e expertise nativos sempre que aplicável.

### 7.1. Regra Adopt Before Build

> **Se uma capability necessária já existir de forma madura, sustentável, contratável e compatível com a soberania de domínio e a não dependência operacional, o FlowED deve adotá-la antes de considerar implementação proprietária.**

A existência de um adapter FlowED nunca justifica duplicar uma capability já consolidada.

### 7.2. Materialização no formato nativo do domínio

```text
fled
   ↓
contrato de intenção
   ↓
adapter
   ↓
ferramenta/domínio escolhido
   ↓
artefato nativo
```

O adapter é ponte, não destino.

### 7.3. FlowED como camada acima, não como substituição

```text
iniciante
   → usa fled

especialista
   → usa diretamente a tecnologia de destino

ambos
   → trabalham sobre o mesmo artefato materializado
```

Essa propriedade diferencia orquestração de apropriação de domínio.

---

## 8. Hipóteses acadêmicas associadas

### H1 — Unified Operational Language / Cognitive Load

Uma linguagem operacional uniforme sobre múltiplos domínios pode reduzir carga cognitiva e erros de integração quando comparada à operação direta de toolchains heterogêneas, sem eliminar a pluralidade metodológica nem centralizar a soberania dos domínios.

### H2 — Education-to-Industry Continuity

Uma abstração operacional que materializa tecnologias industriais nativas pode reduzir a ruptura entre ferramentas usadas no aprendizado e ferramentas usadas em produção.

### H3 — Sovereign Domain Composition

Uma arquitetura baseada em contratos e soberania absoluta de domínio pode permitir substituição de componentes sem propagar dependências transitivas aos consumidores.

### H4 — Non-Captive Materialization / Operational Exitability

Um plano de controle que materializa artefatos nativos e autossuficientes pode permitir a remoção completa do próprio orquestrador sem perda da operabilidade fundamental do resultado.

### H5 — Progressive Determinism

A substituição progressiva de interpretação humana ou probabilística por contratos, validadores e automação determinística pode reduzir custo e variabilidade sem alterar a semântica do processo.

Estas hipóteses devem ser testadas; não devem ser apresentadas como comprovadas apenas por definição arquitetônica.

---

## 9. Critério de admissão de componentes

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
- formato nativo materializado;
- caminho operacional sem FlowED;
- condições que invalidam homologação sem invalidar o artefato nativo.

---

## 10. Relação com os demais princípios do FlowED

Esta tese deve ser interpretada em conjunto com os princípios já documentados de:

- Contract First;
- Stable Contract and Adapter Boundary;
- Critical Adoption;
- Immediate Domain Visibility;
- Deterministic-First Execution;
- Verify Before Propagate;
- adoção antes de construção proprietária.

Nenhuma dessas regras autoriza o FlowED a ultrapassar a soberania de um domínio adotado ou a tornar seus artefatos dependentes do FlowED.

---

## 11. Regra resumida

```text
ONE CONTROL PLANE
+ ABSOLUTE DOMAIN SOVEREIGNTY
+ LOWER COGNITIVE LOAD WITHOUT METHODOLOGICAL MONOCULTURE
+ CONTRACT-BASED COMPOSITION
+ ADOPT BEFORE BUILD
+ NATIVE ARTIFACT MATERIALIZATION
+ EDUCATION-TO-INDUSTRY CONTINUITY
+ ABSOLUTE NON-CAPTIVE OPERATION
+ OPERATIONAL EXITABILITY
= FLOWED ARCHITECTURAL THESIS
```

Esta formulação deve permanecer visível nas decisões arquitetônicas, no desenho do `fled`, na admissão de componentes, nos experimentos de dogfooding e na futura defesa acadêmica do FlowED.
