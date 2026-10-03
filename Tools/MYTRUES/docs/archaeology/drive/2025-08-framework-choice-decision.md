<!--
DRIVE ARCHAEOLOGY COPY — NOT NORMATIVE
Source Drive file ID: 1LGXWeOqaHtLrk1fXxnQ8JtjtypUtncKS
Source title: truth.md
Source URL: https://drive.google.com/file/d/1LGXWeOqaHtLrk1fXxnQ8JtjtypUtncKS/view?usp=drivesdk
Copied on: 2026-10-01
Purpose: preserve MyTrues/EDT/CCP lineage before canonical consolidation.
-->

# MyTrue-Arch-001: Escolha de Framework - JavaScript Puro

- **Data da Decisão:** 2025-08-02
- **Status:** Ativo

## A Verdade

O projeto **CnGames** será desenvolvido utilizando **JavaScript puro (Vanilla JS)**, sem o uso de frameworks de UI como Vue, React ou Angular.

## Justificativa

A decisão foi baseada nos seguintes requisitos críticos do projeto:

1.  **Performance Máxima:** A lógica do jogo requer manipulação direta e de baixa latência do DOM para animações e interações precisas. A sobrecarga de um framework de reatividade é desnecessária e potencialmente prejudicial.

2.  **Tamanho Mínimo do Pacote Final:** Um dos principais requisitos é a capacidade de exportar o jogo inteiro como um único arquivo HTML leve e autônomo. A inclusão de um framework aumentaria desnecessariamente o tamanho do arquivo final.

3.  **Controle Direto do DOM:** As fases do jogo são inerentemente baseadas em eventos de baixo nível (`mousedown`, `touchmove`, etc.) e manipulação direta de estilos e posições. Tentar abstrair essa lógica com um framework seria mais complexo e menos eficiente do que a abordagem direta.

## Implicações

- Toda a lógica de UI e gerenciamento de estado deve ser implementada manualmente.
- A organização do código, garantida por uma arquitetura de classes (`GameManager`, `PhaseBase`), é de vital importância para evitar a desorganização.
- A reatividade da UI (ex: atualizar a pontuação na tela) deve ser tratada por funções explícitas que são chamadas quando o estado do jogo muda.
