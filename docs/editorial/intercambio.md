# Planejamento editorial: Intercâmbio de Disciplinas

Proposta registrada em 28/11/2026. Conteúdo autoral complementar ao currículo; não é parte do catálogo distribuído nem do diário de engenharia Pythoteca por dentro.

## Finalidade

Mostrar como conhecimentos de disciplinas distintas cooperam na resolução de problemas reais. As trilhas devem ser opcionais, progressivas, com pré-requisitos declarados e exemplos originais. Não interromper a progressão principal nem pressupor conhecimentos ainda não apresentados.

## Primeiras trilhas

- Lógica de Programação + Modelagem de Dados: transformar regras de negócio em condições; validar domínios; distinguir identificação, existência e cardinalidade; desenhar algoritmos de cadastro e testes. Pré-requisitos: variáveis, decisões, entidades, atributos e relacionamentos.
- Java + Modelagem de Dados: classes, objetos, formulários Swing, validação de entrada, mapeamento entre objetos e registros, persistência e JDBC em etapa posterior. Não equiparar automaticamente classe a entidade ou objeto a linha.
- Python + Modelagem de Dados: listas, dicionários, classes, validação e SQLite posteriormente. Práticas executáveis em Python ficam pausadas durante as avaliações; ideias podem ser registradas para retomada.
- Futuras possibilidades: Arquitetura + Lógica; Arquitetura + Java; Arquitetura + Sistemas Operacionais; Modelagem + Sistemas Operacionais; Java + Python.

## Projeto integrador sugerido

Biblioteca de empréstimos: modelar leitores, obras, exemplares e empréstimos; explicitar disponibilidade e regras; escrever algoritmos de validação; desenvolver interface Java; acrescentar persistência quando estudada. Usar dados fictícios, preservar histórico de empréstimos e discutir concorrência somente após os fundamentos.

## Integração futura

A categoria Intercâmbio de Disciplinas é uma proposta, não um valor de discipline aceito no esquema v2. Decidir com o leitor como representar pré-requisitos e sugestões sem quebrar versões anteriores. Até lá, pequenas conexões rotuladas podem existir em capítulos das disciplinas atuais. Não atribuir novos identificadores de aulas interdisciplinares antes de definir o contrato. Não publicar material privado.

## Sequência de Modelagem de Dados

601 Dados, informação e bancos de dados; 602 Fundamentos da modelagem; 603 Entidades, atributos e domínios; 604 Relacionamentos e diagramas; 605 Cardinalidade e participação; 606 Modelo relacional; 607 Chaves; 608 Integridade; 609 ER avançado; 610 Entidades associativas e transformação; 611 Normalização; 612 Projeto integrado. A sequência é editorial, não numeração das aulas presenciais.

## Ampliação da proposta — todas as disciplinas

Registro de 28/11/2026, a partir da solicitação de ampliar o intercâmbio para Arquitetura de Computadores e demais disciplinas. A percepção de que Modelagem talvez necessite de menos intercâmbios é uma hipótese pedagógica da estudante, não uma restrição nem conclusão técnica. A relevância será avaliada caso a caso.

### Dois níveis de integração

- Conexões pontuais: capítulos ou exercícios rotulados nas aulas existentes, quando uma relação breve esclarece o tema.
- Trilhas interdisciplinares: sequências autorais opcionais com objetivos próprios, problema integrador, pré-requisitos, progressão e atividades de aplicação. Criar somente quando o ganho pedagógico justifica uma sequência independente; não construir uma trilha para cada par matematicamente possível.

### Arquitetura como eixo transversal

