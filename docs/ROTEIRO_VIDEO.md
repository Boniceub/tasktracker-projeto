# Roteiro para vídeo final - 5 minutos

Preparar gravação horizontal 16:9 com rosto e áudio próprios. Docker validado em 23/10/2026. Antes de gravar, ensaiar o menu interativo. Nenhuma gravação ou publicação foi feita nesta retomada.

0:00-0:30 - Identificação: nome completo confirmado, ADS e Campus Virtual. Apresentar TaskTracker e objetivo da Fase 3.

0:30-1:30 - Mostrar GitHub, histórico de commits, código preservado, planejamento e os três artefatos: Dockerfile, docker-compose.yml e README.

1:30-2:30 - Explicar Python 3.11 slim, WORKDIR /app, ENV PYTHONUNBUFFERED, COPY e CMD. No Compose mostrar build, stdin_open e tty, explicando que permitem a entrada interativa.

2:30-4:30 - Na raiz executar docker build -t tasktracker:local . e docker run --rm -it tasktracker:local. Mostrar opção 2 com lista vazia; opção inválida; cadastrar com título vazio e depois válido; prioridade inválida e depois Media; listar e sair. Executar docker compose run --rm --build tasktracker e demonstrar cadastro/listagem. Preparar o download da imagem antes para evitar que a gravação dependa da velocidade da rede.

4:30-5:00 - Comentar evolução do planejamento ao Python e ao contêiner. Explicar que os dados permanecem em memória e são perdidos ao sair. Encerrar.

Publicar no YouTube como Público ou Não listado. Testar sem login. Guardar URL final real para gerar o PDF da entrega. O vídeo da Fase 2 é apenas evidência histórica.

Na preparação, conferir docker version e docker compose config. Se mostrar execução em segundo plano, usar docker compose up --build -d e docker compose ps; explicar que Up é esperado para este CLI sem HEALTHCHECK. Ao terminar, docker compose down. Os testes automatizados estão documentados em VALIDACAO.md.
