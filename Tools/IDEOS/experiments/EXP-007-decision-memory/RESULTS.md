# RESULTS — EXP-007 Decision Memory

## Execução validada

GitHub Actions run:

- ID: `36806662068`
- resultado: **success**

## Caso 1 — Azure secrets separados ausentes

Erro observado:

`azure.credentials.separate_missing`

DecisionPort retornou:

- decision: `decision.azure.parse_legacy_bundle`
- action: `azure.credentials.parse_legacy_bundle`
- guard: `legacy_azure_bundle_present=true`
- automation: `automatic`
- risk: `low`
- execution allowed: `true`

A execução extraiu os três identificadores do secret legado `AZURE` e continuou.

## Caso 2 — DNS customizado sem credenciais

Erro observado:

`dns.requested_provider_credentials_missing`

DecisionPort retornou:

- decision: `decision.dns.use_azure_provider_fqdn`
- action: `delivery.use_azure_provider_fqdn`
- guard: `azure_provider_fqdn_available=true`
- automation: `automatic`
- risk: `low`
- execution allowed: `true`

O domínio solicitado não foi fingido nem silenciosamente ignorado.

O usuário foi informado de que o domínio customizado não pôde ser configurado e
o fluxo continuou com hostname fornecido pela Azure.

## Resultado materializado

Porter retomou a intenção original após as duas adaptações.

Resultado:

`http://decision-site-36806662068.brazilsouth.azurecontainer.io`

O endpoint respondeu HTTP com sucesso.

## Retain

As duas decisões registraram resultado positivo dentro da memória da execução:

- `decision.azure.parse_legacy_bundle`: successCount=1, failureCount=0
- `decision.dns.use_azure_provider_fqdn`: successCount=1, failureCount=0

## O que foi provado

`failure -> expose -> retrieve -> guard -> approved action -> adapt -> continue -> verify -> retain`

Nenhuma similaridade vetorial autorizou uma ação.

O índice vetorial existe para futura descoberta de casos candidatos, mas as duas
resoluções desta rodada foram feitas por match determinístico de código de falha.

## Limite atual

O container Neo4j desta execução é efêmero.

Portanto:

- decisões aprovadas estão persistidas como código em `seed.cypher`;
- observações de outcome foram retidas durante a execução;
- contadores e novos casos observados ainda não sobrevivem a outro runner.

Persistência cross-run deve ser tratada em experimento separado antes de chamar o
mecanismo de aprendizado operacional persistente.

## Regra de segurança emergente

Conhecimento recuperado por similaridade pode sugerir candidatos.

Somente decisões:

- com identidade explícita;
- `status=approved`;
- `automation=automatic`;
- risco permitido;
- guardas satisfeitas;

podem produzir ação automática.
