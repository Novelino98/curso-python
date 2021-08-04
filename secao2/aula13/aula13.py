'''
Calculadora
'''

# comandos isdigit, isnumeric, isdecimal - verificam se o valor é um número, porém não funciona com float
# Para float, exemplo de código pode ser obtido na aula 27

n1 = input('Valor 1: ')
n2 = input('Valor 2: ')

def cal():
    if n1.isdigit() and n2.isdigit():
        return 1
    else:
        print('Valor inválido. Repita o procedimento.')
        return 0

print('operações :')
print('+ -> soma')
print('- -> subtração')
print('* -> multiplicação')
print('** -> Exponenciação')

operation = input('Qual a operação desejada: ')

if cal():
    n1 = float(n1)
    n2 = float(n2)
    if operation == '+':
        R = n1+n2
    elif operation == '-':
        R = n1-n2
    elif operation == '*':
        R = n1*n2
    elif operation == '**':
        R = n1**n2
    else:
        print('Operação inválida. Repita o processo. ')
        R = 'erro'
    print(R)
    print('FINALIZADO')


