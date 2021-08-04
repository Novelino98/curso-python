"""
25. Operadores lógicos / 26. Função len

25.
and - c1 True E c2 True = True
or - C1 True ou C2 = True --> True
not - (inversor) c1 False => retorno True  not 2 > 3 : True

in e not in - está dentro ou está em

"""

#exemplo in

Sequencia = input('Digite uma sequencia: ')

if "1" not in Sequencia:
    print("não tem 1")

if "3" in Sequencia:
    print('tem o 3')

"""
26. Contagem de caracteres

função 'len' - obs: não funciona com int, float...

"""
Q = len(Sequencia)

print(Sequencia, Q, type(Q))

if Q < 6:
    print('Digite mais de 6 caracteres')
else:
    print('Sequencia foi aceita.')

Sequencia2 = input('Digite outra sequencia: ')

input(f'Foram digitados no total {len(Sequencia2) + Q}')


