# Resultados — EXP-002

## Resultado

**APROVADO em 2026-09-30.**

Workflow validado:

https://github.com/appLaboware/FlowED/actions/runs/36769533522

Todas as etapas do job `porter-containerized-runtime` concluíram com sucesso.

## Propriedades comprovadas

1. Porter não precisou ser instalado diretamente no host.
2. O host forneceu Docker Engine/Docker Compose.
3. O container controlador IDEOS executou Porter 1.6.1.
4. O controlador acessou o Docker Engine do host.
5. Porter construiu e executou invocation image CNAB.
6. A invocation image materializou PHP + MySQL via Docker Compose.
7. O container controlador terminou e a aplicação permaneceu ativa.
8. Porter voltou a ser invocado posteriormente para executar uninstall.
9. A infraestrutura da aplicação foi removida corretamente.

## Estado administrativo do Porter

Durante o teste, Porter criou `porter-mongodb-docker-plugin` para seu estado administrativo.

Esse container permaneceu após o uninstall da aplicação, como esperado, porque pertence ao runtime administrativo do Porter e não à materialização PHP + MySQL.

## Conclusão

A topologia abaixo foi comprovada funcional:

Docker Engine do host
→ container controlador IDEOS
→ Porter
→ invocation container CNAB
→ Docker Compose
→ aplicação materializada

Não foi necessário manter o container controlador IDEOS executando após a materialização.


## Limite de licenciamento posterior

O fato de `porter-mongodb-docker-plugin` ter funcionado no laboratório continua sendo
evidência histórica válida.

A revisão de banca de 2026-10-01 marcou o caminho MongoDB 8.0/SSPL transitivo como
**VERMELHO** para baseline de produto.

Portanto:

- EXP-002 não aprova esse storage administrativo para produção;
- R1 deve esgotar/configurar storage oficial alternativo com licença aceitável;
- upstream permanece imutável;
- nenhum fork local é autorizado enquanto configuração/plugin oficial puder resolver.
