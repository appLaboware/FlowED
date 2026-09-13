# Separação entre intenção, política e materialização — rascunho

**Status:** hipótese conceitual em consolidação para o Manifesto FlowED.

## Síntese desta rodada

A discussão refinou o papel da intenção no FlowED. O ponto central não é apenas separar `o quê` de `como`, mas separar também **momentos de decisão** e **responsabilidades lógicas**.

O mesmo ator pode exercer mais de um papel, sobretudo em uma equipe pequena ou individual, mas os papéis não devem ser confundidos:

1. alguém expressa a intenção operacional e seus requisitos relevantes;
2. alguém estabelece políticas, defaults, restrições e escolhas organizacionais;
3. o sistema resolve a intenção contra contexto, políticas, contratos e capabilities disponíveis;
4. um materializador/provider executa a decisão resultante.

Essa separação é lógica, não necessariamente organizacional. Uma única pessoa pode assumir todos os papéis em momentos diferentes.

## Intenção não é sinônimo de ausência de parâmetros

Uma intenção pode conter parâmetros e restrições que fazem parte do resultado desejado. O objetivo não é reduzir toda solicitação a um verbo sem contexto.

A questão correta é distinguir:

- **parâmetros que qualificam o resultado desejado**;
- **restrições de domínio que fazem parte da necessidade real**;
- **políticas organizacionais**;
- **preferências ou decisões de materialização**;
- **detalhes incidentais de uma ferramenta específica**.

A mesma palavra pode ocupar papéis diferentes conforme o motivo de sua presença. Por exemplo, `Java` pode ser uma restrição real da intenção se compatibilidade Java fizer parte do resultado requerido; pode ser uma política da organização se o time decidiu padronizar Java; ou pode ser apenas detalhe de materialização se a intenção não exigir linguagem específica.

Portanto, a classificação deve ser semântica e contextual, não baseada em listas fixas de termos.

## Exemplo: repositório

A expressão `quero duas branches` pode ser uma descrição prematuramente acoplada a Git.

Uma intenção mais estável pode ser algo como:

- quero uma linha de evolução usada pelos clientes;
- quero uma linha separada para desenvolvimento;
- quero uma terceira linha para validação/testes;
- quero regras específicas de visibilidade e promoção entre essas linhas.

Um provider pode materializar isso com branches Git. Outro mecanismo futuro pode satisfazer a mesma intenção por outra estrutura equivalente.

O conhecimento relevante do usuário é o significado dessas linhas e das relações entre elas. O detalhe `branch` só deve subir para a intenção quando realmente fizer parte da exigência do usuário.

## Aprendizagem e mudança de materialização

Esse modelo reforça o Pilar 2.

Se uma materialização produz resultados ruins, a organização pode aprender e trocar política, provider ou materializador sem obrigar o executor a reaprender ou reescrever a intenção que continuou válida.

Assim, a experiência produz mudança no ponto correto:

**mesma intenção válida + nova evidência -> nova decisão de materialização**

em vez de:

**nova evidência -> todos os executores reaprendem a superfície operacional**.

## Relação com prior art

A separação possui antecedentes fortes e não deve ser apresentada como invenção do FlowED.

- RFC 9315 define intent como objetivos/resultados operacionais declarados sem especificar como alcançá-los e destaca abstração, autonomia, supervisão e linguagem orientada ao usuário.
- RFC 9316 diferencia intent de policy e modela intent por Context + Capabilities + Constraints, além de reconhecer diferentes tipos de intent users e níveis de abstração.
- A tradição de separação entre policy e mechanism em sistemas computacionais reforça a ideia de que decisões normativas e mecanismos executores podem evoluir independentemente.
- APIs declarativas e control loops, como em Kubernetes, demonstram tecnicamente que estado desejado e mecanismo de reconciliação podem ser desacoplados.

Referências de trabalho:
- https://www.rfc-editor.org/info/rfc9315/
- https://www.rfc-editor.org/info/rfc9316/
- https://kubernetes.io/docs/concepts/architecture/controller/
- https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/

## Hipótese para o Manifesto

> **Quem executa deve poder expressar uma intenção estável com os parâmetros e restrições necessários ao resultado. Decisões sobre como essa intenção será materializada devem poder ocorrer separadamente, por políticas e providers substituíveis.**

Essa separação busca preservar conhecimento operacional do usuário enquanto permite que a organização mude tecnologia, padrões e materialização sem reescrever continuamente a forma de expressar o mesmo objetivo.

## Limites

1. FlowED não promete que todo detalhe técnico pode ser escondido. Quando uma tecnologia é parte real da exigência, ela pertence à intenção ou às suas restrições.
2. Especialistas continuam podendo e devendo conhecer profundamente a materialização quando isso fizer parte de sua responsabilidade.
3. Separação de papéis não implica pessoas distintas; implica decisões distinguíveis e rastreáveis.
4. O sistema não deve inferir silenciosamente uma intenção ausente. Quando contrato/contexto/política não forem suficientes, deve haver explicitação ou pedido de esclarecimento.
5. Determinismo deve ser reivindicado no nível da interpretação e decisão contratual quando aplicável, não como garantia universal de toda execução física.

## Impacto provável nos pilares

- **Pilar 1:** a linguagem comum deve ser principalmente linguagem de intenção; políticas e materializações ficam abaixo da fronteira contratual.
- **Pilar 2:** aprendizado pode mudar a política/materialização preservando intenção válida.
- **Pilar 3:** escolhas de política/materialização podem expor a sustentação que as motivou sem transferir julgamento ao FlowED.
- **Pilar 4:** progressividade pode alterar rigor, configuração, provider ou política sem obrigar mudança da superfície de intenção quando o objetivo continuar o mesmo.

## Questão aberta

A fronteira exata entre `intent parameter`, `constraint`, `context` e `policy` deve ser derivada por exemplos e contratos executáveis, preferindo terminologia consolidada na literatura antes de introduzir novos conceitos FlowED.
