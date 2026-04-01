# Ler dados
nome = input("Digite o nome do aluno: ")
idade = int(input("Digite a idade do aluno: "))

# Criar dicionário
aluno = {"nome": nome, "idade": idade}

# Exibir dicionário
print("Dicionário do aluno:", aluno)

# Acesso por chave
print("Nome:", aluno["nome"])
print("Idade:", aluno["idade"])

# Exibir tipo
print("Tipo da variável aluno:", type(aluno))