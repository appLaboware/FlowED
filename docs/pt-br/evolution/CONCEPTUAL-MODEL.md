# Modelo conceitual de trabalho do FlowED

**Status:** registro de descoberta — não normativo

## 1. Missão

A missão do FlowED é cobrir **todos os domínios da Engenharia de Software** por uma organização modular em duas direções complementares:

- **crescimento horizontal**: novos domínios/capacidades entram como módulos pares em um hub comum;
- **crescimento vertical**: cada domínio pode possuir múltiplas materializações substituíveis por adapters/providers.

O objetivo é que a organização possa crescer em abrangência sem perder uma linguagem operacional comum e possa trocar a forma concreta de executar uma intenção sem redefinir a intenção em si.

## 2. Definição consolidada de trabalho

FlowED é, no estado atual do animal, um **sistema operacional modular para a Engenharia de Software**, modular horizontalmente por domínios e verticalmente por materializadores/adapters.

Ele é orientado por **autoeducação monitorada e rastreável**, na qual a organização explicita como trabalha, preserva por que mudou, observa resultados, compara suas referências com conhecimento científico e com sua própria prática e evolui deliberadamente sua cultura técnica.

Essa evolução é tratada de forma empírica e histórica: decisões, referências, mudanças, divergências, resultados e aprendizado devem permanecer rastreáveis. O histórico não serve apenas como arquivo; ele descreve o comportamento e o perfil evolutivo da organização.

Um sistema de pontuação determinística é hipótese estrutural atual para descrever dimensões como alinhamento, força de sustentação, comportamento de mudança e perfil de risco. Esse mecanismo deve permitir caracterizar, por domínio e no agregado, tendências organizacionais como conservadorismo, experimentalismo, estabilidade, agressividade de mudança ou outras categorias que ainda precisarão ser formalmente definidas.

O nome de trabalho **Risco-FlowED** representa a futura leitura do comportamento evolutivo da organização, análoga apenas conceitualmente à ideia de um indicador de risco: não reduz a cultura a 'muda muito' ou 'muda pouco', mas procura representar como a organização assume, controla, sustenta, reverte e aprende com mudanças.

A memória histórica e a proveniência de decisões deverão futuramente ser materializadas por MyTrues ou componente equivalente, sem que a definição do FlowED dependa da implementação concreta desse componente.

## 3. Continuidade com o FlowED histórico

Nada do que o FlowED defendia anteriormente deve ser presumido descartado apenas porque o escopo foi ampliado.

A gestão de projetos baseada em autoeducação, a progressividade, a rastreabilidade, o crescimento do time, a sustentabilidade, a integração metodológica e a redução de fragmentação continuam válidos como partes do animal atual.

O que mudou é a abrangência: esses elementos deixam de descrever sozinhos a categoria inteira do FlowED e passam a compor um sistema mais amplo que pretende cobrir todos os domínios da Engenharia de Software.

A regra de revisão do manifesto histórico será, portanto, **preservar por expansão**: manter tudo o que continuar semanticamente compatível, recontextualizar o que ficou estreito demais e remover apenas o que entrar em contradição real com a definição consolidada.

## 4. Intenção separada da materialização

O usuário expressa uma intenção estável, por exemplo iniciar um projeto. A organização decide como essa intenção se materializa: GitHub, GitLab, Git local, Scrum, Kanban, Jenkins, Kubernetes, documentação, QA, auditoria ou qualquer combinação adequada ao contexto.

O usuário não deve precisar reaprender a linguagem operacional sempre que uma implementação muda.

> Uma intenção, muitas materializações.
> Uma linguagem comum, muitas tecnologias.
> Estabilidade na intenção; liberdade na implementação.

## 5. Três dimensões de composição

### 5.1 Largura

Quais domínios/capacidades fazem parte da composição organizacional: versionamento, documentação, qualidade, infraestrutura, gestão de projeto, ensino e outros.

O objetivo declarado é que o modelo possa se estender a todos os domínios relevantes da Engenharia de Software, sem fixar antecipadamente um conjunto fechado de módulos.

### 5.2 Profundidade

Qual implementação, provider ou adapter realiza cada domínio. Trocar GitHub por GitLab, por exemplo, deve alterar a materialização sem obrigar mudança da intenção pública correspondente.

### 5.3 Intensidade

Quanto rigor de uma capability deve ser aplicado no contexto. A mesma capability de qualidade pode significar testes mínimos em um projeto pequeno ou controles extensos de QA, homologação e auditoria em um ambiente regulado.

## 6. Soberania dos domínios

Os domínios permanecem internamente soberanos. FlowED procura padronizar a expressão de intenção entre eles, não substituir o conhecimento conceitual de cada área nem impor uma implementação única.

A terminologia exata para os contratos laterais entre domínios independentes ainda deve ser pesquisada. Não cristalizar o termo 'contratos entre irmãos' sem anterioridade terminológica.

## 7. Artefatos nativos e ausência de aprisionamento

Repositórios continuam sendo repositórios, documentos continuam documentos, pipelines continuam utilizáveis em suas ferramentas nativas. A abstração FlowED deve facilitar produção e coordenação sem tornar-se proprietária dos artefatos produzidos.

Uma implementação deve poder ser substituída e os resultados devem continuar utilizáveis mesmo sem o FlowED.

## 8. Sofisticação sem burocracia proporcional

A sofisticação da engenharia deve poder crescer sem que a complexidade operacional cresça proporcionalmente para o usuário.

