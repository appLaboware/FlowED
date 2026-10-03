<!--
ARCHAEOLOGY COPY — NOT NORMATIVE
Source repository: MultiUni/MultiUniOS_p
Source path: .initproj/tools/MyTrues/docs/world-scan.md
Source blob SHA: b379cf8b9d4e95a48d776d981c46a16fd3a5afca
Copied for historical/research preservation during MyTrues consolidation.
-->

# MyTrues vs. o Mundo (scan inicial)

Objetivo: mapear **classes de soluções existentes** que se aproximam do MyTrues, para decidir o que **adotar** e o que **não reinventar**.

## 1) ADR (Architecture Decision Records)
- O que entregam: registro de decisões em markdown (geralmente por arquivo).
- Gap típico: foco em arquitetura; pouca estrutura para **grafo de cognições** + **supersession rastreável** + **validação build-time** por schema.
- Adotar: formato/rotina + publicação (ex.: Log4brains).

## 2) IBIS / QOC (design rationale)
- O que entregam: modelos conceituais para discutir e capturar racionalidade.
- Gap típico: não vêm como ferramenta operacional “de devops”; ficam em software de modelagem ou texto.
- Adotar: como *modelo* dentro do CCP Record (question/options/criteria + issue/position/argument).

## 3) Provenance (W3C PROV)
- O que entrega: padrão para rastrear entidades/atividades/agentes.
- Gap típico: modela “rastro” e causalidade; não define o *conteúdo normativo* da decisão.
- Adotar: como camada opcional de interoperabilidade (export PROV).

## 4) Wikis / Notion / Obsidian / PKM
- O que entregam: base de conhecimento navegável e linkável.
- Gap típico: sem “contrato” verificável; fácil gerar drift e incoerência; difícil medir impacto.

## 5) Knowledge Graph / RDF / JSON-LD
- O que entregam: grafo consultável, semântica, queries.
- Gap típico: alto custo inicial; sem um protocolo simples, vira infra sem produto.
- Adotar: como **back-end opcional** (não obrigatório no core).

## 6) RAG / Memória vetorial
- O que entrega: recuperação semântica de conteúdo.
- Gap típico: sem governança, vira “memória alucinável”; precisa contratos e níveis.
- Adotar: opcional, subordinado a CCP validado.

## Tese diferencial (aposta)
**CCP como contrato validável + evidência replicável**, e não só “conhecimento consolidado”.
