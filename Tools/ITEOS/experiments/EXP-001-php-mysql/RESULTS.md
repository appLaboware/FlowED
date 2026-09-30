# Resultados — EXP-001

## Registro

### 2026-09-30 — criação do experimento

Resultado: estrutura criada, sem execução.

Motivo: o ambiente da sessão não possui Docker instalado, portanto não é possível validar localmente o bundle Porter nem o Docker Compose nesta etapa.

### Itens a registrar na primeira execução

- versão do Porter;
- versão dos mixins;
- versão do Docker;
- versão do Docker Compose;
- resultado de `porter build`;
- resultado de `porter install`;
- URL obtida;
- persistência do contador após restart;
- resultado de `porter uninstall`;
- artefatos ou decisões manuais necessárias;
- alterações eventualmente necessárias no bundle.

## Fase Azure

Ainda não iniciada.

Antes de implementá-la, registrar:

1. quais alvos Azure podem executar a mesma aplicação sem alteração;
2. qual deles exige menor quantidade de conhecimento específico no bundle;
3. quais integrações Porter existentes já cobrem o caminho;
4. quais lacunas permanecem.
