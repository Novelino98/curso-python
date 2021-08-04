'''
17. variáveis
'''
Ano_atual = 2021
nome = 'André Luiz Brito Novelino'
nascimento= 1998
idade= (Ano_atual - nascimento)
altura= 1.92
peso = 117
IMC = peso/altura**2
Naturalidade= 'brasilia'

print(nome, idade, altura, sep=',')
#é natural de brasilia?
print(Naturalidade=='brasilia')

if 24.9 > IMC > 18.5:
    print(IMC, 'Peso normal')

if IMC > 29.9:
    print(IMC, 'Obesidade GRAU I')

if 29.9 > IMC > 24.9:
    print(IMC, 'sobrepeso')

print('Para deixar a marca de obesidade grau I, você deve abaixar o peso para ', int(29.9*altura**2), 'kg')