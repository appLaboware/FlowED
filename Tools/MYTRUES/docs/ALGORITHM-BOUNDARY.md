# Algorithm and ownership boundary

## Correção de modelo

O diferencial não é apenas trocar um engine dentro de uma instância global.

Cada técnico/equipe/fornecedor possui **seu próprio MyTrues**:

- memória isolada;
- decisões próprias;
- histórico próprio;
- algoritmo próprio;
- reputação/qualidade futura própria.

O cliente escolhe o fornecedor MyTrues.

## Público

- protocolo;
- schemas;
- lifecycle pending/decided;
- case packet anonimizado;
- submissão de resolução;
- conformance;
- eventos/tracing.

## Privado do fornecedor

- conteúdo da memória decisória;
- ranking;
- embeddings;
- pesos;
- heurísticas;
- políticas de aprovação;
- algoritmo;
- estatísticas internas;
- procedimentos/sandbox utilizados para chegar à decisão.

## Regra humana

Caso desconhecido MUST NOT ser auto-promovido a verdade operacional.

A referência é:

retrieve known -> decide

ou, se desconhecido:

pause -> sanitize -> human sandbox -> explicit resolution -> retain in provider memory -> resume

Uma LLM MAY auxiliar o humano, mas não substitui a aprovação do fornecedor.
