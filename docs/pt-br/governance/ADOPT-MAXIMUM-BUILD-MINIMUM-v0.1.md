# FlowED — Adopt Maximum, Build Minimum

- ID: `FLOWED-ADOPT-MAX-BUILD-MIN`
- Version: `0.1-draft`
- Status: `FUNDAMENTAL / DOGFOODING`
- Owner domain: `FlowED`

## 1. Princípio fundamental

> **ADOTAR O MÁXIMO. FATORAR O MÍNIMO. SUBSTITUIR SEM HESITAR QUANDO JÁ EXISTIR ALGO MELHOR.**

O FlowED não existe para provar capacidade de implementação própria. Ele existe para tornar a produção de software mais eficiente, determinística, rastreável, integrável e não aprisionante.

Portanto, toda capacidade necessária deve ser tratada primeiro como problema de descoberta e adoção, e apenas depois como problema de construção.

## 2. Regra operacional

Antes de construir qualquer mecanismo novo, o FlowED MUST:

1. identificar claramente a capability necessária;
2. pesquisar soluções, padrões, frameworks, bibliotecas, protocolos e produtos existentes;
3. comparar cobertura, maturidade, sustentabilidade, licenciamento, contratos, extensibilidade, soberania de domínio e exitabilidade;
4. preferir adoção direta quando uma solução adequada já existir;
5. preferir adaptação ou composição quando duas ou mais soluções existentes cobrirem conjuntamente a necessidade;
6. construir apenas o residual comprovadamente não atendido;
7. limitar esse residual ao mínimo necessário para integrar, traduzir, validar, compor ou orquestrar capacidades existentes.

## 3. Regra de prioridade

```text
ADOPT
  ↓
COMPOSE
  ↓
ADAPT
  ↓
BUILD MINIMUM RESIDUAL
```

Construção proprietária é a última alternativa, não a primeira.

## 4. Inspirações obrigatórias de estudo

Quando aplicável, o FlowED deve estudar e reutilizar os padrões consolidados abaixo antes de criar equivalentes próprios:

```text
provider / plugin architecture
    → Terraform / OpenTofu

declarative reconciliation
    → Kubernetes

software templates / catalog / self-service
    → Backstage

SDLC control plane
    → GitLab

enterprise workflow / GRC
    → ServiceNow
```

Esses nomes não são limites exclusivos. Eles representam referências mínimas obrigatórias de prior art para os respectivos problemas.

## 5. Residual legítimo do FlowED

O FlowED pode construir quando, e somente quando, existir um residual real após adoção e composição.

Esse residual tende a concentrar-se em:

- contratos entre domínios;
- adapters;
- tradução entre intenção e contratos de ferramentas adotadas;
- composição de capabilities;
- validação;
- evidência;
- resolução de especializações e overlays;
- integração no `fled`;
- mecanismos necessários para preservar soberania e não aprisionamento.

O FlowED não deve reconstruir capacidades maduras apenas para obter identidade própria, uniformidade estética ou controle interno.

## 6. Substituição é sucesso

Se uma solução externa passar a cobrir melhor uma capability anteriormente implementada pelo FlowED, a resposta preferida é substituição, não defesa do código existente.

```text
EXISTE SOLUÇÃO SUPERIOR?
   ├─ SIM → ADOTAR / SUBSTITUIR / MIGRAR
   └─ NÃO → MANTER O RESIDUAL MÍNIMO
```

> **Código removido porque uma solução melhor foi adotada é sucesso arquitetônico, não perda de investimento.**

## 7. Relação com soberania de domínio

Adotar uma ferramenta não autoriza o FlowED a atravessar seu domínio interno.

O FlowED deve consumir a capability pelo contrato público adequado e materializar o resultado de modo compatível com a tecnologia soberana adotada.

A adoção deve reduzir trabalho próprio sem aumentar aprisionamento.

## 8. Gate obrigatório antes de BUILD

Nenhuma implementação proprietária relevante deve ser aprovada sem evidência mínima de que:

```text
DISCOVERY_EXECUTED = YES
PRIOR_ART_REVIEWED = YES
ADOPTION_CANDIDATES_COMPARED = YES
COMPOSITION_ATTEMPTED = YES|NOT_APPLICABLE
RESIDUAL_GAP_IDENTIFIED = YES
BUILD_SCOPE = MINIMUM_RESIDUAL
EXITABILITY_PRESERVED = YES
DOMAIN_SOVEREIGNTY_PRESERVED = YES
```

Se qualquer campo obrigatório for `NO` ou `UNKNOWN`, a decisão padrão é:

```text
DO NOT BUILD YET
```

## 9. Regra final

> **FlowED deve possuir o mínimo código próprio necessário para oferecer o máximo valor por composição de capacidades já comprovadas.**

```text
MAXIMUM ADOPTION
+ MAXIMUM COMPOSITION
+ MINIMUM RESIDUAL CODE
+ EASY REPLACEMENT
= FLOWED DEFAULT ENGINEERING STRATEGY
```
