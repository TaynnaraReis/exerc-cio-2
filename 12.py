f1 = input("Fruta 1: ")
f2 = input("Fruta 2: ")
f3 = input("Fruta 3: ")

frutas = (f1, f2, f3)

busca = input("Digite uma fruta para buscar: ")

if busca in frutas:
    print("Está na tupla!")
else:
    print("Não está na tupla!")