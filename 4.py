notas = [10, 5, 8]
print('Notas para fazer média', notas)
media = sum(notas) / len(notas)
print('Média das notas:', media)
menor = min(notas)
indice_menor = notas.index(menor)
nova_nota = float(input('Digite a nova nota para substituir a menor: '))
notas[indice_menor] = nova_nota
notas.sort()
print('Notas atualziadas: ', notas)
nova_media = sum(notas) / len(notas)
print('Nova média: ', nova_media)
