# Draft — Módulos Horizontais e Ports no FlowED

**Status:** decisão conceitual provisória em simulação.

## 1. Correção arquitetural

O FlowED ocupa a esfera superior de coordenação e linguagem operacional. Abaixo dele existem **módulos horizontais pares**, cada um responsável por uma área/capability da Engenharia de Software.

A ligação entre FlowED e esses módulos não deve ocorrer por conhecimento direto da implementação concreta, mas por **ports com contratos públicos**.

Consequência: uma capability atendida pelo FlowED não deve depender de um módulo específico. O FlowED depende do contrato do port; módulos concretos entram e saem como providers/materializadores desse contrato.

## 2. Regra de substituição

Se dois módulos satisfazem o mesmo port, ambos podem atender a mesma intenção FlowED, ainda que produzam resultados com personalidade, estrutura interna ou artefatos próprios.

A substituição é válida quando o módulo preserva:

- semântica pública do port;
- inputs e outputs obrigatórios;
- invariantes e constraints;
- estados/erros observáveis definidos pelo contrato;
- rastreabilidade e receipts exigidos;
- capabilities e limitações declaradas;
- versionamento compatível do contrato.

O contrato não deve padronizar o resultado além do necessário para interoperabilidade. Personalidade própria do provider é permitida e desejável quando não viola o port.

## 3. Exemplo conceitual

`ISO29110-lite` não deve ser acoplado ao `InitProj` nem tratado automaticamente como profile interno dele.

Se ambos pertencem a esferas/capabilities diferentes, cada um se liga ao FlowED por seus próprios ports. Se `ISO29110-lite` e outro módulo puderem atender a mesma necessidade normativa/metodológica, ambos devem implementar o mesmo port dessa capability e permanecer substituíveis.

Assim:

**FlowED → Port da capability → Provider A / Provider B / Provider C**

O FlowED conhece o port. O provider conhece sua própria materialização.

## 4. Relação horizontal e vertical

- **Horizontal:** capabilities/domínios pares que ampliam a cobertura do FlowED.
- **Port:** contrato estável que expressa o que aquela capability oferece ao FlowED e/ou consome de outras capabilities.
- **Provider/materializador:** implementação concreta que satisfaz um port.
- **Adapter:** tradução entre o contrato do port e tecnologia/produto/protocolo externo quando necessário.

Um mesmo módulo pode oferecer mais de um port e consumir ports de outras capabilities, mas dependências devem continuar explícitas e contratuais.

## 5. Não acoplamento entre módulos

Módulos horizontais não devem conhecer diretamente implementações irmãs quando a interação puder ser expressa por um port.

A regra candidata é:

> **FlowED e seus módulos dependem de contratos; implementações concretas são substituíveis atrás dos ports.**

Acoplamento direto só deve existir quando houver residual demonstrado e documentado.

## 6. Consequência para a linguagem FlowED

A língua pública do FlowED continua comum. `flwd`, YAML, API, SDK, UI e agentes expressam a mesma requisição semântica.

O roteamento decide qual port atende à requisição e qual provider materializa aquele port no contexto atual.

Portanto, a unidade pública não deve codificar o nome do provider salvo quando o usuário explicitamente restringir a materialização.

Exemplo conceitual:

- intenção: executar uma capability de processo leve;
- port: contrato daquela capability;
- provider escolhido: `ISO29110-lite`, outro framework ou implementação própria;
- resultado: pode ter personalidade própria, desde que preserve o contrato observável.

## 7. Implicação para o primeiro piloto

O primeiro piloto não deve começar por “colar ISO29110-lite ao InitProj”.

Deve começar por escolher **um port pequeno e real**, definir seu contrato e então implementar pelo menos dois providers simples ou um provider + fake/reference implementation. O teste central passa a ser substituição sem alterar a linguagem pública nem o consumidor.

`InitProj POC` ainda pode ser um bom provider/capability de teste, mas não deve hospedar conceitualmente outras capabilities que pertencem à esfera horizontal do FlowED.

## 8. Gaps afetados

- GAP-M004: a linguagem comum deve rotear para ports, não para implementações.
- GAP-M005: a fronteira entre coordenação e soberania ganha forma contratual.
- GAP-M015: liberdade governada passa a incluir substituição por contrato.
- novo gap candidato: definir granularidade correta de port/capability e critérios de compatibilidade entre providers.

## 9. Dogfood

Esta correção surgiu ao tentar selecionar o primeiro piloto. O próprio teste revelou acoplamento indevido na hipótese anterior. A decisão foi corrigida antes da implementação, preservando a linhagem da proposta substituída.
