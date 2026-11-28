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


## Auditoria de obrigatoriedade — Arquitetura e práticas futuras (28/11/2026)

Inventário dos 45 módulos: Arquitetura 690/35, Lógica 326/20, Java 423/55, SO 58/45, TI 137/90, Modelagem 244/160 (total/explicitamente essenciais antes desta intervenção). Total corrigido: 1.878 exercícios, 405 essenciais, 1.473 restantes; contagens preliminares de Modelagem e total estavam incorretas. Não equiparar atributo ausente a comportamento confirmado do leitor.

Nos módulos 101–106, os exercícios originais omitiam required e os acréscimos opcionais usavam false. Inspecionados objetivos e enunciados dos seis módulos e essenciais de 107–109. Selecionados 59 exercícios existentes para cobrir objetivos e variadas competências; demais recebem false explícito. Sem criação, remoção, alteração de enunciados ou IDs. A maior parte dos selecionados é discursiva ou de cálculo/rastreamento; respostas exigem avaliação adequada, não equivalem a aprovação automática. A escolha é editorial e revisável na auditoria geral. Os 35 essenciais de 107–109 permanecem intactos.

| Aula | Total | Essenciais | IDs selecionados |
|---|---:|---:|---|
| 101 | 53 | 8 | 15, 34, 36, 42, 46, 47, 48, 49 |
| 102 | 67 | 10 | 36, 41, 43, 44, 46, 51, 54, 57, 59, 60 |
| 103 | 76 | 11 | 37, 45, 47, 48, 49, 52, 54, 56, 57, 60, 62 |
| 104 | 63 | 9 | 39, 42, 44, 47, 48, 51, 53, 55, 58 |
| 105 | 76 | 10 | 31, 37, 39, 40, 45, 49, 53, 61, 67, 71 |
| 106 | 84 | 11 | 29, 42, 45, 46, 47, 53, 55, 59, 67, 74, 81 |

Após a intervenção: Arquitetura 690 exercícios, 94 essenciais, 596 opcionais. Biblioteca: 1.878 exercícios, 464 essenciais, 1.414 restantes. A auditoria posterior verificará carga, qualidade e distribuição dos essenciais sem impor percentual uniforme. Não foi testado o comportamento do leitor com a mudança de required; a migração do progresso não deve exigir repetir aulas anteriormente concluídas sem política explícita.

Decisão da estudante: preservar nesta fase os essenciais de Lógica e Java. A revisão definitiva desses essenciais deverá incluir atividades práticas de construção, depuração, rastreamento e testes de programas quando os respectivos executores/compiladores estiverem implementados e validados no aplicativo. Não aumentar questões teóricas obrigatórias apenas para equilibrar contagens. Práticas de papel e atividades opcionais não substituem a futura avaliação executável. O banco transversal novo deverá considerar competências já apresentadas, sem depender de runtime ainda indisponível. Nenhum executor implementado por este commit.


## Proposta de percurso guiado — verificação inicial

A proposta de sete etapas, sequência completa e matriz de dependências está em [percurso-guiado.md](percurso-guiado.md). Conferência programática contra manifesto: 45 aulas únicas, ordem interna preservada, dependências propostas e conexões recomendadas sem inversões. Preferência editorial por blocos intercalados. Ainda não é conclusão oficial; revisar após auditoria dos exercícios e definição das revisões generalizadas. Nenhum módulo ou exercício alterado neste commit.


## Auditoria de exercícios — Arquitetura (28/11/2026)

Consultados os nove JSONs reais, agrupamentos, modalidades, essenciais, amostras de enunciados por grupo e repetição de modelos por normalização dos dígitos. A heurística identifica famílias de variantes, não duplicidade semântica comprovada nem avaliação de todas as soluções. 690 exercícios, 94 essenciais, 596 opcionais. CI do percurso proposto 46163615752 aprovada.

| Aula | Diagnóstico | Prioridade de revisão inédita |
|---|---|---|
| 101 | Grupos variados, operações, camadas, diagnóstico; cinco intercâmbios, alguns em Python | Distinguir sintomas e evidências, fluxo dado/arquivo/saída; conectar SO e TI |
| 102 | Interfaces e compatibilidade bem cobertas; quatro essenciais em fonte/térmica | Interpretar ficha técnica fictícia, múltiplas restrições, diferenciar conector/protocolo e investigar sem desmontar |
| 103 | Hierarquia e diagnóstico cobertos; quatro variantes de taxa, seis de capacidade | Interpretar indicadores simultâneos, escolher hipótese e teste, comparar unidade/taxa/latência |
| 104 | Conceitos e jornada de soma; comunicação e gargalos | Explicar caminho de instrução e dado em cenário novo, distinguir modelo abstrato de implementação |
| 105 | 22 rastreamentos em quatro famílias (8+6+4+4) | Detectar estado inconsistente, explicar efeito de desvio e escrita, integrar lógica sem equiparar pseudoinstruções a CPU real |
| 106 | 28 cálculos/rastreamentos em quatro famílias (8+8+8+4) | Escolher cálculo adequado sem fórmula anunciada, identificar hipóteses e limites, combinar endereçamento e binário após 108 |
| 107 | Muitas variantes de decomposição e validação | Resolver ambiguidade de base, justificar erro, interpretar notação em contexto |
| 108 | 134 questões em quatro famílias: 50 pesos, 27 divisões, 39 binário-decimal, 18 largura fixa | Escolher método sem indicação, conferir resposta, diagnosticar erro, combinar representação e capacidade |
| 109 | Conversões abundantes, exemplos RGB e pixels | Interpretar custo de imagem, canal inválido, representação versus aparência e armazenamento, conectar Java após 310 |

Decisão: preservar exercícios e IDs atuais. As variantes de treino são úteis para fluência, mas não constituem competências independentes. No futuro seletor transversal, limitar concentração de uma família por sessão quando houver alternativas, sem excluir variantes para treino direcionado. Inéditos devem exigir escolha de estratégia, explicação de hipóteses, análise de erros e transferência de contexto; não apenas trocar números. A revisão deve poder alternar questões monodisciplinares e integradoras. Não depender de Python, compilador ou desmontagem física. A seleção de essenciais de 101–106 permanece; não foi auditada individualmente a correção de todas as respostas nesta passagem. Nenhum exercício novo publicado neste registro; produção do banco separado ocorrerá após diagnóstico das demais disciplinas e definição de representação editorial compatível.
