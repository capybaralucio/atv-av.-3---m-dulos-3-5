#   BIBLIOTECA UNIVERSITARIA (view do autor)

from controller.autor_controller import AutorController

class AutorView:
    def menu(self):
        controller = AutorController()

        while True:
            print("\n---- GERENCIAR AUTOR ----\n")
            print("1 - Cadastrar autor")
            print("2 - Listar autor")
            print("3 - Atualizar autor")
            print("4 - Excluir autor")
            print("5 - Voltar ao menu principal")

        
            opcao = input("Escolha uma opcao: ")


            if opcao == "1":
                nome = input ("Nome do autor: ")
                nacionalidade = input("Nacionalidade: ")

                controller.cadastrar(nome, nacionalidade)


            elif opcao == "2":
                autores = controller.listar()

                print("\n=== LISTA DE AUTORES ===")
                for a in autores:
                    print(f"ID: {a[0]} | Nome: {a[1]} | Nacionalidade: {a[2]}")


            elif opcao == "3":
                id_autor = input("ID do autor: ")

                print("\nDigite novos valores (ou deixe vazio para não alterar):")
                
                novo_nome = input("Novo nome: ") or None
                nova_nacionalidade = input("Nova nacionalidade: ") or None

                controller.atualizar(id_autor, novo_nome, nova_nacionalidade)


            elif opcao == "4":
                id_autor = input("ID do autor: ")
                controller.excluir(id_autor)    


            elif opcao == "5":
                break

            else:
                print ("Opcão inválida. Tente novamente.")