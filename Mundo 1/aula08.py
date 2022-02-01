import math

#Ler número real e mostrar sua porção inteira
n1 = float (input('Digite um número: '))
print ('Porção inteira do número {} é o número {}'.format(n1,math.floor(n1)), end='\n\n\n')

#Ler o cateto oposto e o cateto adjacente e calcular a hipotenusa
n2 = float (input('Digite o cateto oposto: '))
n3 = float (input('Digite o cateto adjacente: '))
print ('A hipotenusa do triângulo retangulo é {:.2f}'.format(math.hypot(n2,n3)), end='\n\n\n')

#Ler um angulo e mostrar o seno, cosseno e tangente
n4 = float (input('Digite um ângulo: '))
print ('Seno: {:.2f}'.format(math.sin(n4)))
print ('Cosseno: {:.2f}'.format(math.cos(n4)))
print ('Tangente: {:.2f}'.format(math.tan(n4)))
