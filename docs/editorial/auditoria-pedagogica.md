# Auditoria pedagógica — percurso guiado e revisão intercalada

Registro inicial: 28/11/2026. Estado: EM AUDITORIA. Este documento não declara uma sequência final antes do confronto com os módulos reais.

## Decisões de escopo

A Pythoteca deve oferecer dois fluxos de estudo complementares e um eixo de revisão transversal:
1. Estudo por disciplina: progressão interna, consulta livre e preparação para avaliações.
2. Estudo guiado: percurso recomendado que intercala as seis disciplinas com dependências justificadas, recuperação de conteúdos e conexões naturais.
3. Revisão generalizada: banco ampliado de atividades autorais, intercalando matérias e assuntos já apresentados, sem limitar a revisão à aula atual.

O progresso de uma mesma aula deve ser compartilhado conceitualmente pelos dois fluxos. A implementação do leitor, armazenamento de progresso, seleção adaptativa e interface pertence ao aplicativo e requer contrato próprio; este documento não afirma que tais funções já existam. Não alterar o schema v2 nem atribuir categoria ou IDs novos sem validar o contrato. Consulta livre não deve ser bloqueada por pré-requisitos pedagógicos.

## Conclusão oficial do percurso guiado — PENDENTE

Esta seção será substituída pelo resultado da auditoria, explicitamente identificado como sequência recomendada, com IDs em ordem, blocos, transições justificadas, pré-requisitos reais versus conhecimentos recomendados, momentos de revisão e alternativas. O catálogo ordenado por IDs não é automaticamente a melhor sequência guiada. Não confundir ordem editorial com ordem das aulas presenciais.

## Critérios de auditoria

- Conferir objetivos, capítulos, exemplos e exercícios dos 45 módulos; mapear conhecimentos pressupostos, dependências necessárias e desejáveis; evitar ciclos e antecipação de conceitos.
- Comparar sequência por disciplina com alternativas intercaladas. Alternar por blocos coerentes, não por sorteio indiscriminado; manter continuidade em assuntos que exigem encadeamento.
- Registrar atividades essenciais e opcionais, distribuição, redundância, lacunas e dificuldade. Preservar IDs e progresso; ampliar ou reformular atividades somente com ganho pedagógico.
- Avaliar intercâmbios já registrados em intercambio.md, priorizando conexões úteis. Não tornar projetos integradores pré-requisitos obrigatórios.
- Manter apostilas como base acadêmica; distinguir relato presencial, complemento técnico, exercício autoral e limitações de fonte. Preservar cautelas de Word localizado, práticas Python pausadas e ausência de obrigação de executar Word/Writer ou Windows.

## Banco de revisão generalizada — requisito explícito

Ampliar efetivamente a quantidade e variedade de exercícios de revisão, além dos exercícios de assimilação já existentes. A revisão deve atravessar as seis matérias, sem exigir que todo exercício misture várias disciplinas. Uma sessão pode alternar questões de uma matéria para outra; questões integradoras devem exigir conexões reais.

Propor um inventário de objetivos por módulo e construir novas questões para lacunas, com recuperação sem pistas excessivas, interpretação, aplicação, diagnóstico de erros, comparação, rastreamento, cenários e problemas integrados. Evitar clones que apenas trocam nomes ou números. Priorizar operadores relacionais e lógicos em Portugol, peculiaridades de Word e retomada de fundamentos de representação e dados. Usar exemplos novos, não republicar questões institucionais.

Metadados desejáveis para futura integração: identificador permanente próprio, módulos/objetivos relacionados, disciplinas, pré-requisitos, dificuldade, tipo de atividade, enunciado, pistas graduais, resposta/explicação ou critérios de avaliação, origem autoral e eventual requisito de ambiente. A seleção deve restringir revisão de recuperação ao conteúdo já apresentado ou marcado como conhecido; distinguir sondagem diagnóstica e revisão. Questões interdisciplinares exigem cobertura dos objetivos de todas as matérias envolvidas. O nome da matéria não precisa revelar antecipadamente o método de resolução.

Planejar revisão logo após aprendizagem, retorno após outras aulas e retomadas mais distantes; ajustar frequência conforme erros e tempo desde a última recuperação, sem fixar algoritmo ou intervalos definitivos antes de discutir o leitor. Dar prioridade a questões novas e objetivos frágeis, sem excluir sucessos anteriores; não exigir completar o banco inteiro para avançar. Oferecer revisão geral e recortes por disciplina/objetivo, com possibilidade de sessão manual.

## Entregáveis finais

- Matriz de dependências e diagnóstico de sequência interna.
- Sequência guiada recomendada, completa e verificável (45 IDs atuais, salvo decisão documentada de expansão), com revisão intercalada e justificativas.
- Inventário de exercícios e cobertura por objetivo; banco novo de revisão com contrato compatível ou arquivo editorial separado até definição do leitor.
- Registro de decisões, alternativas rejeitadas e pendências; validação estrutural e teste de consistência da sequência. Não confundir CI com validação pedagógica ou teste real do aplicativo.

## Registro inicial

O manifesto v2 contém 45 aulas: Arquitetura 101–109, Lógica 201–205, Java 301–311, SO 401–403, TI 501–505, Modelagem 601–612. A auditoria parte desse conjunto, não do catálogo legado de Python. CI da última consolidação de TI (46156791333) concluída com sucesso. Nenhuma sequência final foi decidida nem exercício novo publicado neste registro.
