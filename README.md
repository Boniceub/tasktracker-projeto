# TaskTracker - Fase 3 do Bootcamp II

Aplicação de terminal em Python para cadastrar e listar tarefas. Usa apenas a biblioteca padrão. O código da Fase 2 e o planejamento da Fase 1 foram preservados.

## Preparar Docker no Windows

Validação em 23/10/2026: WSL 3.0.3.0 instalado, distribuição docker-desktop em WSL 2. Docker Desktop 4.96.3 iniciou com sucesso; Client e Server 29.9.2 e Compose v5.6.1 confirmados.

Para retomar após ligar o computador, abra Docker Desktop ou execute `docker desktop start` e aguarde o engine iniciar. Confira:

```powershell
wsl --version
docker version
docker compose version
docker compose config
```

`docker version` deve exibir Client e Server. O erro inicial de pipe inexistente foi resolvido ao iniciar Docker Desktop; não foi necessário reinstalar WSL.

## Construir e executar

Execute na raiz deste projeto. O primeiro build precisa de internet.

Construir a imagem:
```powershell
docker build -t tasktracker:local .
```

Executar diretamente:
```powershell
docker run --rm -it tasktracker:local
```

Executar com Compose (recomendado):
```powershell
docker compose run --rm --build tasktracker
```

Escolha 3 para sair. --rm remove o contêiner ao encerrar. Não há servidor web ou portas a publicar.
O Dockerfile usa Python 3.11 slim, WORKDIR /app, saída imediata e inicia src/main.py. O Compose habilita stdin_open e tty para permitir o uso de input() no terminal.

## Verificar o serviço e encerrar

Também foi validada a execução em segundo plano:

```powershell
docker compose up --build -d
docker compose ps -a
docker compose logs --no-color
```

O serviço fica `Up`, aguardando entrada no menu. Para usar o menu do serviço, execute `docker compose attach tasktracker`; escolher 3 encerra esse contêiner. Para uma sessão independente, prefira `docker compose run --rm --build tasktracker`.

Não há endpoint HTTP, banco, portas ou HEALTHCHECK configurado. `Up` confirma o processo ativo; os testes funcionais registrados em `docs/VALIDACAO.md` verificam o comportamento. Não se deve esperar o rótulo `healthy`.

Para remover o serviço e sua rede ao terminar:

```powershell
docker compose down
```

## Regras da aplicação

- Menu: 1 cadastra, 2 lista e 3 encerra.
- Título obrigatório, sem aceitar apenas espaços.
- Prioridade aceita Alta, Média, Media ou Baixa, respeitando maiúsculas. Media é normalizada para Média.
- Descrição e data limite opcionais, como texto livre.
- Status inicial Pendente.
- Dados em memória: tarefas são perdidas ao encerrar. Não há banco ou volume persistente.

## Executar sem Docker

Requer Python 3; a imagem usa Python 3.11:
```powershell
python src/main.py
```

## Estrutura

```text
tasktracker-projeto/
  Dockerfile
  docker-compose.yml
  .dockerignore
  README.md
  src/main.py
  docs/planejamento_logico.pdf
  docs/FASE_3_CHECKLIST.md
  docs/ROTEIRO_VIDEO.md
  docs/VALIDACAO.md
```

## Entrega

Repositório existente: https://github.com/Boniceub/tasktracker-projeto

O registro anterior informa repositório privado; a visibilidade remota não foi consultada nesta retomada. O desafio exige público. Consulte docs/FASE_3_CHECKLIST.md para publicação, vídeo e PDF. O vídeo da Fase 3 está em gravação e edição; seu link final ainda está pendente. O vídeo anterior não comprova esta etapa. Veja docs/VALIDACAO.md para o que foi realmente testado.
