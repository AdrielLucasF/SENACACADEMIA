import sqlite3

class Conexao:
    def __init__(self, db_name='academia.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def close(self):
        self.conn.close()
