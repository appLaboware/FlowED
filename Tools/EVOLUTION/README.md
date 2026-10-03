# Tool Evolution Program

Este diretório governa como o FlowED/IDEOS/MyTrues adota, valida, personaliza e,
somente quando necessário, inventa tecnologia.

Lei canônica:

**ADOPT → PERSONALIZE → FORK → INSPIRE → INVENT**

O objetivo não é maximizar código próprio. É chegar ao **estado da arte conhecido**
de cada domínio, reproduzi-lo experimentalmente, documentar seus limites e só então
criar a menor lacuna ainda não resolvida.

## Documentos canônicos

- `PROTOCOL.md` — protocolo de evolução e gates de evidência.
- `INVENTORY.md` — inventário atual, estágio e dívida de exploração.
- `ROADMAP.md` — sequência de pesquisas e experimentos.
- `DOSSIERS/` — dossiês técnicos por domínio.

## Regra de classificação

Conhecimento público não vira propriedade intelectual apenas porque o projeto o usa.

- padrão aberto existente -> **OPEN / ADOPT**;
- algoritmo científico conhecido -> **OPEN / ADOPT**;
- implementação de referência -> **OPEN / ADOPT**;
- integração específica do projeto -> preferencialmente **OPEN / PERSONALIZE**;
- dado, segredo ou memória de um fornecedor -> **PRIVATE DATA**, não necessariamente IP;
- melhoria original nossa, não trivial, medida contra baseline público -> candidata a **CORE**.

Nenhum item entra em `core/` sem passar pelo Science Frontier Gate de `PROTOCOL.md`.
