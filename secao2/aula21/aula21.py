'''
Listas em Python

fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
'''

texto = 'Valor'
lista = ['A', 2, 'c', 4, 'andre', True, 1.999999]
lista2 = ['F', 6, 5.999, False]
print(lista[4])    #contagem: 0,1,2,3,...
print(lista[-1])   #contagem de trás para frente

print(lista[::2]) #printar do inicio ao fim da lista de 2 em 2
print(lista[::-1]) #print inverso dos valores
#soma = lista + lista2
lista.extend(lista2)
print(lista)

lista.append('bbb')
print(lista)

lista.insert(2, 'primeiro')   #inserir um novo valor na posição desejada.
print(lista)

lista.pop()     #remove o último elemento da lista
print(lista)

del(lista[2:5]) #excluir os elementos da lista (2, 3 e 4)
print(lista)

l1 = list(range(0,100, 10))
print(l1)
print(max(l1))
print(min(l1))

soma=0
for valor in l1:
    soma = soma+ valor
print(soma)

for tipo in lista:
    print(f'o tipo de {tipo} é {type(tipo)}')