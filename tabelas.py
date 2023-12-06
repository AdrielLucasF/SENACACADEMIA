from conexao import Conexao

class Tabelas:
    def __init__(self, conexao):
        self.conexao = conexao

    def criar_tabelas(self):
        self.conexao.cursor.execute('''
            CREATE TABLE IF NOT EXISTS alunos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_completo TEXT NOT NULL,
                cpf TEXT NOT NULL,
                telefone TEXT NOT NULL,
                email TEXT NOT NULL
            )
        ''')
        self.conexao.conn.commit()
