'''
While - aula 33

'''
x=0
while x < 10:
    if x % 2 != 0:
        x +=1 # x =x+1
        continue # pula os número pares

    x= x +1
    print(x)

print('fim')