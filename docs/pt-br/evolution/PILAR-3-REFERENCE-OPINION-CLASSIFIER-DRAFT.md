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
- deve identificar claramente sua metodologia, versão, dados de entrada e limitações.

A organização pode escolher outro provider de assessment. O classificador de referência existe para garantir que o ecossistema FlowED possua uma alternativa utilizável e reproduzível desde o início.

## 2. Princípio

O produto recebe observações já preservadas pelo contrato do Pilar 3, normaliza indicadores compatíveis, compõe dimensões e produz uma projeção quantitativa resumida.

A saída deve ser tratada explicitamente como uma **opinião baseada em métricas**.

Regra:

> **dados observados + metodologia versionada = opinião reproduzível; opinião não equivale a verdade.**

## 3. Prior art para indicadores compostos

A construção de indicadores compostos possui metodologia estabelecida. O *Handbook on Constructing Composite Indicators* da OECD/JRC trata explicitamente de:

- seleção de indicadores;
- normalização de escalas diferentes;
- pesos;
- agregação;
- correlação entre indicadores;
- compensabilidade entre dimensões;
- métodos alternativos de composição;
- análise de incerteza e sensibilidade;
- transparência da metodologia.

Isso permite tratar o classificador como uma composição metodologicamente disciplinada em vez de inventar uma média arbitrária.

Ao mesmo tempo, DORA e Leiden alertam que um único número pode ocultar diferenças importantes e que indicadores compostos arbitrariamente ponderados podem ser difíceis de interpretar. Portanto, o produto deve sempre expor o score agregado junto com sua decomposição e provenance.

## 4. Horizonte de arquitetura

Fluxo candidato:

**providers de evidência -> observações normalizadas -> famílias de indicadores -> composição versionada -> OpinionScore + decomposição + robustez + provenance**.

Os providers de evidência podem incluir, conforme disponibilidade:

- OpenAlex;
- Crossref;
- Semantic Scholar;
- SciVal/Scopus;
- Dimensions;
- Web of Science/InCites;
- evidência operacional proveniente do Pilar 2;
- outras fontes compatíveis com o contrato.

O classificador não precisa conhecer internamente todos os providers. Ele deve consumir o contrato semântico comum do Pilar 3.

## 5. Evitar dupla contagem

Métricas diferentes podem medir fenômenos muito semelhantes. FWCI, CNCI e FCR, por exemplo, pertencem todos à família de impacto de citação normalizado por campo.

Portanto, o classificador não deve simplesmente somar cada métrica disponível como se representasse evidência independente.

Direção preferida:

1. classificar cada observação em uma **família semântica**;
2. normalizar métricas dentro dessa família;
3. produzir um score da família;
4. somente então combinar famílias diferentes.

Famílias candidatas, ainda não normativas:

- reconhecimento científico formal;
- influência científica normalizada;
- estado/integridade da referência;
- evidência operacional;
- qualidade/completude de provenance.

## 6. Normalização

A proposta de converter indicadores para percentuais ou valores proporcionais é realizável, mas não deve pressupor que toda métrica tenha máximo natural.

Três casos precisam ser distinguidos:

- métricas naturalmente limitadas, como percentis, podem ser mapeadas diretamente para uma escala comum;
- métricas centradas em uma referência, como FWCI/FCR/CNCI em torno de 1.0, exigem função de transformação documentada;
- métricas sem máximo natural, como contagem bruta de citações ou tempo de operação, precisam de normalização contextual, distribuição de referência, percentil, transformação ou teto versionado justificável.

A função usada em cada classe é parte da metodologia pública do classificador.

## 7. Score opinativo

O produto pode expor um `OpinionScore`, possivelmente em escala 0–100 para facilitar comunicação, desde que:

- a escala seja declarada como projeção do classificador;
- os componentes permaneçam disponíveis;
- pesos e transformações sejam públicos/versionados;
- dados ausentes não sejam inventados;
- diferenças de cobertura sejam sinalizadas;
- a robustez do score possa ser informada;
- o resultado seja recalculável a partir do snapshot de entrada.

O score não substitui o vetor de evidências do contrato FlowED.

## 8. Peso e agregação

Não congelar pesos nesta fase.

A OECD/JRC recomenda que a escolha de pesos e método de agregação seja ligada ao framework teórico, que métodos alternativos sejam considerados e que correlação/compensabilidade sejam discutidas.

O produto de referência deve, portanto, tratar sua composição como uma **policy/method versionada**.

Uma primeira implementação experimental pode começar com um modelo simples e explícito, mas ele só se torna baseline do próprio classificador depois de análise de sensibilidade e validação.

## 9. Robustez e sensibilidade

Uma propriedade desejável do produto é mostrar quanto a opinião muda quando variam:

- provider de dados;
- método de normalização;
- pesos;
- inclusão/exclusão de uma família;
- dados faltantes;
- janela temporal.

Isso permite produzir, além do score pontual, uma indicação de robustez ou intervalo de variação da própria opinião.

Essa propriedade vem diretamente da prática de construção de composite indicators e reduz a falsa precisão.

## 10. Contrato público esperado para classificadores

O contrato do Pilar 3 deve permitir que qualquer classificador retorne, no mínimo:

- `classifier_id`;
- `classifier_version`;
- `method_id` / `method_version`;
- score/opinião agregada, se o provider produzir uma;
- escala e interpretação;
- componentes/dimensões;
- observações e snapshots usados;
- normalizações aplicadas;
- pesos/agregação;
- tratamento de missing data;
- warnings/conflitos;
- robustez/incerteza quando calculada;
- provenance;
- timestamp do assessment.

O contrato não obriga todo provider a produzir exatamente a mesma fórmula nem a mesma escala. Ele obriga a tornar o resultado interpretável, rastreável e comparável em nível contratual.

## 11. Relação com o Pilar 1

Este produto é uma consequência direta do Pilar 1:

- o FlowED define o contrato;
- o classificador de referência é um provider;
- classificadores concorrentes podem implementar o mesmo contrato;
- uma organização pode escolher outro provider ou vários;
- nenhuma opinião recebe autoridade especial apenas por ser desenvolvida pela LaboWare/FlowED.

## 12. Relação com o Pilar 2

A evidência operacional do Pilar 2 pode alimentar uma ou mais dimensões do classificador, mas permanece distinguível da evidência científica.

Tempo de uso, quantidade de exposições, diversidade de contexto, sucessos, falhas e recência podem ser incorporados por uma metodologia versionada sem serem confundidos com reconhecimento científico.

## 13. Relação com o Pilar 3

O classificador de referência materializa o princípio do Pilar 3 sem ampliar a claim do manifesto.

O Pilar 3 continua dizendo que sustentação deve ser explícita, rastreável e avaliável. O classificador oferece **uma opinião quantitativa possível** sobre essa base.

A organização continua livre para:

- usar apenas o vetor de evidências;
- usar o classificador de referência;
- usar outro classificador;
- comparar vários classificadores;
- aplicar políticas próprias sobre os resultados.

## 14. Estado

**Realizabilidade:** forte em nível conceitual e metodológico.

Há tecnologia para obter indicadores, contratos para expor observações e metodologia consolidada para construção de indicadores compostos. O trabalho residual é definir e validar a composição específica.

**Rota:** COMPOSE / EXPERIMENTAL PRODUCT.

**Naming:** aberto. Não consolidar nome comercial nesta fase.
