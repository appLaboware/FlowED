# 02 — PMFN e candidato FlowDisP

## PMFN entra, mas também precisa ser testado

O PMFN é altamente relevante porque sua hipótese de fatorar somente até a granularidade necessária para uma decisão parece adequada ao problema de descobrir a fronteira do existente sem cair nem em subfatoração nem em decomposição trivial infinita.

Porém ele não pode entrar como lei presumidamente original. Deve ocupar dois papéis simultâneos:

1. **método candidato** para decidir até onde decompor;
2. **objeto do próprio discovery**.

Pergunta atômica inicial candidata:

> Já existe, em literatura científica, padrões ou práticas formais de engenharia de software, um princípio explícito segundo o qual uma proposta é decomposta somente até a menor granularidade necessária para permitir uma decisão estável entre adoção, configuração, adaptação, composição ou invenção residual?

O resultado pode indicar adoção, personalização, composição, extensão, derivação ou residual distintivo. “Não encontramos” não equivale automaticamente a “inventamos”.

## Candidato a produto/protocolo

```text
FlowED Discovery Protocol
short name: FlowDisP
futura família CLI/execução candidata: FLDP
estado: DISCOVERY / UNVALIDATED
```

Abstração candidata:

```text
OBJECT
→ DISCOVERY INTENT
→ NECESSARY FACTORIZATION
→ ANALYSIS LENS
→ EVIDENCE
→ FRONTIER
→ RESIDUAL
→ DISPOSITION
→ DECISION PACKAGE
```

FlowDisP não deve ser apenas acadêmico. O primeiro perfil/lente a validar será `ACADEMIC`, porque o problema atual é epistemológico: antecedente mais próximo, estado da arte/prior art, claim sustentado, limites, herança, composição, transformação, residual, confiança e linguagem permitida.

Futuramente podem existir lentes tecnológicas, arquiteturais, de produto, comerciais, OSS/upstream, licensing, security, operational e regulatory. Essas lentes são apenas hipóteses agora; não devem ser implementadas ou canonizadas antes de casos reais.

## Resultado multidimensional

FlowDisP não deveria reduzir o objeto a uma única nota de “relevância”. Uma proposta pode ser academicamente herdada e ao mesmo tempo tecnologicamente útil, comercialmente diferenciada ou arquiteturalmente distintiva.

Exemplo meramente ilustrativo:

```yaml
academic:
  inherited: high
  residual_novelty: unresolved
  confidence: medium
technological:
  upstream_coverage: high
  disposition: compose_plus_residual
commercial:
  differentiation: unresolved
architectural:
  standalone_boundary: strong
```

## Relação candidata com protocolos existentes

O TFP e outras práticas LaboWare já contêm a direção de pesquisar upstreams, classificar capabilities, medir residual e preferir adoção/configuração/adaptação/composição antes de construir.

FlowDisP pode vir a ser a abstração geral que esses protocolos consomem, mas isso ainda precisa ser provado:

```text
FlowED
├── FlowDisP
│   └── FLDP (futuro, se justificado)
├── Tool Formation Protocol
│   └── possível consumidor de lenses do FlowDisP
├── projetos FlowED
│   └── possível discovery antes de decisões importantes
└── pesquisa acadêmica
    └── primeira lens a validar
```

Nada nesta estrutura está aprovado como arquitetura final.
