# Runtime containerizado do IDEOS

## Objetivo

Executar Porter e seus mixins sem instalar Porter no host.

Pré-requisito do host:

- Docker Engine;
- Docker Compose.

## Topologia validada neste experimento

Docker Engine do host
→ container controlador IDEOS
→ Porter
→ invocation containers CNAB
→ aplicação/infraestrutura materializada

O controlador usa o socket `/var/run/docker.sock`; não há Docker-in-Docker.

## Estado Porter

Neste primeiro proof usamos deliberadamente o storage padrão do Porter v1: `mongodb-docker`.

Porter cria:

- container `porter-mongodb-docker-plugin`;
- volume `porter-mongodb-docker-plugin-data`.

Como o Porter está dentro do controlador e o MongoDB padrão publica em localhost, o experimento Linux usa `network_mode: host`.

Isto é uma escolha de laboratório, não uma decisão de portabilidade final. Windows/macOS serão tratados depois, somente se o proof Linux passar.

## Versões

- Porter: v1.6.1
- docker mixin: v1.0.6
- docker-compose mixin: v1.0.6

## Segurança

Montar o socket Docker concede ao controlador autoridade equivalente ao Docker host. Isso é necessário para Porter criar invocation containers e materializações locais.
