# ARCH-002d: segurança e recuperação

## Evidência

- [d1: exceção e rede](https://github.com/LadyRaquelSouza/Pythoteca-2/actions/runs/46007792523), PR 6, integrado em 364a17961693afcfcc995be0e573f016a08e5e3c.
- [d2: watchdog e recuperação](https://github.com/LadyRaquelSouza/Pythoteca-2/actions/runs/46008825493), PR 7, integrado em f608a594c98e53e1ec6ed59a7a83d82ef2f41944.
- Android 15 x86_64, instrumentação com resultado -1 e todos os marcadores anteriores preservados.

## Exceções e rede

probe.py contém fail(), que lança ValueError, e network_denied(), que tenta abrir socket IPv4 TCP para 192.0.2.1:443 (endereço reservado para documentação). Só EACCES ou EPERM contam como negação; timeout não prova bloqueio. ProbeService converte exceção em PYTHON_ERROR. ProtocolTest exige erro, resultado 42, negação de rede e novamente 42. Marcadores PYTHOTECA_PYTHON_EXCEPTION_RECOVERED e PYTHOTECA_PYTHON_NETWORK_DENIED.

## Concorrência e watchdog

endless() executa while True: pass. AtomicBoolean estático reserva uma execução por processo; compareAndSet evita uma corrida entre verificação e reserva. Uma segunda solicitação recebe PYTHON_BUSY. Após inicialização do runtime, Handler.postDelayed agenda Process.killProcess(Process.myPid()) para cinco segundos. PYTHON_STARTED informa o PID antes da chamada Python. UID identifica o aplicativo para autenticação; PID identifica uma instância de processo, podendo ser reutilizado pelo sistema.

ProtocolTest mantém vínculo BIND_AUTO_CREATE, observa onServiceDisconnected, aguarda novo onServiceConnected e solicita answer(). Exige resultado 42, PID positivo e diferente, UID esperado, versão e sessão. Marcadores PYTHOTECA_WATCHDOG_OK, PYTHOTECA_BUSY_OK e PYTHOTECA_PROCESS_RECOVERY_OK. O leitor de instrumentação sobreviveu; a interface Compose não foi testada nesse cenário de recuperação.

## Limites

Watchdog experimental apenas para endless(), não cobre inicialização nem bloqueio da thread principal. STARTED antecede a entrada efetiva na função; morte e recuperação são observadas, não uma prova universal de interrupção. Handler usa tempo de atividade e pode atrasar. Não há execução arbitrária, limites de memória/saída, proteção contra todos os canais indiretos de rede ou homologação física. O teste de rede cobre uma tentativa IPv4 específica. As operações experimentais precisam ser removidas ou segregadas antes da distribuição.

## Leituras e prática

- [Processos e threads](https://developer.android.com/guide/components/processes-and-threads)
- [ServiceConnection](https://developer.android.com/reference/android/content/ServiceConnection)
- [Process](https://developer.android.com/reference/android/os/Process)
- [Exceções Python](https://docs.python.org/pt-br/3/tutorial/errors.html)

Prática: diferencie timeout do cliente, watchdog do executor e exceção Python. Explique por que PID diferente não substitui autenticação por UID. Desenhe o ciclo de reconexão e identifique os pontos onde o teste exige evidência positiva.
