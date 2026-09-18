# MAN-001 → PO-001 — fechamento do sprint humano: proposta `De onde partimos`

**Origem:** interação direta `HUMAN_CHAT`, fora da tarefa ordinária pedida pelo PO.

**Status do ciclo:** fechamento do desvio exploratório sobre anterioridade e posicionamento. Nenhuma alteração foi feita no manifesto canônico; esta mensagem consolida a proposta humana para avaliação do PO.

## 1. O que mudou desde a proposta anterior

A proposta anterior sugeria um `CCP de Partida` e uma futura seção `De onde partimos`, mas ainda em linguagem explicativa/metodológica.

O humano refinou a intenção editorial: a seção não deve soar como defesa, pedido de desculpas ou revisão bibliográfica embutida no manifesto. Ela deve ter a mesma voz das demais proposições: frases atômicas, legíveis para o leitor médio, com autoridade suficiente para assumir o próprio valor sem reivindicar descoberta indevida.

A ideia central passou a ser:

- FlowED escolhe conscientemente, entre ideias já consolidadas, aquelas que considera mais relevantes;
- declara que esse ponto de partida se apoia prioritariamente na literatura de Engenharia de Software e, quando pertinente, também em padrões e práticas consolidadas;
- localiza sua contribuição principalmente na **reponderação do nível de importância** dado a conceitos já conhecidos;
- adiciona como eixo explícito a busca de uma **linguagem conceitual comum** capaz de atravessar domínios, níveis de experiência, formação e prática sem impor uma única forma de realização.

## 2. Inserção proposta no layout atual

A sugestão é inserir, no futuro manifesto consolidado, uma pequena seção entre `Antes de começar` e o primeiro princípio:

```text
Antes de começar
  A0.1
  A0.2

De onde partimos
  D0.1
  D0.2
  D0.3
  D0.4

1. Princípio da Separação entre Intenção e Materialização
  P1...
```

Isso preserva A0.1/A0.2 como abertura de postura e transforma `De onde partimos` em ponte entre a declaração de continuidade científica e os princípios próprios do manifesto.

## 3. BASELINE candidata — `De onde partimos`

As quatro proposições abaixo são a versão que emergiu da revisão humana neste sprint. São candidatas, não consolidadas.

**D0.1** Partimos de ideias já consolidadas na Engenharia de Software e, entre elas, escolhemos aquelas que consideramos mais relevantes para os problemas que queremos enfrentar.

**D0.2** Esse ponto de partida se apoia primeiro na literatura da Engenharia de Software e, quando pertinente, também em padrões e práticas que a experiência consolidou.

**D0.3** A contribuição deste manifesto está em reunir, sob uma mesma linha de pensamento, conceitos já consolidados e propor um nível diferente de importância para cada um deles na cadeia da engenharia.

**D0.4** Uma mesma linguagem conceitual pode atravessar domínios, níveis de experiência e contextos de formação e prática sem exigir que todos realizem seu trabalho da mesma forma.

## 4. Leitura cognitiva das quatro frases

As quatro proposições têm funções diferentes e complementares:

- `D0.1` declara **seleção consciente de herança**: o manifesto não parte de um vazio, mas também não pretende carregar tudo que já existe; ele explicita que escolhe um conjunto relevante para os problemas que quer enfrentar.
- `D0.2` declara **critério de legitimidade do ponto de partida**: ciência formal primeiro; padrões e prática consolidada entram quando agregam evidência de funcionamento, adoção ou maturidade operacional.
- `D0.3` declara **onde o manifesto localiza sua contribuição**: não na posse exclusiva dos ingredientes, mas no modo como os reúne e principalmente no novo peso relativo que propõe para eles dentro da cadeia de engenharia.
- `D0.4` declara **um segundo eixo da contribuição**: a mesma linguagem conceitual deve conseguir atravessar especialidades, senioridades e a passagem entre formação e prática profissional sem exigir uniformidade tecnológica ou operacional.

Essa última frase conecta diretamente o `De onde partimos` ao restante do manifesto: linguagem comum não significa materialização única.

## 5. Postura autoral pretendida

