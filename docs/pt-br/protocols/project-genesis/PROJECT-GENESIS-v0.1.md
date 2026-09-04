# Project Genesis Protocol — PGP 0.1

**ID:** FLOWED-PROJECT-GENESIS  
**Versão:** 0.1-draft  
**Status:** DOGFOODING  
**Owner de domínio:** FlowED  
**Escopo:** nascimento de um projeto até existir autoridade local capaz de governá-lo.

## 1. Problema

Um projeto pode precisar de infraestrutura, comunicação, repositório, regras ou tecnologia mínima antes de possuir Product Owner próprio. Em cenários de dogfooding, a própria tecnologia necessária para o futuro PO exercer sua função pode ainda não existir.

Se ninguém puder agir antes da existência do PO, o projeto não nasce. Se a autoridade superior continuar decidindo depois que o projeto já pode se governar, ocorre invasão de domínio.

## 2. Princípio

```text
NO LOCAL PO -> PARENT BOOTSTRAP AUTHORITY
LOCAL PO READY -> TRANSFER AUTHORITY
```

A autoridade imediatamente superior pode atuar temporariamente apenas para tornar o projeto governável e capaz de receber seu próprio PO.

## 3. Bootstrap Authority

A Bootstrap Authority pode:

- declarar a existência/intenção do projeto;
- criar o mínimo de infraestrutura e repositórios;
- materializar regras mínimas de identidade, autoridade, comunicação e estado;
- executar uma vertical slice necessária ao próprio funcionamento do projeto;
- em dogfooding, fabricar o mínimo da tecnologia que o futuro PO precisa para conduzir o projeto;
- produzir evidência e handoff;
- designar/eleger o primeiro PO quando os gates de prontidão forem satisfeitos.

Não pode tratar decisões provisórias como produto definitivo nem continuar governando o bounded context após a transferência, salvo mandato explícito posterior.

## 4. Dogfooding Bootstrap Exception

Quando o produto em criação é também infraestrutura necessária para sua própria governança, aplica-se:

```text
BOOTSTRAP ENOUGH OF THE PRODUCT
TO MAKE PRODUCT OWNERSHIP POSSIBLE.
THEN HAND IT TO THE PRODUCT OWNER.
```

Exemplo: se InterMembers será o mecanismo institucional para a comunicação com o próprio PO de InterMembers, a autoridade incubadora pode implementar primeiro o fluxo mínimo de comunicação necessário para entregar a demanda ao PO e receber sua resposta.

Essa implementação é:

- mínima;
- explicitamente experimental;
- revisável/rejeitável pelo futuro PO;
- evidência de dogfooding, não doutrina permanente.

## 5. Estados

```text
G0 — IDEA
G1 — INCUBATING
G2 — BOOTSTRAPPING
G3 — PO_READY
G4 — OWNED
```

### G0 — IDEA

Existe uma intenção, mas ainda não um projeto governável.

### G1 — INCUBATING

A autoridade pai assume responsabilidade temporária e define missão inicial, limites e origem.

### G2 — BOOTSTRAPPING

São criados apenas os meios necessários para o projeto existir e ser governado: identidade, repositório, comunicação, estado, artefatos mínimos e tecnologia habilitadora quando indispensável.

### G3 — PO_READY

Existe um canal pelo qual o futuro PO pode:

- receber missão e contexto;
- identificar sua autoridade;
- acessar artefatos e estado;
- tomar decisões do produto;
- registrar mudanças;
- responder/escalar para a autoridade pai.

### G4 — OWNED

O PO aceitou o papel por evidência materializada e passa a ser autoridade local. A Bootstrap Authority volta a ser apenas stakeholder, cliente, patrocinador ou autoridade superior conforme o caso.

## 6. Gate PO_READY

O projeto só pode ser entregue ao PO quando todos forem verdadeiros ou explicitamente classificados:

```text
PROJECT_IDENTITY_RESOLVABLE
REPOSITORY_OR_WORKSPACE_ACCESSIBLE
MISSION_MATERIALIZED
AUTHORITY_BOUNDARY_MATERIALIZED
CURRENT_STATE_RESOLVABLE
INBOUND_COMMUNICATION_WORKS
OUTBOUND_COMMUNICATION_PATH_DEFINED
FIRST_WORK_CYCLE_EXECUTABLE
HANDOFF_REVIEWABLE
```

Em projeto que depende de InterMembers, `INBOUND_COMMUNICATION_WORKS` deve usar o próprio bootstrap de InterMembers quando esse for o objetivo do dogfooding.

## 7. Transferência de autoridade

A transferência deve ser um evento rastreável:

1. Bootstrap Authority entrega uma mensagem/demanda formal.
2. PO lê os artefatos e executa o primeiro ciclo.
3. PO responde pelo canal institucional definido.
4. Resposta classifica hipóteses incubadas e blockers.
5. A partir da resposta/aceite, decisões de produto pertencem ao PO.

## 8. Regra para equipe

```text
NO PRODUCT TEAM EXECUTION BEFORE PRODUCT GOVERNANCE EXISTS,
EXCEPT BOOTSTRAP WORK REQUIRED TO CREATE THAT GOVERNANCE.
```

O bootstrap pode usar executores técnicos somente no escopo necessário para tornar o projeto governável. Feature development normal aguarda autoridade local.

## 9. Relação com outros protocolos

- RBP: faz nascer o repositório.
- Project Genesis: faz nascer a autoridade/governança do projeto.
- InterMembers: materializa comunicação e interação quando adotado.
- ISO29110-Lite: estrutura POPs/DOCs e rastreabilidade quando adotado.
- Dec-B: cuida da mecânica/política SCM.

## 10. Exemplo InterMembers

```text
LaboWare Bootstrap Authority
        ↓
cria organização/repositório + comunicação mínima
        ↓
materializa mensagem na inbox de INTERM-POi-001
        ↓
INTERM-POi-001 revisa produto/incubação
        ↓
INTERM-POi-001 escreve OUT-001
        ↓
LaboWare lê OUT-001
        ↓
InterMembers = G4 OWNED
```

Até `OUT-001`, o trabalho é bootstrap. Depois, evolução do protocolo é decisão do PO do InterMembers.

## 11. Regra final

```text
A PROJECT MAY BE BORN BEFORE ITS PO,
BUT ONLY UNDER EXPLICIT TEMPORARY BOOTSTRAP AUTHORITY.
BUILD ONLY WHAT IS REQUIRED TO MAKE LOCAL OWNERSHIP POSSIBLE.
TRANSFER AUTHORITY AS SOON AS THE PROJECT CAN GOVERN ITSELF.
```
