# Fila inicial
fila = ["Ana", "Bruno"]
print("Fila inicial:", fila)

# Ler dois nomes e adicionar usando extend
nome1 = input("Digite o primeiro nome: ")
nome2 = input("Digite o segundo nome: ")
fila.extend([nome1, nome2])
print("Após adicionar dois nomes:", fila)

# Ler cliente prioritário e inserir na posição 1
prioritario = input("Digite o nome do cliente prioritário: ")
fila.insert(1, prioritario)
print("Após inserir prioritário na posição 1:", fila)

# Atender (remover o primeiro da fila)
atendido = fila.pop(0)
print("Cliente atendido:", atendido)
print("Fila após atendimento:", fila)