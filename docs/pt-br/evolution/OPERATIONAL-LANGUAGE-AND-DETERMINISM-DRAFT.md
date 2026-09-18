# Draft — Linguagem Operacional e Determinismo do FlowED

**Status:** Referência Experimental em `R1 — realizável em princípio / escopo aberto`.

**Reference ID:** `REF-2026-002`  
**Origem:** GAP-M004, GAP-M005 e GAP-M015; debate sobre comando, parâmetros, declaratividade e determinismo.  
**Diligência de Discovery:** L1 — exploratory/scoping.  
**Rota provisória:** `COMPOSE` — combinar padrões existentes antes de inventar sintaxe/semântica própria.

## 1. Correção de arquitetura desta rodada

A rodada anterior misturou dois níveis diferentes: **linguagem pública do FlowED** e **comportamento interno do runtime**.

A distinção provisória passa a ser:

1. **FlowED Language/Protocol** — contrato semântico comum, independente de transporte e cliente;
2. **`flwd`** — cliente CLI de referência para humanos e automação de shell;
3. **YAML/arquivo declarativo** — outra forma de expressar a mesma linguagem semântica;
4. **API/SDK/UI/agentes/outros clientes** — outros meios de falar a mesma língua;
5. **runtime/materializadores** — interpretam a requisição normalizada e realizam a operação segundo contratos internos.

Portanto, `flwd` não é a linguagem: é um cliente da linguagem FlowED.

## 2. Objetivo da linguagem pública

A linguagem precisa suportar a vasta gama de operações que podem partir do FlowED sem obrigar todos os domínios a expor a mesma implementação interna.

A regra central passa a ser:

> **Muitos clientes e transportes; uma semântica operacional comum.**

CLI, YAML, API, SDK, UI e agentes não precisam ter a mesma sintaxe superficial, mas devem preservar o mesmo vocabulário, tipos, operações, parâmetros, opções, constraints e significado observável.

## 3. Forma humana primária: `flwd`

Hipótese atual para o cliente de referência:

**`flwd <verbo> [parâmetros] [opções]`**

O verbo expressa a operação. Parâmetros posicionais são usados apenas quando sua função é inequívoca e estável. Opções nomeadas refinam a operação, selecionam comportamento, contexto, intensidade, materialização ou fonte declarativa.

Exemplos meramente ilustrativos:

- `flwd create project myapp`
- `flwd validate release 1.4.0`
- `flwd publish release 1.4.0 --channel stable`
- `flwd test project --level standard`
- `flwd apply --file flowed.yaml`

Não se fixa ainda uma gramática definitiva nem um conjunto final de verbos.

## 4. Declarativo como outra projeção da mesma língua

Uma opção do cliente pode apontar para uma declaração YAML ou outro formato suportado. Nesse caso, o usuário troca a expressão curta imperativa por uma descrição declarativa mais extensa sem mudar de modelo semântico.

Exemplo conceitual:

- CLI curta: verbo + parâmetros + opções;
- CLI declarativa: `flwd apply --file flowed.yaml`;
- API: envia uma requisição estruturada equivalente;
- SDK: constrói a mesma estrutura por objetos/tipos;
- UI: produz a mesma estrutura a partir de controles;
- agente: propõe/preenche a mesma estrutura e a submete ao mesmo contrato.

A equivalência exigida é **semântica**, não textual.

## 5. Envelope semântico comum

Nome de trabalho: **FlowED Operational Request**.

O envelope é o contrato compartilhado entre clientes e runtime. Campos candidatos mínimos:

- versão do protocolo/schema;
- operação/verbo canônico;
- alvo/objeto;
- parâmetros;
- opções;
- contexto declarado;
- constraints/policies aplicáveis;
- origem/ator;
- identificador da requisição;
- referências de proveniência/racional quando exigidas pelo risco ou pela operação.

Domínio/capability pode existir como metadado explícito ou ser resolvido deterministicamente pelo registro da operação. Não deve ser imposto na sintaxe humana se não trouxer valor ao usuário.

A representação física desse envelope ainda não está decidida. YAML, JSON, CUE, Protobuf ou combinação permanecem candidatos de materialização do contrato.

## 6. Relação verbo × declarativo

O FlowED não precisa escolher entre uma CLI imperativa e uma configuração declarativa como modelos concorrentes.

- **verbo** é a forma compacta de solicitar uma operação;
- **parâmetros** identificam os elementos essenciais da solicitação;
- **opções** refinam ou qualificam a operação;
- **arquivo declarativo** expressa de forma explícita e reprodutível uma configuração/solicitação maior;
- todos convergem para o mesmo envelope semântico.

Assim, um mesmo conceito pode nascer de comando curto, arquivo, API ou outro cliente sem criar dialetos semanticamente incompatíveis.

## 7. O que pertence à linguagem e o que pertence ao runtime

### 7.1 Pertence à linguagem/protocolo público

- operações e seus significados;
- tipos de alvo;
- parâmetros e opções válidos;
- schemas e constraints públicas;
- erros/estados observáveis;
- capabilities declaradas;
- compatibilidade/versionamento do contrato;
- proveniência e requisitos de autoridade quando fizerem parte da operação;
- equivalência semântica entre clientes.

