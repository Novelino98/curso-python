"""
23. Condições IF, ELIF e ELSE

if = uma condição
elif = outra condição
else = se a condições não são satisfeitas


EXEMPLO DE LOOP USANDO ELSE E IF    
"""
i=3
def Win():
    print("ACABOU")
def Lose():
    print('Game over')
def Loop():
    print(f'Você tem mais {i} oportunidade(s). Responda certo!')
    n1=input('insira um número --> ')
    n2= input('repita o mesmo número --> ')
    try:
        int(n1)      # o uso do 'try' foi para verificar se o valor introduzido pelo usuário é realmente um número.
        int(n2)
    except:
        print("é NÚMERO! Sabe ler não?")  #caso não seja um número o 'except' é usado para introduzir uma msg personalizada
        if n1==n2:
            print('Mas pelo menos você soube colocar igual...')
        return 0  #reiniciar a função para não ter mensagem de erro


    n1= int(n1)
    n2= int(n2)

    D = n1==n2

    if D == True:
        print('parabéns cabeção.')
        Win()
        return 1              #retorna o valor 1 (True) para a função "Loop()"
    else:
        print('EROUUU!')
        return 0             # retorna o valor 0 (False) para a função "Loop()"


while i > 0:  #enquanto houver tentativas restantes (i) haverá repetição do while
    if Loop():    # o uso do Loop() somente significa que o valor deve ser "true (1)" para entrar no if
        break
    i = i - 1
    if i ==0:    #acabar as tentativas
        break



if i == 0 :  # mensagem de game over
    Lose()