# Resultados — EXP-001

## Resultado

**APROVADO em 2026-09-30.**

Execução validada no GitHub Actions:

- workflow: `IDEOS laboratory`;
- run: https://github.com/appLaboware/FlowED/actions/runs/36769533522;
- job: `porter-containerized-runtime`;
- conclusão: `success`.

## Ambiente observado

- host: Ubuntu 24.04.5 LTS;
- Docker Engine host: 28.0.4;
- Docker Compose host: 2.38.2;
- Docker CLI no controlador: 27.5.1;
- Porter: 1.6.1;
- mixin `docker`: 1.0.6;
- mixin `docker-compose`: 1.0.6.

## Evidências

1. A imagem controladora IDEOS foi construída com sucesso.
2. Porter executou de dentro do container controlador.
3. A imagem PHP foi construída pelo controlador usando o Docker Engine do host.
4. O bundle CNAB foi construído com sucesso.
5. `porter install` criou:
   - `ideos-exp001-db`;
   - `ideos-exp001-web`;
   - rede Docker;
   - volume MySQL.
6. MySQL atingiu estado `healthy` antes da aplicação web iniciar.
7. Após o container controlador terminar, a aplicação continuou ativa.
8. O teste HTTP retornou:
   - `IDEOS EXP-001`;
   - `Aplicação PHP + MySQL ativa.`;
   - `Visitas persistidas: 1`.
9. `porter uninstall` removeu:
   - container web;
   - container MySQL;
   - volume MySQL;
   - rede da aplicação.
10. A verificação final confirmou ausência dos containers da aplicação.

## Conclusão

Foi comprovado que Porter pode ser executado dentro do container controlador IDEOS e materializar uma aplicação PHP + MySQL no Docker host sem Porter instalado diretamente no host.

A aplicação materializada permanece independente do container controlador durante sua execução.

## Limitações observadas

### Socket Docker

Porter executa invocation images como usuário não-root. No runner utilizado, o socket Docker não era acessível a esse usuário.

Para concluir o experimento, o workflow concedeu explicitamente acesso ao socket antes da instalação.

Isso é aceitável como prova experimental, mas **não é a solução final de segurança**. Deve ser substituído por mecanismo mais restrito, como ACL específica, proxy do Docker API ou outra fronteira de autorização.

### Tamanho da invocation image

A invocation image observada ficou grande, pois o contexto de build inclui mais conteúdo do que o necessário.

Isso é uma questão de empacotamento/otimização, não uma falha funcional, e deverá ser reduzido em experimento posterior.
