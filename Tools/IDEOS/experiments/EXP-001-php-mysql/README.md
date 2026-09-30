# EXP-001 — PHP + MySQL: baseline local

## Pergunta

Uma aplicação PHP + MySQL existente pode ser materializada sem instalar Porter no host e sem modificar o código da aplicação?

## Fluxo

Docker host
→ container controlador IDEOS
→ Porter
→ invocation container CNAB
→ Docker Compose
→ PHP + MySQL

## Preparação

A imagem da aplicação é construída pelo controlador e registrada no Docker Engine do host:

`./runtime/ideos docker build -t ideos-exp001-web:local experiments/EXP-001-php-mysql/app`

Depois Porter constrói e instala o bundle:

`./runtime/ideos porter build --dir experiments/EXP-001-php-mysql`

`./runtime/ideos porter install ideos-exp001 --file experiments/EXP-001-php-mysql/porter.yaml --allow-docker-host-access`

A aplicação deve responder em:

`http://localhost:18080`

## Critérios

1. Porter não está instalado no host.
2. O mesmo código PHP é usado sem alteração.
3. Porter controla install/uninstall.
4. A aplicação continua funcionando após o container controlador terminar.
5. Uninstall remove a materialização local.
