# Base científica — contrato executável orientado pelo consumidor no `flwd`

**Status:** referência científica/operacional para o piloto `FLWD-CONTRACT-BY-EXAMPLE-PILOT.md`.

**Reference ID:** `REF-SCI-FLWD-CBE-001`  
**Estado:** sustentação externa encontrada; adoção composta (`ADOPT/COMPOSE`), não invenção metodológica.  
**Escopo da claim:** projetar e verificar contratos públicos a partir de interações observáveis do consumidor, usar mocks/fakes antes do provider real e verificar posteriormente providers por conformidade ao mesmo contrato.

## 1. Conclusão de Discovery

A ideia do piloto do `flwd` possui anterioridade científica e técnica suficiente para não ser tratada como método novo do FlowED.

O padrão mais próximo é **Consumer-Driven Contract Testing (CDCT)**, complementado por **contract-based testing**, **specification-based conformance testing**, **behavioral contracts/substitutability** e **mock objects**.

Portanto, “TDD” pode permanecer como analogia informal de desenvolvimento de fora para dentro, mas não deve ser o nome científico principal da abordagem. A formulação tecnicamente mais defensável é:

> **consumer-driven executable contract / contrato executável orientado pelo consumidor**, com verificação de conformidade do provider.

O FlowED pode adaptar e compor esse prior art para uma linguagem operacional horizontal, mas não deve reivindicar como inovação a sequência “consumidor + mock primeiro; provider depois; mesmo contrato para verificar ambos”.

## 2. Referência científica principal — Consumer-Driven Contract Testing

### Schwarz, Quast & Riehle (2025)

**Título:** *Ensuring Syntactic Interoperability Using Consumer-Driven Contract Testing*  
**Periódico:** Software Testing, Verification and Reliability, 35(5), e70006  
**DOI:** `10.1002/stvr.70006`

O estudo combina **systematic literature review** e **participatory action research** para construir uma teoria sobre quando e como usar consumer-driven contract testing. A conclusão reportada é que CDCT pode assegurar interoperabilidade sintática entre microservices por execução isolada de testes, complementar a estratégia de testes e favorecer APIs/código de maior qualidade.

**Relação direta com FlowED:**

- consumidor explicita expectativas do provider;
- contrato é verificável por testes isolados;
- compatibilidade pode ser checada sem depender de E2E completo;
- o contrato funciona como fronteira entre consumidor e provider independentemente de implementação interna.

**Limite:** o artigo trata principalmente interoperabilidade sintática em arquiteturas de microservices. Ele não demonstra que o mesmo mecanismo garante equivalência semântica geral entre todos os domínios que FlowED pretende cobrir.

## 3. Evidência empírica complementar — CDCT em sistemas reais

### Ayas, Fischer, Leitner & Gomes (2022)

**Título:** *An Empirical Analysis of Microservices Systems Using Consumer-Driven Contract Testing*  
**Evento:** 48th Euromicro Conference on Software Engineering and Advanced Applications (SEAA 2022)  
**DOI:** `10.1109/SEAA56994.2022.00022`

O trabalho minerou repositórios GitHub, analisou 16 projetos de microservices e aprofundou quatro que utilizavam consumer-driven contract testing, mostrando como os artefatos de contrato se encaixavam em arquiteturas de teste em múltiplos níveis.

**Relação com FlowED:** demonstra que CDCT não é apenas construção teórica; há materialização observável em projetos reais e integração com outras camadas de teste.

**Limite:** amostra pequena e domínio específico de microservices; não sustenta generalização automática para o FlowED inteiro.

## 4. Contratos comportamentais e simulação de componentes

### Heckel & Lohmann (2005)

**Título:** *Towards Contract-based Testing of Web Services*  
**Periódico:** Electronic Notes in Theoretical Computer Science, 116, 145–156  
**DOI:** `10.1016/j.entcs.2004.02.073`

O trabalho argumenta que interoperabilidade entre requestor e provider exige mais que tipos e assinaturas: contratos podem expressar informação comportamental, incluindo pré e pós-condições. A interpretação operacional desses contratos é proposta também como forma de **simular componentes requeridos durante unit testing**.

