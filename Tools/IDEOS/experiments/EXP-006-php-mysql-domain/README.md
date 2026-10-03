# EXP-006 — artefato PHP + MySQL + domínio próprio

## Intenção observável

O usuário fornece:

- um artefato de aplicação;
- um nome;
- um domínio.

Não fornece uma receita Azure.

## Comando alvo

`porter install site -c cloud --param app=./site.tar.gz --param site_name=<nome> --param domain=<domínio>`

## O que o bundle sabe

Somente propriedades técnicas:

- o artefato é uma aplicação PHP;
- existe uma dependência MySQL;
- o destino deste bundle é Azure;
- o domínio está em Cloudflare.

Não existe conceito de WordPress.

## Materialização desta prova

A aplicação e o banco são dois containers no mesmo Azure Container Instance group.

A aplicação recebe o arquivo passado como parâmetro CNAB e o executa em PHP.

O MySQL não é exposto publicamente.

Cloudflare recebe um CNAME DNS-only apontando para o FQDN criado pela Azure.

## Limitação deliberada

Para manter o experimento pequeno, o artefato é transferido para o container como base64 e o MySQL usa armazenamento efêmero.

Isso não é desenho de produção e não serve para artefatos grandes como um WordPress completo.

O objetivo desta rodada é medir a UX de materialização. O passo seguinte deve substituir o transporte do artefato por uma solução existente de build/registry, preferencialmente `az containerapp up --source`/Buildpacks, sem alterar a intenção do usuário.
