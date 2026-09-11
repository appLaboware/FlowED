# POC — materializador CCP

Recorte experimental de WRK-001: uma unidade real, P2.3, com REDUCT-MAX, BASE e DEFESA. Não é implementação normativa do CCP nem revisão do manifesto.

## Executar

Requisito: Python 3.10 ou superior. Validado com Python 3.12.14. Sem instalação de pacotes ou acesso à rede.

Dentro desta pasta:

```sh
python3 materialize.py
python3 -m unittest -v
```

Em Windows, pode-se usar `python` no lugar de `python3`.

As saídas ficam em `output/`: três pares Markdown/JSON, CCP completo, contrato, fonte preservada e relatório com hashes. Evidência versionada do primeiro ciclo: `evidence/`.

Seleção explícita:

```sh
python3 materialize.py --unit P2.3 --projection REDUCT-MAX --output output-reduct
```

O programa resolve seus inputs pela própria localização; também pode ser chamado de outra pasta. Toda a execução depende apenas desta árvore.

## Pipeline

| Etapa | Artefato | Função |
|---|---|---|
| Fonte preservada | inputs/source.md + source-origin.json | Cópia integral de documento editorial, fixada a commit/blob |
| Marcação | inputs/markings.json | 14 trechos exatos com linhas, tipos e autoria da anotação |
| CCP estruturado | output/ccp.json | Unidade, nós, invariantes, textos e proveniência |
| Contrato | inputs/projection-contract.json | Público, eixo, seleção, retenção obrigatória e omissões permitidas |
| Adapter | materialize.py | Seleção determinística e renderização Markdown/JSON |
| Compilação | output/*.md e *.json | Projeções e relatório reproduzíveis |

BASE mantém a nomenclatura existente na fonte; corresponde ao papel central denominado BASELINE no protocolo editorial. DEFESA está no eixo argumentativo, separado da densidade editorial. O trecho da fonte chamado “Caminho cognitivo resumido” é preservado como argumento existente; não é apresentado como história bruta reconstruída.

## Invariantes e proveniência

Estado candidato, texto central, causalidade e limites permanecem integralmente em cada JSON. O Markdown inclui o estado e links para esses elementos obrigatórios, além dos textos próprios da projeção. O contrato deste caso de revisão permite acesso progressivo aos limites e à causalidade completa; isso não estabelece um piso para outros públicos ou tarefas.

Cada nó mantém o trecho literal, linhas, SHA-256 e URL fixada ao commit de origem. O CCP completo e a cópia da fonte ficam junto às saídas para inspeção offline. `build-report.json` associa hashes aos artefatos. A integridade local não autentica por si só uma origem remota nova: neste bootstrap, o blob foi obtido e conferido pelo conector GitHub.

Falham antes de escrever saídas: fonte divergente do SHA-256/blob, trecho divergente da marcação, span inválido, IDs duplicados/desconhecidos, unidade inexistente, perda de invariantes, cobertura/omissões incoerentes e eixo inválido. Erros retornam código 1.

## Limites do experimento

- A fonte é documento editorial real de MAN-001; não é log bruto do chat.
- A marcação é curada por WRK-001. A seleção não extrai cognição automaticamente.
- As três redações já estavam na fonte; o adapter não inventa resumos nem defesa.
- Os testes verificam integridade, retenção, seleção e reprodutibilidade. Não provam monotonicidade semântica, qualidade editorial ou eficácia cognitiva.
- O estado da proposição continua candidato. Não se atribui aprovação humana ausente.
- Relações causais presentes permanecem como trechos tipados. Não há inferência automática de arestas causais nem ontologia geral.
- A fonte contém argumentação, não comprovação científica. Nenhuma pesquisa externa foi necessária.
- A compilação selecionada pode coexistir com artefatos anteriores na pasta de saída; o relatório enumera somente os produzidos naquela execução. Use uma pasta nova para uma entrega isolada.

## Próximo alvo: Como chegamos aqui

O recorte valida materialização e proveniência documental. A próxima investigação deve usar registros preservados com eventos/ordem e separar relações explicitamente documentadas de cronologia. Resumos de sessão e commits podem apoiar uma trilha parcial, mas não substituem o chat bruto ausente. DEFESA e seu caminho resumido não devem ser convertidos em uma narrativa histórica por inferência.

Referências operacionais: CONTEXT e INBOX de 260911-025000-worker; CCP-PROJECTION-ADAPTERS-AND-MANIFESTO-LAYOUT-DRAFT; CCP-LAYOUT-PARALLEL-BRANCH-CAPTURE; CCP-REALIZABILITY-BOUNDARY; MANIFESTO-PROPOSITION-DENSITY-PROTOCOL-DRAFT. Todos consultados no repositório antes deste recorte.
