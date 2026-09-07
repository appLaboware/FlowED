# Run 003 — Ingestão do protótipo estrangeiro do InitProj PR #2

Status: `DOGFOOD / FOREIGN PROTOTYPE / NON-AUTHORITATIVE`
Date: 2026-09-07
Source: `InitProjHQ/InitProj` PR #2, branch `docs/project-discovery-dogfood`

## 1. Purpose

Avaliar o material criado prematuramente dentro do InitProj sem promover sua localização, autoridade ou arquitetura.

O objetivo é separar:

```text
CONTEÚDO APROVEITÁVEL
        ≠
LOCALIZAÇÃO / SOBERANIA CORRETA
        ≠
DECISÃO DE IMPLEMENTAR
```

O PR permanece evidência estrangeira. Nenhum conteúdo abaixo adquire autoridade apenas porque já foi materializado.

## 2. O que o protótipo trouxe

O PR introduziu uma tool `tools/project-discovery/` contendo:

- README de missão e fronteira;
- system prompt para analista de discovery;
- semente PMFN;
- evidence model;
- pre-consultancy model;
- pipeline;
- market landscape inicial;
- self-dogfood.

Também registrou a tool como integrante do catálogo do InitProj.

## 3. Erro processual observado

O conteúdo foi materializado antes de estarem estabelecidos:

- soberania de domínio;
- protocolo de discovery;
- decisão de sourcing;
- residual justificável;
- autorização de materialização.

Logo, a ocorrência fornece evidência direta para a necessidade de um `PRE-MATERIALIZATION AUTHORIZATION GATE`.

## 4. Conteúdo aproveitável como hipótese

### A. Neutralidade

A formulação `Not a verdict. A position.` é compatível com a direção atual e deve permanecer como hipótese de UX/protocolo.

### B. PMFN

São úteis como hipóteses:

```text
ΔD(split)
F* = argmin Complexity(F)
subject to DecisionSufficiency(F) = true
```

Ainda não são métricas validadas.

### C. Modelo de evidência

É aproveitável a exigência de separar:

- claim;
- fact / inference / hypothesis;
- source;
- search scope;
- coverage;
- confidence;
- counterevidence;
- assumptions;
- open questions.

### D. Não colapsar tudo em um score

É compatível com o perfil multidimensional atual.

### E. COMPOSE como possível dimensão transversal

O protótipo reconhece que `COMPOSE` talvez não pertença a uma escada ordinal única. Isso deve ser testado no protocolo.

### F. Dogfood real

É correta a regra de que o primeiro caso da tool seja ela própria e de que um resultado de redução de escopo, composição, adoção ou abandono seja sucesso metodológico.

## 5. Conteúdo que NÃO deve ser adotado automaticamente

- o nome `project-discovery` como identidade definitiva;
- a localização dentro de InitProj;
- a promoção a tool do InitProj;
- o pipeline com nomes de produtos ainda não validados como dependências obrigatórias;
- `MNI` como terminologia final;
- a escada linear `ADOPT → CONFIGURE → EXTEND → ADAPT → COMPOSE → INVENT`;
- qualquer score antes de instrumento e calibração;
- qualquer claim de inovação ou exclusividade.

## 6. Reclassificação sob soberania atual

```text
InitProj PR #2
    ↓
FOREIGN PROTOTYPE
    ↓
CANDIDATE FINDINGS
    ↓
Project Genesis live dogfood
    ↓
ADOPT | MODIFY | REJECT por átomo
```

## 7. Regras de protocolo descobertas

### PR-001 — Foreign artifacts are evidence, never authority by arrival

Um artefato produzido fora do fluxo pode ser ingerido, mas sua existência não lhe concede autoridade arquitetural.

### PR-002 — Content/location separation

Toda ingestão deve julgar separadamente:

1. valor do conteúdo;
2. domínio proprietário correto;
3. estágio de maturidade;
4. autorização de implementação.

### PR-003 — Premature implementation must be reversible

Artefatos produzidos antes do gate devem permanecer em branch/PR experimental ou outra quarentena reversível até reconciliação.

### PR-004 — No sunk-cost privilege

Horas ou linhas já produzidas não aumentam o direito de uma capability existir.

## 8. Resultado desta ingestão

O protótipo contribui materialmente com hipóteses de protocolo e exemplos, mas não altera a autoridade atual:

```text
SOVEREIGN DEVELOPMENT:
appLaboware/FlowED/tools/project-genesis/

FOREIGN EXPERIMENT:
InitProjHQ/InitProj PR #2
```

## 9. Dual output

### Use evidence

O acidente mostra que a própria ideia precisa de um gate anterior à materialização.

### Implementation evidence

Project Genesis precisa suportar ingestão de artefato externo com provenance e estado `NON-AUTHORITATIVE`, permitindo adoção parcial sem importar autoridade ou topologia.