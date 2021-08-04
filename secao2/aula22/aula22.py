'''
aula 40 - aplit, join e enumerate
'''

string = 'Hoje é dia 29 de Julho.'

lista1 = string.split(' ')
lista2 = string.split(',')

for valor in lista1:
    print(f'A palavra {valor} e aparece {lista1.count(valor)} vezes')

string2 = '.'.join(lista1)
print(string2)

for indice, valor in enumerate(lista1):
    print(indice, valor)