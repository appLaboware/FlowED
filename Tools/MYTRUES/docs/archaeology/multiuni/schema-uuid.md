<!--
ARCHAEOLOGY COPY — NOT NORMATIVE
Source repository: MultiUni/MultiUniOS_p
Source path: .initproj/tools/MyTrues/docs/pt-br/schema-uuid.md
Source blob SHA: 81f6abe000b24aecdd33aee8d445a55e279a2ee7
Copied for historical/research preservation during MyTrues consolidation.
-->

<!--
AI: FILE: tools/MyTrues/docs/pt-br/schema-uuid.md
AI: PURPOSE: Especificação de UUID e identidade de cognições
-->
# Schema de Identidade (UUID)

## Objetivo
Garantir que cada cognição/verdade tenha um identificador **global e estável**, permitindo sincronização e merge entre bases distintas.

## Regra
- Cada verdade recebe um `truth_id` (UUID v4).
- O `truth_id` **nunca muda**, mesmo com updates de conteúdo.
- Versões e revisões referenciam o mesmo `truth_id`.

## Onde fica
- `truth.yaml` ao lado do `README.md`.

## Exemplo (metadados)
```yaml
truth_id: 4b5c3a8a-0d1f-4a0e-97b3-9b7b0f3d7a6f
created_at: 2026-01-21T12:00:00Z
updated_at: 2026-01-21T12:30:00Z
status: active
namespace: USER|TEAM|PROJECT
scope: INITPROJ/PROMPTS
```

## Estratégia de migração
- Verdades antigas sem UUID recebem `truth_id` na primeira indexação.
- O `truth_id` passa a ser persistido no YAML da verdade.

## CLI (POC)
```bash
python3 tools/mytrues_uuid.py --root .
```
