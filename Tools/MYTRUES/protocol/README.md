# MyTrues Open Decision Protocol — draft 0.2

## Modelo de interação

O cliente escolhe um **endpoint MyTrues de um fornecedor**.

### Caso conhecido

`POST /v1/decisions/resolve.failure`

Retorna `200 decided`.

### Caso desconhecido

O mesmo POST retorna:

`202 awaiting-provider-decision`

com:

- `decisionRequestId`;
- `statusUrl`;
- identidade pública do provedor;
- `casePacket` anonimizado;
- estado do pedido.

A execução chamadora deve persistir seu checkpoint e aguardar.

### Resolução humana

O fornecedor resolve o caso num sandbox sintético e registra:

`POST /v1/provider/decision-requests/{id}/resolution`

A decisão passa a pertencer ao MyTrues **daquele fornecedor**.

### Retomada

O cliente pode:

- consultar `GET /v1/decision-requests/{id}`; ou
- receber futuramente `mytrues.decision.resolved` via CloudEvents.

Quando o estado se torna `decided`, o processo retoma do checkpoint.

## Privacidade do caso

O pacote enviado ao fornecedor MUST NOT carregar secrets ou identificadores reais
necessários apenas à execução do cliente.

A implementação deve transformar o incidente em um caso técnico genérico.

Exemplos:

- domínio real -> `<domain>`;
- IP real -> `<ip>`;
- secret/token -> `<redacted>`;
- IDs de conta/subscription -> `<id>`.

Valores técnicos necessários ao raciocínio podem ser preservados, por exemplo
`runtime=php`, `database=mysql`, `missing_extension=pdo_mysql`.

O sandbox usa dados sintéticos/reservados.

## Semântica

`202` não representa falha terminal. Representa uma decisão ainda não disponível.

Um MyTrues conforme nunca fabrica uma ação apenas para evitar a pausa.
