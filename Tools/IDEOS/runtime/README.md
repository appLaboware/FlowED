# Runtime containerizado do IDEOS

## Objetivo

Executar Porter e seus componentes sem instalar Porter no host.

Pré-requisito do host:

- Docker Engine;
- Docker Compose.

## Componentes

### Container controlador IDEOS

Contém:

- Porter CLI;
- Docker CLI;
- mixin Docker;
- mixin Docker Compose;
- plugin MongoDB do Porter.

### MongoDB

Mantém o estado administrativo do Porter para o laboratório.

### Invocation containers

São criados pelo Porter para executar ações CNAB. São separados do controlador e podem ser efêmeros.

## Uso

A partir de `Tools/IDEOS/runtime`:

`./ideos porter version`

`./ideos docker version`

`./ideos porter mixins list`

`./ideos porter plugins list`

## Segurança

O socket `/var/run/docker.sock` concede ao controlador autoridade equivalente à do Docker host.

Isto é intencional no laboratório e não deve ser confundido com isolamento de segurança.
