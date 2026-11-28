# ARCH-002e: páginas de memória e investigação experimental

## Objetivo e conceitos

Uma página é uma unidade de gerenciamento de memória virtual. O tamanho de página do sistema não é a quantidade total de RAM. Bibliotecas nativas ELF têm segmentos LOAD com requisitos de alinhamento; o APK é um contêiner ZIP, cujo alinhamento de bibliotecas não comprimidas também importa para mapeamento direto. Verificar um não substitui verificar o outro.

## e1: inspeção estática

[Execução 46044913235](https://github.com/LadyRaquelSouza/Pythoteca-2/actions/runs/46044913235), PR #8. tests/apk-inspect.sh usa zipalign -c -P 16 4, apksigner verify e readelf -Wl. O teste verifica alinhamento dos segmentos LOAD e igualdade dos certificados dos dois APKs. Foram registrados 20 marcadores ELF_LOAD_16K_OK e PYTHOTECA_APK_ALIGNMENT_AND_SIGNATURE_OK. A inspeção não demonstra sozinha que o runtime funciona em páginas de 16 KB.

## e2: teste funcional e controles

tests/page16k.sh exige getconf PAGE_SIZE igual a 16384. A preparação configura propriedades de compatibilidade via adb root, retorna ao UID 2000 e confere os valores. A leitura de volta não prova que a imagem Android aplica essas propriedades.

Falhas de ADB, UIAutomator e system_server motivaram controles sem aplicativos e experimentos separados: leitor, executor, ambos, IPC autenticado e Python. A estabilização de 120 segundos e as 24 amostras posteriores de cinco segundos ajudam a observar o ambiente. O PID de system_server é um indicador de continuidade do processo, não prova de saúde integral.

A comparação Python com 2048 e 4096 MB manteve os APKs e a preparação iguais. Ambos retornaram 42 e completaram 24 amostras. Isso demonstra funcionamento nas duas configurações testadas, não estabelece RAM mínima nem exclui pressão de memória.

## Pipeline e evidências

Uma falha de resolução do plugin Chaquopy impediu a produção de APKs e provocou seis falhas secundárias de download. Separar build de runtime permite que dependentes aguardem artefatos válidos. Controles ambientais continuam independentes. Tentativas limitadas de resolução e logs detalhados ajudam a investigar falhas intermitentes, sem provar sua causa.

[Execução 46091383922](https://github.com/LadyRaquelSouza/Pythoteca-2/actions/runs/46091383922), head 417dbf16d821c9b8842430b749a35f917caf002a: bateria 4/16 KB aprovada, B5 em ambas as RAMs aprovado, B4 falhou antes de instalar APKs e passou na segunda tentativa. Total 10/10 considerando ambas. Merge PR #9 db1ef21. A execução posterior 46094319345 aprovou 12/12 incluindo validação documental e classificação do CI.

## Limites

Emulador x86_64 não substitui ARM64 físico. A instabilidade ambiental permanece possível. Não há homologação de release, inventário completo de licenças ou confirmação do efeito das propriedades de compatibilidade. A investigação operacional completa está no [diário de desenvolvimento](https://github.com/LadyRaquelSouza/Pythoteca-2/tree/main/docs/development).

## Leituras e prática

- [Suporte a páginas de 16 KB](https://developer.android.com/guide/practices/page-sizes)
- [Gradle Wrapper](https://docs.gradle.org/current/userguide/gradle_wrapper.html)
- [GitHub Actions](https://docs.github.com/pt/actions)

Prática: diferencie RAM, página de memória, alinhamento ELF e alinhamento ZIP. Desenhe o grafo de dependência entre build e testes. Explique por que uma falha anterior à instalação não demonstra defeito funcional do aplicativo. Proponha uma comparação controlada e identifique quais resultados poderiam refutar sua hipótese.


## e3.1: Gradle Wrapper e confiança na cadeia de build

### O problema

Gradle é a ferramenta que coordena tarefas de compilação, resolução de dependências e empacotamento. Antes desta etapa, o CI baixava uma distribuição e gerava um Wrapper provisório. Isso acrescentava passos e dificultava reproduzir localmente o procedimento. O Wrapper versionado permite iniciar o build com a versão definida pelo projeto, sem depender de uma instalação global do Gradle.

### Como funciona

- `gradlew` e `gradlew.bat`: scripts de entrada para Unix e Windows.
- `gradle-wrapper.jar`: código Java que prepara a distribuição e inicia o Gradle.
- `gradle-wrapper.properties`: configura URL, versão e checksum esperado da distribuição.

No CI, a verificação do JAR acontece antes de executar o script. O JAR e a distribuição são objetos distintos: verificar apenas o ZIP não protege contra um JAR adulterado. SHA-256 é uma função de hash, não criptografia reversível nem assinatura digital. A comparação depende de obter o valor esperado de uma fonte confiável.

A versão 8.11.1 foi mantida. Os scripts e o JAR vieram da tag oficial correspondente. O bit executável do script Unix foi preservado (modo Git 100755). A API textual não aceitou o binário; a alternativa foi transportar os bytes em base64 e criar um blob no repositório de destino. Base64 é codificação, não proteção criptográfica.

Exemplo de inspeção local, a partir da pasta que contém o Wrapper:

```sh
sha256sum gradle/wrapper/gradle-wrapper.jar
git ls-files -s gradlew
```

Compare o hash com a publicação oficial antes de executar `./gradlew --version`. Fixar a versão e verificar integridade melhora a repetibilidade, mas não garante APKs idênticos byte a byte: dependências transitivas, SDK, JDK, ambiente e metadados também podem influenciar o resultado.

### Testes, falhas e decisão

[PR #12](https://github.com/LadyRaquelSouza/Pythoteca-2/pull/12), [execução 46095581452](https://github.com/LadyRaquelSouza/Pythoteca-2/actions/runs/46095581452), head f63d452. A primeira tentativa aprovou 10/12 jobs, incluindo Wrapper e compilação. Runtime 16 KB e ping isolado falharam; houve ADB offline, aborto de instrumentação por falha do sistema e SIGSEGV em processo Google. A segunda tentativa aprovou 12/12 no mesmo head. O resultado reforça a hipótese ambiental, mas não identifica a causa raiz. O PR foi integrado por squash em 9a12903; o registro operacional foi consolidado no PR #13.

Não houve homologação física ARM64 nem teste do script Windows. A licença do projeto e o inventário completo de terceiros continuam pendentes.

### Leituras e atividades opcionais

- [Gradle Wrapper](https://docs.gradle.org/current/userguide/gradle_wrapper.html)
- [Checksums oficiais](https://gradle.org/release-checksums/)
- [Alterações reais do PR #12](https://github.com/LadyRaquelSouza/Pythoteca-2/pull/12/files)

Prática: explique a diferença entre hash, assinatura e base64; compare os quatro arquivos do Wrapper e identifique qual controla a versão. Imagine um ZIP legítimo acompanhado de um JAR adulterado: qual verificação detectaria a alteração? Explique por que repetir o mesmo commit é mais informativo para investigar intermitência do que alterar simultaneamente código e ambiente.
