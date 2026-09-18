# INBOX 003 — Adotar protocolo central de fluxo de sessões

**From:** `PO-001-01` (`RETIRED_AUDITOR`, sob solicitação humana explícita)
**To:** `PO-001-02` (`ACTIVE`)
**Type:** protocol adoption / post-handoff stabilization

O primeiro handoff real revelou regras que agora foram consolidadas em:

`DEV/ia-sessions/SESSION-FLOW-PROTOCOL.md`

Antes de continuar a próxima frente de trabalho, leia integralmente esse protocolo e reconheça explicitamente em seu `session_resume.md` que:

1. `PO-001-02` é a única instância `ACTIVE` de `PO-001`;
2. `PO-001-01` permanece apenas como `RETIRED_AUDITOR`;
3. futuras sucessões devem usar o protocolo central independentemente de a sessão nascer por branch, novo chat, projeto ou outro mecanismo;
4. contexto conversacional herdado nunca substitui o estado autorizado do repositório;
5. testes A/B devem congelar `H0`, isolar branches e manter avaliação cega quando possível;
6. o controle do predecessor só é reproduzível quando corpo integral + hash + timestamp/commit forem congelados antes da inspeção dos candidatos;
7. após PASS, canonical catch-up é obrigatório se HEAD avançou;
8. durante a janela opcional `SHADOW AUDIT`, você continua com plena autoridade operacional; o predecessor apenas audita inputs/respostas a pedido do humano e não funciona como segunda instância ativa;
9. prompt lineage pode ser numerada para distinguir intenção humana, texto enviado, interpretação e ação;
10. o objetivo da janela de observação é encerrar dependência do predecessor, não perpetuá-la.

Não trate a existência de um novo chat como prova de ausência de memória. Registre apenas a condição observável do mecanismo de materialização.

Para este input, não emita novo trabalho a MAN-001 ou WRK-001 apenas por causa do protocolo. Faça somente:

- leitura/sincronização;
- atualização de seu `session_resume.md`;
- commit de adoção com prefixo `[PO-001-02]`;
- resposta curta ao humano confirmando adoção e commit.

Depois disso, retome normalmente a autoridade operacional de `PO-001-02`.
