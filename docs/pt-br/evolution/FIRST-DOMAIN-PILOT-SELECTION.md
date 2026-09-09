# Seleção do primeiro piloto de domínio FlowED

**Status:** decisão de trabalho provisória; revisada após dogfood arquitetural.

## Contexto

Após estabilizar parcialmente a hipótese de uma linguagem pública comum do FlowED — com `flwd` como cliente e CLI/YAML/API/SDK/UI/agents falando o mesmo contrato semântico — tornou-se necessário escolher um primeiro recorte concreto para testar a arquitetura.

Dois candidatos imediatos foram inicialmente considerados:

1. `ISO29110-lite`;
2. `InitProj POC`.

A primeira proposta sugeriu usar `InitProj POC` como piloto e `ISO29110-lite` como profile/reference ligado a ele. O debate seguinte revelou **acoplamento arquitetural indevido** nessa formulação.

## Correção

Na esfera maior está o FlowED. Abaixo dele existem módulos horizontais/capabilities pares, ligados por **ports com contratos públicos**.

FlowED não deve depender diretamente de `ISO29110-lite`, `InitProj` ou de qualquer provider específico. Deve depender do contrato do port correspondente à capability desejada.

Um provider concreto pode ser retirado e substituído por outro que implemente o mesmo port, mesmo que o resultado produzido possua personalidade, organização interna ou artefatos próprios.

Portanto, `ISO29110-lite` não deve ser modelado como profile interno do `InitProj` salvo se um caso futuro demonstrar explicitamente essa relação. Ambos devem permanecer desacoplados enquanto pertencem a capabilities distintas.

## Novo critério para o primeiro piloto

O primeiro piloto não é mais “qual produto/módulo devemos estruturar primeiro?”.

A pergunta correta passa a ser:

> **qual é o menor port real que podemos especificar e testar com substituição de provider?**

O piloto deve:

- representar uma capability pequena e observável;
- possuir contrato semântico independente da implementação;
- ser acionável pela mesma língua FlowED via CLI/YAML/API;
- permitir ao menos dois providers, ou um provider real + fake/reference implementation;
- permitir verificar substituição sem alterar o consumidor;
- preservar personalidade própria do provider fora do mínimo exigido pelo contrato;
- produzir evidence/receipt suficiente para comparação.

## Papel de InitProj e ISO29110-lite

`InitProj POC` continua candidato forte como fonte de uma capability/port pequeno porque possui comportamento executável e já conhecido.

`ISO29110-lite` continua candidato forte para testar uma capability normativa/metodológica porque força o FlowED a absorver referência externa e permitir providers alternativos.

Entretanto, nenhum deles deve ser declarado o “domínio hospedeiro” do outro.

## Próxima ação sugerida

Escolher uma operação mínima e desenhar primeiro:

- nome provisório da capability;
- port público;
- inputs;
- outputs;
- invariantes;
- estados/erros observáveis;
- contrato de compatibilidade;
- dois providers candidatos;
- CLI/YAML semanticamente equivalentes;
- teste de substituição.

Somente depois escolher qual implementação será usada como primeiro provider real.

## Evidência de dogfood

A tentativa anterior de escolher InitProj como primeiro piloto revelou que a arquitetura poderia absorver `ISO29110-lite` como profile e, com isso, criar acoplamento entre módulos horizontais que deveriam permanecer substituíveis por contrato.

A proposta foi corrigida antes da implementação. Este caso constitui evidência documental inicial de que o dogfood do protocolo consegue detectar e corrigir acoplamento conceitual durante a evolução da arquitetura.

Documento relacionado: `HORIZONTAL-MODULES-AND-PORTS-DRAFT.md`.
