# Seleção do primeiro piloto de domínio FlowED

**Status:** decisão de trabalho provisória; ainda não normativa.

## Contexto

Após estabilizar parcialmente a hipótese de uma linguagem pública comum do FlowED — com `flwd` como cliente e CLI/YAML/API/SDK/UI/agents falando o mesmo contrato semântico — é necessário escolher um primeiro recorte de domínio para estruturar de forma concreta.

Dois candidatos imediatos foram considerados:

1. `ISO29110-lite`;
2. `InitProj POC`.

## Critérios de escolha

O primeiro piloto deve maximizar aprendizagem arquitetural com custo baixo. Deve, preferencialmente:

- produzir operações reais e observáveis;
- exercitar verbo + parâmetros + opções e equivalente declarativo;
- exigir múltiplos materializadores/adapters ou pelo menos admitir sua substituição;
- possuir fronteira suficientemente pequena para um POC;
- expor rapidamente gaps na linguagem comum, contracts e progressividade;
- permitir dogfood sem depender de certificação ou de uma taxonomia normativa já fechada;
- ter relação com artefatos e fluxos já existentes, para evitar inventar um cenário artificial.

## Comparação preliminar

### ISO29110-lite

Vantagens:
- traz uma referência normativa externa e força o FlowED a provar que consegue materializar uma referência sem tratá-la como implementação única;
- é excelente para testar baseline, alinhamento, intensidade e projeção normativa;
- pode se tornar um caso forte de Adapt First.

Riscos neste momento:
- pode misturar cedo demais problemas de interpretação normativa, copyright/licenciamento, baseline e score com problemas básicos da linguagem operacional;
- existe risco de desenhar o primeiro domínio em torno da norma em vez de testar a generalidade do FlowED;
- o recorte “lite” ainda precisaria ser formalmente definido.

### InitProj POC

Vantagens:
- já possui intenção operacional clara: transformar um contexto inicial de projeto em uma estrutura executável/reprodutível;
- possui ações, estado desejado, arquivos, Git, sessões/agents, templates e possíveis adapters;
- exercita naturalmente CLI, YAML e API sobre a mesma língua;
- possui alta capacidade de dogfood porque o próprio FlowED e outros projetos podem ser inicializados por ele;
- expõe cedo a fronteira entre linguagem pública e comportamento interno;
- permite começar pequeno e depois ligar ISO 29110, Scrum, XP ou outro baseline como profiles/references, sem tornar a norma o próprio domínio.

Riscos:
- InitProj pode carregar decisões históricas específicas demais se não separarmos capability de implementação existente;
- é necessário evitar transformar “InitProj atual” em contrato canônico por acidente.

## Recomendação provisória

Escolher **InitProj POC como primeiro piloto de domínio/capability**, e usar **ISO29110-lite como um dos primeiros profiles/baselines que deverão ser materializados sobre esse piloto**.

A razão principal é metodológica: primeiro testar a língua operacional e a arquitetura com um problema executável e conhecido; depois testar se uma referência normativa externa consegue entrar sem contaminar o domínio com sua própria estrutura.

A sequência recomendada é:

**InitProj mínimo → contrato público FlowED → CLI/YAML equivalentes → materialização local/Git → profile simples → ISO29110-lite como profile/reference → comparação com outro profile não-ISO.**

Isso permitirá testar tanto generalidade quanto Adapt First.

## Próxima ação sugerida

Não portar o InitProj inteiro. Escolher uma capability mínima, provavelmente **`project.init`** ou equivalente ainda a nomear, e modelar:

- objetivo;
- inputs;
- outputs;
- invariantes;
- estados observáveis;
- erros públicos;
- CLI;
- YAML equivalente;
- contrato de adapter/materializer;
- critérios de idempotência/reexecução;
- evidence/receipt mínimo.

A escolha do nome e da semântica deve passar pelo intake e pelo Discovery do próprio FlowED antes de ser consolidada.
