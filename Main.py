from cadastro import CadastroAluno

cadastro_aluno = CadastroAluno()

# Cadastrar aluno
cadastro_aluno.cadastrar_aluno(
    nome_completo="Fulano da Silva",
    cpf="123.456.789-01",
    telefone="(11) 98765-4321",
    email="fulano@example.com"
)

# Listar alunos
alunos = cadastro_aluno.listar_alunos()
print("Todos os alunos:")
print(alunos)

# Adicione mais operações conforme necessário

cadastro_aluno.close_connection()