#usuario deve tentar acertar o número que o computador escolheu entre 0 e 10 

from random import randrange
from time import sleep

num = randrange(0,11)
tentativa = 12
erros = 0

print ('\n O Computador está escolhendo seu número ...')
sleep(2)
    
while (num != tentativa):
    tentativa = int(input('\n\nQual o número escolhido pelo computador: '))
    if (num == tentativa):
        print ('\n\nParabéns o número era {}!!!! \nVocê acertou o número escolhido pelo computador!! foram necessárias {} tentativas para acertar'.format(num, erros))
    else:
        print ('\nNão foi esse número...'.format(num),end=" ") 
        print ('Tente Novamente')
    erros+=1

    