# EXP-003 — mesma aplicação para Azure

## Objetivo

Medir até onde a composição existente consegue levar a mesma aplicação PHP + MySQL do EXP-001 para Azure, evitando criar abstrações próprias.

## Regra

Começar pelo mecanismo mais direto já existente no Azure:

`az containerapp compose create`

O comando Azure é GA e aceita um arquivo Docker Compose.

Não será criado Terraform, Bicep ou adapter próprio antes de provar que o caminho direto é insuficiente.

## Autenticação

O bootstrap usa `az login --use-device-code` dentro do container oficial Azure CLI.

O cache resultante permanece em `$HOME/.azure` no host e é montado somente para leitura no container controlador IDEOS.

Porter injeta os arquivos necessários no invocation container através de credentials CNAB:

- `azureProfile.json`
- `msal_token_cache.json`

Nenhuma senha ou token Azure é versionado.

## Primeiro alvo

Subdomínio reservado para o experimento: `ideos.me.dev.br`.

DNS só será alterado depois que a Azure fornecer um endpoint real.

## Fronteiras que queremos observar

- se Azure consegue consumir diretamente o Compose;
- se precisa de registry;
- se cria ou exige Container Apps Environment;
- como trata MySQL e volume;
- o que Porter resolve;
- o que ainda precisa ser declarado por nós.
