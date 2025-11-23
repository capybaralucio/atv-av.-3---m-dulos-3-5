#   BIBLIOTECA UNIVERSITARIA (controller do autor)

from model.autor_model import AutorModel


class AutorController:
    def __init__(self):
        self.model = AutorModel()


    def cadastrar_autor(self, nome, nacionalidade):
        if not nome:
            return "\nO nome do autor não pode ser nulo.\n"
        self.model.cadastrar_autor(nome, nacionalidade)
        return "\nAutor cadastrado com sucesso!!\n"


    def listar_autores(self):
        autores = self.model.listar_autores()

        if not autores:
            return "\nNenhum autor encontrado.\n"
        
        return autores
    

    def atualizar_autor(self, id_autor, novo_nome=None, nova_nacionalidade=None):
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