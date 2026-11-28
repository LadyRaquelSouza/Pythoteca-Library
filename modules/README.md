# Módulos multidisciplinares

Arquivos JSON de formato 2, importáveis manualmente na Pythoteca 0.8. Permanecem separados do catálogo legado para não quebrar a compatibilidade com leitores antigos. Baixe o JSON (Raw) para importar.

## Proveniência das aulas de Arquitetura

- 101–103: baseadas no caderno didático da Aula 01, com aprofundamento autoral rotulado.
- 104–106: baseadas nos quadros observados do vídeo da Aula 02, com aprofundamento rotulado; não houve transcrição da narração nem do áudio complementar.
- 107–108: revisadas com base nos cadernos didáticos das Aulas 03 e 04 (texto consultado em 28/11/2026). IDs e banco original preservados; atividades essenciais e opcionais identificadas. Conversões octais e hexadecimais e intercâmbios com outras disciplinas são aprofundamentos.
- 109: representação digital das cores, baseada no caderno da Aula 04, com exemplos e atividades autorais. Complementos sobre sRGB, pixels, hexadecimal, Java e tamanho de imagens rotulados. Apresentações sem texto extraível, infográficos e mídias não examinados nesta revisão. Nenhuma prática Python requerida.

Não incluir material institucional privado no repositório público. Preservar os IDs dos módulos em futuras revisões para manter o progresso local.

## Catálogo online v2

O arquivo [index.json](index.json) é um manifesto JSON de schema 2 com ID, disciplina, título, subtítulo, tamanho exato e SHA-256 de cada aula. O leitor futuro poderá obter o índice e depois buscar apenas a aula aberta pela estudante, validando tamanho, hash e formato antes de renderizar. A ação **Guardar offline** deve permanecer separada do carregamento temporário.

A verificação automatizada usa os bytes reais dos arquivos. O índice legado em `catalog/index.json` (schema 1) não foi alterado e continua servindo versões antigas. A Pythoteca 0.8 ainda não lê este novo índice: é necessário atualizar o aplicativo para navegação online multidisciplinar.

## Modelagem de Dados

601–603: fundamentos, níveis de modelagem, entidades e atributos, com base no texto dos quatro PDFs das Aulas 01 e 02. Exemplos e atividades autorais; figuras e vídeo não examinados. Sem execução obrigatória de Python. Ver [planejamento editorial e intercâmbios](../docs/editorial/intercambio.md).
