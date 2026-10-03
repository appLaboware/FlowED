# EXP-007 — Decision Memory / self-healing control loop

## Hipótese

Falhas conhecidas não devem necessariamente quebrar a intenção do usuário.

O sistema pode:

1. observar e normalizar o erro;
2. expor o erro;
3. consultar uma memória de decisões;
4. selecionar somente uma decisão previamente aprovada;
5. verificar guardas determinísticas;
6. aplicar uma adaptação permitida;
7. continuar ou repetir a execução;
8. registrar o resultado para aprendizado operacional.

## Base adotada

### Case-Based Reasoning

O ciclo adotado é compatível com CBR:

- retrieve;
- reuse;
- revise;
- retain.

A primeira versão NÃO aprende novas ações executáveis sozinha.

Novas observações podem ser retidas, mas uma decisão precisa ser promovida para
`status=approved` antes de permitir execução automática.

### Microsoft

São usados como referências:

- Decision-Theoretic Case-Based Reasoning — troubleshooting representado por problemas,
  causas, sintomas e reparos;
- Microsoft GraphRAG — referência para memória estruturada em grafo e recuperação;
  não é usado como autoridade de execução.

### Grafo + vetor

Neo4j Community é usado como memória única:

- grafo: fonte de verdade de falhas, decisões, guardas, ações e evidências;
- índice vetorial: mecanismo de recuperação futura para casos desconhecidos.

Regra fundamental:

> vector retrieves; approved graph decisions authorize.

Similaridade vetorial jamais executa reparo diretamente.

## Casos desta rodada

### Caso 1 — Azure secrets no formato legado

Erro:

`azure.credentials.separate_missing`

Condição:

- secrets separados não existem;
- `AZURE` legado contém as três chaves.

Decisão:

`decision.azure.parse_legacy_bundle`

Ação:

`azure.credentials.parse_legacy_bundle`

Resultado esperado:

- erro é registrado;
- decisão é recuperada;
- três valores são extraídos;
- OIDC prossegue;
- ciclo não quebra.

### Caso 2 — domínio prometido sem credencial DNS

Erro:

`dns.requested_provider_credentials_missing`

Condição:

- foi solicitado domínio customizado;
- credenciais DNS não existem;
- Azure consegue fornecer hostname próprio.

Decisão:

`decision.dns.use_azure_provider_fqdn`

Ação:

`delivery.use_azure_provider_fqdn`

Resultado esperado:

- erro é registrado;
- domínio customizado não é fingido;
- deployment continua;
- usuário recebe hostname Azure e aviso explícito;
- ciclo termina como sucesso com fallback.

## Porta

`decision_port.py` é deliberadamente pequeno e representa a fronteira:

`resolve(failure, context) -> decision`

A implementação Neo4j é um adapter do laboratório; o chamador não deve depender da
topologia interna do banco.
