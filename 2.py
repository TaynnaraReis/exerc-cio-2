#Ler quatro numeros inteiros
lista = []
num1 = int(input("Digite um número: "))
lista.append(num1)
num2 = int(input("Digite um número: "))
lista.append(num2)
num3 = int(input("Digite um número: "))
lista.append(num3)
num4 = int(input("Digite um número: "))
lista.append(num4)

#Lista antes
print("Tamanho antes:", len(lista))

#Valor alvo
alvo = int(input('Digite o valor a ser removido da lista: '))

#Remover numero
lista.remove(alvo)
print("Valor removido!")

#Lista depois
print("Tamanho depois:", len(lista))