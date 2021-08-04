"""
Formatando valores com modificadores - aula 31

:s - Texto (strings)
:d - inteiros
:f - número de pontos flutuantes (float)
:.(NÚMERO)f - Quantidade de casa decimais (float)

:(CARACTERE) (> ou < ou ^)(Quantidade)(tipo - s, d ou f)

"""

n1 = 10
n2= 3

div = n1/n2

print('{:.2f}'.format(div))     #:2f - duas casas decimais
print(f'{div:.2f}')

# o número com o número de casas desejáveis
"""
> esquerda
< direita
^ centro
"""

print(f'{n1:*>8}')  # a variável deve ter 5 casas
print(f'{n1:*<8}')  # a variável deve ter 5 casas
print(f'{n1:*^8}')  # a variável deve ter 5 casas

nome = 'anDRé'
sobrenome = 'NoVELino'
print (len(nome))

print(f'{nome:#^30}')

nome_formatado = '{n:@>6} {p:#^10}'.format(n=nome, p=sobrenome)
print(nome_formatado)
print(nome_formatado.lower()) #todas as letras minúsculas
print(nome_formatado.upper()) #... Maiúsculas
print(nome_formatado.title()) # Primeiras letras maiusculas