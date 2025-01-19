<p align="center">
  <img src="./assets/FlowED.svg" alt="FlowED Logo" width="30%"/>
</p>

> 🚧 **FlowED ainda está em fase de protótipo!**
>
> Esta versão está focada na **definição conceitual e estruturação inicial**. Algumas seções podem estar **incompletas ou em revisão**.  
> Funcionalidades, documentação detalhada e exemplos práticos ainda estão sendo desenvolvidos.  
>
>📌 Nesta fase, estamos estruturando:
>
> - 🏗 Conceitos e fundamentos globais
> - 📄 Documentação progressiva vinculada a este README
> - 🌍 Repositórios do ecossistema como protótipos

# FlowED - _Flow Education-Driven_

![Status](https://img.shields.io/badge/Status-Protótipo-orange?style=for-the-badge)
![GitHub contributors](https://img.shields.io/github/contributors/SysDevTools/FlowED?label=Contribuidores&style=for-the-badge)
![Metodologia](https://img.shields.io/badge/Metodologia-Gestão%20de%20Projetos-green?style=for-the-badge)

**FlowED** (Flow Education-Driven - Fluxo Orientado por Educação) é uma metodologia de gestão de projetos que defende:

>**"Conceito modelado desde o início, eficiência progressiva por aprendizado próprio."**

O FlowED não é uma metodologia prescritiva, mas um modelo baseado em princípios sólidos de rastreabilidade, progressividade e adaptação, garantindo um fluxo estruturado sem comprometer a autonomia e identidade dos times. Ele fornece um ponto de partida comum e evolui conforme a experiência do time e do projeto.

🔎 Para mais detalhes, acesse **[Visão Geral do FlowED](./docs/pt-br/philosophy/overview.md)**

O termo **_Education-Driven_** reflete a ideia de que a educação dos _stakeholders_ é o pilar central para a evolução do projeto. A metodologia estabelece princípios e pilares essenciais desde o início, garantindo **rastreabilidade** e **progressividade**. No entanto, defende que o próprio projeto se torne a principal fonte de aprendizado contínuo para a equipe, promovendo uma evolução estruturada, adaptativa e alinhada às necessidades reais do time e do produto.

🔎 Para mais detalhes, acesse **[Filosofia do FlowED](./docs/pt-br/philosophy/philosophy.md)**

## Motivação

O **FlowED** nasceu da experiência no ambiente acadêmico, mas se mostrou igualmente relevante para a indústria. Seu desenvolvimento foi impulsionado por lacunas observadas nas metodologias tradicionais, especialmente na dificuldade de adaptação a diferentes escopos de projetos e times, além da desconexão entre _Academia_ e _Indústria_.

Essas lacunas se manifestam de maneiras distintas na indústria e na academia, criando desafios específicos que dificultam a adoção de metodologias eficazes. Isso pode ser observado em dois paradoxos:

🔧 **Na indústria**: Pequenos projetos evitam metodologias porque são burocráticas demais, mas, quando crescem, não possuem rastreabilidade suficiente para adotá-las.

🎓 **Na academia**: A complexidade dos métodos e a falta de estrutura prática impedem que alunos experimentem a gestão de projetos de forma realista.

🔎 Para uma análise detalhada das lacunas metodológicas que motivaram a criação do FlowED, incluindo os paradoxos enfrentados pela indústria e pela academia, acesse **[A Motivação por Trás do FlowED](./docs/pt-br/philosophy/motivation.md)**

### O manifesto FlowED

A partir de reflexões sobre as motivações que produziram os conceitos do FlowED, um manifesto foi criado para defender pilares e princípios. O Manifesto FlowED documenta os pilares e princípios da metodologia, consolidando sua filosofia em um formato independente. Embora seja um documento autônomo, ele se mantém alinhado e integrado ao FlowED.

🔎 Para mais detalhes, acesse **[http://flowedmanifest.org].**

## Como Funciona

### 🔹 Introdução: os Níveis de Implantação no FlowED  

O FlowED define **três níveis progressivos de implantação**, permitindo que projetos e times adotem um modelo compatível com sua complexidade e necessidade de rastreabilidade. Cada nível mantém **princípios comuns** desde o início, mas evolui progressivamente em termos de versionamento, gestão e documentação.  

> **Os níveis não são permanentes.** Um projeto pode iniciar como _Mono Dev_ e, conforme cresce ou novas necessidades surgem, pode adotar práticas do _Mono Release Dev_ ou _Feature Dev_. A transição entre níveis ocorre naturalmente conforme a maturidade do time e do produto, sendo documentada nos changelogs e nos registros de evolução do projeto.

### 🏗️ **Níveis de Implantação**  

🔹 **Mono Dev** → Desenvolvedor Único.  
 No nível mais básico, o desenvolvedor trabalha com **uma história local** e **uma história remota**, garantindo versionamento desde o início. A branch local funciona como um ambiente **de desenvolvimento isolado**, enquanto a branch remota representa a versão **em produção**.  

- O ambiente de desenvolvimento é padronizado utilizando **ambiente isolado, reproduzível e armazenável**.  
- O fluxo de trabalho mantém um **ciclo estruturado**, permitindo rastreabilidade desde o primeiro commit.  
- Sem necessidade de sincronização entre múltiplos desenvolvedores, mas com histórico rastreável e documentação mínima.  
- **Documentação mínima exigida**, com backlog e changelog obrigatórios, permitindo transições rastreáveis entre níveis.  

🔹 **Mono Release Dev** → Pequenos times com divisão de tarefas estruturada.  
 A estrutura evolui para permitir **colaboração entre desenvolvedores**. Tem todas as características da anterior, mas adiciona **branches temporárias** para cada release, garantindo uma organização modular do desenvolvimento.  

- Introdução de **cerimônias de início e conclusão de releases**.  
- Cada desenvolvedor trabalha em um ambiente isolado como no nível anterior, mas em uma branch de _Release_.  
- Atualizações intermediárias (antes do final de release) são enviadas diretamente para a branch do release remoto sempre que necessário.  

🔹 **Feature Dev** → Equipes maiores e desenvolvimento distribuído por features.  
 Neste nível, cada **release se fragmenta em múltiplas features**, operando de forma independente. As features funcionam como **sub-releases**, permitindo desenvolvimento escalável.  

- Cada **feature** recebe um fluxo semelhante ao de um **release** no nível anterior.  
- Permite **múltiplos níveis de subdivisão**, criando um modelo dinâmico que pode escalar conforme a complexidade do projeto.  
- Estrutura altamente modular, facilitando a rastreabilidade e permitindo a adoção de subfeatures conforme necessário.  

🔎 Para uma análise detalhada sobre os níveis de desenvolvimento acesse **[Estratégias de Implantação](./docs/pt-br/adoption/implementation_levels.md)**  

No FlowED, essa **progressão não acontece de forma abrupta**, mas sim documentada e rastreável. A evolução de um projeto ou time ocorre de forma iterativa, e cada mudança nos ciclos deve ser acompanhada por **changelogs, backlog e documentação mínima**, garantindo transparência e continuidade.

> **A experiência acumulada pelo time e pelo projeto se torna parte do conhecimento estruturado da equipe, servindo como referência para novos integrantes e garantindo evolução contínua sem comprometer identidade ou rastreabilidade.**  

**A metodologia se estrutura em quatro ciclos principais**, que funcionam tanto como base para o ciclo de vida de um projeto quanto como _templates_ para novos projetos que adotam o FlowED:

### 🔄 **Ciclos do FlowED**  

Os quatro ciclos do FlowED estruturam o desenvolvimento e a gestão do projeto, mas **não são estáticos nem obrigatoriamente sequenciais**. Dependendo do contexto, um projeto pode iniciar já com processos de desenvolvimento contínuo, enquanto outro pode passar por várias iterações na fase de prototipagem antes de evoluir.

> **A progressão entre ciclos é guiada pela necessidade do time e pela maturidade do projeto, mantendo rastreabilidade e adaptabilidade conforme a equipe define suas práticas.**  

Os **quatro ciclos** servem como base para todos os **ciclos de vida do projeto** e como _template_ para novos projetos que seguem essa mesma estrutura progressiva:

1️⃣ **Prototipagem** – Construção livre do conceito inicial, focada em experimentação e validação de ideias.  
2️⃣ **Implantação** – Organização inicial do ambiente, definição de fluxos e adoção do modelo de versionamento adequado ao escopo do time e do projeto.  
3️⃣ **Desenvolvimento** – Evolução iterativa do código, baseada nos princípios do FlowED e adaptada às necessidades do projeto.  
4️⃣ **Homologação** – Validação final, refinamento e preparação para o ambiente de produção.  

🔎 Para uma análise detalhada dos ciclos consulte **[Fluxo de Desenvolvimento no FlowED](./docs/pt-br/adoption/development_cycles.md)**  

#### **Mudanças e Adaptação dos Ciclos**  

 O **FlowED** **não impõe uma transição obrigatória entre ciclos**, pois cada equipe e projeto evolui de acordo com sua própria experiência. No entanto, a metodologia fornece **critérios rastreáveis e um modelo inicial sólido**, permitindo que a progressão ocorra de maneira orgânica, sem burocracia imposta.  

 > **A rastreabilidade é garantida por changelogs, backlog e documentação mínima obrigatória**, assegurando que qualquer mudança de ciclo seja documentada e acessível para todos os envolvidos.  

 Esse modelo assegura que:

- Cada equipe se **autoeduque**, evoluindo naturalmente conforme suas necessidades e registrando suas adaptações.
- A adaptação aos diferentes **tamanhos de equipe** ocorra de forma fluida, garantindo que projetos pequenos cresçam sem barreiras e que times maiores escalem sem engessamento.
- As alterações nos ciclos sejam **revisadas e justificadas**, garantindo um aprendizado progressivo, sem perda de identidade ou boas práticas.  

### 🔹 Conclusão: Rastreabilidade, progressividade e adaptabilidade com autonomia

 O **FlowED** permite que cada projeto cresça **sem limitações artificiais**, mantendo flexibilidade sem comprometer a rastreabilidade. Seu modelo se baseia em **princípios sólidos**, mas a evolução **é conduzida pelo próprio projeto e pelo aprendizado contínuo do time**.

 > **A estrutura é flexível, mas não arbitrária: a documentação e a rastreabilidade garantem que o progresso seja estruturado, consciente e alinhado com os objetivos do projeto.**

## 🌍 Ecossistema FlowED  

O `FlowED` possui um ecossistema integrado que cobre **versionamento, documentação, infraestrutura e processos de desenvolvimento**, garantindo que todas as fases do projeto sejam rastreáveis e estruturadas desde o início.  

Os projetos do ecossistema foram projetados para funcionar de forma **independente ou integrada**, permitindo que cada equipe adote apenas os elementos necessários para seu contexto. Cada repositório fornece **ferramentas práticas** para implementar os princípios fundamentais da metodologia.  

> **A metodologia prioriza a adoção dos conceitos essenciais desde o início do projeto, garantindo que as boas práticas sejam incorporadas progressivamente e refinadas conforme a equipe evolui.**  

### 🚀 **Por que um ecossistema integrado?**

- Desde o início, todos os projetos aplicam **os princípios da engenharia de software**, independentemente do nível de maturidade do time.  
- O objetivo não é impor um modelo rígido, mas fornecer **uma base rastreável** para que projetos evoluam sem perder coerência.  
- A eficiência **não é um pré-requisito inicial**, mas uma **consequência natural do aprendizado e da experiência acumulada**.  

A seguir, os repositórios que compõem o ecossistema do `FlowED` e como cada um se alinha à metodologia.  

### [ISO29110-Lite](https://github.com/SysDevTools/ISO29110-Lite)  

 Adapta e simplifica a norma **ISO/IEC 29110**, fornecendo um modelo de documentação e rastreabilidade adequado a projetos de diferentes tamanhos. No `FlowED`, o **ISO29110-Lite** garante que a documentação evolua junto com o projeto, sem sobrecarga, estruturando processos desde o início.  

 Além do [README](https://github.com/SysDevTools/ISO29110-Lite/README.md) do repositório, mais informações sobre sua integração com o `FlowED` estão disponíveis em:  
🔹 **[FlowED <-> ISO29110-Lite](./docs/pt-br/philosophy/iso29110-lite-alignment.md)**  

### [WSL-PortableEnv](https://github.com/SysDevTools/WSL-PortableEnv)  

 Proporciona ambientes de desenvolvimento isolados, versionáveis e portáveis. No `FlowED`, garante que cada projeto tenha um ambiente reprodutível, evitando inconsistências entre desenvolvimento, homologação e produção.  

 Ele permite que times trabalhem com configurações padronizadas e replicáveis, garantindo rastreabilidade e estabilidade desde o início do projeto.

 Através de templates disponibilizados no repositório, cria a cultura do versionamento, da padronização, do isolamento e da reprodutividade do ambiente de desenvolvimento, adicionando-o ao versionamento e controles do projeto.

 > **A metodologia defende que um ambiente de desenvolvimento deve ser completamente portável, reprodutível e versionável Assim, todo o poder e eficiência de um ambiente deve primeiramente satisfazer a sua portabilidade.**

 Além do [README](https://github.com/SysDevTools/WSL-PortableEnv/README.md) do repositório, mais informações sobre sua integração com o `FlowED` estão disponíveis em:  
🔹 **[FlowED <-> WSL-PortableEnv](./docs/pt-br/philosophy/wsl-portableenv-alignment.md)**  

### [Dec-B](https://github.com/SysDevTools/Dec-B)  

 O `Dec-B` é, ao mesmo tempo, um workflow estruturado para versionamento e um framework auxiliar para automação de `Git`. No `FlowED`, ele padroniza processos de versionamento, garantindo que a rastreabilidade e a organização do código evoluam de maneira estruturada e progressiva.  

 Diferente de ferramentas que impõem abstrações sobre o `Git`, o `Dec-B` auxilia sem acoplar. Ele sugere fluxos padronizados, verifica se os comandos seguem as boas práticas do `FlowED` e fornece um **wizard interativo**, permitindo que desenvolvedores iniciantes executem operações complexas de forma progressiva. À medida que ganham experiência, podem substituir o `Dec-B` pelo `Git` puro sem fricção.  

 O `Dec-B` contém comandos específicos alinhados com o `FlowED`, garantindo padronização em:  
🔹 Nomenclatura e ciclo de vida das branches.  
🔹 Estrutura mínima obrigatória de backlog e changelog.  
🔹 Automação de processos como início e encerramento de releases e features.  

 Além do [README](https://github.com/SysDevTools/Dec-B/README.md) do repositório, mais informações sobre sua integração com o `FlowED` estão disponíveis em:  
🔹 **[FlowED <-> Dec-B](./docs/pt-br/philosophy/dec-b-alignment.md)**  

## Por onde começar

O **FlowED** não exige ferramentas específicas, mas oferece um fluxo estruturado para que qualquer projeto possa evoluir progressivamente.
Quem desejar pode seguir o método manualmente, enquanto quem busca eficiência pode contar com a automação do **Dec-B**.
Assim, para adotar a metodologia do **FlowED** em um projeto, há dois caminhos recomendados e mantidos pos este repositório:

1️⃣ **Usando o Dec-B** (automação recomendada) → O `Dec-B` verifica a existência de um repositório remoto, estrutura o versionamento inicial e clona os templates do `ISO29110-Lite` para configurar a documentação mínima necessária.

2️⃣ **Configuração manual** → Seguindo a estrutura metodológica do `FlowED`, o repositório pode ser montado manualmente, garantindo que os documentos essenciais sejam incluídos e versionados corretamente.

### 🔹 Automação com Dec-B

 Se estiver usando o **Dec-B**, a criação do repositório `FlowED` ocorre automaticamente ao iniciar um novo projeto. O `Dec-B`:

✅ Verifica se o repositório já existe e está configurado corretamente.

✅ Clona os templates do `ISO29110-Lite` e gera os **POP’s** iniciais necessários para a rastreabilidade do projeto. 

✅ Define as **branches base** conforme o nível de implantação escolhido (`Mono Dev`, `Mono Release Dev` ou `Feature Dev`). 

✅ Organiza a **documentação inicial** (`README.md`, `CHANGELOG.md`, `BACKLOG.md`). 

✅ Proporciona comandos para versionamento contínuo dos documentos.

🔎 Para uma análise detalhada essa abordagem, consulte **[Automação com Dec-B](./docs/pt-br/adoption/dec-b-integration.md)**

### 🔹 Configuração Manual

Se preferir seguir o **FlowED** sem automação, os mesmos princípios podem ser aplicados manualmente:

1️⃣ Criar a estrutura base do repositório seguindo os padrões do `FlowED`.

2️⃣ Adicionar os arquivos essenciais (`README.md`, `CHANGELOG.md`, `BACKLOG.md`).

3️⃣ Clonar ou adaptar os templates do `ISO29110-Lite` manualmente.

4️⃣ Configurar o fluxo de versionamento com base no nível de implantação adotado.

🔎 Para uma análise detalhada sobre essa abordagem, consulte **[Estrutura manual de um projeto FlowED](./docs/pt-br/adoption/manual-setup.md)**

## Contribuição

Para contribuir com o projeto `FlowED`, siga estas etapas:

1. Crie um fork do repositório.
2. Clone o seu fork para sua máquina local.
3. Crie uma branch para a sua contribuição.
4. Faça as alterações necessárias e commit.
5. Envie suas alterações para o seu fork.
6. Crie um Pull Request descrevendo suas alterações.

Para mais detalhes sobre como contribuir, consulte o [Guia de Contribuição](./docs/pt-br/guide.md).

---

## Contato

Para dúvidas ou sugestões, entre em contato através do email: <contato@flowed.org>

---

## Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo [LICENSE](./LICENSE) para mais detalhes.
