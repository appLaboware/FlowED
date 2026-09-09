# Piloto — Contrato por exemplo para `flwd`

**Status:** Referência Experimental. Refinamento do piloto anteriormente descrito como “TDD”.

## 1. Correção conceitual

O objetivo do piloto não é usar Test-Driven Development como domínio do FlowED.

A intenção é aplicar **desenvolvimento guiado por contrato executável**, criando primeiro exemplos válidos de comandos e respostas para o cliente `flwd`, usando mocks/fakes, e somente depois implementar os produtores reais capazes de satisfazer o mesmo contrato.

O padrão de referência mais próximo é uma composição de:

- contract-first / API-first design;
- contract testing;
- consumer-driven contracts;
- contract by example;
- mocks/fakes como substitutos temporários do provider real.

A regra Adapt First exige tratar essa linha como adoção/composição de prior art, não como invenção metodológica própria.

## 2. Hipótese principal

> O contrato público do FlowED pode ser projetado e testado a partir do consumidor antes de existir qualquer implementação real do provider.

O `flwd` é o primeiro consumidor de referência desse contrato.

A execução inicial usa respostas mockadas conformes ao contrato. Depois, implementações reais são construídas e submetidas aos mesmos testes até produzirem respostas semanticamente equivalentes.

## 3. Sequência experimental

### Fase A — Definir interação pública

Para cada operação candidata, declarar:

- verbo;
- parâmetros posicionais quando realmente necessários;
- opções nomeadas;
- representação declarativa equivalente, quando aplicável;
- requisição canônica correspondente;
- respostas válidas;
- erros públicos válidos;
- invariantes observáveis;
- versão do contrato.

### Fase B — Criar mockup válido

Criar um mock/fake de provider que aceite a requisição canônica e devolva uma resposta válida segundo o contrato.

O mockup não tenta reproduzir implementação interna. Ele existe apenas para materializar comportamento público suficiente para testar o consumidor.

### Fase C — Testar `flwd`

O `flwd` deve conseguir:

1. receber verbo + parâmetros + opções;
2. validar a entrada;
3. convertê-la para a requisição canônica;
4. enviar a requisição ao provider mockado;
5. receber a resposta;
6. validar a resposta contra o contrato;
7. projetar a resposta corretamente ao usuário;
8. produzir comportamento de erro previsível quando a resposta for inválida.

Nesse estágio não existe dependência de provider real.

### Fase D — Congelar a primeira versão executável do contrato

Quando o consumidor consegue operar integralmente contra o mock, o conjunto de exemplos passa a funcionar como **especificação executável** da versão do contrato.

O contrato não é apenas documentação: ele deve poder ser executado como teste de compatibilidade.

### Fase E — Implementar o provider real

Somente então um provider real é desenvolvido ou adaptado.

O provider recebe as mesmas requisições usadas pelo mock e precisa produzir respostas que satisfaçam os mesmos testes de contrato.

A implementação é livre internamente.

### Fase F — Verificação de substituição

O teste decisivo é trocar:

`Mock Provider -> Provider Real A -> Provider Real B`

sem alterar a semântica do `flwd` nem os testes públicos do contrato.

Se o cliente precisar conhecer detalhes internos do provider, o contrato está insuficiente ou houve acoplamento indevido.

## 4. O que significa “resposta igual”

Não exigir igualdade byte a byte quando isso não fizer parte do contrato.

A equivalência deve ser **contratual/semântica**.

Exemplos:

- campos obrigatórios presentes;
- tipos corretos;
- estados públicos equivalentes;
- códigos/erros previstos;
- invariantes preservados;
- efeitos observáveis compatíveis;
- campos livres ou específicos do provider permitidos quando o contrato os admite.

Isso preserva personalidade própria das implementações.

## 5. Contrato por exemplo

Cada operação deve possuir pelo menos exemplos positivos e negativos.

Exemplo conceitual:

**Entrada CLI:**

`flwd <verbo> <parametro> --opcao valor`

**Requisição canônica:** representação estruturada equivalente.

**Resposta válida:** representação estruturada contendo somente as garantias públicas necessárias.

**Resposta inválida:** exemplo que viola o contrato e deve ser rejeitado pelo `flwd`.

A representação física inicial pode ser YAML/JSON + testes automatizados; a escolha definitiva ainda não está fechada.

## 6. Relação com a linguagem FlowED

Este piloto testa diretamente a hipótese:

**CLI / YAML / API / SDK / UI / agente -> mesma requisição semântica -> contrato público -> provider substituível**.

O `flwd` é apenas um cliente dessa língua.

O FlowED conceitual não precisa conhecer implementação interna do provider. Precisa conhecer apenas o contrato e os significados públicos.

## 7. Evidência produzida pelo piloto

O piloto deve produzir evidência separada para:

- capacidade do `flwd` de falar a língua FlowED;
- suficiência do contrato público;
- validade dos exemplos como especificação executável;
- capacidade de substituir mock por provider real;
- capacidade de substituir um provider real por outro;
- existência de vazamentos de detalhes internos para o consumidor.

## 8. Critérios de sucesso

O piloto é bem-sucedido quando:

1. o `flwd` funciona integralmente contra mocks definidos pelo contrato;
2. os mesmos testes verificam providers reais;
3. pelo menos dois providers estruturalmente distintos podem satisfazer o contrato;
4. a troca de provider não exige alterar o cliente nem a semântica pública;
5. respostas podem variar além do mínimo contratual;
6. erros incompatíveis são detectados automaticamente;
7. mudança incompatível de contrato exige versão nova ou mecanismo explícito de compatibilidade.

## 9. Determinismo relevante neste estágio

O foco é determinismo de **interpretação e verificação pública**:

- mesma entrada canônica e mesma versão de contrato -> mesma interpretação;
- mesma resposta -> mesmo resultado de validação;
- matching rules versionadas -> mesmo resultado de compatibilidade.

Determinismo interno da implementação fica fora do escopo salvo quando produzir comportamento observável prometido pelo contrato.

## 10. Dogfood

Este refinamento corrige a leitura anterior de “TDD” como domínio piloto.

O próprio debate mostrou que a intenção real era testar o FlowED de fora para dentro: primeiro o consumidor e seus contratos executáveis, depois os produtores reais.

Isso reduz acoplamento e aproxima o piloto de prior art consolidado de contract testing/consumer-driven contracts.

## 11. Próxima ação

Escolher uma operação mínima de `flwd` e criar quatro artefatos antes de qualquer provider real:

1. exemplo de comando CLI;
2. requisição canônica;
3. resposta válida + resposta inválida;
4. teste executável contra um mock provider.

Depois implementar o primeiro provider real e submetê-lo ao mesmo contrato.
