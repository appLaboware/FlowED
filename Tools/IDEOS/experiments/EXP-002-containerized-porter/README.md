# EXP-002 — Porter dentro do container controlador

## Pergunta

É possível deixar o host responsável somente por Docker/Docker Compose e executar Porter, seus mixins e seu estado auxiliar em containers?

## Critérios

1. Porter não está instalado no host.
2. `porter version` funciona no controlador.
3. O controlador acessa o Docker Engine do host.
4. Porter usa MongoDB containerizado para estado.
5. Porter cria invocation containers.
6. O EXP-001 é instalado e removido por esse runtime.
