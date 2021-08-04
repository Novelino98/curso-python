# programa para retornar o horário


from datetime import datetime

datetime_1 = datetime.now()
print(str(datetime_1))

from sys import stdout

def get_part_of_day(hour):
    return (
        "Bom dia" if 5 <= hour <= 11
        else
        "Boa tarde" if 12 <= hour <= 17
        else
        "Boa noite" if 18 <= hour <= 24
        else
        "Boa madrugada"
    )

# If you want to use current hour:

h = datetime_1.hour
stdout.write('Tenha um(a) {0}!\n'.format(get_part_of_day(h)))


'''
Exercício 1 - aula 30
Programa número par ou impar
'''

n = input('Digite um número: ')

if n.isdigit():
    n = int(n)
    if n == 0:
        print('Digite um número diferente de "zero"')
    elif n % 2 == 0:
        print('Esse número é par.')
    else:
        print('Esse número é ímpar.')
else:
    print('Os caracteres inseridos não são numerais ou não são numerais inteiros')

