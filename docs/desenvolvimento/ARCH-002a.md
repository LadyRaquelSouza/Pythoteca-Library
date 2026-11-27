# ARCH-002a: do código aos APKs

## Objetivo e evidência

Compilar dois aplicativos Android independentes: leitor Kotlin/Compose e executor Chaquopy/Python. [PR integrado](https://github.com/LadyRaquelSouza/Pythoteca-2/pull/3), [execução aprovada](https://github.com/LadyRaquelSouza/Pythoteca-2/actions/runs/45924994028), commit integrado 10abd53ba7cc1976e8fb31c758f867e45e489bc0. Build concluído em 1m33s. Ainda não houve instalação, execução Python ou IPC em dispositivo.

## Anatomia do projeto

- settings.gradle.kts: define repositórios de dependências e módulos reader e executor.
- build.gradle.kts raiz: declara versões dos plugins sem aplicá-los à raiz. Cada módulo aplica os plugins de que precisa.
- reader/build.gradle.kts: Kotlin 2.1.20, Compose BOM 2025.04.01, Android API 35, Java 17. BOM coordena versões de bibliotecas, não é compilador.
- MainActivity.kt: onCreate recebe o estado salvo; setContent inicia a composição; MaterialTheme fornece tema; Box ocupa a tela e centraliza Text. Compare com JFrame e JLabel no Swing: Compose descreve a interface declarativamente.
- executor/build.gradle.kts: Chaquopy 17.2.0 e Python 3.13, ABIs arm64-v8a e x86_64. ABI é o contrato binário entre código compilado e plataforma.
- probe.py: def answer(): return 6 * 7. A função está empacotada, mas ainda não foi chamada no Android.
- AndroidManifest.xml: identidade e componentes de cada aplicativo. IDs distintos permitem instalação separada; ausência de INTERNET no manifesto final do executor é uma evidência estática, não prova de isolamento completo.

## CI e depuração

O workflow .github/workflows/arch-002.yml executa em Ubuntu 24.04, com permissões de leitura e sem chaves de distribuição. Ações fixadas por SHA reduzem risco de alterações inesperadas. Gradle 8.11.1 foi baixado e comparado ao checksum publicado; falta fixar independentemente o hash e incluir wrapper definitivo.

1. [Primeira tentativa](https://github.com/LadyRaquelSouza/Pythoteca-2/actions/runs/45924555494): python3.13: command not found, saída 127. O PATH é uma lista de diretórios pesquisados pelo shell para encontrar executáveis. Declarar Python no Gradle não instala Python no servidor. Correção: actions/setup-python.
2. [Segunda tentativa](https://github.com/LadyRaquelSouza/Pythoteca-2/actions/runs/45924742081): Python 3.13.18 disponível, sdkmanager ausente, saída 127. Correção: android-actions/setup-android.
3. [Terceira tentativa](https://github.com/LadyRaquelSouza/Pythoteca-2/actions/runs/45924856539): sdkmanager instalado, mas a ação solicitava o pacote legado tools, indisponível. Saída 1. Inspecionar action.yml revelou packages: tools platform-tools. Correção: packages: platform-tools.
4. Quarta tentativa: build aprovado, aapt confirmou IDs distintos e ABIs, verificação de INTERNET passou. O leitor contém também armeabi-v7a e x86; avaliar redução futura.

Com set -euo pipefail, falhas de comandos, variáveis indefinidas e falhas em pipelines podem interromper o script. Ler o primeiro erro relevante, identificar a etapa e evitar mudanças não relacionadas. Um erro de ambiente não demonstra erro no código da aplicação.

## Leituras e prática opcional

- [Gradle: fundamentos](https://docs.gradle.org/current/userguide/userguide.html)
- [Android SDK Manager](https://developer.android.com/tools/sdkmanager)
- [Compose](https://developer.android.com/develop/ui/compose)
- [Chaquopy](https://chaquo.com/chaquopy/doc/current/)
- [GitHub Actions](https://docs.github.com/pt/actions)
- [Bash](https://www.gnu.org/software/bash/manual/bash.html)

No Linux, experimente command -v python3 e printf '%s\n' "$PATH". Execute um comando inexistente e imediatamente echo $? para observar 127. Compare os logs das quatro tentativas e identifique quais etapas nunca chegaram a executar. Não é necessário instalar Android SDK para essas práticas.

## Próximo marco

IPC autenticado entre APKs, testes em Android 15, execução Python e testes negativos. Moto G05 continua referência física; Galaxy A06 fora do escopo. Nenhum APK de produção homologado.
