# Resultados — EXP-002

## 2026-09-30 — scaffold

Status: preparado, não executado.

Motivo: o ambiente da sessão não possui Docker.

## Evidências a coletar

- sistema operacional do host;
- versão do Docker Engine;
- versão do Docker Compose;
- build da imagem controladora;
- versão real do Porter dentro do container;
- mixins disponíveis;
- containers existentes antes do teste;
- containers criados durante `porter build/install`;
- volumes criados;
- estado do MongoDB Porter;
- containers restantes após saída do controlador;
- resultado do EXP-001;
- resultado após remover o controlador;
- qualquer problema de paths entre container controlador e Docker host.
