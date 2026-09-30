# 001 — aplicação PHP + MySQL genérica

## Entrada

O diretório `app/` contém apenas código PHP.

Ele não contém:

- Dockerfile;
- Porter;
- CNAB;
- Azure;
- conhecimento de produto específico.

O bundle declara apenas que esse código será executado em PHP/Apache e que a aplicação depende de MySQL.

## Fluxo

Porter
→ docker mixin
→ build da imagem PHP
→ docker-compose mixin
→ PHP + MySQL

## Lifecycle

- install: build + materialização;
- upgrade: rebuild + recreate;
- uninstall: remoção de containers, rede e volume.

## Critério de aprovação

O teste passa somente se:

1. Porter construir a imagem a partir do código PHP;
2. Porter materializar PHP e MySQL;
3. HTTP responder;
4. banco persistir entre duas requisições;
5. upgrade funcionar;
6. uninstall remover os recursos da aplicação.
