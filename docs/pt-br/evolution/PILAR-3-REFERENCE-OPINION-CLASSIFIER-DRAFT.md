# Pilar 3 — classificador de opinião composto como implementação de referência

**Status:** candidato a produto / implementação de referência. Não normativo. Não define a verdade nem o score canônico do FlowED.

## 1. Decisão desta rodada

Antes de avançar ao Pilar 4, o Pilar 3 deve possuir não apenas um horizonte de contrato, mas também uma alternativa concreta de materialização que alguém possa implementar posteriormente.

A decisão é manter um **classificador composto de referência** que reúna bons indicadores externos já praticados e produza uma **opinião quantitativa versionada** sobre a sustentação de uma referência.

Esse classificador terá exatamente o mesmo estatuto de qualquer outro provider compatível com o contrato FlowED:

- não é autoridade do FlowED;
- não define verdade;
- não é obrigatório;
- pode ser substituído por outro classificador;
- pode coexistir com classificadores concorrentes;
- sua confiabilidade, validade e qualidade metodológica são problema do próprio classificador, não do contrato FlowED.

A organização pode escolher outro provider de assessment. O classificador de referência existe para garantir que o ecossistema FlowED possua uma alternativa utilizável e reproduzível desde o início.

## 2. Princípio

O produto recebe observações já preservadas pelo contrato do Pilar 3, normaliza indicadores compatíveis, compõe dimensões e produz uma projeção quantitativa resumida.

A saída deve ser tratada explicitamente como uma **opinião baseada em métricas**.

Regra:

> **dados observados + metodologia versionada = opinião reproduzível; opinião não equivale a verdade.**

Cumprir o contrato FlowED demonstra conformidade de interface/comportamento. Não demonstra que a opinião do classificador é cientificamente ou empiricamente confiável. Essa sustentação pertence ao próprio provider e pode ser avaliada separadamente como uma Referência FlowED.

## 3. Prior art para indicadores compostos

A construção de indicadores compostos possui metodologia estabelecida. O *Handbook on Constructing Composite Indicators* da OECD/JRC trata explicitamente de seleção de indicadores, normalização, pesos, agregação, correlação, compensabilidade, métodos alternativos e análise de sensibilidade.

Isso permite tratar o classificador como composição metodologicamente disciplinada em vez de inventar uma média arbitrária.

O produto deve sempre expor o score agregado junto com sua decomposição e provenance.

## 4. Horizonte de arquitetura

Fluxo candidato:

**providers de evidência -> observações normalizadas -> famílias de indicadores -> composição versionada -> OpinionScore + decomposição + provenance**.

Os providers de evidência podem incluir OpenAlex, Crossref, Semantic Scholar, SciVal/Scopus, Dimensions, Web of Science/InCites, evidência operacional proveniente do Pilar 2 e outras fontes compatíveis.

O classificador deve consumir o contrato semântico comum do Pilar 3, e não depender conceitualmente de um provider específico.

## 5. Evitar dupla contagem

Métricas diferentes podem medir fenômenos muito semelhantes. FWCI, CNCI e FCR, por exemplo, pertencem todos à família de impacto de citação normalizado por campo.

Portanto, o classificador não deve simplesmente somar cada métrica disponível como se representasse evidência independente.

Direção preferida:

1. classificar cada observação em uma família semântica;
2. normalizar métricas dentro dessa família;
3. produzir uma opinião da família;
4. somente então combinar famílias diferentes.

Famílias candidatas, ainda não normativas:

- reconhecimento científico formal;
- influência científica normalizada;
- estado/integridade da referência;
- evidência operacional;
- qualidade/completude de provenance.

## 6. Normalização e métricas sem máximo

A proposta de converter indicadores para percentuais ou valores proporcionais é realizável quando existe máximo natural ou uma escala já normalizada.

Quando **não existe máximo natural**, a direção preferida é **não inventar um teto**. O classificador deve preferir posição relativa em uma população declarada:

- `rank` — posição ordinal dentro da população de referência;
- `percentile` — posição relativa normalizada, preferível quando se deseja projetar a observação para uma escala comum como 0–100;
- `top_k_percent` ou faixas equivalentes quando a fonte já as oferece.

