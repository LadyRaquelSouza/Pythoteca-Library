# ARCH-002c: primeira execução Python

[PR integrado](https://github.com/LadyRaquelSouza/Pythoteca-2/pull/5), [execução aprovada](https://github.com/LadyRaquelSouza/Pythoteca-2/actions/runs/46006985426), commit 705253b5128732c62597d174d25f950117ad0800.

## Da interface ao interpretador

O botão Compose chama ProbeClient.start(true). O cliente envia PYTHON_PROBE com versão e sessão. ProbeService autentica o remetente antes de iniciar uma thread. Python.start(new AndroidPlatform(getApplicationContext())) inicializa o runtime se necessário; Python.getInstance().getModule("probe").callAttr("answer").toInt() importa o módulo, chama a função e converte seu retorno em inteiro Java. probe.py contém:

```python
def answer():
    return 6 * 7
```

O serviço devolve PYTHON_RESULT com um Bundle contendo value. O leitor verifica UID, assinatura, versão, sessão e tipo da resposta antes de atualizar o estado Compose. PYTHON_ERROR representa falha da operação.

## Concorrência

Thread separada evita bloquear o Handler principal durante a inicialização. AtomicBoolean.compareAndSet(false, true) reserva a execução atomicamente; finally libera a reserva. A proteção é experimental e precisa de revisão do ciclo de vida do serviço. O timeout de 30 segundos do cliente limita a espera, não interrompe Python. Ainda não há execução arbitrária.

## Evidência

Build aprovado em 1m43s. Android 15 x86_64: PYTHOTECA_PYTHON_42_OK, PYTHOTECA_IPC_PONG_OK, PYTHOTECA_SHELL_PERMISSION_DENIED, PYTHOTECA_FOREIGN_UID_DENIED e PYTHOTECA_INVALID_MESSAGES_DENIED. Ambos os testes de instrumentação retornaram -1. Não houve teste físico ARM64.

## Leituras e prática

- [Chaquopy: API Java](https://chaquo.com/chaquopy/doc/current/java.html)
- [Python: funções](https://docs.python.org/pt-br/3/tutorial/controlflow.html)
- [Android: processos e threads](https://developer.android.com/guide/components/processes-and-threads)
- [AtomicBoolean](https://developer.android.com/reference/java/util/concurrent/atomic/AtomicBoolean)

Prática opcional: acompanhe o tipo do valor 42 desde o retorno Python até o texto Compose. Explique por que esperar 30 segundos não equivale a interromper a execução. Compare return com print e o papel de uma thread com o de um processo independente.
