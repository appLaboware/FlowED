# Manifesto FlowED — estrutura da filosofia para a prática

**Status:** hipótese estrutural para consolidação do manifesto. Não normativa.

## Introdução pretendida

O manifesto deve assumir explicitamente que nasce de perguntas recorrentes sobre como a Engenharia de Software trabalha, aprende e evolui.

Formulação preferida nesta rodada:

> **Este manifesto nasce de perguntas recorrentes sobre como a Engenharia de Software trabalha, aprende e evolui. As proposições a seguir não pretendem encerrar o raciocínio; pretendem iniciá-lo.**

Também permanece aceita a posição de não reivindicação de novidade filosófica:

> **Não reivindicamos a criação dos princípios que seguem. Propomos reconsiderar a ordem de importância que damos a ideias já presentes na ciência, nos padrões e na prática da engenharia.**

A intenção é que as frases filosóficas sejam lidas como proposições abertas à reflexão, crítica, colaboração e desenvolvimento, mesmo quando redigidas de forma afirmativa.

## Estrutura em camadas

A estrutura proposta para a próxima consolidação do manifesto é:

1. introdução filosófica e convite à reflexão;
2. três princípios filosóficos centrais;
3. uma transição explícita do tipo **"portanto"**;
4. compromissos de engenharia derivados desses princípios;
5. passagem da filosofia à prática e referência à materialização de referência;
6. fechamento autoaplicável e revisável.

A intenção não é criar novos princípios filosóficos para toda propriedade prática. Memória operacional, sustentação explícita, progressividade governada, contratos, substituibilidade, conformance, rastreabilidade e propriedades semelhantes devem ser tratadas prioritariamente como **compromissos derivados** quando puderem ser justificadas pelos princípios filosóficos centrais.

A derivação deve permanecer visível: quando um compromisso não puder ser ligado de forma convincente a um dos princípios, deve-se verificar se falta uma formulação filosófica, se o compromisso pertence apenas ao produto/contrato ou se ele não deve fazer parte do manifesto.

## Relação com os dois manifestos anteriores

Os dois candidatos anteriores possuem grande quantidade de conteúdo específico sobre contratos, memória operacional, evidência, progressividade, substituibilidade, conformance, materializações, aprendizado e documentação dinâmica.

Esse conteúdo não deve ser descartado. Deve ser reclassificado e reaproveitado na camada **"portanto, na Engenharia de Software defendemos que..."**, evitando que decisões de produto ou mecanismo técnico sejam confundidas com metafilosofia.

A sequência desejada é:

**princípio filosófico → compromisso de engenharia → contrato público → materialização substituível**.

## Memória operacional e aprendizagem

A aprendizagem pela execução pode ser derivada do Princípio do Foco no Caminho Cognitivo quando execução, resultado e evidência passam a integrar o percurso de revisão da decisão.

A cadeia conceitual passa a ser:

**decisão → execução → resultado → evidência → revisão → nova decisão**.

O princípio filosófico não precisa determinar logging, event streams, provenance ou tecnologia. O compromisso derivado é que experiência relevante possa retornar ao racional e participar conscientemente da evolução do conhecimento e da forma de trabalhar.

## Sustentação explícita

Ciência, norma, evidência empírica, lacunas, divergências, incertezas e autoria de avaliações podem ser compreendidas como componentes do caminho cognitivo de decisões que dependem dessas fontes.

Formulação conceitual desta rodada:

> **A ciência progride quando afirmações permanecem relacionadas a método, evidência, crítica, revisão e conhecimento anterior.**

Essa cadeia é entendida como exemplo forte de caminho cognitivo estruturado: conhecimento novo não aparece isolado, mas se relaciona a conhecimento anterior, método, crítica e revisão.

Scores, rankings, classificadores e providers continuam pertencendo a materializações posteriores e não à filosofia em si.

## Progressividade governada

A progressividade pode ser apresentada como compromisso derivado: se intenção e materialização são separáveis, se a identidade operacional pode sobreviver à troca de tecnologia e se decisões podem ser compreendidas e revistas, então a forma de trabalhar pode evoluir conscientemente sem exigir que toda mudança represente ruptura de identidade.

Mecanismos específicos como increase, reduce, pause, rollback, engines e policies pertencem ao contrato e à materialização.

## Da filosofia à prática

Há interesse em provocar o leitor que considere o manifesto excessivamente aspiracional ou impraticável, mas sem transformar a implementação de referência em autoridade filosófica nem afirmar superioridade.

Formulação candidata:

> **Se estas proposições parecerem apenas aspiracionais, a implementação de referência existe para demonstrar algo mais modesto e verificável: que ao menos uma materialização coerente é possível. Ela não reivindica ser a melhor; reivindica apenas mostrar que este caminho pode ser percorrido.**

Uma implementação de referência pode fornecer **evidência construtiva de realizabilidade de pelo menos uma composição**, mas não prova que a filosofia seja universalmente correta, superior ou a melhor solução para todos os contextos.

A localização preferida é uma seção final do tipo **"Da filosofia à prática"**, depois dos compromissos derivados e antes do fechamento, ou uma nota imediatamente após o manifesto. Não deve interromper os três princípios filosóficos.

## Compromisso educacional e continuidade academia–indústria

A intenção de oferecer a materialização de referência gratuitamente a estudantes está alinhada à filosofia de continuidade do conhecimento entre aprendizado e prática profissional, mas é uma **decisão de produto/ecossistema**, não um princípio constitutivo do manifesto.

O manifesto pode sustentar um compromisso mais geral:

> **O conhecimento operacional aprendido no início da formação deve poder continuar válido e aprofundável ao longo da prática profissional.**

A política concreta de disponibilização gratuita para estudantes e eventual oferta comercial à indústria deve ser apresentada no README do `flwd`, em documento de posicionamento do produto ou em um compromisso educacional da implementação de referência.

Essa separação evita transformar modelo comercial, licenciamento ou estratégia de adoção em requisito filosófico do FlowED, preservando a liberdade de outras implementações conformantes adotarem modelos diferentes.

## Fechamento autoaplicável

Duas frases permanecem fortes para o encerramento:

> **Se o FlowED estiver errado, ele próprio deve ajudar a demonstrá-lo.**

> **Se a crítica e a evidência mostrarem que este manifesto está errado, no todo ou em parte, seus próprios princípios exigem que ele seja revisto.**

A primeira mantém a provocação e leve ironia desejadas. A segunda explicita que não se trata de bravata: crítica, evidência e revisão devem poder atingir o próprio FlowED.

## Regra para a próxima consolidação

Na próxima versão, reaproveitar os dois manifestos anteriores por classificação, não por simples cópia:

- o que for metafilosófico deve ser comparado aos três princípios centrais;
- o que for consequência normativa deve ir para os compromissos derivados;
- o que for semântica pública deve ir para contratos;
- o que for mecanismo, ferramenta, distribuição, licenciamento ou estratégia comercial deve permanecer fora do corpo filosófico e ser colocado na documentação adequada da implementação/ecossistema.
