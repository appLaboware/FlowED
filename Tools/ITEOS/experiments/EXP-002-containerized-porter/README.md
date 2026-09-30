# EXP-002 — Porter executado dentro do container controlador

## Pergunta

É possível deixar o host responsável somente pelo Docker e executar Porter, seus mixins e o laboratório ITEOS dentro de um container controlador?

## Topologia sob teste

Docker Engine no host
→ container controlador ITEOS
→ Porter
→ invocation container do bundle
→ materialização

O container controlador utiliza o Docker Engine do host pelo socket Unix. Não há Docker-in-Docker.

## Critérios de aceitação

1. Porter não está instalado no host.
2. O host possui somente Docker/Docker Compose como pré-requisito do laboratório.
3. `porter version` funciona dentro do controlador.
4. O controlador consegue acessar o Docker Engine do host.
5. Porter consegue criar e executar uma invocation image.
6. O EXP-001 pode ser controlado a partir deste runtime.
7. O container controlador pode ser removido sem remover a infraestrutura já materializada.

## Estado

Implementação preparada, ainda não executada neste ambiente.

O ambiente desta sessão não possui Docker disponível, portanto a validação deverá ser feita em um host Docker real.

## Observação sobre estado

Porter v1 usa por padrão MongoDB em container para persistir seu próprio estado em desenvolvimento. Isso significa que o teste poderá mostrar, além do controlador e da invocation image, o container `porter-mongodb-docker-plugin`.

Ele não faz parte da aplicação materializada; é armazenamento de estado do Porter.

## Próxima execução

1. Construir o controlador.
2. Executar `porter version`.
3. Confirmar acesso ao Docker com `docker version`.
4. Executar um bundle Porter mínimo.
5. Executar EXP-001.
6. Remover o controlador.
7. Verificar se a aplicação materializada continua funcionando.
8. Registrar todos os containers, volumes e artefatos realmente criados.
