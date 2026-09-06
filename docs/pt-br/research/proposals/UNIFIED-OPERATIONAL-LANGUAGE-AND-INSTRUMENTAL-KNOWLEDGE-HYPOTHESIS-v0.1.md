# FlowED — Proposta de Tese: Linguagem Operacional Uniforme e Conhecimento Instrumental

**ID:** FLOWED-RESEARCH-UOL-001  
**Versão:** 0.1-draft  
**Status:** RESEARCH PROPOSAL / UNVALIDATED  
**Domínio:** FlowED  

## Tese candidata

> **Uma linguagem operacional uniforme pode reduzir o conhecimento instrumental necessário para operar uma toolchain heterogênea sem substituir o conhecimento conceitual dos domínios nem criar dependência operacional do próprio orquestrador.**

Esta formulação é uma hipótese de pesquisa, não uma conclusão comprovada.

## Distinção central

O estudo deve separar explicitamente:

- **conhecimento instrumental:** saber quais ferramentas, CLIs, sintaxes e sequências operacionais utilizar para executar uma tarefa;
- **conhecimento conceitual do domínio:** compreender os conceitos, decisões, invariantes, riscos e consequências próprios do domínio.

A hipótese não afirma que uma abstração operacional elimina a necessidade de conhecimento de Git, infraestrutura, CI/CD, documentação, testes ou outros domínios. Afirma que parte do conhecimento instrumental necessário para operar uma toolchain heterogênea pode ser reduzida por uma linguagem operacional comum, enquanto os artefatos e conceitos nativos permanecem acessíveis.

## Pergunta de pesquisa principal

> Em que medida uma linguagem operacional uniforme sobre ferramentas heterogêneas reduz carga e conhecimento instrumental necessários à execução de tarefas de engenharia de software, preservando simultaneamente conhecimento conceitual, transparência dos artefatos nativos e independência operacional do orquestrador?

## Hipóteses iniciais

**H1 — Instrumental Knowledge Reduction**  
Participantes utilizando uma linguagem operacional uniforme necessitam dominar menos interfaces e sintaxes específicas para completar um conjunto equivalente de tarefas heterogêneas.

**H2 — Domain Knowledge Preservation**  
A redução do conhecimento instrumental obrigatório não implica redução necessária da capacidade de compreender, inspecionar ou operar diretamente os artefatos do domínio nativo.

**H3 — Operational Exitability**  
Os resultados materializados permanecem fundamentalmente operáveis pelas ferramentas nativas depois da remoção do orquestrador.

**H4 — Progressive Learning**  
Usuários podem iniciar pela abstração operacional e progressivamente acessar os domínios nativos sem substituir os artefatos anteriormente produzidos por artefatos de outra classe pedagógica.

## Variáveis e métricas candidatas

- número de interfaces/CLIs que o participante precisa utilizar;
- número de comandos/sintaxes específicas que precisa conhecer;
- tempo para completar tarefa;
- erros operacionais;
- retrabalho;
- necessidade de assistência;
- taxa de conclusão;
- qualidade do artefato final;
- capacidade de explicar conceitos do domínio;
- capacidade de inspecionar o artefato nativo;
- capacidade de continuar a operação após remoção do FlowED;
- carga cognitiva percebida;
- tempo de aprendizagem;
- retenção e transferência de conhecimento.

## Desenho experimental candidato

Comparar grupos ou execuções equivalentes:

```text
MESMAS TAREFAS
MESMOS DOMÍNIOS
MESMOS CRITÉRIOS DE ACEITAÇÃO
        ↓
A — toolchain nativa heterogênea
B — linguagem operacional uniforme FlowED
        ↓
medir operação + qualidade + aprendizagem + exitabilidade
```

O experimento deve impedir que facilidade operacional seja confundida com qualidade inferior ou com ocultação permanente da tecnologia nativa.

## Relação com princípios do FlowED

A tese depende de quatro propriedades que devem ser testadas separadamente:

1. uma porta operacional comum;
2. materialização em artefatos nativos;
3. conhecimento e interfaces do domínio continuam acessíveis;
4. o FlowED pode ser removido sem tornar o resultado fundamentalmente inoperável.

Se a quarta propriedade falhar, redução de conhecimento instrumental pode ser apenas lock-in e não sustenta a tese pretendida.

## Prior art obrigatório antes de artigo

O estudo deverá revisar pelo menos:

- Platform Engineering e Internal Developer Platforms;
- cognitive load em developer experience/tooling;
- Application Lifecycle Management;
- Model-Driven Engineering / Model-Driven Architecture;
- Software Factories e Domain-Specific Languages;
- Infrastructure as Code;
- control planes e provider/plugin architectures;
- abstraction, progressive disclosure e end-user development;
- technology transfer e education-to-industry continuity;
- operational portability, interoperability e lock-in.

A contribuição não poderá ser alegada simplesmente como "uma interface reduz carga cognitiva". O possível residual científico está na combinação e nas condições sob as quais a redução instrumental ocorre **sem perda de transparência conceitual e sem dependência operacional do orquestrador**.

## Critério de falsificação

A hipótese deverá ser rejeitada ou reformulada se evidência mostrar, entre outros casos, que:

- a linguagem uniforme não reduz significativamente o esforço instrumental;
- a abstração prejudica de forma relevante a compreensão dos domínios;
- os artefatos produzidos não podem ser assumidos diretamente pelas ferramentas nativas;
- a remoção do FlowED impede a operação fundamental do resultado;
- soluções existentes já demonstram integralmente a mesma combinação, eliminando o residual de pesquisa.

## Relação com o Prior-Art/Novelty Gate

Esta proposta permanece deliberadamente **UNVALIDATED** até o Prior-Art/Novelty Gate do FlowED.

O gate poderá concluir que a tese é:

- conhecida;
- combinação conhecida;
- potencialmente nova como combinação;
- potencialmente nova em propriedade específica;
- não defensável;
- insuficientemente sustentada.

Nenhuma alegação de novidade deve preceder esse resultado.
