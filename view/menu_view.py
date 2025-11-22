#   BIBLIOTECA UNIVERSITARIA (view)

from view.autor_view import AutorView
from view.livro_view import LivroView

class MenuView:

    def menu_principal(self):
        while True
            print("\n===== MENU PRINCIPAL =====")
            print("1 - Gerenciar autor")
            print("2 - Gerenciar livro")
            print("3 - Sair")
            op = input("Escolha uma opção: ")

            if op == "1":
                AutorView().menu()
            
            elif op == "2":
                LivroView().menu()

            elif op == "3":
                print("Encerrando o programa da Bilioteca. . .")
                break

            else:
                print("Opcao inválida! Tente novamente.")
