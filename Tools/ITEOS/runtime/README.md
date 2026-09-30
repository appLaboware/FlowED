# Runtime containerizado

## Objetivo

Executar o laboratório ITEOS sem instalar Porter nem seus mixins no host.

O host precisa apenas de um Docker Engine compatível com Docker Compose.

## Topologia

O desenho inicial possui três papéis distintos:

1. **Container controlador ITEOS**
   - contém Porter CLI;
   - contém Docker CLI;
   - contém os mixins Porter usados pelo laboratório;
   - é descartável.

2. **Invocation containers**
   - são criados pelo Porter para executar bundles CNAB;
   - são específicos de cada bundle/ação;
   - podem ser efêmeros.

3. **Estado Porter**
   - Porter v1 usa por padrão o plugin `mongodb-docker`;
   - esse plugin cria o container `porter-mongodb-docker-plugin` e um volume Docker;
   - isso é adequado apenas para desenvolvimento/teste.

Todos usam o mesmo Docker Engine do host.

## Por que não Docker-in-Docker

O controlador não executa outro daemon Docker.

Ele usa o socket do Docker do host:

`/var/run/docker.sock`

Assim:

host Docker Engine
→ container ITEOS/Porter
→ invocation containers
→ infraestrutura/aplicações materializadas

## Uso previsto

A partir desta pasta:

`./iteos porter version`

`./iteos porter mixins list`

Para abrir um shell:

`./iteos bash`

Para executar o EXP-001:

`./iteos porter build --dir experiments/EXP-001-php-mysql`

Os comandos seguintes serão consolidados somente depois da primeira execução real.

## Segurança

Montar `/var/run/docker.sock` concede ao container controlador poder equivalente ao do Docker host. Neste laboratório isso é deliberado, pois Porter precisa construir imagens e iniciar invocation containers.

Isso não deve ser tratado como sandbox de segurança.

## Versões iniciais

- base: `docker:27-cli`
- Porter: `v1.1.0`
- mixins: `docker` e `docker-compose`

As versões serão fixadas/ajustadas após a primeira execução reproduzível.
