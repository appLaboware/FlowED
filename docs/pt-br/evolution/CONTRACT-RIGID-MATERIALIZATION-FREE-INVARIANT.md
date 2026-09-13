# Invariante transversal — contrato rígido, materialização livre

**Status:** decisão conceitual para revisão dos quatro pilares do Manifesto FlowED.

## Tese

O FlowED deve ser normativo no nível do **contrato público** e deliberadamente não normativo no nível da **materialização concreta**.

Formulação curta:

> **rígido no contrato; livre na materialização.**

O contrato pode ser rigoroso sobre o que deve existir, o significado das operações, as entradas e saídas públicas, os estados e garantias observáveis, a rastreabilidade mínima, compatibilidade, evidência exigível e demais propriedades necessárias à interoperabilidade e à governança.

O contrato não deve determinar algoritmo, arquitetura interna, framework, produto, fornecedor, banco, broker, classificador, interface gráfica ou outro detalhe de implementação quando esses detalhes não fizerem parte da garantia pública.

## Conformidade

Qualquer provider/materializador capaz de cumprir integralmente o contrato aplicável é uma materialização válida daquela capability FlowED, independentemente de ter sido produzida pela LaboWare, pelo ecossistema FlowED, por uma empresa terceira ou pelo próprio time usuário.

Uma implementação de referência existe para demonstrar realizabilidade e oferecer um caminho pronto, mas não recebe autoridade normativa adicional.

`Full FlowED` deve significar conformidade com o conjunto de contratos constitutivos aplicáveis, não adoção das ferramentas de referência do ecossistema.

A confiabilidade, qualidade, eficiência, metodologia ou preferência por uma implementação específica é uma avaliação separada da conformidade contratual. Um provider pode cumprir perfeitamente um contrato e ainda ser considerado ruim por um time; outro pode ser preferido. Essa escolha pertence à política e à opinião do adotante, salvo garantias explicitamente exigidas pelo próprio contrato.

## Aplicação aos pilares

### Pilar 1

É o próprio fundamento desta separação. FlowED define linguagem, contratos, comportamento público, interoperabilidade e substituibilidade. Tecnologias permanecem livres.

### Pilar 2

FlowED deve exigir a capability de memória operacional estruturada e relacionável à aprendizagem/decisão no nível definido pelo contrato. Kafka, CDEvents, OpenTelemetry, OCEL, MyTrues, EDT/CCP ou qualquer composição concreta são referências/materializações possíveis, não conteúdo normativo do pilar.

### Pilar 3

FlowED deve exigir que sustentação, origem, estado e evidência relevante possam ser explicitados, transportados e avaliados pelo contrato. FlowED não ranqueia, não julga e não produz uma verdade oficial. COR ou qualquer outro classificador pode emitir uma opinião sobre esses dados. A confiabilidade da opinião pertence ao classificador; o contrato apenas torna sua saída interoperável quando essa capability for utilizada.

O manifesto pode defender que sustentação científica, normativa e empírica é um fator importante para decisões técnicas e filosóficas de um time sem impor como um classificador deve transformar esses fatores em score.

### Pilar 4

FlowED deve exigir que mudanças de intensidade, rigor ou configuração possam ser decididas e registradas de forma governada conforme contexto, risco, evidência e política. A engine que recomenda, decide ou executa a transição permanece substituível.

## Consequência para produtos FlowED/LaboWare

Produtos de referência podem nascer das composições pesquisadas para cada capability. Eles servem como:

- prova de realizabilidade;
- alternativa pronta para adoção;
- dogfood dos contratos;
- produto educacional/industrial quando aplicável.

Mas nunca devem ser retroativamente promovidos a requisito do próprio FlowED.

## Regra de revisão do manifesto

Toda redação de pilar deve passar pela pergunta:

> **Este texto está exigindo uma capacidade/garantia contratual ou está acidentalmente exigindo nossa ferramenta preferida?**

Se estiver exigindo a ferramenta, framework ou método concreto sem necessidade contratual, a redação deve ser corrigida.
