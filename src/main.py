"""TaskTracker: cadastro e listagem de tarefas em memória."""


def ler_titulo():
    while True:
        titulo = input("Título: ").strip()
        if titulo:
            return titulo
        print("O título é obrigatório e não pode conter apenas espaços.")


def ler_prioridade():
    while True:
        prioridade = input("Prioridade (Alta/Média/Baixa): ").strip()
        if prioridade in ("Alta", "Média", "Media", "Baixa"):
            return "Média" if prioridade == "Media" else prioridade
        print("Prioridade inválida. Digite Alta, Média (ou Media) ou Baixa.")


def cadastrar_tarefa(tarefas):
    titulo = ler_titulo()
    descricao = input("Descrição: ").strip()
    prioridade = ler_prioridade()
    data_limite = input("Data limite (texto livre ou DD/MM/AAAA): ").strip()
    tarefas.append({
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "data_limite": data_limite,
        "status": "Pendente",
    })
    print("Tarefa cadastrada com sucesso!")


def listar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa cadastrada no momento.")
        return
    for numero, tarefa in enumerate(tarefas, start=1):
        print(f"\n--- Tarefa {numero} ---")
        print(f"Título: {tarefa['titulo']}")
        print(f"Descrição: {tarefa['descricao'] or '(não informada)'}")
        print(f"Prioridade: {tarefa['prioridade']}")
        print(f"Data limite: {tarefa['data_limite'] or '(não informada)'}")
        print(f"Status: {tarefa['status']}")


def main():
    tarefas = []
    print("TaskTracker")
    while True:
        print("\n1. Cadastrar nova tarefa")
        print("2. Visualizar tarefas cadastradas")
        print("3. Sair da aplicação")
        try:
            opcao = input("Escolha uma opção: ").strip()
            if opcao == "1":
                cadastrar_tarefa(tarefas)
            elif opcao == "2":
                listar_tarefas(tarefas)
            elif opcao != "3":
                print("Opção inválida. Escolha 1, 2 ou 3.")
        except (EOFError, KeyboardInterrupt):
            print("\nAplicação encerrada.")
            break
        if opcao == "3":
            print("Até logo!")
            break


if __name__ == "__main__":
    main()
