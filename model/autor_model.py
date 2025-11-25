#   BIBLIOTECA UNIVERSITARIA (model do autor)
<<<<<<< HEAD
from model.conexao import Conexao
=======
import psycopg2
>>>>>>> b4da2420e70473d557b3618dd00105dacdae441c

class AutorModel:
    def __init__(self):
        try:
<<<<<<< HEAD
            self.conexao = Conexao().conectar()
            self.cursor = self.conexao.cursor()
=======
            self.conexao = psycopg2.connect(
                host = "localhost",
                database = "bibliotecabd",
                user = "postgres",
                password = "admin6",
                port = "5432"
            )
            self.cursor = self.conexao.cursor()

>>>>>>> b4da2420e70473d557b3618dd00105dacdae441c
        except Exception as e:
            print("\nErro ao conectar ao banco:\n", e)


    def cadastrar_autor(self, nome, nacionalidade):
        try:
            sql = "INSERT INTO autor (nome, nacionalidade) VALUES (%s, %s)"
            self.cursor.execute(sql, (nome, nacionalidade))
            self.conexao.commit()
<<<<<<< HEAD
            return True
=======
            print("\nAutor cadastrado com sucesso!\n")
>>>>>>> b4da2420e70473d557b3618dd00105dacdae441c

        except Exception as e:
            print("\nErro ao cadastrar autor:\n", e)
            self.conexao.rollback()
<<<<<<< HEAD
            return False

    def listar_autores(self):
        try:
            self.cursor.execute("SELECT * FROM autor ORDER BY id")
=======


    def listar_autores(self):
        try:
            self.cursor.execute("SELECT * FROM autor")
>>>>>>> b4da2420e70473d557b3618dd00105dacdae441c
            return self.cursor.fetchall()
        
        except Exception as e:
            print("\nErro ao listar autores.\n", e)
            return[]
       

    def atualizar_autor(self, id_autor, novo_nome=None, nova_nacionalidade=None):
        try:
            sql = "UPDATE autor SET "
            valores = []
            partes = []


            if novo_nome is not None:
                partes.append("nome = %s")
                valores.append(novo_nome)

            if nova_nacionalidade is not None:
                partes.append("nacionalidade = %s")
                valores.append(nova_nacionalidade)

            
            if not partes:
<<<<<<< HEAD
                return False
=======
                print("\nNenhum campo para atualizar.\n")
                return
>>>>>>> b4da2420e70473d557b3618dd00105dacdae441c
            

            sql += ", ".join(partes) + " WHERE id = %s"
            valores.append(id_autor)


            self.cursor.execute(sql, tuple(valores))
            self.conexao.commit()
<<<<<<< HEAD
            return self.cursor.rowcount > 0
=======
            print("\nAutor atualizado com sucesso!\n")
>>>>>>> b4da2420e70473d557b3618dd00105dacdae441c

        except Exception as e:
            print("\nErro ao atualizar o autor.\n", e)
            self.conexao.rollback()
<<<<<<< HEAD
            return False
=======

>>>>>>> b4da2420e70473d557b3618dd00105dacdae441c

    def excluir_autor(self, id_autor):
        try:
            sql = "DELETE FROM autor WHERE id=%s"
            self.cursor.execute(sql, (id_autor,))
            self.conexao.commit()
<<<<<<< HEAD
            return self.cursor.rowcount > 0
=======
>>>>>>> b4da2420e70473d557b3618dd00105dacdae441c

        except Exception as e:
            print("\nErro ao excluir autor.\n", e)
            self.conexao.rollback()
<<<<<<< HEAD
            return False
    
=======

    
    def fechar_conexao(self):
        if self.cursor:
            self.cursor.close()
        if self.conexao:
            self.conexao.close()
>>>>>>> b4da2420e70473d557b3618dd00105dacdae441c
