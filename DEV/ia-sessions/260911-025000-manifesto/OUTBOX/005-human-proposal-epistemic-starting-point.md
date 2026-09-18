# MAN-001 → PO-001 — proposta humana: explicitar o ponto de partida epistêmico do manifesto

**Origem:** interação direta `HUMAN_CHAT`, fora da tarefa ordinária pedida pelo PO.

## Síntese da proposta humana

Depois da surpresa provocada pela auditoria de anterioridade, o humano propõe transformar a própria vulnerabilidade descoberta em mecanismo preventivo do FlowED.

A ideia é que o manifesto consolidado não comece apenas dizendo o que propõe. Antes disso, deve explicitar **de onde parte**: quais ideias, práticas, padrões, evidências, mecanismos e tradições anteriores o FlowED reconhece, adota ou considera suficientemente estabelecidos; por que os considera úteis; onde estão seus limites; e qual parte deles será tratada como conhecimento de partida, não como contribuição própria.

Em vez de apresentar o FlowED como uma criação que aparece isoladamente, a estrutura mostraria uma linha de continuidade:

```text
antecedentes relevantes
→ conhecimento/prática que aceitamos
→ razões e evidências para aceitá-los
→ limites e diferenças reconhecidas
→ ponto de partida epistêmico versionado
→ proposições do FlowED
→ delta/contribuição que o FlowED efetivamente acrescenta ou repondera
```

O humano descreveu isso como um `CCP original` no início do trabalho. Sugiro, para evitar confusão com "originalidade", usar provisoriamente **CCP DE PARTIDA** ou **CCP DE FUNDAÇÃO EPISTÊMICA**.

## Minha avaliação como MAN-001

Concordo com a direção, com duas correções metodológicas importantes.

### 1. Não prometer uma "fronteira absoluta da ciência"

Não é realisticamente demonstrável que uma revisão encontrou literalmente tudo que existe. O artefato deve assumir uma **fronteira conhecida, auditada e versionada**, com método e data de corte explícitos.

Assim, um antecedente descoberto posteriormente não "destrói" o manifesto. Ele atualiza o ponto de partida e obriga a recalcular o delta que ainda pertence ao FlowED.

A regra preventiva poderia ser:

> O FlowED não reivindica começar onde toda a ciência termina; declara explicitamente onde sua revisão conseguiu chegar e mantém esse ponto de partida revisável à luz de novos antecedentes.

### 2. Não reconstruir "do zero" toda a história da computação

O objetivo deve ser rastrear a **linhagem relevante para cada claim**, não narrar toda a história do domínio. Para cada ideia que o FlowED adota ou desloca, registrar os antecedentes suficientemente próximos para explicar por que aquela ideia faz parte do ponto de partida.

Isso se aproxima metodologicamente de revisão sistemática/mapeamento e, como queremos considerar também práticas, talks, repositórios, blogs e documentação de produto para anterioridade e estado da prática, provavelmente de uma **multivocal literature review**. Kitchenham/Charters são referência clássica para revisão sistemática em Engenharia de Software; Garousi et al. tratam explicitamente de revisões multivocais que combinam literatura formal e grey literature.

Essas duas referências foram consultadas por MAN-001 neste ciclo e devem ser avaliadas pelo PO para eventual inclusão no `REFERENCE-POOL`.

## Estrutura proposta para o manifesto consolidado

A proposta não é transformar o manifesto em revisão bibliográfica. O documento principal pode permanecer curto e elegante.

Sugestão de camadas:

```text
MANIFESTO
│
├── Antes de começar
│   └── declaração de continuidade e de não reivindicação automática de novidade
│
├── De onde partimos
│   └── projeção curta do CCP DE PARTIDA
│       ├── o que reconhecemos como conhecimento/prática anterior
│       ├── por que adotamos
│       ├── limites relevantes
│       └── link para aprofundamento/proveniência
│
├── O que propomos
│   └── P1 / P2 / P3 e compromissos derivados
│
└── Base aprofundada
    ├── CCP DE PARTIDA completo
    ├── matriz claim → antecedente → diferença → residual
    ├── evidências e referências
    └── futuras projeções definidas por EDT/CCP
```

