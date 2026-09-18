# Draft — Pilar 3: scoring determinístico de sustentação

**Status:** Referência Experimental para fechamento do Pilar 3 do Manifesto FlowED.

## 1. Correção de linguagem

O FlowED não deve chamar publicação, citação ou uso prolongado de medição de "verdade". Esses sinais medem tipos diferentes de **sustentação, reconhecimento, influência e evidência operacional**.

Uma referência pode ser operacionalmente adotada sem publicação científica e ainda acumular forte evidência contextual. Da mesma forma, uma publicação científica pode possuir pouco uso operacional ou vir a ser contradita posteriormente.

## 2. Proposta do usuário preservada

A proposta é construir um score determinístico a partir de sinais externos, evitando que o próprio FlowED invente arbitrariamente autoridade:

1. existência de reconhecimento científico formal;
2. relevância/influência científica observável por citações;
3. tempo e experiência de operação da referência;
4. quando houver métrica externa do veículo, usá-la como informação adicional em vez de atribuir prestígio manualmente.

Uma organização continua livre para adotar uma referência sem publicação científica se possuir outras razões/evidências; a fragilidade e a natureza dessa sustentação permanecem explícitas.

## 3. Avaliação crítica

A direção é considerada forte, mas a fórmula simples `publicação × score do periódico + citações + tempo` não deve ser congelada.

### 3.1 Publicação/revisão científica

Pode existir um atributo determinístico de reconhecimento científico formal, desde que a regra declare quais processos contam e preserve o tipo de artefato/revisão. Artigo revisado por pares, trabalho de conferência e tese aprovada são produtos acadêmicos legítimos, porém passam por processos de validação diferentes e não devem ser silenciosamente tratados como equivalentes.

Esse atributo indica que a referência passou por um processo científico institucionalizado; não prova que a claim é verdadeira.

### 3.2 Métrica do veículo

Qualis, Journal Impact Factor, SJR, CiteScore e métricas semelhantes avaliam principalmente veículos ou conjuntos de publicações, não a qualidade de um artigo individual.

A CAPES declara que o Qualis existe exclusivamente para apoiar a avaliação da produção dos programas de pós-graduação e não assume responsabilidade por outros usos. DORA recomenda explicitamente não usar métricas de periódico como substituto da qualidade de um artigo individual.

Portanto, uma métrica externa do veículo pode ser registrada e eventualmente usada como sinal contextual, mas não deve ser multiplicador central de "qualidade científica" sem validação metodológica específica.

### 3.3 Citações

Citações são um sinal útil e determinístico de influência/uso científico, mas não equivalem a confirmação. Podem ocorrer por crítica, controvérsia ou simples referência metodológica.

Contagens brutas também variam fortemente com campo, idade do artigo, tipo de documento e cobertura da base. Se forem usadas comparativamente, devem preferir normalização por campo/tempo ou manter esses fatores explicitamente separados.

### 3.4 Evidência operacional

Tempo em operação é um sinal relevante, mas sozinho é insuficiente. Vinte anos de uso esporádico não necessariamente oferecem mais evidência que meses de grande exposição observada.

A dimensão operacional deve poder considerar, quando disponível:

- tempo desde adoção/primeira execução;
- quantidade de execuções/exposição;
- diversidade de contextos;
- quantidade de organizações/projetos;
- falhas e sucessos observados;
- recência;
- mudanças de versão.

Esses elementos permanecem mensuráveis e podem ser determinísticos.

## 4. Modelo recomendado nesta fase

Não reduzir tudo imediatamente a um único número. Manter um vetor auditável, por exemplo:

- **S — reconhecimento científico formal**: existência e tipo de revisão/publicação reconhecida;
- **I — influência científica**: citações e indicadores normalizados quando disponíveis;
- **V — contexto do veículo**: métricas externas do venue, apenas como sinal contextual, não proxy automático do artigo;
- **O — evidência operacional**: tempo, exposição, diversidade, falhas/sucessos e contexto;
- **T — rastreabilidade**: qualidade/proveniência dos dados usados para calcular os demais componentes.

Cada componente deve ser calculado por regra explícita, versionada e reproduzível. Um score agregado pode ser criado depois, mas somente se houver justificativa para pesos, normalizações e combinação e se a agregação não apagar informação relevante.

## 5. Compliance versus sustentação

A existência de publicação científica não deve ser gate global de Full FlowED, pois isso contradiz a própria liberdade de uma organização adotar referências não publicadas quando a decisão é explícita e rastreável.

Ela pode, porém, ser uma condição de **compliance científico** ou um atributo binário/ordinal dentro do perfil da referência.

Assim, uma referência pode ter:

- compliance científico ausente;
- forte evidência operacional;
- ou o inverso;
- ou ambos.

O FlowED mostra a situação em vez de converter ausência de publicação em proibição automática.

## 6. Sustentação externa para esta cautela

- CAPES: Qualis serve exclusivamente à avaliação da produção dos programas de pós-graduação; uso fora desse escopo não é responsabilidade da CAPES.
- DORA: métricas de periódico não devem ser usadas como substituto da qualidade de artigos individuais.
- Leiden Manifesto/DORA: métricas quantitativas devem ser transparentes, contextuais e apoiar, não substituir cegamente, interpretação adequada.
- Literatura bibliométrica: citações precisam de cautela e normalização por campo, idade, tipo de documento e cobertura da base.

## 7. Consequência para o Pilar 3

O Pilar 3 pode prometer algo mais humilde e realizável:

> **Toda referência relevante deve tornar explícitos os tipos de sustentação que possui, sua proveniência, sua influência científica quando mensurável, sua evidência operacional e suas lacunas. O FlowED pode calcular indicadores determinísticos a partir de sinais externos e regras versionadas, sem declarar que esses indicadores medem verdade.**

Essa formulação preserva liberdade organizacional, auditabilidade e determinismo, sem transformar bibliometria ou longevidade em autoridade absoluta.

## 8. Linhas abertas

- definição exata do que conta como reconhecimento científico formal;
- fonte canônica para citações e normalização;
- tratamento de autocitação, retratação e citações negativas;
- escolha e papel de métricas de venue;
- desenho da dimensão operacional;
- eventual score agregado e seus pesos;
- validação empírica da relação entre o perfil de sustentação e resultados de Engenharia de Software.

Essas linhas pertencem principalmente a P02, P06 e P09 e não precisam ser encerradas para o manifesto, desde que o Pilar 3 não prometa um "score de verdade" universal.
