#   BIBLIOTECA UNIVERSITARIA (view)

from view.autor_view import AutorView
from view.livro_view import LivroView

class MenuView:
<<<<<<< HEAD
    def __init__(self):
        self.autor_view = AutorView()
        self.livro_view = LivroView()

    def exibir_menu(self):
=======

    def menu_principal(self):
>>>>>>> b4da2420e70473d557b3618dd00105dacdae441c
        while True:
            print("\n===== MENU PRINCIPAL =====")
            print("1 - Gerenciar autor")
            print("2 - Gerenciar livro")
            print("3 - Sair")
            op = input("Escolha uma opção: ")

            if op == "1":
<<<<<<< HEAD
                self.autor_view.menu_autor()
            
            elif op == "2":
                self.livro_view.menu_livro()

            elif op == "3":
                print("Encerrando o programa da Biblioteca. . .")
=======
                AutorView().menu()
            
            elif op == "2":
                LivroView().menu()

            elif op == "3":
                print("Encerrando o programa da Bilioteca. . .")
>>>>>>> b4da2420e70473d557b3618dd00105dacdae441c
                break

            else:
                print("Opcao inválida! Tente novamente.")