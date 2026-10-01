<!--
ARCHAEOLOGY COPY — NOT NORMATIVE
Source repository: InitProjHQ/InitProj
Source path: DEV/drafts/mytrues/estudo03.md
Source blob SHA: 28c05ab8d785e37f652b30801213cae8debde2fa
Copied for historical/research preservation during MyTrues consolidation.
-->

# Estudo Preliminar: Fundamentação Científica do MyTrues e CCP

## 1) Objetivo do Estudo

O objetivo deste estudo é estruturar a validação científica do **MyTrues** e do conceito de **CCP (Cognitive Creator Path)**. A meta é demonstrar que o CCP não é apenas uma ferramenta de engenharia, mas uma contribuição científica que avança o estado da arte em rastreabilidade cognitiva, superando limitações de ADRs (Architectural Decision Records) tradicionais através de grafos de decisão, proveniência formal (PROV) e reuso de cognição.

---

## 2) Leituras “semente” (coloque no NotebookLM primeiro)

### 2.1 Método de pesquisa para defender tese (você + artefato + avaliação)

* **Hevner et al. (2004)** — diretrizes clássicas de **Design Science** em IS (bom pra estruturar “artefato + avaliação” com rigor). ([AIS eLibrary](https://aisel.aisnet.org/misq/vol28/iss1/6/?utm_source=chatgpt.com))
* **Peffers et al. (2007)** — **DSRM**: processo bem operacional de design science (ótimo pra “roadmap científico” do MyTrues). ([Taylor & Francis Online](https://www.tandfonline.com/doi/abs/10.2753/MIS0742-1222240302?utm_source=chatgpt.com))
* **Sein et al. (2011)** — **Action Design Research**: construção + intervenção + avaliação no contexto real (perfeito se você provar CCP dentro de um projeto vivo, ex.: InitProj). ([AIS eLibrary](https://aisel.aisnet.org/misq/vol35/iss1/5/?utm_source=chatgpt.com))

### 2.2 Linguagem normativa e regras “MUST” (pra virar spec de verdade)

* **RFC 2119** — define MUST/SHOULD/MAY etc. ([IETF Datatracker](https://datatracker.ietf.org/doc/html/rfc2119?utm_source=chatgpt.com))
* **RFC 8174** — remove ambiguidade de maiúsculas/minúsculas (use UPPERCASE sempre). ([IETF Datatracker](https://datatracker.ietf.org/doc/rfc8174/?utm_source=chatgpt.com))

### 2.3 Base conceitual de “decisão + alternativas + porquês” (o coração do CCP)

* **IBIS (Kunz & Rittel, 1970)** — modelo “issues/posições/argumentos” (rastro argumentativo). ([Magrawal](https://magrawal.myweb.usf.edu/phd/articles/ibis_wp_70.pdf?utm_source=chatgpt.com))
* **QOC (MacLean et al., 1991)** — “Questions–Options–Criteria” (formaliza a estrutura de decisão). ([ResearchGate](https://www.researchgate.net/profile/Victoria_Bellotti/publication/233367028_Questions_Options_and_Criteria_Elements_of_Design_Space_Analysis/links/00b7d53211940ad48e000000/Questions-Options-and-Criteria-Elements-of-Design-Space-Analysis.pdf?utm_source=chatgpt.com))
* **ADR (Nygard / prática)** — padrão leve pra registrar decisões; útil como baseline do “mundo real” pra comparar com MyTrues. ([Architectural Decision Records](https://adr.github.io/adr-templates/?utm_source=chatgpt.com))
* **ISO/IEC/IEEE 42010** — padrão de descrição de arquitetura (te ajuda a posicionar “decisões arquiteturais” como objeto formal). ([OMG Wiki](https://www.omgwiki.org/MBSE/lib/exe/fetch.php?media=mbse%3Aincose_mbse_iw_2022%3Aiw2022_iso_iec_ieee_42010_update.pdf&utm_source=chatgpt.com))

### 2.4 Proveniência (CCP como “audit trail” formal, não só texto)

* **W3C PROV-DM** — modelo de dados de proveniência (entidades/atividades/agentes). ([W3C](https://www.w3.org/TR/prov-dm/?utm_source=chatgpt.com))
* **W3C PROV-O** — ontologia (OWL/RDF) pra representar PROV. ([W3C](https://www.w3.org/TR/prov-o/?utm_source=chatgpt.com))
* Artigos aplicando PROV em processos de software (pra você não parecer “reinventando provenance”):

  * Exemplo de uso de PROV + ontologia para processos de software. ([IME-USP](https://www.ime.usp.br/~ontobras/wp-content/uploads/2015/09/Using-Ontology-and-Data-Provenance-to-Improve-Software-Processes.pdf?utm_source=chatgpt.com))
  * Modelo de proveniência para processos de desenvolvimento usando PROV (exemplo mais recente). ([ACM Digital Library](https://dl.acm.org/doi/10.1145/3387940.3392220?utm_source=chatgpt.com))

### 2.5 “Docs vivas” e dívida de documentação (pra provar ganho do CCP)

* Exemplo acadêmico de **living documentation** com specs executáveis. ([SciTePress](https://www.scitepress.org/Papers/2015/56437/pdf/index.html?utm_source=chatgpt.com))
* Estudo ligando **user stories** e **documentation debt** (bom pra motivação e métrica). ([ResearchGate](https://www.researchgate.net/publication/282375423_Investigating_the_Link_between_User_Stories_and_Documentation_Debt_on_Software_Projects?utm_source=chatgpt.com))

---

## 3) Projetos/práticas OSS pra mapear (pra evitar reinventar roda)

Você vai usar isso como “baseline do mundo” (MyTrues precisa bater o baseline, não só ser diferente):

* **Log4brains** (Apache-2.0): ADRs + publicação (docs-as-code). Serve como “concorrente direto” do lado *decisão registrada*, mas sem CCP em grafo/proveniência. ([GitHub](https://github.com/thomvaill/log4brains?utm_source=chatgpt.com))
* **MADR**: template mais formal (não é Apache, mas é baseline conceitual). ([GitHub](https://github.com/adr/madr?utm_source=chatgpt.com))
* **ADR tooling catalog** (lista de práticas/ferramentas, bom pra varrer o ecossistema). ([Architectural Decision Records](https://adr.github.io/adr-tooling/?utm_source=chatgpt.com))