| Conexão | Proposta | Pré-requisitos ou limites |
|---|---|---|
| Arquitetura + Lógica | Bits, bases numéricas, operadores booleanos, limites e representação de números, relação entre decisões algorítmicas e operações físicas | Sistemas numéricos, condições; distinguir lógica proposicional, operações bit a bit e circuitos |
| Arquitetura + Java | Tipos primitivos, representação, overflow, memória, bytecode, JVM e execução | Tipos, classes e CPU; distinguir modelo abstrato da JVM de implementação física |
| Arquitetura + Sistemas Operacionais | CPU, memória, armazenamento, processos, escalonamento, interrupções, drivers e E/S | Componentes e ciclo de instruções; fundamentos internos de SO ainda precisam ser estudados |
| Arquitetura + Python | Inteiros de precisão arbitrária, ponto flutuante, bits, objetos, memória e desempenho | Tipos e representação; distinguir semântica da linguagem de detalhes de CPython; práticas executáveis pausadas |
| Arquitetura + Modelagem | Representação física de registros, páginas, índices, cache e custos de acesso | Modelo lógico e físico, armazenamento; não confundir normalização com organização física |
| Arquitetura + TI | Unicode, codificações, RGB, resolução, compressão e tamanho de arquivos | Bits, bytes, representação de cores; distinguir formatos, contêineres e codificação |

### Demais conexões candidatas

- Sistemas Operacionais + Lógica/Java/Python: execução, processos, arquivos, caminhos, permissões, ambiente de execução e concorrência, gradualmente.
- Sistemas Operacionais + TI: associação de arquivos, impressão, fontes, acessibilidade, organização e proteção documental.
- Sistemas Operacionais + Modelagem: armazenamento e permissões de bancos, serviços, backups e concorrência; após fundamentos necessários.
- TI + Lógica/Java/Python: regras de validação, automação de documentos, transformação de dados e geração de relatórios.
- TI + Modelagem: mala direta como aplicação de registros e campos, fontes tabulares, relatórios e consistência; não equiparar planilha ou documento a SGBD.
- Lógica + Java/Python: comparar solução algorítmica, tipos, estruturas de controle e implementação; evitar repetir aulas de sintaxe sem objetivo.
- Java + Python: comparar modelos de execução, tipagem, objetos e bibliotecas por problemas equivalentes; somente após retomada de Python.

### Projetos integradores candidatos

1. Biblioteca de empréstimos: preservar o projeto anterior e acrescentar processos, arquivos, persistência, relatórios e custos de armazenamento conforme os pré-requisitos.
2. Do bit à imagem: representar canais RGB, converter bases, explicar tamanho de imagens sem compressão e suas ressalvas, desenvolver operações de cor em Java quando estudadas, relacionar tela e arquivos de imagem, e documentar resultados.
3. Do algoritmo ao programa em execução: acompanhar uma solução de Lógica até a implementação Java, distinguir compilação, bytecode, JVM, processo, memória, CPU e E/S. Python poderá ser incorporado após retomada.
4. Do dado ao documento: modelar dados fictícios, validar entradas, gerar relatórios ou correspondências, distinguir conteúdo estruturado, arquivo editável e exportação. Não requerer prática de Word ou Writer se o objetivo for conceitual.

### Prioridade e critérios de publicação

A prioridade imediata continua sendo revisão acadêmica para avaliações, análise multimídia retroativa e cobertura de lacunas. Intercâmbios não substituem apostilas nem interrompem trilhas principais. Não exigir execução em Windows ou práticas Python durante a pausa. Escolher sequências com benefício real, sem inflar material, sem dependências circulares, com separação clara entre conteúdo de curso e autoral. A decisão sobre categoria e identificadores continua condicionada ao contrato do leitor; nenhum novo módulo interdisciplinar é publicado por este registro.


### Complemento ao projeto Do bit à imagem

Após revisão do podcast A04 (28/11/2026), incluir como possibilidade opcional a comparação entre tripla RGB, três bytes, notação CSS hexadecimal e inteiro empacotado RRGGBB; demonstrar a perda de informação na soma simples e a recuperação dos campos pela representação posicional. Em Java, relacionar ao uso de int e à distinção entre RGB de 24 bits e representações com alfa. Em TI, relacionar à escolha de cores e aos limites da gama de reprodução. Pré-requisitos: 107–109, tipos Java e propriedades visuais (310); não exigir operações bit a bit nem código executável antes dos fundamentos correspondentes. Não constitui nova aula nem prática Python imediata.
