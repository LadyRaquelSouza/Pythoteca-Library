# Pythoteca por dentro

Diário de engenharia e percurso complementar de estudos baseado no desenvolvimento público da Pythoteca. Não integra o catálogo de aulas distribuído pelo aplicativo.

## Como acompanhar

Cada etapa deverá registrar objetivo, conceitos prévios, decisões e alternativas, arquivos e trechos de código relevantes, explicação do funcionamento, testes e resultados reais, limitações, sugestões de leitura e atividades opcionais. Distinguir propostas de implementação e resultados homologados. Não publicar credenciais, materiais privados ou dados pessoais.

## Primeiras etapas

### FOUNDATION-001 — Fundação

Um repositório Git registra versões de arquivos; commits são registros de alterações, branches permitem trabalhar separadamente e pull requests permitem revisar antes de integrar. O README apresenta objetivos e estado do projeto. Um repositório público não equivale a uma licença de código aberto.

Estude: [Git Book em português](https://git-scm.com/book/pt-br/v2), [documentação de pull requests](https://docs.github.com/pt/pull-requests).
Prática: explique a diferença entre commit, branch e merge; examine o histórico público sem modificar arquivos.

### SECURITY-001 — Segurança

Um modelo de ameaças identifica ativos, fronteiras de confiança, ameaças, controles e evidências necessárias. O leitor e o executor devem ter UIDs distintos: o Android usa a identidade do aplicativo para restringir acesso a dados e permissões. IPC é comunicação entre processos; deve autenticar o interlocutor e validar mensagens. HTTPS protege o transporte; SHA-256 verifica integridade quando o hash esperado é confiável; assinatura digital permite verificar autenticidade usando uma chave pública.

Estude: [sandbox Android](https://source.android.com/docs/security/app-sandbox), [segurança Android](https://developer.android.com/privacy-and-security/security-tips), [modelo de ameaças OWASP](https://owasp.org/www-community/Threat_Modeling).
Prática: desenhe as fronteiras entre leitor, executor e biblioteca. Explique por que modificar um arquivo e seu hash no mesmo catálogo não é detectado por uma verificação de hash isolada.

### ARCH-001 — Arquitetura

A proposta separa interface Kotlin/Compose, executor Chaquopy/Python, contratos IPC e futuro instalador Suite. Compose descreve interfaces a partir de estado; Kotlin interoperará com Java. Chaquopy incorpora um runtime Python ao APK executor. Gradle organiza módulos, plugins e dependências. minSdk é a API mínima, targetSdk determina comportamentos de compatibilidade e compileSdk determina APIs disponíveis na compilação.

Estude: [Kotlin](https://kotlinlang.org/docs/home.html), [Compose](https://developer.android.com/develop/ui/compose), [Chaquopy](https://chaquo.com/chaquopy/doc/current/), [Gradle](https://docs.gradle.org/current/userguide/userguide.html), [PackageInstaller](https://developer.android.com/reference/android/content/pm/PackageInstaller).
Prática: compare uma interface declarativa com um formulário Java Swing; explique por que dois módulos Gradle não implicam automaticamente dois UIDs Android.

### ARCH-002 — Experimento

Pendente de implementação e testes. O objetivo é demonstrar compilação e comunicação entre APKs independentes no Android 15, antes de desenvolver funcionalidades pedagógicas. O Moto G05 é o dispositivo físico de referência. Os resultados e explicações de código serão acrescentados conforme evidências reais.

## Referência de engenharia

[Repositório público Pythoteca-2](https://github.com/LadyRaquelSouza/Pythoteca-2). As etapas FOUNDATION-001, SECURITY-001 e ARCH-001 são documentais; sua integração não comprova que os controles ou a arquitetura já funcionam.