**Relação direta com o piloto:** apoia cientificamente a ideia de representar o comportamento público esperado antes da implementação real e usar uma simulação/mock do provider para testar o consumidor.

## 5. Conformidade derivada de especificação

### Tretmans (1999)

**Título:** *Testing Concurrent Systems: A Formal Approach*  
**Evento:** CONCUR’99, LNCS 1664, 46–65  
**DOI:** `10.1007/3-540-48320-9_6`

O trabalho formaliza testes baseados em especificações, com definições de conformidade, execução de testes e derivação de testes a partir de sistemas de transição rotulados.

**Relação com FlowED:** sustenta a separação entre:

- especificação/contrato esperado;
- implementação concreta;
- conjunto de testes que decide conformidade da implementação com a especificação.

Isto reforça que o mock não precisa ser a implementação real; o artefato autoritativo é o contrato/especificação e seus testes de conformidade.

## 6. Interfaces como comportamento, não apenas assinatura

### de Alfaro & Henzinger (2001)

**Título:** *Interface Automata*  
**Evento:** ESEC/FSE 2001, ACM, 109–120  
**DOI:** `10.1145/503209.503226`

O trabalho propõe interfaces que capturam aspectos temporais de componentes, incluindo suposições sobre entradas e garantias sobre saídas, e define compatibilidade/refinamento entre interfaces.

**Relação com FlowED:** apoia a decisão de que contrato público não deve significar apenas formato de request/response. Dependendo da capability, ordem, estados e garantias comportamentais também podem fazer parte do contrato observável.

## 7. Substituição por comportamento

### Liskov & Wing (1994)

**Título:** *A Behavioral Notion of Subtyping*  
**Periódico:** ACM Transactions on Programming Languages and Systems, 16(6), 1811–1841  
**DOI:** `10.1145/197320.197383`

A formulação comportamental de subtipagem exige que propriedades garantidas para um tipo abstrato continuem válidas para seus subtipos.

**Relação com FlowED:** é uma base formal importante para a regra de substituição: Provider B pode substituir Provider A apenas no escopo em que preserva as propriedades observáveis prometidas pelo contrato público. Não é necessário possuir a mesma implementação ou produzir bytes idênticos.

## 8. Design by Contract

### Meyer (1992)

**Título:** *Applying “Design by Contract”*  
**Periódico:** IEEE Computer, 25(10), 40–51  
**DOI:** `10.1109/2.161279`

Design by Contract consolida o uso explícito de obrigações e garantias por contratos, especialmente pré-condições, pós-condições e invariantes.

**Relação com FlowED:** fornece uma base clássica para distinguir “o que deve ser garantido publicamente” de “como a implementação produz a garantia”.

## 9. Mock objects como técnica de desenvolvimento e teste

### Freeman, Mackinnon, Pryce & Walnes (2004)

**Título:** *Mock Roles, Not Objects*  
**Evento:** OOPSLA 2004 Companion  
**DOI:** `10.1145/1028664.1028765`

O trabalho descreve mock objects como extensão de TDD que pode guiar a descoberta das relações e papéis do sistema, não apenas isolar dependências.

### Spadini, Aniche, Bruntink & Bacchelli (2019)

**Título:** *Mock objects for testing java systems: Why and how developers use them, and how they evolve*  
**Periódico:** Empirical Software Engineering, 24, 1461–1498  
**DOI:** `10.1007/s10664-018-9663-0`

Estudo empírico de uso de mocks em sistemas Java. Confirma o uso de mocks para substituir dependências e simular comportamento esperado, ao mesmo tempo em que mostra que mocks precisam ser usados com disciplina e possuem trade-offs.

**Relação com FlowED:** sustenta o mock/fake como materializador inicial do lado provider, mas também justifica a regra de não tornar o mock o próprio contrato nem acoplar o cliente a detalhes internos do mock.

## 10. Referência operacional importante — Pact

Pact não é usado aqui como evidência científica principal, mas como materialização madura do padrão. Seu fluxo operacional é especialmente próximo do piloto FlowED:

