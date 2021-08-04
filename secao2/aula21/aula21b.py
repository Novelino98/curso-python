'''
Descubra qual é a palavra
'''

palavra = 'paciencia'
letras_digitadas = []

chances = 3

while True:
    if chances < 1:
        print('Você perdeu!')
        print(f'A palavra era {palavra.upper()}')
        break

    entrada = input('Digite uma letra: ')

    if len(entrada) > 1:
        print('Digite apenas uma letra.')   # limitar a entrada em apenas uma letra
        continue

    letras_digitadas.append(entrada)  #adicionar dado na lista

    if entrada in palavra:
        print(f'A letra {entrada} está na palavra! Tente adivinhar outra letra.')
    else:
        print(f'A letra {entrada} não está presente na palavra')
        chances = chances-1
        print(f'Você tem mais {chances} chances.')
        letras_digitadas.pop()  #tirar a letra errada

    segredo =''     # palavra apresentada sendo completada
    for letra_segredo in palavra:
        if letra_segredo in letras_digitadas:
            segredo+= letra_segredo
        else:
            segredo += '*'
    print(segredo)

    if segredo == palavra:
        print('Parabéns, você descobriu a palavra')
        break