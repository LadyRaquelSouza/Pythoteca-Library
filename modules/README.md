# Módulos multidisciplinares

Arquivos JSON de formato 2, importáveis manualmente na Pythoteca 0.8. Permanecem separados do catálogo legado para não quebrar a compatibilidade com leitores antigos. Baixe o JSON (Raw) para importar.

## Proveniência das aulas de Arquitetura

- 101–103: baseadas no caderno didático da Aula 01, com aprofundamento autoral rotulado.
- 104–106: baseadas nos quadros observados do vídeo da Aula 02, com aprofundamento rotulado; não houve transcrição da narração nem do áudio complementar.
- **107–108: conteúdo AUTORAL e PROVISÓRIO, sem base em apostila ou transcrição da professora**, ainda não disponibilizada. O relato da estudante delimita apenas os tópicos: decimal e binário estudados; octal e hexadecimal mencionados. Exemplos, métodos e questões são independentes. Revisar alinhamento quando o material acadêmico chegar.

Não incluir material institucional privado no repositório público. Preservar os IDs dos módulos em futuras revisões para manter o progresso local.

## Catálogo online v2

O arquivo [index.json](index.json) é um manifesto JSON de schema 2 com ID, disciplina, título, subtítulo, tamanho exato e SHA-256 de cada aula. O leitor futuro poderá obter o índice e depois buscar apenas a aula aberta pela estudante, validando tamanho, hash e formato antes de renderizar. A ação **Guardar offline** deve permanecer separada do carregamento temporário.

A verificação automatizada usa os bytes reais dos arquivos. O índice legado em `catalog/index.json` (schema 1) não foi alterado e continua servindo versões antigas. A Pythoteca 0.8 ainda não lê este novo índice: é necessário atualizar o aplicativo para navegação online multidisciplinar.
