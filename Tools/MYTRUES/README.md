# MyTrues

MyTrues é um ensaio de um produto geral de **decisão operacional assistida por memória**.

A fronteira do produto é deliberada:

- **protocolo aberto**: qualquer projeto pode solicitar e consumir decisões sem depender da implementação MyTrues;
- **engine substituível**: o algoritmo que recupera, organiza, ranqueia e escolhe decisões fica atrás de uma porta interna;
- **execução fora do MyTrues**: MyTrues decide; o chamador continua responsável por executar a ação e reportar o resultado.

## Origem

O protótipo foi promovido a partir do experimento
`Tools/IDEOS/experiments/EXP-007-decision-memory`.

O EXP-007 permanece como evidência histórica do primeiro ciclo validado:

`failure -> expose -> retrieve -> guard -> decide -> adapt -> continue -> verify -> retain`

## Fronteira pública x proprietária

```
project
   |
   | MyTrues Open Decision Protocol
   v
+---------------------------+
| MyTrues Decision Service  |
|                           |
| protocol adapter          |  <- aberto
| conformance               |  <- aberto
| DecisionEngine port       |  <- aberta a interface
|        |                  |
|        v                  |
| proprietary engine        |  <- substituível / não faz parte do protocolo
|        |                  |
| decision memory adapter   |
+---------------------------+
```

A implementação em `reference/` existe somente para testar o protocolo.
Os engines de exemplo são fixtures transparentes de conformidade e NÃO representam
o futuro algoritmo proprietário do produto.

## Dois MyTrues, mesmo protocolo

O laboratório sobe duas instâncias que recebem **a mesma requisição**:

- `mytrues-fqdn`: prefere devolver o hostname fornecido pela Azure;
- `mytrues-ip`: prefere devolver o IP público da mesma aplicação.

O cliente não muda.

Somente o engine atrás da porta muda.

Isso demonstra a propriedade central:

> o protocolo define como pedir e receber uma decisão; o algoritmo define qual decisão é melhor.

## Padrões adotados

MyTrues não cria do zero aquilo que já possui padrão maduro:

- OMG DMN 1.5 — vocabulário e conceitos de decisão/decision service;
- HTTP + JSON;
- OpenAPI 3.1 — contrato de API;
- RFC 9457 — erros HTTP estruturados;
- W3C Trace Context — correlação distribuída;
- CloudEvents 1.0 — eventos assíncronos opcionais.

O protocolo MyTrues é uma composição pequena desses padrões para o caso operacional
de decisão, não uma substituição deles.
