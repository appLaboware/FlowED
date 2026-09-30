# Arquitetura experimental do ITEOS

## Princípio

O laboratório começa pela composição, não pela criação.

A aplicação deve permanecer independente do mecanismo de implantação. Cada camada deve ser substituível.

## Fluxo de referência

Aplicação existente
→ detecção/build
→ artefato executável
→ bundle CNAB
→ Porter
→ mixin/adaptador
→ ferramenta determinística
→ destino

## Responsabilidades

### Aplicação

Contém somente o software e seus requisitos próprios. Não deve conhecer Azure, AWS, Porter ou o laboratório.

### Detecção/build

Quando necessário, Cloud Native Buildpacks pode detectar runtime e produzir imagem OCI.

Essa camada é opcional: aplicações que já possuem artefato de build podem fornecê-lo diretamente.

### Porter/CNAB

Porter é o primeiro orquestrador adotado pelo laboratório.

Responsabilidades observadas:

- bundle;
- lifecycle de install/upgrade/uninstall;
- parâmetros;
- credenciais;
- outputs;
- dependências;
- estado;
- distribuição OCI;
- execução de mixins.

### Mixins

Mixins são a fronteira de extensão primária.

Exemplos existentes:

- docker;
- docker-compose;
- az;
- aws;
- terraform;
- kubernetes;
- helm;
- exec.

Se uma ferramenta ou provedor não possuir integração adequada, a primeira opção é criar somente um mixin independente, sem alterar Porter.

### Ferramentas determinísticas

Continuam responsáveis pela execução concreta:

- Docker/Compose;
- OpenTofu/Terraform;
- Azure CLI;
- AWS CLI;
- Kubernetes;
- Helm;
- Ansible;
- outras ferramentas existentes.

## Critério para criação de código próprio

Código novo só entra depois que um experimento registrar uma lacuna que não possa ser resolvida razoavelmente por:

1. configuração;
2. bundle CNAB;
3. mixin existente;
4. novo mixin independente;
5. buildpack existente;
6. novo buildpack independente;
7. composição com outra ferramenta aberta.

## Não objetivo atual

Não existe, neste estágio, uma nova linguagem intencional, um novo sistema operacional DevOps ou um novo engine de infraestrutura.

O laboratório existe para descobrir empiricamente se alguma dessas camadas realmente falta.
