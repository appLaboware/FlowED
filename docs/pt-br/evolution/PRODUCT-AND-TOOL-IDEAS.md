# Produtos e ferramentas derivados — notas de trabalho

**Status:** ideias de produto — não comprometem roadmap

## 1. Baseline Manager

Gerenciar baselines FlowED por versão, incluindo referências, scores, histórico de mudanças e comparação entre versões.

## 2. Alignment Analyzer

Calcular afinidade de uma organização/projeto com um baseline FlowED específico, sem confundir afinidade com compliance ou maturidade epistemológica.

## 3. Evidence Scorer

Avaliar a sustentação de uma referência por categorias de evidência. A matemática e os pesos dependem de pesquisa própria e não devem ser inventados no produto antes disso.

### 3.1 Classificador composto de opinião — produto de referência

Evolução da ideia de `Evidence Scorer`: manter uma implementação de referência capaz de consumir bons indicadores científicos, bibliométricos e operacionais já disponíveis e produzir uma **opinião quantitativa composta**, explicitamente não autoritativa.

Princípios:

- o classificador não define verdade;
- sua saída é uma opinião reproduzível baseada em métricas e metodologia versionada;
- ele possui o mesmo peso contratual de qualquer classificador concorrente;
- equipes podem usar outro provider ou comparar vários;
- os dados e componentes subjacentes permanecem visíveis;
- métricas semelhantes devem ser agrupadas por família para evitar dupla contagem;
- normalização, pesos, agregação e tratamento de missing data devem ser públicos/versionados;
- análise de robustez/sensibilidade é desejável antes de promover uma fórmula a baseline do produto.

Base metodológica principal: literatura de **composite indicators**, especialmente o *OECD/JRC Handbook on Constructing Composite Indicators*, combinada com princípios de responsible research assessment (DORA/Leiden).

Documento de aprofundamento: `PILAR-3-REFERENCE-OPINION-CLASSIFIER-DRAFT.md`.

Naming comercial permanece aberto.

## 4. Epistemic Weakness Report

Gerar relatório de pontos fracos com foco em referências de menor sustentação, ausência de evidência, divergências frágeis e gaps de compliance.

Uso principal: priorizar melhoria contínua e consultoria.

## 5. Supplier Evidence Profile

Produzir perfil verificável de maturidade epistemológica e sustentação das práticas de um fornecedor de software para apoiar clientes em avaliação de risco.

Não vender como garantia absoluta de qualidade antes de validação empírica.

## 6. Deterministic Certification Engine

Motor para certificação não binária e versionada. Deve separar regras determinísticas de avaliações humanas explícitas.

Saída esperada: vetor de compliance, alinhamento, força de evidência, divergências, gaps e histórico.

## 7. Evolution Risk / Risco-FlowED

Ferramenta para caracterizar o risco do comportamento evolutivo da cultura técnica da organização, considerando não apenas frequência de mudança, mas amplitude, reversibilidade, força de evidência, recuperação e exposição.

## 8. Epistemic Change Gate

Gate para mudanças organizacionais e técnicas baseado em política configurável. Exemplos:

- bloquear regressão de sustentação;
- exigir piso relativo ao baseline;
- permitir divergência somente com sustentação equivalente ou superior;
- abrir janela experimental com score reduzido e critérios de saída.

## 9. Experimental Reference Sandbox

Suportar adoção controlada de referências inicialmente de score baixo ou zero, acompanhando exposição, resultados, falhas, duração e aprendizado.

## 10. Longitudinal Evidence Collector

Coletar evidência operacional ao longo do tempo: duração de uso, quantidade de projetos, contextos, incidentes, resultados, reversões e outras observações relevantes.

Seu score depende do futuro modelo científico de evidência; o coletor não deve inventar peso próprio.

## 11. Research Gap Miner

Identificar referências de baixa sustentação e divergências recorrentes entre organizações que possam representar lacunas relevantes de pesquisa.

Objetivo: transformar prática industrial em fonte organizada de perguntas para academia.

## 12. Academia–Indústria Bridge

Materializar a mesma linguagem operacional em contextos educacionais e empresariais, permitindo que capacidades e intensidade cresçam sem troca completa do modelo mental do usuário.

## 13. Baseline Challenger

Comparar referências organizacionais com as correspondentes do baseline e destacar pontos em que uma organização apresenta sustentação superior. Pode servir tanto para melhoria do próprio baseline quanto para reputação verificável da organização.

## 14. Evolution Dashboard

Visualizar estado atual e trajetória: alinhamento por versão, compliance, maturidade epistemológica, mudanças, regressões, avanços, experimentos e pontos em que a organização superou o baseline.

## 15. Consultoria orientada por gaps

Produto/serviço de consultoria que não começa auditando tudo do zero. O consultor recebe o mapa de baixa sustentação e atua prioritariamente nos pontos de maior fragilidade, risco ou incerteza.
