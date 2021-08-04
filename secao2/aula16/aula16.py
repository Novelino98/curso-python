'''
manipulação de strings - Aula 32
'''

# contagem [01234] - indices positivos
variavel = "André"

print(variavel[4]) #printar apenas a letra 'é' - variavel[n]

# [987654321] - indices negativos

url = 'www.sigaa.unb.br/enm'

print(url[:-4]) # tirar os ultimos 4 digitos

nova_string = url[4:9] # pega os caracteres 4 até 9 da variavel 'url'
print(nova_string)
print(url[-10:-7]) #pegar do caractere 7 ao 10 de trás para frente

string = 'abcdefghijklmnopq'
string_2 = string[::2] #pula os caracteres de 2 em 2
print(string_2)