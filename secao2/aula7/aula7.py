'''
19 - Introducao a formatacao de strings
'''

#dados
Ano_atual = 2021
nome = 'André Luiz Brito Novelino'
nascimento= 1998
idade= (Ano_atual - nascimento)
altura= 1.92
peso = 117
IMC = peso/altura**2

#formas para formatação de strings

print(f'{nome} tem {idade} anos e possui o IMC de {IMC:.2f}')  # {IMC:.2f} retornar o IMC com 2 casas decimais
print('{} tem {} anos e possui o IMC de {}'.format(nome, idade, IMC))  #definir os pontos e colocar em ordem os dados
print('{n} tem {i} anos e possui o imc de {c}'.format(i=idade, n=nome, c=IMC))  #definir variáveis para o preenchimento