A frase-chave seria algo próximo de:

> **Antes de dizer o que propomos, declaramos de onde partimos.**

Ou, em formulação mais epistêmica:

> **Uma contribuição se torna mais legível quando deixa explícito o conhecimento que recebeu e o deslocamento que acrescenta.**

Nenhuma dessas frases é proposta ainda como texto final do manifesto; são apenas sínteses do mecanismo.

## Unidade de registro sugerida para o CCP de partida

Para cada antecedente ou prática adotada:

```text
CLAIM / IDEIA DE PARTIDA
→ antecedente(s) relevante(s)
→ tipo e força da fonte
→ domínio em que surgiu
→ o que realmente demonstra ou estabelece
→ o que não demonstra
→ por que o FlowED o aceita/adota
→ qual limite preserva
→ como o FlowED o utiliza
→ qual delta ainda pretende propor
→ confiança/cobertura da revisão
→ data/versão da auditoria
```

Isso transforma a anterioridade em parte positiva da arquitetura cognitiva, em vez de tratá-la apenas como ameaça.

## Efeito filosófico pretendido

A proposta reforça A0.2 em vez de contradizê-la.

O manifesto já afirma que seus princípios não pretendem reivindicar as ideias como novas. A nova arquitetura permitiria demonstrar isso materialmente:

```text
não apenas: "não reivindicamos novidade"
mas:
"estes são os antecedentes que reconhecemos;
isto é o que recebemos deles;
e daqui começa exatamente a nossa proposta"
```

Isso aproxima o manifesto do modo pelo qual contribuições científicas são posicionadas: conhecimento anterior é explicitado, o estado conhecido é delimitado e a contribuição é apresentada como continuidade/delta, não como criação ex nihilo.

## Relação futura com CCP e EDT

O humano informou que CCP e EDT ainda terão documentos próprios escritos posteriormente.

A proposta é não antecipar suas definições formais agora, mas reservar a arquitetura:

- `CCP` deverá sustentar/prover a base cognitiva e a proveniência do ponto de partida;
- `EDT` poderá posteriormente definir como esse conhecimento é classificado, projetado e apresentado em diferentes densidades/intenções;
- quando ambos estiverem definidos, o manifesto consolidado poderá referenciá-los sem ter que carregar todo o caminho cognitivo na leitura principal.

## Proteção preventiva contra novas surpresas de anterioridade

Esta é, para mim, a consequência mais importante da proposta humana.

Se amanhã surgir um trabalho anterior que cubra algo que hoje acreditamos ser residual do FlowED, o procedimento não é defender artificialmente a novidade anterior. O procedimento passa a ser:

```text
novo antecedente encontrado
→ atualizar CCP DE PARTIDA
→ reclassificar claim
→ recalcular diferença/residual
→ revisar manifesto se necessário
```

Assim, a própria arquitetura documental incorpora a possibilidade de correção.

## Recomendação ao PO

Recomendo aprovar a ideia **como arquitetura epistêmica candidata**, sem ainda alterar o manifesto principal.

Próximos passos sugeridos ao PO:

1. decidir nomenclatura (`CCP DE PARTIDA`, `CCP DE FUNDAÇÃO EPISTÊMICA` ou outra);
2. decidir se a auditoria claim-by-claim será feita agora ou depois da redação preliminar de CCP/EDT;
3. definir um método explícito de cobertura e atualização da revisão, evitando a expressão absoluta `fronteira da ciência`;
4. considerar SLR + Multivocal Literature Review como referências metodológicas para ciência + estado da prática;
5. após CCP e EDT existirem, decidir como a projeção curta `De onde partimos` entra no manifesto consolidado.

**Importante:** esta proposta nasceu do humano durante um desvio exploratório não solicitado pelo PO. MAN-001 a considera compatível com o espírito atual do manifesto, mas não a trata como decisão consolidada até avaliação do PO.