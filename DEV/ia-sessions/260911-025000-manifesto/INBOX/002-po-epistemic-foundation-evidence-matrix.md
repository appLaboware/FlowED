# PO-001-02 → MAN-001 — fechar substrato evidencial de `De onde partimos`

**Origem:** revisão PO das OUTBOX 004/005/006 e da POC WRK-001.
**Prioridade:** próxima ação MAN antes de consolidar `D0.*`.

## Decisão do PO

A arquitetura de explicitar um **ponto de partida epistêmico** é aprovada como **candidata forte**. Não estão aprovados ainda:

- o nome normativo `CCP de Partida` / `CCP de Fundação Epistêmica`;
- a inserção de `De onde partimos` no manifesto principal;
- `D0.1–D0.4` como BASELINE consolidada;
- qualquer claim de originalidade científica.

Não altere manifesto principal nem P2.3 neste ciclo.

## Trabalho solicitado

### 1. Matriz claim-by-claim

Construa um artefato de trabalho que parta **do texto canônico real do manifesto**, nunca de uma versão fortalecida para produzir residual.

Para cada claim relevante ao ponto de partida, registre no mínimo:

```text
claim canônico
→ fonte/caminho no manifesto
→ antecedente relevante
→ tipo de relação: equivalência | sobreposição | analogia | diferença | unresolved
→ força científica da fonte
→ relevância como prior art / divulgação pública
→ o que a fonte realmente sustenta
→ o que não sustenta
→ limite conhecido
→ como o FlowED herda/adota/repondera
→ residual/delta candidato, ou UNRESOLVED
→ confiança/cobertura
```

Não force residual quando a evidência não permitir.

### 2. Corrigir o pool de referências

Você registrou no sprint fontes efetivamente consultadas, mas `docs/research/REFERENCE-POOL.md` ainda não as incorpora.

Atualize o pool, no mesmo ciclo, com as referências que você realmente verificou e que influenciaram o parecer. Para cada uma, preserve versão/data/URL ou DOI quando disponível e preencha com rigor `SUPPORTS`, `DOES_NOT_SUPPORT`, `STATUS`, `LAST_CHECKED` e uso no FlowED.

Distingua explicitamente:

- **força científica/evidencial**;
- **relevância para anterioridade/prior art/estado da prática**.

Uma fonte fraca como evidência científica pode continuar relevante como divulgação anterior; não misture os dois eixos.

Se alguma referência mencionada no sprint não puder ser reconfirmada, registre a incerteza ou deixe-a fora até nova verificação; não normalize metadados por memória.

### 3. Reavaliar `D0.1–D0.4`

Depois da matriz, devolva ao PO uma avaliação das quatro candidatas, sem ainda consolidá-las.

Atenção especial:

- `D0.1`: a expressão "ideias já consolidadas" precisa ser compatível com a cobertura/evidência real, não um atestado genérico de consenso;
- `D0.4`: verifique se pertence de fato a `De onde partimos` ou se é uma proposição/ambição transversal melhor posicionada em outro ponto do manifesto.

Não aplique ainda todo o ciclo `EXPAND-MAX / REDUCT-MAX / DEFESA` às D0 se o substrato epistemológico ainda exigir correção.

## Relação com WRK-001

WRK-001 está em HOLD depois de concluir a primeira fatia vertical. O PO pretende, se sua matriz ficar suficientemente estruturada e rastreável, congelar um recorte dela como **segunda necessidade real** do materializador:

`claim → antecedente → evidência → limite → adoção → delta → projeção De onde partimos`

Isso deverá acontecer antes de qualquer salto para reconstrução histórica de `Como chegamos aqui`.

Portanto, produza o artefato pensando em proveniência rastreável, mas **não desenhe a implementação do worker** e não redefina CCP/EDT.

## Entrega esperada

Ao concluir:

1. atualize seu `session_resume.md`;
2. registre a matriz em caminho próprio de trabalho/evolução, sem alterar manifesto canônico;
3. atualize `docs/research/REFERENCE-POOL.md` somente com fontes realmente consultadas/verificadas;
4. publique OUTBOX ao PO com:
   - matriz produzida;
   - referências normalizadas;
   - lacunas/UNRESOLVED;
   - parecer revisado sobre D0.1–D0.4;
   - recomendação de qual recorte está maduro para um futuro input ao WRK.

Mantenha o prefixo de commit vigente de sua sessão.
