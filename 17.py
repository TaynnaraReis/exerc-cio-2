n1 = int(input("Número 1: "))
n2 = int(input("Número 2: "))
n3 = int(input("Número 3: "))
n4 = int(input("Número 4: "))

tupla = (n1, n2, n3, n4)

ordenada = sorted(tupla)

print("Tupla original:", tupla)
print("Ordenado:", ordenada)
print("Tipo da ordenada:", type(ordenada))