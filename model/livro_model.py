#   BIBLIOTECA UNIVERSITARIA (model do livro)
import psycopg2

class LivroModel:
    def __init__(self):
        try:
            self.conexao = psycopg2.connect(
                host = "localhost",
                database = "bibliotecabd",
                user = "postgres",
                password = "admin6",
                port = "5432"
            )
        except Exception as e:
            print("Erro ao conectar ao banco:", e)


    def gerenciar_livro(self, id, titulo, ano_publicacao, id_autor):
        pass