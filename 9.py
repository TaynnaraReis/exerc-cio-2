nome = input("Nome do produto: ")
preco = float(input("Preço: "))
quantidade = int(input("Quantidade: "))

produto = {"nome": nome, "preco": preco, "quantidade": quantidade}

# Aumento percentual
percentual = float(input("Aumento (%): "))
produto["preco"] = produto["preco"] * (1 + percentual / 100)

# Somar 2 unidades
produto["quantidade"] += 2

# Calcular total
total = produto["preco"] * produto["quantidade"]

print("Produto atualizado:", produto)
print("Total:", total)