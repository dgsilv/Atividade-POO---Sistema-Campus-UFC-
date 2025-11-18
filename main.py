from campus.campus import Campus

def menu_principal():
    print("\n===== SISTEMA UFC - POO =====")
    print("1 - Criar Campus")
    print("2 - Selecionar Campus")
    print("3 - Listar Campi")
    print("0 - Sair")
    return input("Escolha uma opção: ")

def menu_campus(campus):
    while True:
        print(f"\n--- Campus {campus.nome} ---")
        print("1 - Adicionar curso")
        print("2 - Listar cursos")
        print("3 - Atualizar curso")
        print("4 - Remover curso")
        print("0 - Voltar")

        op = input("Escolha uma opção: ")

        if op == "1":
            nome = input("Nome do curso: ")
            carga = int(input("Carga horária (h): "))
            campus.adicionar_curso(nome, carga)

        elif op == "2":
            campus.listar_cursos()

        elif op == "3":
            id_curso = int(input("ID do curso: "))
            novo_nome = input("Novo nome: ")
            nova_carga = int(input("Nova carga horária: "))
            campus.atualizar_curso(id_curso, novo_nome, nova_carga)

        elif op == "4":
            id_curso = int(input("ID do curso: "))
            campus.remover_curso(id_curso)

        elif op == "0":
            break
        else:
            print("Opção inválida!")

def main():
    campi = []

    while True:
        opcao = menu_principal()

        if opcao == "1":
            nome = input("Nome do campus: ")
            campi.append(Campus(nome))
            print(f"Campus '{nome}' criado!")

        elif opcao == "2":
            if not campi:
                print("Nenhum campus cadastrado.")
                continue

            print("\nCampi cadastrados:")
            for i, campus in enumerate(campi):
                print(f"{i+1} - {campus.nome}")

            escolha = int(input("Escolha um campus: ")) - 1

            if 0 <= escolha < len(campi):
                menu_campus(campi[escolha])
            else:
                print("Campus inválido.")

        elif opcao == "3":
            if not campi:
                print("Nenhum campus cadastrado.")
            else:
                for c in campi:
                    print(c)

        elif opcao == "0":
            print("Encerrando...")
            break

        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
