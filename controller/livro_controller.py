#   BIBLIOTECA UNIVERSITARIA (controller do livro)

from model.livro_model import LivroModel


class LivroController:
    def __init__(self):
        self.model = LivroModel()


    def cadastrar_livro(self, titulo, ano_publicacao, id_autor):
        if not titulo:
            return "\nO título não pode ser nulo.\n"
        
        if not ano_publicacao:
            return "\nO ano de publicação não pode ser nulo.\n"
        
        if not id_autor:
            return "\nO ID do autor não pode ser nulo.\n"
        
<<<<<<< HEAD
        sucesso = self.model.cadastrar_livro(titulo, ano_publicacao, id_autor)
        
        if sucesso:
            return "\nSeu livro foi cadastrado com sucesso!!\n"
        else:
            return "\nErro ao cadastrar o livro.\n"
=======
        self.model.cadastrar_livro(titulo, ano_publicacao, id_autor)
        return "\nSeu livro foi cadastrado com sucesso!!\n"
    
>>>>>>> b4da2420e70473d557b3618dd00105dacdae441c

    def atualizar_livro(self, id_livro, novo_titulo=None,novo_ano=None, novo_autor=None):
        if not id_livro:
            return "\nID inválido.\n"
        
        if novo_titulo is None and novo_ano is None and novo_autor is None:
            return "\nNada para atualizar.\n"
        
<<<<<<< HEAD
        atualizado = self.model.atualizar_livro(id_livro, novo_titulo, novo_ano, novo_autor)
        
        if atualizado:
            return "\nLivro atualizado com sucesso!!\n"
        else:
            return "\nNenhum livro atualizado (ID pode não existir).\n"
=======
        self.model.atualizar_livro(id_livro, novo_titulo, novo_ano, novo_autor)
        return "\nLivro atualizado com sucesso!!\n"
    
>>>>>>> b4da2420e70473d557b3618dd00105dacdae441c

    def excluir_livro(self, id_livro):
        if not id_livro:
            return "\nID inválido.\n"
        
        try:
<<<<<<< HEAD
            excluido = self.model.excluir_livro(id_livro)

            if excluido:
                return "\nLivro excluído com sucesso!!\n"
            else:
                return f"\nNenhum livro encontrado com esse ID.\n"

        except Exception as e:
            return "\nErro ao excluir livro: {e}\n"
=======
            self.model.excluir_livro(id_livro)
            return "\nLivro excluído com sucesso!!\n"
        except Exception as e:
            return f"\nErro ao excluir o livro: {e}\n"
>>>>>>> b4da2420e70473d557b3618dd00105dacdae441c
        

    def listar_livros(self):
        livros = self.model.listar_livros()

        if not livros:
            return "\nNenhum livro foi encontrado.\n"
        

        texto = "\n----LISTA DE LIVROS----\n"
        for livro in livros:
<<<<<<< HEAD
            texto += (
                f"ID: {livro[0]}\n"
                f"Título: {livro[1]}\n"
                f"Ano: {livro[2]}\n"
                f"Autor: {livro[3]}\n"
                f"Nacionalidade: {livro[4]}\n"
                "------------------------------\n"
            )

=======
            texto += f"ID: {livro[0]} | Título: {livro[1]} | Ano: {livro[2]} | Autor: {livro[3]}\n"
        
>>>>>>> b4da2420e70473d557b3618dd00105dacdae441c
        return texto