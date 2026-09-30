# Arquitetura experimental do IDEOS

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

## Runtime do laboratório

O host deve precisar apenas de Docker/Docker Compose.

O próprio Porter roda dentro do container controlador IDEOS.

Topologia:

Docker Engine do host
→ container controlador IDEOS
→ Porter
→ invocation containers CNAB
→ infraestrutura/aplicação materializada

Não há Docker-in-Docker. O controlador usa o socket do Docker do host.

## Estado do Porter

Porter v1 precisa de armazenamento para instalações. O laboratório usa um MongoDB separado, também containerizado e administrado pelo compose do runtime.

Esse MongoDB guarda apenas estado administrativo do Porter no laboratório; não faz parte da aplicação materializada.

## Critério para código próprio

Código novo só entra depois que um experimento registrar uma lacuna que não possa ser resolvida razoavelmente por:

1. configuração;
2. bundle CNAB;
3. mixin existente;
4. novo mixin independente;
5. buildpack existente;
6. novo buildpack independente;
7. composição com outra ferramenta aberta.
