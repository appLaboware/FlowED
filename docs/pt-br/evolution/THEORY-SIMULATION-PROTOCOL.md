# Protocolo de Simulação e Evolução de Teorias

**Status:** protocolo de trabalho preliminar. Destina-se a permitir uso controlado de teorias, princípios, referências e mecanismos ainda não plenamente validados sem promovê-los silenciosamente a conhecimento consolidado.

## 1. Objetivo

Permitir que uma teoria ou referência minimamente realizável seja colocada em uso de forma explícita, rastreável, reversível e comparável, produzindo evidência para sua própria evolução.

O protocolo deve permitir simular uma teoria antes de sua validação plena, desde que seu estado epistemológico e seu limite de realizabilidade permaneçam visíveis.

## 2. Unidade de simulação

Cada item simulado deve ser tratado como uma **Referência Experimental** versionada. Pode ser um princípio, pilar, regra, mecanismo, hipótese, fluxo, contrato ou composição.

Cada Referência Experimental deve possuir, no mínimo:

- identificador estável;
- versão;
- enunciado atual;
- objetivo declarado;
- escopo de aplicação;
- interlocutores/atores afetados;
- estado de realizabilidade;
- estado de sustentação/evidência;
- fontes e ancestrais conhecidos;
- hipóteses assumidas;
- gaps conhecidos;
- critérios observáveis de sucesso e falha;
- riscos conhecidos;
- decisão de adoção experimental;
- responsável pela decisão;
- data/período da simulação;
- resultados observados;
- divergências ocorridas;
- decisão posterior: manter, fortalecer, restringir, revisar, suspender ou abandonar;
- ligação rastreável com o estado anterior.

## 3. Estados mínimos de realizabilidade

Estados provisórios:

1. **R0 — desconhecido:** ainda não existe base suficiente para afirmar que a referência é operacionalmente realizável.
2. **R1 — realizável em princípio / escopo aberto:** existe mecanismo plausível, antecedente, protótipo conceitual ou decomposição suficiente para permitir simulação limitada, mas o escopo máximo não está demonstrado.
3. **R2 — parcialmente demonstrado:** parte relevante da referência foi materializada ou testada no escopo declarado.
4. **R3 — demonstrado no escopo declarado:** a realizabilidade operacional foi demonstrada para o recorte explicitamente definido.

Realizabilidade não equivale a correção, eficácia ou sustentação científica.

## 4. Sustentação

O score de sustentação deve permanecer separado da realizabilidade.

Uma Referência Experimental pode estar em R1 e possuir score de sustentação zero. Ela pode ser simulada se seu risco e seu contexto permitirem, mas o sistema não deve apresentá-la como comprovada.

A sustentação pode aumentar, permanecer estável ou diminuir a partir de:

- evidência científica;
- normas e padrões aplicáveis;
- estudos empíricos;
- experimentos controlados ou comparativos;
- observação operacional;
- replicação;
- falhas e resultados adversos;
- contradições encontradas;
- evidência contextual relevante.

O cálculo final do score ainda é objeto de pesquisa. Este protocolo normaliza o registro antes de normalizar a fórmula.

## 5. Fluxo normalizado de simulação

Toda Referência Experimental percorre, quando aplicável:

**formulação → crítica → refinamento → classificação de realizabilidade → baseline inicial de sustentação → plano de simulação → uso controlado → coleta de evidência → avaliação → alteração de estado/score → decisão → nova versão**.

Esse fluxo especializa o fluxo fundamental do FlowED sem substituí-lo.

## 6. Gaps como objetos de primeira classe

Um gap não é ausência informal de trabalho. Deve ser registrado como objeto rastreável.

Cada gap deve conter:

- identificador;
- referência afetada;
- descrição objetiva;
- por que o gap importa;
- tipo: conceitual, científico, empírico, operacional, arquitetural, terminológico, de segurança, de mensuração ou outro declarado;
- impacto potencial;
- bloqueante ou não bloqueante;
- condição necessária para fechamento;
- evidência que poderia resolvê-lo;
- estado atual;
- histórico de revisões.

