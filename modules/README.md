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

604–606: relacionamentos, ER/UML, cardinalidade e teoria relacional, baseados nas Aulas 01 e 02 e nos capítulos 2 e 3 da apostila. Diagramas textuais e exercícios originais; convenções de leitura explicitadas. Álgebra relacional introdutória e diferenças práticas de SQL identificadas como complementos.

607–609: identificação, chaves, integridade e ER avançado, com base nas seções 2.4–2.7 e 3.3–3.5 da apostila e slides 25–29, 38–41 da apresentação. Exemplos originais; superchaves, lógica de NULL, concorrência e estratégias de mapeamento recebem complementos explicitados. Sem práticas Python.

610–612: transformação ER-relacional, normalização e projeto integrado. Base nos PDFs das Aulas 01 e 02; dependências funcionais, definições formais, testes e implementação são aprofundamentos autorais. Vídeo de Modelagem: 25 quadros observados, sem transcrição sonora; reflexão sobre evolução incorporada à aula 612. Ver [metodologia e registro de cobertura](../docs/editorial/metodologia-fontes.md). Nenhuma execução Python obrigatória.

## Tecnologia da Informação

501–502: revisão acadêmica de Word, com foco em atalhos do manual Fundação Bradesco (Word 2016 PT-BR), provisoriamente até confirmação docente. Apostilas de Elias de Souza Santana e Fernando Borges Vale como fontes complementares, divergências explicitadas. Texto de Fernando extraído parcialmente; figuras não examinadas. Sem prática obrigatória em LibreOffice. Próximos módulos: 503 estilos/listas/tabelas/visuais; 504 referências/revisão/colaboração/acessibilidade; 505 correspondências/proteção/impressão/gerenciamento.

503–505: estilos, listas, tabelas, referências, revisão, acessibilidade, correspondências e gerenciamento documental. Revisão cumulativa de atalhos baseada em Bradesco 2016 PT-BR, confirmação docente pendente. Tópicos conhecidos apenas pelo sumário de Fernando são identificados como complementos autorais; figuras e páginas sem extração continuam pendentes. Cinco módulos publicados, sem práticas obrigatórias em Writer.

## Sistemas Operacionais

401–403: Windows 11, interface, janelas, arquivos, pastas, atalhos, captura, aparência, tela e áudio. Base nas quatro imagens Área de Trabalho — Partes 01–04, inspecionadas visualmente em 28/11/2026. Revisão de todos os 25 atalhos da Parte 03; divergência com Word localizado e ressalvas para Print Screen e exclusões explicitadas. Práticas em Windows opcionais; sem exigência de instalação ou prática equivalente em Linux. Complementos conceituais identificados.
