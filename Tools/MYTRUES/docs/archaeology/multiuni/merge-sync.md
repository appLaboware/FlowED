<!--
ARCHAEOLOGY COPY — NOT NORMATIVE
Source repository: MultiUni/MultiUniOS_p
Source path: .initproj/tools/MyTrues/docs/pt-br/merge-sync.md
Source blob SHA: 2f86ca6e13c96e0a46547f7d15bf79c50e6c199b
Copied for historical/research preservation during MyTrues consolidation.
-->

<!--
AI: FILE: tools/MyTrues/docs/pt-br/merge-sync.md
AI: PURPOSE: Fluxo de merge e sincronização de verdades
-->
# Merge & Sync (MyTrues)

## Objetivo
Permitir sincronização de bases divergentes, com **revisão humana** antes da consolidação.

## Fluxo
1. **Exportar** verdades locais (A) e remotas (B).
2. **Comparar por truth_id**.
3. **Detectar conflitos**: conteúdo distinto para o mesmo `truth_id`.
4. **Gerar proposta de merge**.
5. **Humano valida** e resolve divergências.
6. **Aplicar merge** e registrar no histórico.

## Tipos de conflito
- **Texto diferente** (README/CCP divergente).
- **Metadados diferentes** (tags, status, scope).
- **Relações divergentes** (substitui/contradiz/depende).

## Saída esperada
- `merge-report.json`: lista de conflitos e diferenças.
- `merge-applied.log`: **planejado** (aplicação automática de merge não existe no POC).

## Regras
- Nunca sobrescrever sem confirmação humana.
- Manter histórico de versões por `truth_id`.
- Registrar autor da resolução.

## CLI (POC)
```bash
python3 tools/mytrues_export.py --root . --out /tmp/mytrues-local.jsonl
python3 tools/mytrues_export.py --root /path/remoto --out /tmp/mytrues-remote.jsonl
python3 tools/mytrues_merge.py --local /tmp/mytrues-local.jsonl --remote /tmp/mytrues-remote.jsonl --out /tmp/merge-report.json
```
