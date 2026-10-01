# EXP-005 — GRyCAP Infrastructure Manager

## Objetivo

Replicar o experimento anterior com um produto científico aberto diferente do Porter.

Produto avaliado: **GRyCAP Infrastructure Manager (IM)**.

Hipótese:

> Dada uma aplicação PHP simples e uma conta Azure já existente, quanto o IM realmente abstrai até entregar infraestrutura utilizável?

Este experimento não tenta adaptar o IM ao IDEOS. Primeiro ele deve ser usado conforme foi projetado.

## O que o produto declara fazer

O IM automatiza seleção de imagem, deployment, configuração, instalação de software, monitoramento e atualização de infraestrutura em múltiplos provedores.

Ele possui:

- serviço IM;
- cliente CLI oficial;
- descrição de infraestrutura via RADL/TOSCA;
- conector Azure.

## Experimento

### Fase A — produto executável

Subir o container oficial `grycap/im`, verificar que o serviço inicia e executar o cliente oficial `ghcr.io/grycap/im-client`.

Critério: o software precisa iniciar sem nenhuma implementação nossa.

### Fase B — fronteira Azure

Usar a autenticação que o produto realmente suporta.

A documentação atual do `im-client` define para Azure:

- `subscription_id + username + password`; ou
- no conector Azure atual, `subscription_id + client_id + secret + tenant`.

Nosso laboratório Azure atual usa **GitHub OIDC**, portanto possui `client_id`, `tenant_id` e `subscription_id`, mas não possui `client_secret`.

Isto é deliberadamente registrado como dado do experimento: não criaremos um secret permanente apenas para fazer o produto parecer mais automático.

### Fase C — aplicação

Somente depois da autenticação compatível será criado um RADL/TOSCA mínimo para publicar uma aplicação PHP e obter uma URL.

## Critério IDEOS

O IM só vence este experimento conceitualmente se conseguir partir de uma intenção equivalente a:

> publique este site PHP na Azure

e resolver automaticamente os detalhes necessários até entregar uma URL.

Se exigir que o usuário forneça uma descrição técnica de infraestrutura e credenciais específicas do provider, isso será registrado como fronteira do produto, não como falha de instalação.

## Resultado esperado

O experimento deve separar claramente:

1. o que o IM resolve;
2. o que precisa ser previamente configurado;
3. o que ainda precisa ser informado por um especialista;
4. o que impede intenção → materialização.
