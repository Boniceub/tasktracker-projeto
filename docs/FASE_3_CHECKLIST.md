# Fase 3 - etapas executáveis

## 1. Recuperação e requisitos - concluído
- [x] Ler os 12 slides do desafio e a entrega da Fase 2.
- [x] Conferir src/main.py com o GitHub: blob 42087ab3a8c72d6d9965161e891a556a1be755cc.
- [x] Preservar código e planejamento existentes.
- [x] Preparar Dockerfile, docker-compose.yml e README na raiz.

## 2. Ambiente Windows - concluído em 23/10/2026
- [x] WSL instalado: versão 3.0.3.0; docker-desktop em WSL 2.
- [x] Docker Desktop iniciado com sucesso (4.96.3).
- [x] docker version com Client e Server 29.9.2; Compose v5.6.1.

## 3. Testar Docker - concluído tecnicamente
- [x] docker compose config: configuração válida.
- [x] docker compose up --build -d: imagem construída e serviço iniciado.
- [x] docker compose ps -a: serviço Up; inspeção sem erro e sem OOM.
- [x] docker run --rm -i tasktracker:local: cenários funcionais aprovados com entrada automatizada.
- [x] docker compose run --rm -T tasktracker: mesmos cenários aprovados.
- [x] Lista vazia; opção inválida; título vazio/espaços; prioridade inválida; Media normalizada; dois cadastros; listagem; opcionais vazios; saída 0.
- [x] Nova execução sem dados anteriores, conforme armazenamento em memória.
- [x] Evidências em docs/evidencias e relatório em VALIDACAO.md.
- [ ] Ensaio manual para o vídeo com docker run --rm -it tasktracker:local e docker compose run --rm --build tasktracker (testes automatizados usaram -i/-T).

## 4. GitHub - pendente
- [ ] Revisar git diff; adicionar os arquivos da Fase 3 e registrar commit descritivo.
- [ ] Enviar à main do repositório existente, preservando o histórico remoto.
- [ ] Tornar o repositório público conforme exigência, após revisar o conteúdo publicado.
- [ ] Abrir o link sem login e verificar código, Dockerfile, Compose, README e planejamento.
Observação: a cópia local recuperada tem histórico próprio. Não usar force push; sincronizar o remoto antes de enviar.

## 5. Vídeo - pendente, realizado pelo estudante
- [ ] Gravar cerca de 5 minutos seguindo ROTEIRO_VIDEO.md.
- [ ] Horizontal 16:9, rosto e áudio próprios obrigatórios.
- [ ] Mostrar histórico e três arquivos; explicar Dockerfile e Compose; demonstrar build, execução interativa, erros de entrada, cadastro e listagem.
- [ ] Publicar no YouTube como Público ou Não listado, nunca Privado ou Shorts.
- [ ] Testar o link sem login. Não reutilizar o link da Fase 2 como se fosse final.

## 6. PDF e AVA - pendente após vídeo
- [ ] Confirmar nome completo (o PDF anterior contém a grafia Bonifacop; confirmar correção).
- [ ] Montar PDF com nome e links ativos do GitHub e do vídeo final.
- [ ] Conferir os links clicáveis e o acesso sem login.
- [ ] Enviar o PDF no AVA dentro do prazo informado pela disciplina (não consta data nos slides).

Avaliação: conteinerização e orquestração 8 pontos; organização e README 7; vídeo 10. O repositório deve ser público. O PDF é o arquivo de entrega no AVA.
