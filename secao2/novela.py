i=4

def Win():
    print("ACABOU")
def Lose():
    print('Game over')

def Loop():
    print(f'Você tem mais {i} oportunidade(s). Responda certo!')
    n1=input('insira um número --> ')
    n2= input('repita o mesmo número --> ')
    try:
        int(n1)
        int(n2)
    except:
        print("é NÚMERO! Sabe ler não?")
        if n1==n2:
            print('Mas pelo menos você soube colocar igual. Anda logo repete ai...')
        Loop()

    n1= int(n1)
    n2= int(n2)

    D = n1==n2

    if D == True:
        print('parabéns cabeção.')
        Win()
        return 1
    else:
        print('EROUUU!')
        return 0


while i > 1:

    i=i-1
    if Loop(): break

    if i == 0: break

if i == 1:
    Lose()