# Processamento multimídia privado

Código público, dados privados. Primeira etapa: transcrição local em português, CPU/int8, com Faster-Whisper e FFmpeg. Não há integração com Drive nesta versão; não há execução de mídia acadêmica no GitHub Actions público. O CI do catálogo testa regras e caminhos. O workflow separado Transcrição sintética gera exclusivamente fala original fixa com eSpeak NG, usa o modelo small em CPU/int8 e verifica segmentos e pelo menos seis de nove palavras-chave. Não recebe arquivos externos, credenciais ou parâmetros de mídia; não publica artifacts nem transcrições. A CLI privada permanece bloqueada no CI.

## Uso local (Linux)

Instale FFmpeg e Python em seu sistema. No Garuda/Arch, verifique a disponibilidade dos pacotes python e ffmpeg com pacman; use o ambiente virtual fora do checkout. Exemplo, a partir da raiz da Library:

    python -m venv ~/.local/share/pythoteca-media/venv
    ~/.local/share/pythoteca-media/venv/bin/pip install -r tools/media-processing/requirements.txt
    mkdir -p ~/pythoteca-privado
    chmod 700 ~/pythoteca-privado
    ~/.local/share/pythoteca-media/venv/bin/python tools/media-processing/transcribe.py ~/pythoteca-privado/entrada.m4a ~/pythoteca-privado/saida.json

Na primeira execução o modelo small multilíngue será baixado; requer rede, espaço e memória. O modelo base é alternativa mais leve. Use --model base se necessário. O resultado JSON contém segmentos temporizados; a transcrição pode conter erros e precisa ser conferida. O arquivo de entrada não é removido. Áudio intermediário é limpo ao sair normalmente ou por exceção; encerramento abrupto do sistema pode deixar temporários. O cache de modelos não contém transcrições por projeto, mas deve permanecer fora do checkout.

## Privacidade

Nunca colocar mídia, transcrição, credencial, identificador privado ou informação pessoal na árvore pública. Não usar artifacts, caches ou logs públicos para processar materiais acadêmicos. O validador de caminhos é uma barreira adicional, não garante que JSON ou Markdown autorizados estejam livres de conteúdo privado. Revisão editorial obrigatória. A proteção de branch depende de configuração do proprietário: CI executado após push não impede que um commit já publicado seja visto.

Próximas etapas: teste real com fala sintética não acadêmica; validação de versões e desempenho; processamento em lote e formatos TXT/SRT; avaliação de integração autenticada ao Drive com escopo mínimo e execução privada. Não compartilhar a pasta de aulas publicamente para viabilizar download. Não inserir segredos em comandos ou arquivos versionados. Não publicar transcrições integrais.

O teste sintético mede viabilidade funcional, não qualidade em podcasts reais. O tempo informado inclui carregamento/download do modelo e processamento. Python 3.12 foi escolhido para o runner de transcrição, separado do CI do catálogo (3.13). O resultado de reconhecimento ainda depende da execução efetiva do workflow.
