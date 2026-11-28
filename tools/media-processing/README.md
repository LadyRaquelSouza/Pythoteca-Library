# Processamento multimídia privado

Código público, dados privados. Primeira etapa: transcrição local em português, CPU/int8, com Faster-Whisper e FFmpeg. A integração experimental com Drive usa rclone local, sem autenticação no CI; não há execução de mídia acadêmica no GitHub Actions público. O CI do catálogo testa regras e caminhos. O workflow separado Transcrição sintética gera exclusivamente fala original fixa com eSpeak NG, usa o modelo small em CPU/int8 e verifica segmentos e pelo menos seis de nove palavras-chave. Não recebe arquivos externos, credenciais ou parâmetros de mídia; não publica artifacts nem transcrições. A CLI privada permanece bloqueada no CI.

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

## Correção de compatibilidade

A primeira execução sintética falhou porque faster-whisper 1.2.1 chamou av.open com metadata_errors, rejeitado por PyAV 19.0.2. Como FFmpeg já produz WAV PCM mono de 16 kHz e 16 bits, o motor agora lê esse formato com wave e converte amostras para NumPy float32 normalizadas, passando o vetor diretamente ao Whisper. O teste sintético verifica também os valores extremos da normalização. PyAV continua dependência transitiva; seu decodificador não é usado neste fluxo. A correção ainda requer confirmação em CI.

## Processamento em lote (experimental)

A CLI privada aceita diretórios separados fora do checkout. Crie o destino com chmod 700. Exemplo:

    mkdir -m 700 ~/pythoteca-resultados
    ~/.local/share/pythoteca-media/venv/bin/python tools/media-processing/batch.py ~/pythoteca-privado ~/pythoteca-resultados

Percorre subpastas sem seguir links simbólicos; reconhece mídias suportadas, identifica conteúdo por SHA-256 + modelo + versão do pipeline, reutiliza o motor na mesma execução, valida hashes dos três resultados e ignora duplicatas/conteúdos já concluídos. Cada conjunto contém transcript.json, transcript.txt, transcript.srt e manifest.json. Nomes de saída são hashes, não nomes privados; o hash da fonte identifica o original. Não sobrescreve resultados incompletos ou corrompidos; inspecione-os localmente antes de remover ou mover. Arquivos alterados criam novo conjunto. Execute um lote por vez. Erros de mídia são isolados; o resumo contém apenas contagens e retorna código 1 se houver falhas. Não é um inventário de nomes nem um log de diagnóstico individual. A publicação do conjunto usa diretório de staging e renomeação; interrupção abrupta pode deixar staging privado. O áudio integral é carregado em memória após normalização; arquivos muito longos podem requerer segmentação futura.

O CI sintético cobre duas falas geradas, duplicata, mídia inválida e retomada, sem dados externos. A CLI de lote permanece bloqueada em CI; somente o script fixo de teste chama a função interna. A ponte Drive está implementada experimentalmente; autenticação real e transcrição acadêmica ainda não testadas. A execução anterior de reconhecimento único passou com 8/9 palavras-chave; o lote passou na execução 46107544410.

## Ponte privada para Google Drive (experimental)

Utiliza rclone instalado no ambiente de execução privado. Configure um remote Google Drive dedicado, com acesso apenas às pastas necessárias quando possível; uma configuração normal de OAuth pode conceder acesso mais amplo do que os caminhos usados pelo script. Não confundir restrição do programa com escopo do token. Não publique a pasta nem compartilhe tokens. Crie duas pastas disjuntas e de acesso restrito no Drive (originais e resultados); confirme permissões de compartilhamento antes de executar. O programa não altera permissões remotas. O arquivo de configuração deve ficar fora do checkout, com chmod 600. A configuração padrão de rclone pode conter token OAuth; não o envie ao chat, ao GitHub nem aos logs. Não utilizar configuração criptografada interativa neste fluxo experimental sem preparação específica.

Exemplo fictício, sem identificadores reais:

    python tools/media-processing/drive_io.py --config ~/.config/rclone/rclone.conf --source privado:Originais --destination privado:Transcricoes

Sem --execute, somente lista mídias e apresenta contagens. Com --execute, restaura resultados remotos, baixa mídias para diretório temporário, processa e envia somente os quatro arquivos de cada resultado novo, com manifesto por último. Não apaga originais nem resultados remotos; copyto --immutable evita alterações de arquivos existentes. Não usar rclone sync. Execute um lote por vez. Uma transferência interrompida pode exigir inspeção privada de resultados incompletos. Nesta versão os arquivos remotos são baixados novamente para conferir hashes; otimização por metadados remotos e mapeamento de nomes originais ficam pendentes. Requer espaço temporário suficiente. O destino deve existir previamente. O teste automatizado usa cliente simulado e não verifica OAuth, rclone real, compartilhamento ou rede. Nenhum segredo é necessário no CI público. A execução privada em nuvem não foi provisionada; o código não habilita runners públicos para dados reais.
