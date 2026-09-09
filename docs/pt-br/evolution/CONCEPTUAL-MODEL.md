# Modelo conceitual de trabalho do FlowED

**Status:** registro de descoberta — não normativo

## 1. Propósito central

FlowED busca fornecer uma linguagem operacional comum para expressar intenções de Engenharia de Software através de domínios diferentes sem exigir que todos usem as mesmas tecnologias, metodologias ou ferramentas.

A intenção é estabilizar a forma de expressar o que se deseja realizar e deixar a materialização variável.

> Uma intenção, muitas materializações.
> Uma linguagem comum, muitas tecnologias.
> Estabilidade na intenção; liberdade na implementação.

## 2. Intenção separada da materialização

O usuário expressa uma intenção estável, por exemplo iniciar um projeto. A organização decide como essa intenção se materializa: GitHub, GitLab, Git local, Scrum, Kanban, Jenkins, Kubernetes, documentação, QA, auditoria ou qualquer combinação adequada ao contexto.

O usuário não deve precisar reaprender a linguagem operacional sempre que uma implementação muda.

## 3. Três dimensões de composição

### 3.1 Largura

Quais domínios/capacidades fazem parte da composição organizacional: versionamento, documentação, qualidade, infraestrutura, gestão de projeto, ensino e outros.

### 3.2 Profundidade

Qual implementação, provider ou adapter realiza cada domínio. Trocar GitHub por GitLab, por exemplo, deve alterar a materialização sem obrigar mudança da intenção pública correspondente.

### 3.3 Intensidade

Quanto rigor de uma capability deve ser aplicado no contexto. A mesma capability de qualidade pode significar testes mínimos em um projeto pequeno ou controles extensos de QA, homologação e auditoria em um ambiente regulado.

## 4. Soberania dos domínios

Os domínios permanecem internamente soberanos. FlowED procura padronizar a expressão de intenção entre eles, não substituir o conhecimento conceitual de cada área nem impor uma implementação única.

A terminologia exata para os contratos laterais entre domínios independentes ainda deve ser pesquisada. Não cristalizar o termo "contratos entre irmãos" sem anterioridade terminológica.

## 5. Artefatos nativos e ausência de aprisionamento

Repositórios continuam sendo repositórios, documentos continuam documentos, pipelines continuam utilizáveis em suas ferramentas nativas. A abstração FlowED deve facilitar produção e coordenação sem tornar-se proprietária dos artefatos produzidos.

Uma implementação deve poder ser substituída e os resultados devem continuar utilizáveis mesmo sem o FlowED.

## 6. Sofisticação sem burocracia proporcional

A sofisticação da engenharia deve poder crescer sem que a complexidade operacional cresça proporcionalmente para o usuário.

FlowED simplifica a forma de pedir e coordenar; não necessariamente simplifica o trabalho técnico executado abaixo da interface.

## 7. Experimentação barata e autoeducação

Uma nova tecnologia, metodologia ou prática deve poder ser experimentada pela troca, inclusão ou configuração de capabilities e adapters, em vez de exigir a criação de um processo paralelo completo.

A organização aprende modificando progressivamente sua própria forma de trabalhar sem destruir o que funciona e sem abandonar a linguagem comum.

## 8. Continuidade academia–indústria

A mesma linguagem operacional deve poder ser ensinada em ambiente acadêmico e continuar útil na indústria. O aluno pode começar com uma composição mínima e, ao longo da carreira, ampliar largura, profundidade e intensidade sem descartar o modelo mental aprendido.

## 9. Escala

FlowED não deve carregar como princípio a limitação pessoal de um desenvolvedor solo ou de uma equipe pequena. Deve poder representar desde estudante/indie hacker até empresas grandes com múltiplos projetos, governança, compliance e integrações corporativas.

## 10. Cultura explícita e memória organizacional

As decisões, princípios, justificativas, mudanças e aprendizados da organização devem ser explicitáveis e preserváveis. MyTrues é atualmente imaginado como componente adjacente de memória/proveniência dessa cultura, mas sua relação arquitetural definitiva com FlowED ainda precisa ser formalizada.

## 11. Autoaplicação

O time que desenvolve FlowED deve usar o próprio mecanismo FlowED para desenvolver o FlowED. A autoaplicação deve ir além de dogfooding superficial: o sistema deve ser capaz de explicar e rastrear sua própria evolução usando o mesmo mecanismo que oferece aos usuários.
