# FlowED — naming, conformance e separação entre filosofia e produto

**Status:** decisão de naming ainda aberta; recomendação provisória registrada para fechamento do manifesto.

## 1. Problema

A evolução conceitual do FlowED revelou uma possível ambiguidade de marca: `FlowED` pode ser entendido simultaneamente como filosofia/manifesto, conjunto de contratos e produto/ecossistema executável.

Essa ambiguidade pode gerar a falsa impressão de que usar o software oficial é condição para ser FlowED ou de que opiniões produzidas por ferramentas oficiais representam automaticamente a opinião normativa do framework.

Ao mesmo tempo, separar completamente os nomes pode fragmentar a marca, enfraquecer a associação comercial entre a filosofia e sua materialização de referência e aumentar o custo cognitivo de adoção.

## 2. Condição constitutiva já aceita

Uma organização, ferramenta ou ecossistema pode ser **Full FlowED** mesmo sem usar uma única linha de código, CLI, adapter, hub ou produto produzido pela LaboWare, desde que cumpra integralmente os contratos constitutivos aplicáveis.

Portanto:

> **Full FlowED é uma condição de conformidade, não uma condição de uso de produto.**

O produto oficial existe para materializar e facilitar o cumprimento dos contratos, não para monopolizar a conformidade.

## 3. Opção A — manter Manifesto FlowED e produto FlowED sob a mesma marca

### Vantagens

- máxima continuidade entre ideia, contrato e materialização;
- uma única marca a ensinar, pesquisar e divulgar;
- forte transferência reputacional entre manifesto, comunidade, documentação e produto;
- menor custo cognitivo para estudante e organização;
- permite que o produto oficial seja apresentado naturalmente como a materialização de referência construída pelos autores do manifesto.

### Riscos

- percepção de conflito de interesse ou auto-certificação;
- possibilidade de usuários confundirem `FlowED` com o software específico;
- fornecedores concorrentes podem interpretar o ecossistema como capturado pela implementação oficial;
- críticas a uma ferramenta podem ser confundidas com críticas ao manifesto;
- comunicação comercial inadequada pode sugerir que Full FlowED exige produtos oficiais.

## 4. Opção B — criar outro nome para o manifesto/standard e manter FlowED apenas como produto

### Vantagens

- separação semântica imediata entre norma e implementação;
- facilita comunicar neutralidade em relação a fornecedores;
- uma ferramenta FlowED poderia declarar conformidade ao manifesto/standard externo exatamente como qualquer concorrente;
- reduz a percepção de que o criador da implementação define unilateralmente o critério que a certifica.

### Riscos

- cria duas marcas para um único modelo mental;
- enfraquece a associação entre a pesquisa, o manifesto e o produto;
- aumenta esforço de documentação, ensino, busca, publicação e branding;
- pode produzir pergunta recorrente do tipo “qual a diferença entre X e FlowED?”;
- corre o risco de fazer o manifesto parecer uma entidade artificial criada apenas para certificar o próprio produto.

## 5. Opção C — mesma marca-raiz, papéis explicitamente diferentes

Recomendação provisória.

Manter `FlowED` como nome do **ecossistema normativo aberto**, mas tornar os papéis inequívocos:

- **Manifesto FlowED** — valores, princípios e posições filosóficas;
- **FlowED Contracts / FlowED Specification** — obrigações normativas, comportamento público e conformidade;
- **Full FlowED / FlowED Conformant** — condição de conformidade independente de fornecedor ou código;
- **`flwd`** — cliente/runtime oficial de referência;
- **FlowED Platform / distribuição de referência da LaboWare** — composição opcional de `flwd`, hub, adapters e providers de referência;
- ferramentas como COR, MyTrues e outros produtos — providers/materializadores opcionais.

Neste modelo, a marca permanece unificada, mas a implementação oficial não é confundida com o critério de conformidade.

## 6. Referências arquiteturais observadas

Há precedentes para as duas estratégias.

- O OpenAPI Specification nasceu do Swagger Specification e, após a doação, tornou-se um projeto separado sob uma iniciativa de governança própria. Isso mostra o valor de separar especificação interoperável de uma marca/ferramenta original quando neutralidade de ecossistema se torna importante.
- A Open Container Initiative recebeu especificações e uma implementação de referência originadas no ecossistema Docker e trabalha com especificações mínimas abertas que permitam múltiplas implementações independentes.
- Kubernetes mantém uma marca forte e, ao mesmo tempo, possui programa de conformance em que diferentes fornecedores demonstram suporte às APIs necessárias por uma suíte comum. Isso mostra que **mesma marca e neutralidade de implementação podem coexistir**, desde que conformidade e governança sejam públicas e verificáveis.

Esses exemplos sugerem que o problema central não é somente o nome. São também **governança, teste de conformidade, política de marca e ausência de privilégio técnico para a implementação oficial**.

## 7. Analogia Manifesto Ágil / Scrum

A analogia é útil, mas apenas figurativa.

O Manifesto Ágil declara valores e princípios; Scrum é um framework concreto e não é condição para aderir ao Manifesto Ágil.

Para FlowED, a separação desejada é semelhante em espírito:

**Manifesto FlowED -> contratos FlowED -> uma ou muitas materializações**.

Entretanto, o produto `flwd` é mais próximo de um cliente/runtime de referência de um sistema contratual do que Scrum é de uma implementação do Manifesto Ágil. Portanto, a analogia não deve definir nossa arquitetura ou nomenclatura.

## 8. Critério de neutralidade

Mesmo mantendo o nome FlowED para manifesto e ecossistema, a neutralidade só existe se forem verdadeiras pelo menos estas propriedades:

1. contratos e critérios de conformidade são públicos e versionados;
2. testes de conformidade podem ser executados contra implementações de terceiros;
3. ferramentas oficiais não recebem exceções de contrato;
4. opiniões de providers permanecem atribuídas ao provider;
5. Full FlowED não exige código da LaboWare;
6. fornecedor concorrente pode implementar o contrato completo sem autorização arquitetural especial;
7. a marca/certificação, quando existir, possui regras públicas que não confundem autoria com conformidade.

## 9. Recomendação provisória

**Não renomear o Manifesto FlowED agora.**

O ganho de neutralidade de um segundo nome parece menor do que o custo de fragmentação neste estágio. A separação mais limpa é deslocar a distinção para os papéis:

> **FlowED = filosofia + contratos + ecossistema aberto.**
>
> **`flwd` e a distribuição LaboWare = materialização oficial de referência.**

Assim, `FlowED` não é propriedade semântica do executável. O executável demonstra FlowED.

Essa decisão deve permanecer revisável. Se o ecossistema ganhar múltiplos fornecedores, certificação externa ou governança independente e a marca começar a produzir conflito real, pode-se avaliar posteriormente uma fundação/iniciativa normativa independente ou renaming específico sem alterar os contratos existentes.

## 10. Consequência para as críticas

A separação desejada passa a ser explícita:

- discordar de um valor -> crítica ao Manifesto FlowED;
- apontar incapacidade de representar um comportamento necessário -> crítica aos contratos FlowED;
- apontar erro de cálculo, baixa confiabilidade ou metodologia ruim -> crítica ao provider;
- apontar falha de orquestração -> crítica ao `flwd`/produto;
- implementar tudo sem código oficial e cumprir os contratos -> continua elegível a Full FlowED.
