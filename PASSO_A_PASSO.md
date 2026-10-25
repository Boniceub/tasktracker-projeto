# TaskTracker — passo a passo

## 1. Preparar o Python

Instalar o Python 3 e conferir no terminal:

```powershell
python --version
python -m pip --version
```

Se o VS Code já estava aberto durante a instalação, fechar todas as suas
janelas e abrir novamente para carregar o PATH atualizado.

## 2. Abrir a pasta correta

No VS Code, usar Arquivo > Abrir Pasta e selecionar a pasta desta entrega,
`outputs/tasktracker-projeto`. A pasta antiga na Área de Trabalho ainda está vazia.

## 3. Montar a estrutura

Criar `README.md`, `.gitignore`, `docs/` e `src/main.py`.
Ignorar `__pycache__/`, arquivos `.pyc` e ambientes `.venv/`.
Adicionar em `docs/planejamento_logico.pdf` o planejamento original da Fase 1,
quando disponível. O PDF do enunciado não substitui o planejamento.

## 4. Implementar o programa

Em `src/main.py`, criar uma lista em memória e um menu que se repete:

1. Cadastrar nova tarefa.
2. Visualizar tarefas cadastradas.
3. Sair da aplicação.

No cadastro, pedir título, descrição, prioridade e data limite.
Repetir o pedido de título quando vazio ou formado apenas por espaços.
Aceitar somente `Alta`, `Média`, `Media` e `Baixa` como prioridade.
Guardar `Media` como `Média` e definir o status como `Pendente`.
Adicionar o dicionário à lista somente após concluir as entradas.

Na listagem, avisar quando a lista estiver vazia. Caso contrário, exibir
todas as tarefas com seus cinco campos. Mostrar erro para opções inválidas
do menu e continuar a execução.

## 5. Documentar e versionar

O README deve explicar objetivo, tecnologias, execução e armazenamento em memória.
Iniciar o Git na própria pasta do TaskTracker, usando a branch `main`.
Registrar separadamente estrutura, menu e regras de negócio.
Nesta entrega os commits são de autoria da automação Codex; não representam
uma declaração de que o estudante escreveu pessoalmente cada etapa.

## 6. Executar e validar

Na pasta do projeto:

```powershell
python src/main.py
```

Conferir nesta ordem:

1. Escolher 2 sem cadastrar: deve informar que não existem tarefas.
2. Escolher 9: deve informar opção inválida e manter o menu.
3. Escolher 1 e informar título vazio ou somente espaços: deve pedir novamente.
4. Informar um título válido e uma descrição.
5. Informar prioridade `Urgente`: deve rejeitar e pedir novamente.
6. Informar `Media` e uma data livre: deve confirmar o cadastro.
7. Escolher 2: deve mostrar todos os campos, prioridade `Média` e status `Pendente`.
8. Cadastrar outra tarefa e listar: ambas devem aparecer.
9. Escolher 3: deve encerrar sem erro.

Os dados são mantidos somente durante a execução; ao reabrir, a lista começa vazia.

## 7. Concluir a Fase 3

O planejamento já está em docs/planejamento_logico.pdf. Dockerfile e Compose foram preparados e testados em 23/10/2026; consultar README.md, docs/VALIDACAO.md e docs/FASE_3_CHECKLIST.md.

Ainda é necessário ensaiar a demonstração manual, revisar e sincronizar o histórico Git com o repositório existente sem force push, publicar somente após orientação, gravar o vídeo pelo estudante seguindo docs/ROTEIRO_VIDEO.md e montar o PDF final com os links reais. Confirmar nome completo e prazo no AVA. Nenhum push ou vídeo foi realizado nesta retomada.