Um gap não bloqueante pode coexistir com uma simulação em R1. Um gap bloqueante impede a simulação no escopo afetado.

## 7. MyTrues mínimo simulado

Enquanto MyTrues não estiver implementado, o repositório pode simular seu papel por um conjunto normalizado de artefatos versionados.

A simulação mínima deve preservar cinco relações:

1. **referência → origem**;
2. **referência → evidência**;
3. **referência → gaps**;
4. **referência → decisão/alteração**;
5. **versão atual → versões anteriores**.

Git fornece versionamento físico, mas não substitui o modelo conceitual. Commits são evidência de mudança; não são, por si só, representação suficiente do racional.

## 8. Registro mínimo de cada rodada

Ao final de uma rodada de debate, uso ou experimento, registrar:

- o que existia antes;
- o que foi questionado;
- o que mudou;
- por que mudou;
- qual evidência ou argumento motivou a alteração;
- que gaps foram abertos, fechados ou modificados;
- impacto no manifesto, teoria, protocolo ou implementação;
- estado de realizabilidade depois da rodada;
- efeito esperado sobre sustentação/score;
- próximo teste necessário.

## 9. Regras de segurança epistemológica

- hipótese não é fato;
- realizabilidade não é eficácia;
- uso não é validação automática;
- consenso não é evidência suficiente por si só;
- ausência de evidência não significa falsidade;
- experiência local não deve ser universalizada silenciosamente;
- uma projeção não pode ganhar autoridade apenas por ser mais legível que sua fonte;
- alteração de interpretação deve preservar a linhagem anterior;
- gaps conhecidos devem permanecer visíveis nas projeções que dependem deles, na intensidade adequada ao interlocutor.

## 10. Aplicação imediata ao Manifesto FlowED

O arquivo `MANIFESTO-PRELIMINARY-001.md` é a primeira Referência Experimental de grande escopo submetida a este protocolo.

Estado inicial sugerido:

- realizabilidade geral: **R1 — realizável em princípio / escopo aberto**;
- sustentação: ainda sem score consolidado;
- uso autorizado: debate conceitual, simulação documental e futura aplicação controlada;
- publicação como norma consolidada: não autorizada;
- objetivo da simulação: descobrir gaps, testar coerência interna, testar projeções dinâmicas, identificar ancestrais e produzir evidência para uma versão preliminar posterior.

## 11. Gaps iniciais abertos pela primeira simulação

GAP-M001 — definir critério mínimo de pertencimento/Full FlowED.

GAP-M002 — definir modelo de score multidimensional e quais dimensões podem ou não ser agregadas.

GAP-M003 — definir como um sistema determina o mínimo informacional necessário para cada interlocutor sem paternalismo, omissão ou opacidade.

GAP-M004 — definir o objeto primário da linguagem operacional comum: intenção, capability, ação, contrato ou composição.

GAP-M005 — definir o limite formal entre coordenação central do FlowED e soberania dos domínios pares.

GAP-M006 — definir quais requisitos de autoeducação são constitutivos do FlowED e quais admitem intensidade reduzida.

GAP-M007 — confirmar a necessidade do artigo-pai de síntese após pesquisa de anterioridade.

GAP-M008 — formalizar CCP/CCC suficientemente para sustentar EDT sem pressupor captura de cognição privada não observável.

GAP-M009 — definir a fronteira entre evidência científica, normativa, operacional e decisão contextual no score.

GAP-M010 — testar se os quatro pilares são independentes, suficientes e não redundantes.

## 12. Critério de maturação

Uma teoria deixa de ser apenas simulada quando os critérios de seu escopo declarado forem satisfeitos e houver evidência suficiente para promovê-la ao próximo estado definido pelo processo FlowED.

A promoção nunca apaga o histórico experimental. A versão consolidada deve continuar ligada às hipóteses, gaps, testes, revisões e evidências que a produziram.
