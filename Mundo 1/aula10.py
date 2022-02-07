#usuario deve tentar acertar o número que o computador escolheu entre 0 e 5

from random import randrange

num = randrange(0,6)
tentativa = int(input('Digite um número: '))

if (num == tentativa):
    print ('\nParabéns o número era {}! \nVocê acertou o número escolhido pelo computador!!'.format(num))
else:
    print ('\nNão foi dessa vez, o numero escolhido pelo computador era {}'.format(num)) 
    
    
#ler a velocidade de um carro e mostrar se ele foi  multado ou não e quanto vai custar a multa
velocidade = float(input('\n\nDigite a velocidade do carro: '))
if (velocidade > 80):
    print ('Você foi multado!!! pois ultrapassou em {:.2f}km/h da velocidade máxima permitida'.format(velocidade-80))
    print ('Valor da multa: R${:.2f}'.format((velocidade-80)*7))
else:
    print ('Você esta dentro do limite de velocidade permitido de 80km/h')
    
    
#ler a distancia de uma viagem, calcular o preço  da passagem
#R$0.50 para até 200km e R$0.45 para viagens mais longas
distancia = float (input('\n\nDigite a distancia da sua viagem: '))
if (distancia <= 200):
    print ('O valor da sua passagem é: R${:.2f}'.format(distancia*0.50))
else:
    print ('O valor da sua passagem é: R${:.2f}'.format(distancia*0.45))