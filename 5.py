# Fila inicial
fila = ["Ana", "Bruno"]
print("Fila inicial:", fila)

nome1 = input("Digite o primeiro nome: ")
nome2 = input("Digite o segundo nome: ")
fila.extend([nome1, nome2])
print("Após adicionar dois nomes:", fila)

prioritario = 'Nara'
fila.insert(1, prioritario)
print("Após inserir prioritário na posição 1:", fila)

atendido = fila.pop(0)
print("Cliente atendido:", atendido)
print("Fila após atendimento:", fila)