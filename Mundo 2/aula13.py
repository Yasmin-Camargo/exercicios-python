#Mostrar a contagem regressiva para os fogos de artificio de 10 até 0
from time import sleep
print ('Contagem regressiva para os fogos de artificio:')
for c in range(10,0,-1):
    print(c)
    sleep(1)
print ('\nFogos estourando!!')

#tabuada
num = int(input('\n\nDigite um número: '))
for c in range(1,11):
    print ('{:<2} x {:>2} = {:>3}'.format(c,num,num*c),end="\n\n")
    
#ler seis numeros e realizar a soma dos pares
soma=0
for c in range (0,6):
    n1 = int (input('Digite o {} número: '.format(c+1)))
    if (n1%2==0):
        soma+=n1
print ('\nA soma do números pares é {}'.format(soma))