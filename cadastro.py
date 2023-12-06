from conexao import Conexao
from tabelas import Tabelas

class CadastroAluno:
    def __init__(self):
        self.conexao = Conexao()
        self.tabelas = Tabelas(self.conexao)
        self.tabelas.criar_tabelas()

    def cadastrar_aluno(self, nome_completo, cpf, telefone, email):
        self.conexao.cursor.execute(
            "INSERT INTO alunos (nome_completo, cpf, telefone, email) VALUES (?, ?, ?, ?)",
            (nome_completo, cpf, telefone, email)
        )
        self.conexao.conn.commit()

    def listar_alunos(self):
        self.conexao.cursor.execute("SELECT * FROM alunos")
        return self.conexao.cursor.fetchall()

    def close_connection(self):
        self.conexao.close()
