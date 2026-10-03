# EXP-005 — um comando Porter → site público no Azure

## Pergunta

Qual é a experiência máxima que Porter já entrega, sem uma camada IDEOS própria?

## UX testada

Depois do bootstrap de credenciais, a ação do usuário é um comando:

`porter install site -c azure-oidc --param site_name=<nome>`

O bundle já conhece:

- Azure como target;
- Resource Group do laboratório;
- região;
- imagem HTTP;
- porta pública;
- lifecycle de install/uninstall.

O usuário não escreve ARM, Bicep, Terraform ou comandos `az container create`.

## Materialização

O bundle usa somente recursos já existentes do Porter:

- parâmetros CNAB;
- credentials CNAB;
- mixin oficial `az`;
- Azure CLI contido na invocation image.

O target deste experimento é Azure Container Instances porque permite provar a UX com o menor número de decisões adicionais.

## Limite conscientemente preservado

Este bundle ainda é Azure-specific. Ele não prova seleção genérica de target.

A próxima comparação será verificar quanto precisa mudar para oferecer a mesma Application em Docker sem mudar a intenção do usuário.
