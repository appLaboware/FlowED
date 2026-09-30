# EXP-004 — uma Application, dois targets

## Hipótese

A camada inferior do IDEOS deve conseguir receber **um único contrato de aplicação** e materializá-lo em destinos diferentes sem transformar cada aplicação em um produto específico.

Neste experimento, `vitrine` é apenas uma instância da entidade genérica **Application**.

## Contrato único

`application.env` contém a definição usada pelos dois targets:

- identificador da aplicação;
- imagem;
- porta;
- conteúdo apresentado pela aplicação.

Não existe um manifesto Docker e outro manifesto Azure.

## Superfície de comando

A mesma interface é usada para os dois destinos:

`./materialize.sh deploy docker`

`./materialize.sh deploy azure`

O lifecycle também é simétrico:

`./materialize.sh verify <target>`

`./materialize.sh endpoint <target>`

`./materialize.sh destroy <target>`

## O que muda

Somente o materializador:

- `docker`: Docker Engine;
- `azure`: Azure Container Instances.

A Application permanece a mesma.

## Critério de aceite

O experimento passa somente se:

1. o target Docker servir HTTP com o conteúdo da Application;
2. o target Azure servir HTTP com o mesmo conteúdo;
3. ambos forem gerados a partir de `application.env`;
4. ambos puderem ser removidos pelo mesmo lifecycle.

## O que este experimento NÃO prova

Isto ainda não prova linguagem de intenção, resolução arquitetural ou conhecimento especializado.

Prova apenas a camada inferior:

**Application canônica → materializador selecionado → infraestrutura real**

Essa é a base sobre a qual as camadas de intenção poderão ser construídas sem acoplamento ao provider.
