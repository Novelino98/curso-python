"""
24. Operadores relacionais + if/elif/else
"""
#  == igualdade
#  > maior que
#  >= maior ou igual a
#  < menor que
#  <= menor ou igual a
#  != diferente

variavel = 'valor'  #afirmando uma igualdade
print( 2 == 2 )     #perguntando uma igualdade, retornando booleano True

print(2 == '2')  # False - variaveis diferentes, tipos diferentes (int - str)

n1 = 4
n2 = 5
expressao = (n1 >= n2)  # bool - False
print(expressao)

v1 = 'Luiz'
v2 = 'Andre'

comp = v1 != v2  #strings diferentes - True
print(comp)

nome = input('qual seu nome?')
nota = float(input("Qual sua nota?"))
nota_recuperacao = 50
nota_passou = 70
if nota >= (nota_recuperacao) and nota <= (nota_passou - 0.1):
    print(f'{nome} está de recuperação.')
elif nota >= (nota_passou - 0.1):
    print(f'{nome} passou no curso.')
else:
    print(f'{nome} reprovou.')