FlowED simplifica a forma de pedir e coordenar; não necessariamente simplifica o trabalho técnico executado abaixo da interface.

## 9. Experimentação barata e autoeducação

Uma nova tecnologia, metodologia ou prática deve poder ser experimentada pela troca, inclusão ou configuração de capabilities e adapters, em vez de exigir a criação de um processo paralelo completo.

A organização aprende modificando progressivamente sua própria forma de trabalhar sem destruir o que funciona e sem abandonar a linguagem comum.

A autoeducação no FlowED atual não é apenas pedagógica: ela é monitorada, histórica e comparável. A organização deve conseguir observar o que adotou, por que adotou, como aquilo se comportou, o que aprendeu e por que manteve, revisou ou abandonou uma referência.

## 10. Ciência, prática e empirismo

FlowED pretende manter explícita a relação entre três fontes de sustentação e evolução:

- conhecimento científico e normativo disponível;
- prática observada da própria organização;
- decisões humanas contextualizadas, inclusive quando divergem das duas anteriores.

O sistema não deve transformar ciência em dogma nem experiência local em verdade universal. Deve tornar visível onde existe alinhamento, divergência, incerteza, sustentação forte ou sustentação inexistente.

## 11. Continuidade academia–indústria

A mesma linguagem operacional deve poder ser ensinada em ambiente acadêmico e continuar útil na indústria. O aluno pode começar com uma composição mínima e, ao longo da carreira, ampliar largura, profundidade e intensidade sem descartar o modelo mental aprendido.

## 12. Escala

FlowED não deve carregar como princípio a limitação pessoal de um desenvolvedor solo ou de uma equipe pequena. Deve poder representar desde estudante/indie hacker até empresas grandes com múltiplos projetos, governança, compliance e integrações corporativas.

## 13. Cultura explícita, comportamento e memória organizacional

As decisões, princípios, justificativas, mudanças e aprendizados da organização devem ser explicitáveis e preserváveis.

O histórico de evolução deve permitir descrever aspectos do comportamento organizacional, inclusive quão conservadora, inovadora, experimental, estável ou agressiva em mudança uma organização tende a ser em diferentes domínios.

Essas categorias ainda não são taxonomia final. Elas descrevem a intenção de que o FlowED consiga representar 'personalidade evolutiva' sem reduzi-la a opinião narrativa.

MyTrues é atualmente imaginado como componente adjacente de memória/proveniência dessa cultura, mas sua relação arquitetural definitiva com FlowED ainda precisa ser formalizada.

## 14. Pontuação determinística

A pontuação é parte importante do animal pretendido, mas a matemática ainda não está definida.

No nível conceitual, ela deve:

- ser reproduzível sempre que os dados e regras forem objetivos;
- deixar explícito onde existe julgamento humano;
- permitir comparação histórica;
- permitir comparação com baseline versionado;
- admitir score zero sem invalidar a decisão operacional;
- incorporar, quando defensável, evidência científica, normativa, empírica e longitudinal;
- permitir observar tendências de comportamento e risco sem fingir que um único número explica toda a organização.

O manifesto deve defender o princípio de mensuração e rastreabilidade, não congelar prematuramente fórmula, pesos ou escala.

## 15. Autoaplicação

O time que desenvolve FlowED deve usar o próprio mecanismo FlowED para desenvolver o FlowED. A autoaplicação deve ir além de dogfooding superficial: o sistema deve ser capaz de explicar e rastrear sua própria evolução usando o mesmo mecanismo que oferece aos usuários.

## 16. Pontos ainda necessários para uma definição final de manifesto

Antes de considerar a definição do animal completamente fechada, ainda faltam decisões humanas sobre:

1. **Fronteira do termo 'sistema operacional'** — decidir se é metáfora identitária/arquitetural ou categoria formal do produto. O manifesto pode usar a expressão, mas precisa evitar sugerir que FlowED é um OS de máquina se essa não for a intenção.
2. **Objeto primário da linguagem comum** — confirmar se a unidade fundamental é 'intenção', 'capability', 'ação operacional' ou combinação dessas ideias.
3. **Relação entre hub horizontal e coordenação** — esclarecer se FlowED apenas conecta domínios pares ou se existe um núcleo com autoridade de orquestração, políticas e estado compartilhado.
4. **Obrigatoriedade da autoeducação** — definir se todo uso que se declare FlowED precisa registrar aprendizado/evolução ou se isso pode variar por intensidade.
5. **Obrigatoriedade da pontuação** — definir se score é constitutivo de FlowED ou capability opcional de uma implantação mínima.
6. **Escopo do empirismo** — esclarecer se toda mudança deve produzir observação verificável ou se decisões puramente estratégicas também entram no mesmo mecanismo com score possivelmente zero.
7. **Personalidade/Risco-FlowED** — decidir se o manifesto deve declarar explicitamente que FlowED caracteriza comportamento organizacional ou apenas registrar os dados que permitem ferramentas futuras inferirem esse perfil.
8. **MyTrues** — decidir se a memória histórica é princípio obrigatório do FlowED e MyTrues apenas uma materialização, ou se memória/proveniência é um domínio opcional.
9. **Compatibilidade com o legado** — revisar o manifesto/README histórico cláusula a cláusula usando a regra 'preservar por expansão' e marcar qualquer contradição real.
10. **Critério de pertencimento** — definir o mínimo que uma organização precisa adotar para dizer que usa FlowED sem transformar baseline em obrigação.

Esses pontos são gaps do animal, não pesquisa científica. A ciência deverá ser buscada depois que essas decisões estiverem estabilizadas.