O humano rejeitou formulações excessivamente defensivas, como:

- explicar repetidamente que outras pessoas já disseram algo semelhante;
- afirmar que a contribuição só é válida se cada parte for inédita;
- transformar o manifesto em justificativa preventiva contra críticas de anterioridade.

A postura desejada é:

```text
conhecemos a tradição
→ escolhemos conscientemente de onde partir
→ explicamos por que esse ponto de partida é confiável
→ assumimos que os conceitos podem ter antecedentes
→ mostramos o deslocamento de importância que propomos
→ buscamos uma linguagem comum sem impor realização uniforme
```

Humildade aqui significa delimitar corretamente a contribuição, não diminuí-la.

## 6. Relação com a auditoria de anterioridade

A auditoria externa passa a ter um papel positivo: ajudar a preencher o futuro `CCP de Partida`, não servir apenas como mecanismo defensivo.

O artefato profundo deverá, quando implementado, permitir algo como:

```text
conceito adotado
→ antecedente relevante
→ fonte/evidência
→ por que consideramos consolidado
→ limite conhecido
→ como entra no FlowED
→ qual reponderação/delta o manifesto propõe
```

A projeção `De onde partimos` continuará curta. A profundidade fica no CCP e, futuramente, nas formas de projeção definidas pelo EDT.

## 7. Relação com A0.2

A0.2 já afirma que o manifesto não pretende reivindicar como novas as ideias que o sustentam. A nova seção não substitui necessariamente A0.2; ela o **materializa**.

A0.2 declara a postura. `D0.1–D0.4` mostram:

- o que fazemos com o conhecimento recebido;
- onde buscamos apoio;
- onde localizamos nossa contribuição;
- qual transversalidade de linguagem queremos explorar.

Durante a consolidação futura, o PO/MAN poderá avaliar eventual redundância redacional entre A0.2 e `D0.*`, mas este sprint não propõe remover ou reescrever A0.2.

## 8. O que este sprint NÃO decidiu

Não foi decidido ainda:

- nomenclatura normativa final de `CCP de Partida`;
- conteúdo formal do CCP;
- conteúdo formal do EDT;
- lista definitiva de referências que preencherão a base de partida;
- claim de originalidade científica do FlowED;
- alteração imediata do manifesto principal;
- mudança em P1, P2, P3 ou P2.3.

Esses pontos permanecem para avaliação do PO e ciclos posteriores.

## 9. Recomendação MAN-001 ao PO

Recomendo tratar esta proposta como **candidata forte para a arquitetura final do manifesto**, porque ela resolve três problemas simultaneamente:

1. torna explícita a continuidade com conhecimento consolidado sem transformar o manifesto em uma revisão bibliográfica;
2. localiza a contribuição de FlowED de forma coerente com o que já vinha emergindo: **reponderação de importância**, não invenção necessária dos ingredientes;
3. explicita a ambição transversal de uma linguagem conceitual comum que atravesse domínios, senioridades e formação/prática sem confundir linguagem comum com implementação uniforme.

Se aprovada pelo PO, a recomendação é incorporar `D0.1–D0.4` ao próximo ciclo editorial normal e então submetê-las ao mesmo protocolo de densidade já adotado (`BASELINE → EXPAND-MAX / REDUCT-MAX / DEFESA`).

## 10. Fechamento do sprint

O desvio exploratório iniciado pelo humano pode ser considerado encerrado neste ponto.

Entregas produzidas durante o ciclo:

- verificação crítica das consultorias externas e correção de erros de anterioridade;
- pareceres progressivos ao PO;
- proposta de auditoria por claim;
- proposta de `CCP de Partida` / fundação epistêmica;
- refinamento editorial da seção `De onde partimos`;
- BASELINE candidata `D0.1–D0.4`;
- explicitação de que FlowED pretende reponderar conceitos conhecidos e estender uma linguagem conceitual comum pela cadeia de engenharia.

**Estado recomendado após este fechamento:** aguardar crítica/decisão do PO sobre a proposta e, salvo nova orientação, retomar o trabalho editorial ordinário de P2.3.