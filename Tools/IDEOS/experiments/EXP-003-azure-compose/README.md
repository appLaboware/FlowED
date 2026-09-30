# EXP-003 — mesma aplicação para Azure

## Objetivo

Medir até onde a composição existente consegue levar a mesma aplicação genérica do laboratório para Azure, evitando criar abstrações próprias antes de provar que são necessárias.

WordPress não é o produto nem a abstração. Quando usado, é somente uma aplicação de teste. O contrato a ser perseguido é **Application → target**, de modo que a mesma aplicação possa ser materializada em destinos diferentes.

## Regra

Começar pelo mecanismo mais direto já existente no Azure e só introduzir novas abstrações quando houver evidência de que a composição disponível é insuficiente.

## Bootstrap de confiança

O portal Azure não faz parte do fluxo operacional do produto. Ele foi usado apenas para observar e estabelecer a confiança inicial.

O estado esperado é:

1. App Registration `FlowED-GitHub-Actions`;
2. credencial federada GitHub OIDC limitada a `appLaboware/FlowED` e à branch `tools/ideos-lab`;
3. Resource Group `rg-flowed-ideos-lab`;
4. função built-in `Contributor` limitada a esse Resource Group.

A atribuição RBAC é automatizada por:

`Tools/IDEOS/experiments/EXP-003-azure-compose/bootstrap-rbac.sh`

O script é idempotente: verifica o estado antes de criar a atribuição.

## Autenticação operacional

GitHub Actions usa OIDC. Não há `az login --use-device-code`, cache de token persistente nem `client_secret` Azure no repositório.

O workflow `.github/workflows/ideos-azure-auth.yml` requer estes GitHub Actions secrets:

- `AZURE_CLIENT_ID`
- `AZURE_TENANT_ID`
- `AZURE_SUBSCRIPTION_ID`

Eles são identificadores; não são o token de acesso. O token Azure é efêmero e obtido durante cada execução pela federação OIDC.

## Critério de aceite da autenticação

O workflow só passa se:

- GitHub obtiver identidade Azure por OIDC;
- a assinatura puder ser consultada;
- `rg-flowed-ideos-lab` puder ser lido;
- a identidade possuir `Contributor` nesse escopo.

## Próxima fronteira

Depois do probe OIDC, a próxima entrega é materialização real e reversível:

1. criar uma aplicação mínima no target Azure;
2. obter endpoint;
3. validar HTTP;
4. destruir os recursos criados;
5. repetir com a mesma Application em outro target.

Nenhuma etapa repetível deve depender do portal.
