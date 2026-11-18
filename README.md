# Pythoteca Library

Catálogo público de aulas para a Pythoteca, aplicativo educacional de Python para Android.

## Estado atual

Biblioteca experimental. Apenas o módulo de demonstração (Aula 99) está disponível. Ele não faz parte de nenhum curso e não contém material acadêmico privado.

## Formato

- `catalog/index.json`: índice JSON de versão 1, com identificador, título, subtítulo, tamanho em bytes e SHA-256 de cada aula.
- `catalog/aula99.json`: módulo demonstrativo.
- Os identificadores são permanentes. O catálogo referencia apenas arquivos no próprio diretório.
- Um arquivo é verificado antes de ser adicionado à biblioteca local. Exemplos não são executados automaticamente.
- Material novo só será publicado após revisão de autoria, direitos de uso, qualidade e ausência de dados pessoais.

O catálogo é público para permitir consultas sem autenticação. Não armazena dados de estudo e não recebe envios de estudantes. Não há contas, analytics ou serviço de execução de código neste repositório.

A publicação de uma licença de conteúdo será decidida separadamente; a visibilidade pública não equivale a uma licença de reutilização irrestrita.
