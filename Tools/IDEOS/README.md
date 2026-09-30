# IDEOS

> Status: laboratório experimental dentro do FlowED.

## Objetivo

Descobrir até onde é possível chegar usando exclusivamente ferramentas abertas já existentes antes de propor qualquer produto novo.

A composição inicial usa:

1. **Cloud Native Buildpacks** para detecção/build quando aplicável.
2. **Porter/CNAB** como empacotador e orquestrador do ciclo de vida.
3. **Mixins Porter** como adaptadores para ferramentas e provedores.
4. Ferramentas consolidadas como Docker/Compose, OpenTofu/Terraform, Azure CLI, AWS CLI, Kubernetes, Helm e Ansible para materialização.

IDEOS, neste estágio, não é uma implementação concorrente dessas ferramentas. É um laboratório de composição.

## Regra do laboratório

Antes de escrever código novo:

1. procurar uma ferramenta ou protocolo aberto existente;
2. provar a capacidade em um experimento reproduzível;
3. registrar exatamente onde a composição existente termina;
4. implementar somente a menor lacuna comprovadamente ausente.

## Estado validado

Em 2026-09-30 foi validado o primeiro fluxo completo:

Docker Engine do host
→ container controlador IDEOS
→ Porter
→ invocation container CNAB
→ Docker Compose
→ PHP + MySQL

A aplicação permaneceu ativa depois que o controlador terminou e foi posteriormente removida por `porter uninstall`.

Evidência:

https://github.com/appLaboware/FlowED/actions/runs/36769533522

## Primeira fronteira comprovada

O host não precisa de Porter instalado diretamente.

Para o experimento atual, o requisito externo é Docker/Docker Compose. O restante do controle Porter está empacotado no container IDEOS.

## Estrutura

- `docs/`: arquitetura e decisões.
- `runtime/`: container controlador do laboratório.
- `experiments/`: provas reproduzíveis.