Exemplo conceitual: quantidade bruta de citações não possui máximo. Em vez de criar arbitrariamente um valor máximo, a ferramenta pode determinar a posição daquela referência entre trabalhos comparáveis por área, tipo e período e converter essa posição em percentil.

O mesmo raciocínio pode ser usado, quando houver população comparável defensável, para outras variáveis sem teto natural, como volume de adoção ou exposição operacional.

A população de referência é parte indispensável da opinião. Um rank sem declarar **contra quem** se está comparando não é suficientemente interpretável.

Portanto, qualquer transformação por ranking/percentil deve preservar pelo menos:

- população/universo de comparação;
- filtros usados;
- tamanho da população;
- momento/snapshot da comparação;
- tratamento de empates;
- direção da métrica (maior é melhor, menor é melhor ou contextual);
- provider/fonte;
- versão da regra.

**Ranking pertence à metodologia do classificador, não ao contrato normativo do FlowED.** O contrato apenas precisa ser capaz de transportar e explicar essa opinião.

## 7. Score opinativo

O produto pode expor um `OpinionScore`, possivelmente em escala 0–100 para facilitar comunicação, desde que a escala seja declarada como projeção do classificador e os componentes permaneçam disponíveis.

Uma estratégia candidata é converter famílias heterogêneas para posições relativas/percentis sempre que houver população defensável e, a partir dessas posições, produzir a opinião composta.

Isso não torna percentil universalmente superior: quando uma métrica já possui semântica normalizada própria, o classificador pode preservá-la. A escolha é responsabilidade da metodologia versionada do provider.

## 8. Peso e agregação

Não congelar pesos nesta fase.

O produto de referência deve tratar composição como uma **policy/method versionada**. Uma primeira implementação experimental pode começar simples, mas sua qualidade é responsabilidade do próprio produto e precisa ser sustentada por validação, não pelo contrato FlowED.

## 9. Robustez e sensibilidade

Uma propriedade desejável do produto é mostrar quanto a opinião muda quando variam provider de dados, população de ranking, método de normalização, pesos, inclusão/exclusão de uma família, dados faltantes ou janela temporal.

Isso permite caracterizar a estabilidade da própria opinião sem fazer dessa característica uma obrigação universal de todos os classificadores.

## 10. Contrato público esperado para classificadores

O contrato do Pilar 3 deve permitir que qualquer classificador retorne uma opinião de modo interpretável, incluindo identidade/versão do classificador, valor e escala, momento da avaliação, provenance e metadados necessários para entender o resultado.

Quando o provider decidir expor decomposição, ranking, percentil, pesos, incerteza ou robustez, o contrato deve ser extensível o suficiente para transportá-los sem transformar essas escolhas metodológicas em obrigação normativa universal.

## 11. Relação com o Pilar 1

Este produto é consequência direta do Pilar 1:

- o FlowED define o contrato;
- o classificador de referência é um provider;
- classificadores concorrentes podem implementar o mesmo contrato;
- uma organização pode escolher outro provider ou vários;
- nenhuma opinião recebe autoridade especial apenas por ser desenvolvida pela LaboWare/FlowED.

## 12. Relação com o Pilar 2

A evidência operacional do Pilar 2 pode alimentar uma ou mais dimensões do classificador, mas permanece distinguível da evidência científica.

Tempo de uso, quantidade de exposições, diversidade de contexto, sucessos, falhas e recência podem ser incorporados por metodologia própria do classificador.

## 13. Relação com o Pilar 3

O classificador de referência materializa o princípio do Pilar 3 sem ampliar a claim do manifesto.

O Pilar 3 continua dizendo que sustentação deve ser explícita, rastreável e avaliável. O classificador oferece **uma opinião quantitativa possível** sobre essa base.

A organização continua livre para usar apenas o vetor de evidências, usar o classificador de referência, usar outro, comparar vários ou aplicar políticas próprias.

## 14. Estado

**Realizabilidade:** forte em nível conceitual e metodológico.

Há tecnologia para obter indicadores, contratos para expor observações e metodologia consolidada para construção de indicadores compostos. O trabalho residual é definir e validar a composição específica.

**Rota:** COMPOSE / EXPERIMENTAL PRODUCT.

**Naming:** aberto. Não consolidar nome comercial nesta fase.
