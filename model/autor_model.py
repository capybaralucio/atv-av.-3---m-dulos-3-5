#   BIBLIOTECA UNIVERSITARIA (model do autor)
import psycopg2

class AutorModel:
    def __init__(self):
        try:
            self.conexao = psycopg2.connect(
                host = "localhost",
                database = "bibliotecabd",
                user = "postgres",
                password = "admin6",
                port = "5432"
            )
            self.cursor = self.conexao.cursor()
        except Exception as e:
            print("Erro ao conectar ao banco:", e)


    def cadastrar_autor(self, nome, nacionalidade):
        sql = "INSERT INTO autor (nome, nacionalidade) VALUES (%s, %s)"
        self.cursor.execute(sql, (nome, nacionalidade))
        self.conexao.commit()


    def listar_autores(self):
        self.cursor.execute("SELECT * FROM autor")
        return self.cursor.fetchall()
    

    def atualizar_autor(self, id, novo_nome, nova_nacionalidade):
        sql = "UPDATE autor SET nome=%s, nacionalidade=%s WHERE id=%s"
        self.cursor.execute(sql, (novo_nome, nova_nacionalidade, id))
        self.conexao.commit()


    def excluir_autor(self, id):
           sql = "DELETE FROM autor WHERE id=%s"
           self.cursor.execute(sql, (id,))
           self.conexao.commit()