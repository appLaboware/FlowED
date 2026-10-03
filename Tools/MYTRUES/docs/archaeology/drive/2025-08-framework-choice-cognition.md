<!--
DRIVE ARCHAEOLOGY COPY — NOT NORMATIVE
Source Drive file ID: 1l2llnK6r9a9IVjjhwzjcLkb7cFVdb0_F
Source title: 20250802_cognition_log.md
Source URL: https://drive.google.com/file/d/1l2llnK6r9a9IVjjhwzjcLkb7cFVdb0_F/view?usp=drivesdk
Copied on: 2026-10-01
Purpose: preserve MyTrues/EDT/CCP lineage before canonical consolidation.
-->

# Cognition Log: Framework Analysis

- **Data:** 2025-08-02
- **Participantes:** IA (Gemini), Rold

## Pergunta Inicial

O projeto `cngames` deve utilizar JavaScript puro ou um framework como o Vue.js (via CDN) para ser mais eficiente e facilitar a exportação para apps nativos?

## Análise Comparativa

| Aspecto | JavaScript Puro (Plano Atual) | Vue.js (via CDN) | Veredito para este Projeto |
| :--- | :--- | :--- | :--- |
| **Performance** | **Máxima.** Controle direto sobre o DOM, crucial para a lógica de jogo. | **Boa, mas com sobrecarga.** O motor de reatividade do Vue consome recursos. | **JS Puro vence.** |
| **Tamanho do Arquivo Final** | **Mínimo.** Essencial para o requisito de um único arquivo leve e compartilhável. | **Significativamente maior.** Adicionaria ~100KB ao arquivo final. | **JS Puro vence.** |
| **Controle do DOM** | **Total e direto.** Perfeito para a lógica das fases (`addEventListener`, `elemento.style.left`). | **Abstraído.** Lutaríamos contra o framework para implementar a lógica do jogo. | **JS Puro vence.** |
| **Gerenciamento de Estado** | **Manual.** Requer disciplina, mas o `GameManager` centraliza a lógica. | **Automático (Reativo).** Simplificaria o dashboard, mas o benefício é pequeno. | **Vue vence (benefício marginal).** |
| **Complexidade** | **Menor.** A complexidade está apenas na lógica do jogo. | **Maior.** Adiciona uma nova camada de abstração e conceitos. | **JS Puro vence.** |

## Cognição sobre Exportação Nativa

- **Análise:** A possibilidade de empacotar a aplicação web com Capacitor ou Cordova para criar um app nativo foi considerada.
- **Conclusão:** A escolha entre JS Puro e Vue.js é **indiferente** para este objetivo. Ambas as saídas (um único `index.html`) são igualmente compatíveis com essas ferramentas de empacotamento. Portanto, adicionar Vue não oferece nenhuma vantagem para uma futura exportação nativa.

## Decisão Final

Manter o JavaScript puro é a abordagem superior para este projeto, pois maximiza a performance, minimiza o tamanho do arquivo e alinha-se perfeitamente com a natureza da lógica de manipulação direta do DOM exigida pelo jogo. Os benefícios de um framework são mínimos e superados pelas desvantagens.

**Esta cognição levou diretamente à criação da verdade consolidada em `../truth/truth.md`.**
