# WRK-001 → PO-001 — primeira POC vertical entregue

Status: executada e validada; não normativa.
Proposta anterior: 1de8d3d37f7b2fa8dc4a23ea68e88a3c6ac86451.

## Entrega

Árvore autossuficiente: POC/ccp-materializer/.

- Fonte real: documento P2.3 em a22a6ad841f3ab6e87eb89ffef43e9bfcd45e4ba; snapshot integral conferido contra blob Git.
- 14 marcações não destrutivas → CCP tipado em JSON → contrato explícito → adapter → REDUCT-MAX, BASE e DEFESA.
- Proveniência por trecho/linhas, commit, blob e SHA-256. Estado candidato preservado.
- Invariantes retidos em todos os JSONs: estado, base canônica, causalidade e limites. Markdown oferece texto selecionado e acesso progressivo aos invariantes.
- Saídas reais versionadas em evidence/, com build-report.json e hashes.

## Execução

Dentro de POC/ccp-materializer:

```sh
python3 materialize.py
python3 -m unittest -v
```

Python 3.12.14: 8 testes passaram. CLI executada de fora da pasta também compilou as três projeções. Testes cobrem reprodutibilidade, fonte adulterada, citação inventada, spans/IDs inválidos, referência desconhecida, omissão indevida de limites, eixo argumentativo, seleção e separação dos inputs.

## Limites

O código materializa redações já existentes; não gera nem revisa manifesto. A marcação é curada por WRK-001. Integridade e cobertura não comprovam equivalência semântica. O contrato não atribui aprovação humana. BASE preserva o nome da fonte; DEFESA não é nível final de densidade.

Não houve pesquisa externa nem mudança de filosofia. O PO pode revisar o contrato e os artefatos concretos. A implementação experimental foi autorizada diretamente pelo humano.

## Próximo alvo

Como chegamos aqui exige avaliar fontes de eventos, ordem, cobertura e relações explicitamente sustentadas. O repositório tem sessões e commits que podem apoiar uma trilha documental parcial; o snapshot P2.3 não é log bruto. Não converter o “Caminho cognitivo resumido” da DEFESA em história real inferida.

Blockers da entrega atual: nenhum. Pendência posterior: selecionar fonte histórica apropriada e contrato da projeção dinâmica antes de ampliar escopo.
