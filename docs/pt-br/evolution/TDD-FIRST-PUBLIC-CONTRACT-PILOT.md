# Primeiro piloto de contrato público — TDD

**Status:** decisão experimental de trabalho; usada para fechar o núcleo conceitual do FlowED antes de expandir para outros domínios.

## 1. Decisão

O primeiro piloto concreto do modelo de contratos públicos do FlowED será **TDD — Test-Driven Development**.

A escolha substitui a tentativa anterior de iniciar por `InitProj POC` ou `ISO29110-lite` como primeiro recorte estrutural. Esses itens permanecem candidatos futuros, mas o objetivo imediato passa a ser testar o modelo conceitual do FlowED em uma prática amplamente conhecida, com múltiplas ferramentas e ecossistemas possíveis.

## 2. Por que TDD

TDD é adequado ao piloto porque:

- possui uma intenção metodológica reconhecível e independente de linguagem/ferramenta;
- pode ser materializado por stacks muito diferentes (`JUnit`, `pytest`, `Vitest`, `PHPUnit`, etc.);
- permite distinguir claramente contrato público de implementação;
- possui comportamento observável suficiente para testar a linguagem FlowED;
- é pequeno o bastante para não arrastar a arquitetura inteira de um sistema como InitProj;
- permite verificar se ferramentas distintas podem satisfazer a mesma semântica pública sem produzir artefatos idênticos;
- exerce progressividade: a primeira versão do contrato pode ser mínima e ganhar rigor conforme evidências e uso.

## 3. Escopo do piloto

O objetivo não é implementar um framework de TDD nem definir uma nova teoria de TDD.

O objetivo é usar TDD como **domínio/prática piloto para provar o contrato público do FlowED**.

O FlowED deve ser capaz de expressar, de forma independente da implementação, aquilo que precisa ser observável para considerar uma prática/materialização compatível com o contrato TDD declarado.

O contrato não deve impor detalhes internos como biblioteca, runner, IDE, linguagem, organização de arquivos ou estilo de mocks, salvo quando algum desses elementos for explicitamente parte do contrato de uma variante/perfil.

## 4. Hipótese arquitetural testada

> **FlowED se orienta conceitualmente por contratos públicos. Ferramentas e módulos concretos implementam esses contratos e podem variar livremente além do comportamento e dos artefatos observáveis exigidos.**

O piloto deve demonstrar que duas implementações distintas podem receber semanticamente a mesma requisição FlowED e satisfazer o mesmo contrato público sem o FlowED precisar conhecer seu funcionamento interno.

## 5. Primeira fatia do contrato TDD

A primeira versão deve ser propositalmente pequena. Em vez de tentar codificar todo TDD, ela deve declarar apenas um ciclo mínimo observável.

Hipótese inicial de ciclo contratual:

1. existe um comportamento/critério ainda não satisfeito;
2. existe uma verificação automatizada associada a esse comportamento;
3. a verificação pode demonstrar inicialmente o não atendimento;
4. uma alteração de implementação pode levar ao atendimento;
5. a verificação pode ser reexecutada e registrar o novo resultado;
6. o histórico/receipt preserva a sequência relevante de estados e resultados.

Essa formulação ainda é experimental e deve passar por Discovery antes de ser tratada como definição canônica de TDD.

## 6. O que o contrato público deve declarar

A primeira versão deve tentar limitar-se a:

- operação pública;
- parâmetros e opções semanticamente necessários;
- entradas obrigatórias;
- outputs/receipts observáveis;
- estados públicos relevantes;
- erros públicos;
- invariantes;
- capacidades/limitações declaradas;
- equivalência CLI/YAML/API;
- critérios mínimos de compatibilidade entre implementações.

Tudo que for detalhe interno da ferramenta/materializador fica fora do contrato.

## 7. Ferramentas como materializadores

Para o primeiro teste, duas implementações suficientemente diferentes devem satisfazer o mesmo contrato.

Exemplos candidatos:

- Java + JUnit;
- Python + pytest;
- JavaScript/TypeScript + Vitest/Jest;
- PHP + PHPUnit.

A seleção final não importa conceitualmente. O teste principal é substituição por contrato.

## 8. Critério de sucesso do piloto

O piloto será considerado suficientemente bem-sucedido para fechar o núcleo conceitual desta etapa do FlowED quando demonstrar que:

- `flwd`, YAML e API conseguem expressar a mesma requisição semântica;
- o contrato público é compreensível sem conhecimento da implementação;
- pelo menos duas implementações distintas conseguem satisfazê-lo;
- a troca de implementação não exige mudança na semântica pública;
- diferenças de personalidade/artefatos internos permanecem possíveis;
- receipts/erros públicos permitem verificar conformidade;
- detalhes internos de execução não precisam subir para o modelo conceitual do FlowED;
- o próprio dogfood gera gaps e refinamentos rastreáveis.

## 9. Relação com o fechamento do FlowED

TDD será usado como **último piloto estrutural desta fase conceitual**.

Após esse teste, a intenção é consolidar e fechar a primeira versão coerente do FlowED — manifesto, arquitetura conceitual, linguagem pública, contratos, governança epistemológica, progressividade e protocolo de evolução — antes de iniciar a modelagem de outros domínios/capabilities.

Esse fechamento não significa imutabilidade. Significa estabelecer um baseline versionado suficientemente estável para que novas expansões sejam tratadas como evolução do FlowED, e não como continuação indefinida de sua definição inicial.

## 10. Gaps que o piloto deve pressionar

- GAP-M004 — unidade primária da linguagem operacional;
- GAP-M005 — coordenação comum versus soberania dos domínios;
- GAP-M015 — liberdade governada;
- GAP-M021 — suficiência da classificação interna de requisições;
- GAP-M022 — vocabulário operacional transversal;
- GAP-M023 — contrato formal de determinismo;
- GAP-M024 — representação canônica/schema;
- granularidade e compatibilidade dos contratos públicos.

## 11. Dogfood

A própria escolha de TDD entra como referência experimental: surgiu como alternativa aos pilotos anteriores, foi avaliada pelo critério de baixo acoplamento e alto poder de pressão sobre os contratos públicos, e será mantida somente se o piloto realmente gerar evidência útil para o fechamento do FlowED.
