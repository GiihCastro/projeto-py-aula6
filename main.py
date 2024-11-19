lista_de_tarefas = []

# Função para exibir a lista de tarefas
def exibir_tarefas(lista_de_tarefas):
    if not lista_de_tarefas:
        print("Nenhuma tarefa cadastrada.")
        return
    
    print(f"{'Nome':<25} {'Prioridade':<15} {'Categoria':<15} {'Status':<15}")
    print("-" * 70)  

    for tarefa in lista_de_tarefas:
        status_tarefa = "Completa" if tarefa['Status'] else "Incompleta"
        if tarefa['Prioridade'] == "1":
            prioridade_tarefa = "Baixa"
        elif tarefa['Prioridade'] == "2":
            prioridade_tarefa = "Média"
        else:
            prioridade_tarefa = "Alta"
        print(f"{tarefa['Nome']:<25} {prioridade_tarefa:<15} {tarefa['Categoria']:<15} {status_tarefa:<15}")

# Função para marcar uma tarefa como concluída
def marcar_concluida(lista_de_tarefas):
    try:
        num_tarefa = int(input("\nDigite o número da tarefa a ser marcada como concluída: "))
        if 1 <= num_tarefa <= len(lista_de_tarefas):
            lista_de_tarefas[num_tarefa - 1]['Status'] = True
            print("Tarefa marcada como concluída!")
        else:
            print("Número de tarefa inválido.")
    except ValueError:
        print("Por favor, digite um número válido.")

# Escolher as opções
while True:
    print('\nEscolha uma das opções abaixo:')
    menu = input('''\n ------ Sistema MyToDo ------
        | 1 - Cadastrar tarefa
        | 2 - Exibir lista de tarefas
        | 3 - Marcar como concluída
        | 0 - Sair
            
        Digite sua escolha => ''')
    match menu:
        # Cadastrar tarefa
        case "1":
            print("\n----- Cadastrar tarefa -----\n")
            nome = input("Digite sua tarefa: ")
            prioridade = input("Digite o nível de prioridade dessa tarefa de 1-3: ")
            categoria = input("Digite a categoria da sua tarefa: ")
            status = False

            tarefa = {
                "Nome": nome,
                "Prioridade": prioridade,
                "Categoria": categoria,
                "Status": status
            }
            lista_de_tarefas.append(tarefa)

        case "2":
        # Exibir lista de tarefas
            print("\n----- Exibir lista de tarefas -----\n")
            exibir_tarefas(lista_de_tarefas)

        case "3":
        # Marcar uma tarefa como concluída
            while True:
                menu = input('''\n ----- Marcar uma tarefa -----
        | 1 - Encontrar tarefa por nome
        | 2 - Encontrar tarefa por prioridade
        | 3 - Encontrar tarefa por categoria
        | 0 - Retornar
                Digite sua escolha => ''')
                # Encontrar por nome
                if menu == "1":
                    nome_busca = input("Digite o nome da tarefa: ")
                    tarefas_filtradas = [tarefa for tarefa in lista_de_tarefas if nome_busca.lower() in tarefa['Nome'].lower()]
                # Encontrar por prioridade
                elif menu == "2":
                    prioridade_busca = input("Digite a prioridade da tarefa (1-3): ")
                    tarefas_filtradas = [tarefa for tarefa in lista_de_tarefas if tarefa['Prioridade'] == prioridade_busca]
                # Encontrar por categoria
                elif menu == "3":
                    categoria_busca = input("Digite a categoria da tarefa: ")
                    tarefas_filtradas = [tarefa for tarefa in lista_de_tarefas if categoria_busca.lower() in tarefa['Categoria'].lower()]

                elif menu == "0":
                    break

                else:
                    print("Opção inválida!")
                
                if tarefas_filtradas:
                    print("\nTarefas encontradas:")
                    print(f"{'ID':<5} {'Nome':<25} {'Prioridade':<15} {'Categoria':<15} {'Status':<15}")
                    print("-" * 70)
                    for i, tarefa in enumerate(tarefas_filtradas, 1):
                        status_tarefa = "Completa" if tarefa['Status'] else "Incompleta"
                        if tarefa['Prioridade'] == "1":
                            prioridade_tarefa = "Baixa"
                        elif tarefa['Prioridade'] == "2":
                            prioridade_tarefa = "Média"
                        else:
                            prioridade_tarefa = "Alta"
                        print(f"{i:<5} {tarefa['Nome']:<25} {prioridade_tarefa:<15} {tarefa['Categoria']:<15} {status_tarefa:<15}")

                    marcar_concluida(tarefas_filtradas)
                else:
                    print("Nenhuma tarefa encontrada com os critérios informados.")
        
        
        case "0":
            break

        case _:
            print("Opção inválida!")
