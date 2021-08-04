'''
36. For in - estrutura de repetição

iteração de strings com for

'''

texto = 'Volante Longitech G920'
nova_string = ''
#for n, letra in enumerate(texto):
 #   print(n,letra)

#for n in range(1000, 199, -100):
 #   print(n)

#for n in range (100):
#    if n % 17 == 0:
 #       print(n)

for letter in texto:
    if letter == 't':
        nova_string = nova_string + letter.upper()
    elif letter == 'h':
        nova_string += letter.upper()
        break
    else:
        nova_string += letter

print(nova_string)