# Seleção do primeiro piloto de domínio FlowED

**Status:** decisão de trabalho provisória; revisada após dogfood arquitetural e escolha do primeiro contrato público piloto.

## Contexto

Após estabilizar parcialmente a hipótese de uma linguagem pública comum do FlowED — com `flwd` como cliente e CLI/YAML/API/SDK/UI/agents falando o mesmo contrato semântico — tornou-se necessário escolher um primeiro recorte concreto para testar a arquitetura.

Dois candidatos imediatos foram inicialmente considerados:

1. `ISO29110-lite`;
2. `InitProj POC`.

A primeira proposta sugeriu usar `InitProj POC` como piloto e `ISO29110-lite` como profile/reference ligado a ele. O debate seguinte revelou **acoplamento arquitetural indevido** nessa formulação.

## Correção arquitetural

Na esfera maior está o FlowED. Abaixo dele existem capacidades/domínios e implementações concretas. Conceitualmente, o FlowED deve orientar-se por **contratos públicos**, e não por ports, adapters, providers ou qualquer padrão interno obrigatório.

Ports/adapters continuam possíveis como técnica de implementação, mas não são constitutivos do FlowED.

FlowED não deve depender diretamente de `ISO29110-lite`, `InitProj` ou de qualquer implementação específica. Deve depender do contrato público correspondente à capacidade desejada.

Uma implementação concreta pode ser retirada e substituída por outra que satisfaça o mesmo contrato, mesmo que o resultado produzido possua personalidade, organização interna ou artefatos próprios.

A equivalência exigida é **contratual**, não identidade física de artefatos.

## Novo critério para o primeiro piloto

O primeiro piloto não é mais “qual produto/módulo devemos estruturar primeiro?” nem “qual port devemos criar?”.

A pergunta correta passa a ser:

> **qual é o menor contrato público real que podemos especificar e testar com duas implementações estruturalmente diferentes?**

O piloto deve:

- representar uma capacidade/prática pequena e observável;
- possuir contrato semântico independente da implementação;
- ser acionável pela mesma língua FlowED via CLI/YAML/API;
- permitir ao menos duas implementações;
- permitir verificar substituição sem alterar o consumidor;
- preservar personalidade própria da implementação fora do mínimo exigido pelo contrato;
- produzir evidence/receipt suficiente para comparação;
- evitar que detalhes internos de arquitetura subam para o modelo conceitual do FlowED.

## Escolha atual: TDD

A escolha atual para o primeiro piloto é **TDD — Test-Driven Development**.

A decisão é experimental e busca maximizar pressão sobre o contrato público com baixo acoplamento arquitetural.

TDD é adequado porque possui uma intenção metodológica reconhecível e pode ser materializado em ecossistemas muito diferentes, por exemplo Java/JUnit, Python/pytest, JavaScript/Vitest/Jest ou PHP/PHPUnit. O FlowED deve conseguir expressar o contrato sem conhecer essas implementações.

O objetivo não é criar uma nova teoria de TDD nem definir um framework. O objetivo é usar TDD para testar se o FlowED consegue declarar somente o comportamento observável e permitir implementações diferentes abaixo dele.

Documento específico: `TDD-FIRST-PUBLIC-CONTRACT-PILOT.md`.

## Papel futuro de InitProj e ISO29110-lite

`InitProj POC` e `ISO29110-lite` continuam candidatos fortes para expansões futuras, mas deixam de ser o primeiro piloto.

Eles só devem ser modelados depois que o núcleo do FlowED estiver suficientemente consolidado e o piloto TDD tiver fornecido evidência real sobre linguagem, contratos e substituição.

## Sequência pretendida

1. definir contrato público mínimo de TDD;
2. representar a mesma semântica por CLI, YAML e API;
3. satisfazer o contrato com pelo menos duas implementações distintas;
4. registrar dogfood, gaps e correções;
5. consolidar e fechar a primeira versão conceitual do FlowED;
6. somente depois iniciar novos domínios/capabilities.

## Evidência de dogfood

A evolução desta decisão já produziu duas correções relevantes antes da implementação:

- a tentativa de ligar `ISO29110-lite` a `InitProj` revelou acoplamento conceitual indevido;
- a tentativa de elevar ports ao nível conceitual revelou que o FlowED deve depender de contratos públicos, deixando ports/adapters como possíveis técnicas internas.

A escolha de TDD é a próxima hipótese a ser testada, não uma verdade consolidada.
