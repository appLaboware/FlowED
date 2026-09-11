# FlowED — Coordenação multiagente via repositório

**Status:** protocolo operacional experimental inspirado no InitProj.
**Escopo:** coordenação entre o chat original (PO), a branch paralela de revisão do manifesto e o worker de materialização do CCP.
**Autoridade filosófica final:** humano.

## 1. Atores

| ID | Papel | Missão principal | Prefixo obrigatório de commit |
|---|---|---|---|
| `PO-001` | Chat original / PO | coordenar as duas frentes, observar convergências, orientar CCP/materialização e integrar aprendizados | `[PO-001]` |
| `MAN-001` | Branch paralela derivada do chat original | continuar a revisão do Manifesto FlowED; incorporar o protocolo BASE/REDUCT-MAX/DEFESA nas novas proposições | `[MAN-001]` |
| `WRK-001` | Worker CCP/POC | construir a POC vertical do materializador CCP sem redefinir a filosofia nem revisar o manifesto | `[WRK-001]` |

O fato de todos usarem a mesma conexão GitHub torna o autor Git insuficiente para distinguir agentes. **O prefixo no assunto do commit é obrigatório a partir deste bootstrap.**

## 2. Regra de comunicação

A coordenação deve depender do repositório, não de cópia manual de mensagens pelo humano.

Cada ator, antes de iniciar um ciclo de trabalho:

1. consulta os commits mais recentes desta branch;
2. identifica commits dos demais atores pelo prefixo;
3. lê o próprio `INBOX/`;
4. abre os arquivos alterados por outro ator somente quando tocarem seu domínio;
5. executa sua missão;
6. registra a entrega ou estado no próprio `OUTBOX/` quando houver informação útil aos demais;
7. faz commit com seu prefixo de ator.

Mensagens entre atores são arquivos. Um ator pode criar uma nova mensagem dentro do `INBOX/` de outro ator. Não sobrescrever mensagens anteriores.

## 3. Fronteiras de responsabilidade

### `PO-001`

- coordena o mecanismo de materialização do CCP;
- observa o trabalho de `MAN-001` apenas pelo ângulo de CCP, projeções, layouts, adapters, cognição mínima, monotonicidade, proveniência e materialização;
- orienta `WRK-001` e avalia sua POC;
- não substitui o humano em decisões filosóficas do FlowED;
- não reescreve proposições do manifesto que estão sob trabalho de `MAN-001`, salvo decisão explícita do humano.

### `MAN-001`

- continua o trabalho já em curso no manifesto;
- mantém autonomia editorial/conceitual dentro das decisões do humano;
- para novas proposições, registra o agrupamento `BASE → reduções intermediárias → REDUCT-MAX → DEFESA` quando aplicável;
- comunica por commit e `OUTBOX/` descobertas que possam interessar ao materializador CCP;
- não precisa aguardar respostas do PO para continuar a revisão ordinária.

### `WRK-001`

- constrói uma POC vertical executável;
- ponto de partida: `fonte preservada → marcação → CCP estruturado → contrato de projeção → adapter → artefato compilado`;
- primeira demonstração: múltiplas densidades da mesma unidade cognitiva, incluindo `REDUCT-MAX`, `BASE` e `DEFESA`, com proveniência;
- prioriza execução mínima ponta a ponta antes de generalizar POP, DOC ou outros adapters;
- não altera o manifesto nem redefine o CCP por conta própria; dúvidas conceituais vão para o `INBOX/` do PO.

## 4. Propriedade de caminhos para reduzir conflitos

- `PO-001`: `DEV/ia-sessions/COORDINATION.md`, sua sessão e documentos de coordenação/arquitetura CCP que não pertençam à revisão do manifesto.
- `MAN-001`: arquivos do manifesto que já vinha revisando e sua própria sessão.
- `WRK-001`: sua sessão e a futura árvore da POC/materializador.

Antes de editar arquivo compartilhado fora dessas fronteiras, consultar o HEAD atual e registrar a necessidade no repositório quando houver risco de colisão.

## 5. Tags de commit

Formato mínimo:

```text
[ATOR] tipo(escopo): resumo
```

Exemplos:

```text
[PO-001] chore(coordination): bootstrap multi-agent sessions
[MAN-001] docs(manifesto): register P2.x cognitive projections
[WRK-001] feat(ccp-poc): add source-to-projection vertical slice
```

Commits anteriores a este protocolo podem não possuir tag. A obrigatoriedade começa no commit de bootstrap que introduz este arquivo.

## 6. Estado inicial conhecido

O commit imediatamente anterior ao bootstrap é `1a9750491b7db1473190db94027c543e5d815e5e`, produzido pela frente de revisão do manifesto antes da adoção das tags de ator. Ele deve ser tratado como trabalho de `MAN-001` para fins de rastreabilidade histórica.

## 7. Fonte de regras

Este protocolo adapta o padrão de sessões do InitProj — sessões rastreáveis, `CONTEXT`, `INBOX`, `OUTBOX` e handoff por arquivo — ao experimento atual do FlowED. Ele é operacional e pode evoluir a partir da experiência dos três atores.
