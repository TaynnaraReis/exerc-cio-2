n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))

notas = (n1, n2, n3)

media = sum(notas) / len(notas)

print("Notas:", notas)
print("Média:", media)