# Validação real da Fase 3 — 23/10/2026

## Resultado

Etapa técnica Docker validada no Windows com engine Linux/WSL 2. Nenhuma alteração em src/main.py, Dockerfile, Compose ou planejamento PDF foi necessária. Os arquivos existentes foram preservados; documentação atualizada. Sem commit, push, mudança de visibilidade ou gravação de vídeo.

## Ambiente e inicialização

- WSL 3.0.3.0; kernel 6.18.54.1-1; distribuição docker-desktop em WSL 2.
- Docker Desktop 4.96.3 (244472); Client/Server 29.9.2, API 1.56, Linux amd64 no servidor.
- Compose v5.6.1; contexto desktop-linux.
- Inicialmente docker version falhou porque o pipe dockerDesktopLinuxEngine não existia. docker desktop start iniciou o Desktop e resolveu o problema.
- A consulta inicial ao WSL no ambiente restrito retornou E_ACCESSDENIED. Repetida com autorização fora da restrição, confirmou o WSL instalado e funcional. Isso não indicava necessidade de reinstalação.

## Construção e serviço

- docker compose config: sucesso (código 0).
- docker compose up --build -d: sucesso; imagem tasktracker:local construída a partir de python:3.11-slim.
- Digest da base resolvida: sha256:b7a9e5f6a93d6d4a31f129bbd4bdee69efccb6ded0fb230d78aafaf37af98377.
- docker compose ps -a: tasktracker-projeto-tasktracker-1 Up, comando python src/main.py.
- docker inspect: Running=true, OOMKilled=false, Error vazio. Logs mostram o menu aguardando entrada.
- Sem servidor HTTP, dependências externas, banco, portas ou HEALTHCHECK. Não há teste HTTP aplicável nem rótulo healthy a exigir.

## Testes funcionais

Executados com entrada UTF-8 automatizada em docker run --rm -i tasktracker:local e docker compose run --rm -T tasktracker, ambos com saída 0. -T desativa o TTY para a entrada automatizada; o ensaio humano com -it continua pendente para o vídeo.

Em ambos os modos passaram: lista inicial vazia; opção 9 inválida; título vazio e somente espaços rejeitados; prioridade Urgente rejeitada; Media convertida em Média; dois cadastros; listagem das duas tarefas com status Pendente; prioridade Baixa; descrição/data opcionais exibidas como não informadas; opção 3 com Até logo. Uma nova execução com opções 2 e 3 confirmou lista novamente vazia e saída 0.

## Evidências

Transcrições reais em evidencias/docker-direto.txt, compose.txt e respectivos arquivos -reinicio.txt. Saídas de docker version, compose config, compose ps, logs e inspeção em evidencias/. O build foi acompanhado na sessão; sua transcrição completa não foi arquivada. A inspeção inclui identificadores locais do Docker e pode ser omitida da publicação se desnecessária.

O serviço Compose foi deixado em execução, aguardando entrada, para revisão. Use docker compose down quando terminar. Não há dados de teste persistentes.

## Pendências objetivas

1. Ensaiar execução interativa para a apresentação.
2. Revisar git diff e sincronizar o histórico remoto antes de commit/push, sem force push. Publicar e tornar público somente após orientação; visibilidade não consultada nesta retomada.
3. Estudante gravar e publicar o vídeo final; testar acesso sem login.
4. Confirmar nome completo, criar PDF de entrega com links reais, conferir prazo e enviar no AVA.
