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
#  Ler nota
nota = float(input("Digite a nota do aluno: "))

# Adicionar nova chave "nota"
aluno ["nota"] = nota

# Exibir dicionário atualizado
print("Dicionário atualizado:", aluno)

# Acessar a nova informação
print("Nota:", aluno["nota"])