### 7.2 Pertence principalmente ao comportamento interno

- reconciliation loops;
- cálculo de diff;
- plan/apply interno;
- hashes internos;
- locks;
- transações/compensações;
- retries;
- snapshots;
- estratégia de adapters/materializadores;
- implementação de idempotência;
- mecanismos de persistência.

Esses mecanismos podem ser necessários para cumprir garantias públicas de determinismo, rastreabilidade e segurança, mas não precisam aparecer como parte da língua cotidiana do usuário.

## 8. Determinismo como garantia do contrato, não como sintaxe

A linguagem deve permitir que o runtime seja determinístico onde a operação admite determinismo.

A garantia conceitual é:

> **A mesma requisição semântica, no mesmo contexto declarado e sob as mesmas versões relevantes, deve produzir a mesma interpretação e o mesmo plano/decisão quando isso for tecnicamente possível.**

Como o runtime implementa isso é responsabilidade interna. Recursos como canonicalização, snapshots, plan hashes, etags, idempotency keys e hermeticidade são candidatos técnicos para realizar essa garantia, não elementos obrigatórios da gramática humana.

## 9. Prior art atualmente aproveitado

A composição continua inspirada em padrões existentes:

- desired state e reconciliation para operações declarativas persistentes;
- plan/apply para separar intenção de efeito quando necessário;
- resource-oriented/declarative-friendly APIs para semântica uniforme entre clientes;
- request IDs/etags para segurança de repetição e concorrência;
- hermeticidade/reprodutibilidade para reduzir inputs implícitos;
- validation-first para garantir schema e constraints antes de efeitos.

A contribuição candidata do FlowED não é reinventar esses mecanismos, mas oferecer uma linguagem operacional comum capaz de atravessar domínios distintos da Engenharia de Software.

## 10. Hipótese atual para GAP-M004

A unidade primária não deve ser nem a string CLI nem obrigatoriamente uma "intenção" abstrata.

Hipótese refinada:

> **A unidade primária é uma requisição operacional semanticamente tipada; `flwd`, YAML, API e demais clientes são diferentes projeções dessa mesma unidade.**

Essa hipótese ainda precisa ser testada em uma amostra ampla de operações de domínios diferentes.

## 11. Teste necessário

O próximo experimento deve evitar testar apenas Versionamento e Qualidade. Como o FlowED pretende cobrir uma gama ampla de Engenharia de Software, a linguagem deve ser exercitada contra uma matriz heterogênea, por exemplo:

- projeto/inicialização;
- versionamento;
- qualidade/testes;
- documentação;
- release/deploy;
- infraestrutura;
- segurança/compliance;
- gestão de trabalho;
- evidência/research;
- educação/aprendizado;
- comunicação/coordenação;
- consulta/observação.

O objetivo não é implementar todos os domínios, mas verificar se operações reais de naturezas muito diferentes cabem no mesmo contrato `verbo + parâmetros + opções ↔ requisição estruturada`, sem criar exceções semânticas artificiais.

## 12. Estado dos gaps

### GAP-M004 — Unidade primária da linguagem operacional

Permanece `PARTIAL`, com hipótese refinada para `Operational Request` comum a múltiplos clientes.

### GAP-M005 — Coordenação comum versus soberania dos domínios

Permanece `PARTIAL`. A linguagem governa o contrato público; o runtime/materializador conserva liberdade interna desde que satisfaça o contrato.

### GAP-M015 — Liberdade governada

Permanece `PARTIAL`. A governança pública deve se concentrar em semântica, compatibilidade, contratos, rastreabilidade e resultados observáveis, evitando prescrever mecanismos internos desnecessariamente.

### GAP-M021 — Observe × State × Action

Rebaixado de possível fundamento da linguagem para **classificação interna/candidata de operações**, a validar. Pode ser útil ao runtime sem necessariamente aparecer para o usuário.

### GAP-M022 — Vocabulário operacional transversal

Permanece aberto. O desafio é definir verbos suficientemente estáveis para uma gama ampla de domínios sem criar uma DSL artificial.

### GAP-M023 — Contrato formal de determinismo

Permanece aberto, mas separado da gramática pública. Deve definir garantias observáveis e deixar liberdade de implementação interna.

### GAP-M024 — Representação canônica e linguagem de schema

Permanece aberto. A escolha deve ser orientada pela equivalência entre CLI, YAML, API, SDK/UI e automação, não apenas pela conveniência de um runtime específico.

## 13. Dogfood da correção

Esta rodada é uma correção produzida pelo próprio uso conceitual do protocolo: a formulação anterior expôs mecanismos internos como se fossem parte da linguagem. O debate revelou que isso reduziria a clareza e poderia limitar a ampla gama de clientes/operações prevista para FlowED.

A referência `REF-2026-002` é portanto refinada sem apagar a versão anterior. A evidência é conceitual/documental, de força baixa, e exige teste contra a matriz ampla de domínios antes de qualquer promoção.
