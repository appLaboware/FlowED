# Tool Placement and Promotion-Ready Root

- ID: `FLOWED-TOOL-PLACEMENT-PROMOTION-READY-ROOT`
- Version: `0.1-draft`
- Status: `BLUEPRINT / DOGFOODING`
- Owner domain: `FlowED`

## 1. Regra

Toda nova tool ou subtool deve nascer exatamente no diretório que poderá, no futuro, tornar-se seu próprio repositório ou subrepositório sem exigir mudança de identidade, contrato ou caminho público.

```text
A TOOL NASCE ONDE PODERÁ MORAR SOZINHA.
```

Se nunca for promovida, permanece como tool interna no mesmo caminho.

Se for promovida, o diretório é substituído por um boundary de repositório/subrepositório preservando a posição arquitetural.

## 2. Consequências

Cada tool candidata deve ser autocontida no próprio root e possuir, no mínimo:

- identidade e propósito;
- contrato de entrada;
- contrato de saída;
- autoridade/boundary;
- prompts/templates próprios quando aplicável;
- evidências e critérios de conclusão;
- dependências declaradas por contrato, nunca por conhecimento implícito do diretório pai.

Dependências entre tools irmãs devem passar por contratos explícitos. Uma subtool não deve depender de arquivos privados de uma irmã por caminho relativo.

## 3. Estrutura

```text
tools/
└── <tool>/                 # root potencialmente promovível
    ├── README.md
    ├── tool.yaml
    └── tools/              # subtools, cada uma também promovível
        └── <subtool>/
            ├── README.md
            └── tool.yaml
```

A existência de `tools/` dentro de uma tool não obriga promoção futura. Ela apenas preserva essa possibilidade sem refatoração estrutural.

## 4. Promoção

Uma tool interna pode ser promovida somente por decisão explícita de governança, quando houver benefício em soberania, versionamento, ownership, distribuição ou evolução independente.

Promoção não altera o contrato funcional por si só.

```text
INTERNAL DIRECTORY
      ↓
PROMOTION DECISION
      ↓
SAME PATH / SAME CONTRACT
      ↓
SUBREPOSITORY OR INDEPENDENT REPOSITORY BOUNDARY
```

## 5. Não proliferação

Este padrão não autoriza criar repositórios antecipadamente.

```text
SEPARATE PHYSICALLY ONLY WHEN JUSTIFIED.
SEPARATE LOGICALLY FROM BIRTH.
```

O estado preferido inicial é uma tool logicamente soberana e fisicamente interna, até que evidência justifique sua promoção.
