# TaskTracker

Aplicação de terminal da Fase 2 do Bootcamp II para cadastrar e visualizar tarefas.

## Tecnologias

Python 3 e Git. Usa somente a biblioteca padrão; não precisa instalar dependências.

## Executar

Na pasta do projeto, execute:

```powershell
python src/main.py
```

O menu permite cadastrar uma tarefa, visualizar todas as tarefas ou sair.
O título é obrigatório e não aceita apenas espaços. A prioridade aceita
exclusivamente `Alta`, `Média`, `Media` ou `Baixa` (respeitando maiúsculas).
A descrição e a data limite são textos livres. Cada tarefa começa com status
`Pendente`. Os dados ficam na memória e são perdidos ao encerrar o programa.

## Estrutura

```text
tasktracker-projeto/
├── README.md
├── .gitignore
├── docs/
│   └── planejamento_logico.pdf
└── src/
    └── main.py
```

## Documento da Fase 1

O planejamento está em docs/planejamento_logico.pdf, elaborado agora com base
na implementação atual. A identificação acadêmica já está preenchida; falta o link do vídeo
antes da entrega. Se houver um documento original já entregue na Fase 1,
compare-o com esta versão para manter a rastreabilidade.

## GitHub

Repositório: https://github.com/Boniceub/tasktracker-projeto

O histórico local registra a estrutura, o menu e as regras de negócio em etapas.
O repositório foi criado como privado. O envio direto pelo Git está bloqueado
nesta sessão; os arquivos enviados pela interface web terão um histórico próprio.
