# Intenção como superfície operacional estável — rascunho conceitual

**Status:** hipótese forte em discussão para possível promoção ao núcleo do Manifesto FlowED. Não normativa nesta versão.

## 1. Problema observado

Ao longo da formação e da prática em Engenharia de Software, métodos, ferramentas, comandos, interfaces e maneiras de materializar uma mesma necessidade mudam com frequência. Cada substituição tecnológica pode exigir reaprendizado operacional e pode provocar perda temporária de eficiência, mesmo quando a finalidade prática permanece essencialmente a mesma.

Exemplo representativo: a intenção de **iniciar um projeto** pode permanecer reconhecível ao longo de décadas, enquanto os mecanismos concretos para realizá-la mudam repetidamente.

## 2. Hipótese FlowED

O usuário operacional deveria expressar prioritariamente **a intenção**, e não a sequência concreta de materialização.

A intenção pública tende a ser mais estável que as implementações que a realizam. Novas intenções podem surgir e intenções existentes podem evoluir, mas a taxa de mudança esperada das intenções é muito menor que a taxa de mudança de ferramentas, frameworks, comandos e arquiteturas de implementação.

Portanto, evitar formulação absoluta como "a intenção nunca muda". Formulação de trabalho:

> **Intenções operacionais bem definidas devem constituir a superfície mais estável do FlowED, enquanto suas materializações permanecem substituíveis e evolutivas.**

## 3. Separação de responsabilidades

A hipótese implica uma separação entre quem **executa uma intenção** e quem **governa sua materialização**.

O executor cotidiano deveria poder pedir a mesma coisa usando a mesma semântica pública ao longo do tempo. Ele não deveria precisar reaprender detalhes internos sempre que a organização troca de ferramenta ou eleva sua maturidade.

Outra função/papel da organização define ou aprova políticas, perfis, restrições, defaults, providers, adapters, riscos e demais parâmetros que condicionam a materialização. A analogia informal "executor × legislador" é útil para raciocínio, mas não é terminologia FlowED ratificada.

## 4. Pipeline conceitual candidato

A fronteira pública pode ser pensada como:

**intenção declarada + contexto declarado/descoberto + políticas vigentes + contratos/versionamento + capabilities disponíveis -> interpretação/seleção -> materialização por provider/adapter -> resultado observável**

O executor interage principalmente com a intenção e apenas com particularidades que sejam indispensáveis à própria semântica da solicitação. Detalhes de materialização ficam abaixo dessa fronteira.

## 5. Determinismo: correção necessária

A expressão "todo o resto deve ser determinístico" precisa ser refinada.

Não é defensável exigir que todo efeito no mundo externo seja determinístico, porque ambiente, disponibilidade, concorrência, rede, ferramentas e intervenções externas podem variar.

O compromisso mais plausível é:

> **dada a mesma intenção canônica, o mesmo contexto relevante, as mesmas políticas, a mesma versão dos contratos e o mesmo conjunto de capabilities disponíveis, a interpretação e a decisão de materialização devem ser reproduzíveis sempre que o contrato declarar determinismo.**

O resultado físico pode ainda falhar ou variar por causas externas sem que isso torne a interpretação não determinística.

## 6. Relação com o Pilar 1

Esta hipótese aprofunda o Pilar 1.

"Rígido no contrato e livre na materialização" ganha uma superfície humana/operacional explícita:

- **intenção:** o que se quer alcançar;
- **contrato:** o significado público e as garantias observáveis dessa intenção/capability;
- **governança/política:** como a organização condiciona a escolha da materialização;
- **materializador/provider/adapter:** como aquilo é concretamente realizado.

A estabilidade procurada pelo FlowED está principalmente na intenção e no contrato, não na ferramenta.

## 7. Continuidade de aprendizagem

Se a hipótese se sustentar, uma pessoa pode aprender uma intenção operacional no início de sua formação e continuar usando a mesma linguagem semântica durante sua evolução profissional.

A maturidade crescente da organização muda políticas, capacidades, providers, rigor e escala por trás da intenção, e não necessariamente a forma básica de expressar o objetivo.

Isso cria uma possível contribuição educacional e organizacional do FlowED: reduzir reaprendizado operacional provocado por substituição tecnológica sem esconder o conhecimento conceitual que o profissional precisa dominar.

## 8. Prior art encontrado nesta rodada

A hipótese não surge sem antecedentes.

O RFC 9315 do IRTF define `intent` como objetivos operacionais e resultados declarados sem especificar como alcançá-los, e descreve Intent-Based Systems que traduzem e orquestram a intenção até configurações/ações concretas. O mesmo documento separa `intent` de `policy`: intenção expressa resultado desejado; política governa escolhas de comportamento.

O RFC 9316 reforça a ideia de interface de intenção + engine de tradução e lifecycle management.

Policy-Based Management fornece ainda antecedentes para separar definição de políticas de seus pontos de decisão e enforcement.

Esses trabalhos são principalmente de networking/autonomic management; portanto não provam, por si só, que a mesma abordagem cobre toda a Engenharia de Software. Mas demonstram que a separação `intenção -> política/tradução -> materialização` é tecnicamente e conceitualmente realizável em domínios complexos.

## 9. Hipótese residual para FlowED

O possível residual FlowED não é inventar "intent-based management".

A linha a investigar é a generalização dessa superfície de intenção para capacidades transversais da Engenharia de Software, com:

- linguagem operacional comum;
- contratos públicos versionados;
- providers/adapters substituíveis;
- governança progressiva;
- memória/evidência;
- continuidade educacional e profissional;
- conformidade independente da implementação.

Antes de reivindicar novidade, deve haver revisão de anterioridade específica.

## 10. Impacto potencial no manifesto

Se estabilizada, esta hipótese deve subir acima de uma simples regra de implementação. Ela pode afetar a tese central, o compromisso fundamental e o Pilar 1.

Formulação candidata curta:

> **O FlowED procura tornar a intenção operacional mais estável que as ferramentas que a materializam: pessoas expressam o que precisam alcançar; contratos preservam o significado; políticas e implementações podem evoluir sem obrigar a reaprender a intenção.**

## 11. Questões ainda abertas

1. Qual granularidade caracteriza uma intenção suficientemente estável sem se tornar vaga?
2. Quando uma opção é parte legítima da intenção e quando é detalhe de materialização?
3. Como tratar intenções cuja semântica realmente evolui ou deixa de existir?
4. Quanto contexto pode ser inferido automaticamente sem esconder decisões importantes do executor?
5. Qual é a fronteira entre executor, autor de política, autoridade de aprovação e materializador?
6. Qual parte do determinismo é obrigação transversal e qual deve ser declarada capability por capability?
