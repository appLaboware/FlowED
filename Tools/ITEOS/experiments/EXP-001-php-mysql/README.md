# EXP-001 — PHP + MySQL: local e Azure

## Pergunta

Uma aplicação PHP + MySQL existente pode ser materializada em destinos distintos sem modificar seu código-fonte?

## Hipótese

Porter/CNAB pode coordenar o lifecycle e delegar a materialização a ferramentas existentes.

## Aplicação de teste

A aplicação é propositalmente mínima:

- PHP;
- PDO MySQL;
- MySQL;
- variáveis de ambiente para conexão;
- contador persistido no banco.

Ela não contém conhecimento sobre Porter, Azure ou qualquer provedor.

## Critérios de aceitação

O experimento será considerado bem-sucedido se:

1. o mesmo diretório `app/` for usado nos dois destinos;
2. nenhuma alteração de código PHP for necessária entre local e Azure;
3. diferenças de infraestrutura ficarem fora da aplicação;
4. Porter controlar install e uninstall;
5. o resultado e as decisões manuais restantes forem documentados.

## Fase A — baseline local

Arquivos:

- `app/`: aplicação PHP.
- `docker-compose.yml`: materialização local.
- `porter.yaml`: bundle Porter inicial.

Fluxo esperado:

Porter → docker-compose mixin → Docker Compose → PHP + MySQL.

### Pré-requisitos

- Docker;
- Porter;
- mixins Porter `docker` e `docker-compose`.

### Comandos previstos

1. Instalar o mixin Docker.
2. Instalar o mixin Docker Compose.
3. Executar o bundle com acesso ao Docker host.
4. Abrir http://localhost:8080.
5. Executar uninstall.
6. Verificar remoção dos containers.

Os comandos exatos devem ser registrados após a primeira execução real, para evitar documentar sintaxe não validada.

## Fase B — Azure

Ainda não implementada.

A regra é não escolher prematuramente Azure Container Apps, ACI, VM ou Kubernetes.

Primeiro será levantada a alternativa aberta existente que permita materializar a mesma aplicação com o menor acoplamento possível. Porter já possui mixins `az`, Terraform e Kubernetes, que serão avaliados.

## Estado atual

- Estrutura do experimento: criada.
- Aplicação mínima: criada.
- Baseline Docker Compose: criado.
- Bundle Porter local: criado.
- Execução local: **não executada neste ambiente**, pois o runtime disponível para esta sessão não possui Docker.
- Azure: **pendente**.

## Evidência da limitação do ambiente da sessão

Na criação deste experimento, `docker --version` e `docker compose version` retornaram comando inexistente. Portanto nenhum resultado de execução foi inventado.

## Próximo passo

Executar a Fase A em uma máquina com Docker e Porter. Somente após observar o comportamento real será iniciada a Fase B.
