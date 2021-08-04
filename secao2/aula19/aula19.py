'''
35. Iteração de strings com while

0123456789.................33
'''

contador= 0
frase = 'um masagafo teve tres masagafinhos'
tamanho_frase= len(frase)
nova_string = ''
usuario = input('selecione uma letra: ')

while contador<tamanho_frase:
    letra = frase[contador]
    if letra == usuario:
        nova_string += usuario.upper()
    else:
        nova_string += letra
    # print(frase[contador], contador)
    #nova_string += frase[contador]
    print(nova_string)
    contador += 1
