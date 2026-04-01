# Ler dados
nome = input("Nome do produto: ")
preco = float(input("Preço do produto: "))

produto = {"nome": nome, "preco": preco}

print("Antes:", produto)

# Remover chave "desconto" com segurança
produto.pop("desconto", None)

print("Depois:", produto)