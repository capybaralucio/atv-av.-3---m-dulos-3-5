#   BIBLIOTECA UNIVERSITARIA (controller do autor)

from model.autor_model import AutorModel


class AutorController:
    def __init__(self):
        self.model = AutorModel()


    def cadastrar_autor(self, nome, nacionalidade):
        if not nome:
            return "\nO nome do autor não pode ser nulo.\n"
<<<<<<< HEAD

        sucesso = self.model.cadastrar_autor(nome, nacionalidade)

        if sucesso:    
            return "\nAutor cadastrado com sucesso!!\n"
        else:
            return "\nErro ao cadastrar autor.\n"
=======
        self.model.cadastrar_autor(nome, nacionalidade)
        return "\nAutor cadastrado com sucesso!!\n"
>>>>>>> b4da2420e70473d557b3618dd00105dacdae441c


    def listar_autores(self):
        autores = self.model.listar_autores()
<<<<<<< HEAD
=======

        if not autores:
            return "\nNenhum autor encontrado.\n"
        
>>>>>>> b4da2420e70473d557b3618dd00105dacdae441c
        return autores
    

    def atualizar_autor(self, id_autor, novo_nome=None, nova_nacionalidade=None):
<<<<<<< HEAD
        if not str(id_autor).isdigit():
            return "\nID inválido.\n"

        if novo_nome is None and nova_nacionalidade is None:
            return "\nNada para atualizar.\n"

        sucesso = self.model.atualizar_autor(id_autor, novo_nome, nova_nacionalidade)
        
        if sucesso:
            return "\nAutor atualizado com sucesso!!\n"
        else:
            return "\nErro ao atualizar o autor.\n"

    def excluir_autor(self, id_autor):
        if not str(id_autor).isdigit():
            return "\nID inválido.\n"
        
        sucesso = self.model.excluir_autor(id_autor)

        if sucesso:
            return "\nAutor excluído com sucesso!!\n"
        else:
            return f"\nAutor não encontrado ou erro ao excluir.\n"
=======
        if not id_autor:
            return "\nID inválido.\n"
        
        if novo_nome is None and nova_nacionalidade is None:
            return "\nNada para atualizar.\n"
        
        self.model.atualizar_autor(id_autor, novo_nome, nova_nacionalidade)
        return "\nAutor atualizado com sucesso!!\n"
    

    def excluir_autor(self, id_autor):
        if not id_autor:
            return "\nID inválido.\n"
        
        try:
            self.model.excluir_autor(id_autor)
            return "\nAutor excluído com sucesso!!\n"
        
        except Exception as e:
            return f"\nErro ao excluir o autor: {e}\n"
>>>>>>> b4da2420e70473d557b3618dd00105dacdae441c
