from datetime import date

#ler um ano e dizer se ele é bissexto
ano = int (input('Digite um ano ou 0 para analizar o ano atual: '))
if (ano == 0):
    ano = date.today().year
if (ano%4==0 and ano%100!=0 or ano%400==400):
    print ('{} é um ano bissexto!'.format(ano))
else:
    print ('{} não é um ano bissexto'.format(ano))
 
    
#ler tres numeros e indicar qual é o maior entre eles e qual é o menor
n1 = float (input('\n\nDigite o primeiro número: '))
n2 = float (input('Digite o segundo número: '))
n3 = float (input('Digite o terceiro número: '))

if (n1>n2>n3):
    print ('\n{:.2f} é o maior número'.format(n1))
    print ('{:.2f} é o menor número'.format(n3))
elif (n2>n3>n2):
    print ('\n{:.2f} é o maior número'.format(n1))
    print ('{:.2f} é o menor número'.format(n2))
elif (n2>n1>n3):
    print ('\n{:.2f} é o maior número'.format(n2))
    print ('{:.2f} é o menor número'.format(n3))
elif (n2>n3>n1):
    print ('\n{:.2f} é o maior número'.format(n2))
    print ('{:.2f} é o menor número'.format(n1))
elif (n3>n1>n2):
    print ('\n{:.2f} é o maior número'.format(n3))
    print ('{:.2f} é o menor número'.format(n2))
else:
    print ('\n{:.2f} é o maior número'.format(n3))
    print ('{:.2f} é o menor número'.format(n1))
    

#ler o comprimento de tres retas e indicar se elas podem ou não formar um triângulo
reta1 = float (input('\n\nDigite o comprimento da primeira reta: '))
reta2 = float (input('Digite o comprimento da seegunda reta: '))
reta3 = float (input('Digite o comprimento da terceira reta '))

if (reta1+reta2 > reta3):
    if (reta1+reta3 > reta2):
        if (reta3+reta2 > reta1):  
            print ('\nPode formar um triangulo')
        else:
            print ('\nNão pode formar um triangulo')
    else:
        print ('\nNão pode formar um triangulo')
else:
    print ('\nNão pode formar um triangulo')