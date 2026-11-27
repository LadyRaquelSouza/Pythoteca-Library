# ARCH-002b: comunicação autenticada

[PR integrado](https://github.com/LadyRaquelSouza/Pythoteca-2/pull/4), [execução validada](https://github.com/LadyRaquelSouza/Pythoteca-2/actions/runs/45929819699). Commit integrado 25d171b5b214a5d6faae5336d2c63f1f169b73b5.

## Conceitos e código

IPC significa comunicação entre processos. O Binder é a infraestrutura Android que transporta chamadas entre processos; Messenger oferece uma interface baseada em mensagens. Handler recebe mensagens numa fila associada a um Looper. Service oferece um componente sem interface visual; não implica automaticamente uma thread de trabalho.

O módulo protocol é uma biblioteca Java compartilhada, não um APK. Protocol.java define IDs de pacotes, permissão, versão e operações PING/PONG. ProbeClient.kt estabelece conexão explícita, verifica UID e assinatura do executor, envia versão e sessão, recebe resposta e encerra conexão ou aguarda até cinco segundos. ProbeService.java verifica sendingUid, identidade do leitor, assinatura, operação, versão, sessão positiva e replyTo antes de responder. A Activity usa estado Compose para apresentar o resultado.

Permissão signature restringe o acesso a aplicativos com assinatura compatível. Isso não identifica um aplicativo específico: o teste ipc-test possui a mesma assinatura de debug, recebe a permissão, conecta-se, mas não recebe resposta. O UID é atribuído pelo Android e não deve ser confundido com um identificador enviado pelo cliente.

## Testes

- tests/ipc-smoke.sh instala APKs, usa adb e UI Automator para localizar o botão, confirma PONG e rejeição do shell.
- ipc-test/ProbeTest.java usa Instrumentation, HandlerThread e CountDownLatch para verificar ausência de resposta ao UID externo durante três segundos.
- reader/ProtocolTest.java envia operação desconhecida, versão incorreta, sessão zero e mensagem sem replyTo, depois confirma resposta válida. A ausência de replyTo é verificada indiretamente pela continuidade do serviço.
- tests/ipc-negative.sh exige marcador e código de resultado -1 (Activity.RESULT_OK). A primeira execução negativa [45928827242](https://github.com/LadyRaquelSouza/Pythoteca-2/actions/runs/45928827242) imprimiu o marcador de UID mas falhou antes do segundo teste. A saída normal de am instrument -w não incluía o código exigido. Acrescentar -r solicitou saída bruta e confirmou ambos os resultados.

## Limites

Validação em Android 15 x86_64, não em dispositivo físico ARM64. Ausência de resposta durante intervalo limitado não é prova universal de segurança. Ainda faltam execução Python, limites de recursos, rede em execução, recuperação e revisão de ciclo de vida. O módulo ipc-test não deve ser distribuído. Chaves debug não são chaves de produção.

## Leituras e prática

- [Serviços vinculados](https://developer.android.com/develop/background-work/services/bound-services)
- [Messenger](https://developer.android.com/reference/android/os/Messenger)
- [Handler](https://developer.android.com/reference/android/os/Handler)
- [Permissões](https://developer.android.com/guide/topics/permissions/overview)
- [ADB](https://developer.android.com/tools/adb)
- [Instrumentation](https://developer.android.com/reference/android/app/Instrumentation)

Prática opcional: desenhe a sequência bindService, onServiceConnected, PING, PONG e unbindService. Explique por que assinatura válida não basta para identificar o leitor. Compare a saída dos dois testes de instrumentação antes e depois de -r.
