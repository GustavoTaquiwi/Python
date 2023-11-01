
def listar_itens(lista):
    print("Lista de Compras:")
    for i, item in enumerate(lista, start=1):
        print(f"{i}. {item}")


lista_compras = []


while True:
    print("\n--- Menu ---")
    print("1. Inserir item")
    print("2. Apagar item")
    print("3. Editar item")
    print("4. Listar itens")
    print("5. Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        novo_item = input("Digite o nome do novo item: ")
        lista_compras.append(novo_item)
        print(f"{novo_item} foi adicionado à lista.")

    elif opcao == "2":
        listar_itens(lista_compras)
        indice = int(input("Digite o número do item a ser apagado: ")) - 1
        if 0 <= indice < len(lista_compras):
            item_removido = lista_compras.pop(indice)
            print(f"{item_removido} foi removido da lista.")
        else:
            print("Índice inválido.")

    elif opcao == "3":
        listar_itens(lista_compras)
        indice = int(input("Digite o número do item a ser editado: ")) - 1
        if 0 <= indice < len(lista_compras):
            novo_nome = input("Digite o novo nome para o item: ")
            lista_compras[indice] = novo_nome
            print(f"Item editado para: {novo_nome}")
        else:
            print("Índice inválido.")

    elif opcao == "4":
        listar_itens(lista_compras)

    elif opcao == "5":
        print("Encerrando o programa.")
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção válida do menu.")