1. consumidor escreve teste contra mock;
2. interações são registradas em contrato;
3. contrato é compartilhado;
4. requests são reproduzidos contra provider real;
5. provider deve satisfazer o contrato.

O FlowED não deve copiar Pact nem se limitar a HTTP/microservices. A relevância é demonstrar que a sequência operacional pretendida já possui implementação consolidada no ecossistema.

## 11. Síntese de sustentação para a claim FlowED

### Sustentado diretamente

- contratos orientados pelo consumidor podem ser definidos e verificados antes de integração E2E completa;
- mocks podem simular o provider para desenvolver/testar o consumidor;
- contratos podem ser executáveis e usados para verificar providers reais;
- compatibilidade pode depender de comportamento observável, não apenas assinatura;
- implementações diferentes podem ser tratadas como substituíveis quando preservam garantias públicas relevantes.

### Sustentado indiretamente / por composição

- usar o mesmo mecanismo para CLI, YAML, API, SDK, UI e agentes;
- usar contratos executáveis como língua horizontal de múltiplos domínios da Engenharia de Software;
- tratar semanticamente equivalente, e não byte-idêntico, como critério de substituição em toda a plataforma.

### Ainda não sustentado

- que um único envelope contratual será suficiente para todos os domínios FlowED;
- que consumer-driven contracts sozinhos garantem equivalência semântica profunda;
- que a abordagem reduzirá custo, complexidade ou retrabalho no FlowED;
- que mocks e contratos de exemplo serão suficientes para todas as operações stateful, temporais ou humanas;
- que o modelo será superior a alternativas em escala organizacional.

Essas claims permanecem experimentais e devem ser testadas pelo próprio protocolo FlowED.

## 12. Decisão epistemológica

A proposta `FLWD-CONTRACT-BY-EXAMPLE-PILOT` deve ser classificada como **COMPOSE**, não INVENT.

O residual possível do FlowED está na integração dessas ideias em uma linguagem operacional comum, progressiva, multi-domínio e epistemicamente rastreável — não na invenção de consumer-driven contract testing, mock-first development, behavioral contracts ou conformance testing.

## 13. Referências

- Schwarz, G.-D., Quast, F., & Riehle, D. (2025). *Ensuring Syntactic Interoperability Using Consumer-Driven Contract Testing*. Software Testing, Verification and Reliability, 35(5), e70006. DOI: 10.1002/stvr.70006.
- Ayas, H. M., Fischer, H., Leitner, P., & Gomes, F. (2022). *An Empirical Analysis of Microservices Systems Using Consumer-Driven Contract Testing*. SEAA 2022, 92–99. DOI: 10.1109/SEAA56994.2022.00022.
- Heckel, R., & Lohmann, M. (2005). *Towards Contract-based Testing of Web Services*. Electronic Notes in Theoretical Computer Science, 116, 145–156. DOI: 10.1016/j.entcs.2004.02.073.
- Tretmans, J. (1999). *Testing Concurrent Systems: A Formal Approach*. CONCUR’99, LNCS 1664, 46–65. DOI: 10.1007/3-540-48320-9_6.
- de Alfaro, L., & Henzinger, T. A. (2001). *Interface Automata*. ESEC/FSE 2001, 109–120. DOI: 10.1145/503209.503226.
- Liskov, B. H., & Wing, J. M. (1994). *A Behavioral Notion of Subtyping*. ACM TOPLAS, 16(6), 1811–1841. DOI: 10.1145/197320.197383.
- Meyer, B. (1992). *Applying “Design by Contract”*. Computer, 25(10), 40–51. DOI: 10.1109/2.161279.
- Freeman, S., Mackinnon, T., Pryce, N., & Walnes, J. (2004). *Mock Roles, Not Objects*. OOPSLA 2004 Companion, 236–246. DOI: 10.1145/1028664.1028765.
- Spadini, D., Aniche, M., Bruntink, M., & Bacchelli, A. (2019). *Mock objects for testing java systems*. Empirical Software Engineering, 24, 1461–1498. DOI: 10.1007/s10664-018-9663-0.
