# Medição, certificação e risco — notas de trabalho

**Status:** hipóteses de produto e pesquisa — não normativas

## 1. Dimensões independentes

O modelo atual separa ao menos quatro dimensões:

- **FlowED Compliance** — quanto a organização segue o mecanismo FlowED de explicitação, proveniência, avaliação e evolução das decisões.
- **Baseline Alignment vX** — quanto a organização coincide com uma versão identificada do baseline.
- **Epistemic Maturity** — qualidade global do tratamento organizacional do conhecimento e das decisões.
- **Evidence Strength** — força da sustentação de uma referência, possivelmente decomposta em científica, normativa, empírica e outras categorias.

Essas dimensões não devem ser reduzidas prematuramente a um único número.

Uma leitura categorial provisória pode distinguir, por exemplo, Full FlowED + Full Baseline, Full FlowED + Baseline divergente, Partial FlowED + alta afinidade de baseline e Partial FlowED + baixa afinidade. Os nomes ainda são de trabalho.

## 2. Superar o baseline

Uma organização pode ter menor afinidade com o baseline e, ao mesmo tempo, referências mais bem sustentadas que as correspondentes do baseline.

Isso deve ser visível. O baseline precisa ter score próprio e pode ser superado.

Uma organização pode inclusive adotar políticas como:

- não aceitar mudanças que reduzam score abaixo da referência atual;
- não aceitar referências abaixo do baseline aplicável;
- aceitar divergência apenas quando ela iguala ou supera a sustentação do baseline;
- permitir quedas temporárias controladas para experimentação.

Superar o baseline pode se tornar sinal reputacional verificável. Uma empresa pode demonstrar que determinadas referências são mais bem sustentadas que as equivalentes do baseline, em vez de apenas alegar excelência. Esse uso reputacional precisa permanecer associado à versão concreta do baseline e às evidências auditáveis.

## 3. Certificação não binária

Investigar certificação determinística e não binária. Em vez de apenas conforme/não conforme, a certificação poderia produzir um vetor versionado e auditável de resultados.

Exemplo meramente ilustrativo:

- FlowED Compliance: 98%
- Baseline v4.2 Alignment: 73%
- Scientific Evidence: 81%
- Other Evidence: 92%
- referências de score zero: 7
- divergências acima do baseline: 3

Os nomes e a matemática ainda precisam ser pesquisados.

## 4. Determinismo

Objetivo: dadas as mesmas entradas, regras e evidências, dois avaliadores ou validadores devem chegar ao mesmo resultado nas partes objetivamente verificáveis.

Onde houver julgamento humano, isso deve ficar explicitamente identificado e separado do componente determinístico.

## 5. Relatório de pontos fracos

Ferramenta candidata: produzir um mapa de fragilidade organizacional com base em compliance FlowED, força das referências, distância do baseline, referências de baixa sustentação, divergências e lacunas de evidência.

Possíveis usos:

- priorização de melhoria contínua;
- consultoria focada nos pontos de menor sustentação;
- diagnóstico de risco;
- auditoria direcionada;
- avaliação de fornecedores;
- comparação histórica da evolução da organização.

## 6. Avaliação de fornecedores

Hipótese de produto e pesquisa: um cliente poderia conhecer a maturidade epistemológica e a sustentação das práticas técnicas de um fornecedor de software, em vez de depender apenas de declarações genéricas de processo.

Isto não deve ser apresentado como medida absoluta de qualidade de software antes de validação empírica. Deve-se pesquisar correlação com defeitos, risco, produtividade, previsibilidade, segurança, qualidade e outros resultados.

## 7. Maturidade epistemológica

Nome de trabalho preferido neste momento: **maturidade epistemológica**.

Ela procura medir quão bem a organização sabe o que considera conhecimento, por que confia nele, qual a força da sustentação, onde existem incertezas, como divergências são registradas e como o conhecimento evolui.

"Qualidade científica" parece estreito demais. "Maturidade epistemológica científica" também exclui evidências não científicas relevantes.

## 8. Evolução como característica cultural

O histórico de mudanças pode caracterizar o perfil cultural da organização. Uma empresa conservadora e criteriosa terá trajetória diferente de uma empresa altamente experimental.

Não se deve presumir que uma das duas seja melhor. O objetivo é medir e tornar explícito o perfil decisório.

Possíveis dimensões futuras:

- frequência de mudanças;
- amplitude das mudanças;
- velocidade de adoção;
- força da evidência exigida antes da mudança;
- quantidade de reversões;
- tempo de recuperação de experimentos malsucedidos;
- capacidade de aprender e estabilizar;
- exposição simultânea a mudanças.

## 9. Risco-FlowED

Nome de trabalho para uma ferramenta/índice análogo à ideia de "risco-país", porém aplicado ao risco de evolução da cultura de engenharia de uma organização.

O risco não deve ser confundido com mera frequência de mudança. Uma empresa que experimenta muito com isolamento, limites e recuperação pode ter menor risco que outra que muda menos, mas sem controle.

Este conceito requer pesquisa de anterioridade e validação própria.

## 10. Queda deliberada de score

Uma política que proíba qualquer queda de score pode produzir conservadorismo estrutural e bloquear inovação.

Hipótese: organizações devem poder assumir uma dívida ou exposição epistemológica deliberada para experimentar uma referência inicialmente de score baixo ou zero, desde que existam limites, observação, critérios de saída e possibilidade de recuperação.

Analogia de trabalho: reformar o restaurante sem deixar de servir. Em certos momentos, uma parte precisa ser desmontada para poder ser reconstruída melhor.

## 11. Velocidade de evolução

Hipótese adicional: além do estado atual, a trajetória pode ser relevante. Uma organização que evolui de forma sustentada pode apresentar uma característica de maturidade diferente de outra com score semelhante, porém estagnada.

Não transformar essa ideia em métrica antes de pesquisa específica.

## 12. Tempo como rendimento de evidência

Intuição de trabalho: uma referência em execução pode "render juros" epistemológicos ao longo do tempo, mesmo sem se transformar em paper e mesmo sem adoção externa. Essa metáfora não implica que duração sozinha prove verdade.

A hipótese a pesquisar é se exposição longitudinal bem observada — tempo, quantidade de execuções, contextos, sucessos, falhas, reversões e estabilidade — pode aumentar de forma calculável uma parcela da sustentação operacional da referência.
