"""
20. Desafio prático
"""
# criar variaveis para nome, idade, altura e peso de uma pessoa
#criar variável com o ano atual
#obter o ano de nscimento da pessoa
#obter IMC da pessoa com 2 casas decimais
#exibir um texto com os valores na tela usando f-strings

print('Coloque seu nome')
nome= input()
print('Coloque sua idade')
idade = int(input())
print('Coloque seu peso em Kg')
peso = int(input())
print('Coloque sua altura em metros')
altura = float(input())

ano_atual= 2021
nascimento= ano_atual-idade
IMC = (peso/altura**2)

if 24.9 > IMC:
    classe = 'Peso normal'
if 29.9 > IMC > 24.9:
    classe = 'sobrepeso'
if IMC > 29.9:
    classe = 'Obesidade GRAU I'


print(f'Obrigado por responder {nome} ,')
print(f'Você nasceu em {nascimento},')
print(f'Seu IMC é de {IMC} e você se encontra na classe {classe}')
