"""
tipos de dados

str - strings - textos 'assim' ou "assim"
int - inteiro - 123456 0 -10 -20 -50
float - real/ponto flutuante - 10.50 1.5 -10.10 -50.93;
bool -  booleano/lógico - true/false 10 == 10

"""
#str
print('André', type('André'))
print("10", type('10'))   #números entre aspas são strings
#int
print(1234, type(1234))
print(type(int("10"))) #type casting - conversão de tipos de dados
#float
print(25.23, type(25.23))  # número com casas decimais
print(10.5, type(float('10.5')))
#bool
print(10==10, type(10==10))
print("10==10", 10==10)
print("10==11", 10==11)
print(" 'l' == 'L' ", 'l'=='L')

print(bool(''),type(bool('')) )  #bool avalia em falso vazios e verdadeiro a presença de caracteres

bool("ANDRE")  #definindo "ANDRÉ" como booleano
print("ANDRE"=="ANDRE")

#exercício
print('Dados pessoais')
#Nome
print("André Novelino", type("André Novelino"))
#idade
print(23, type(23))
#altura
print(1.92, type(1.92))
#maior de idade
print(23 > 18, type(23>18))