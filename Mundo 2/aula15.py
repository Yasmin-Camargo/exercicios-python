#tabuada
from ast import Break

cont=0

while True:
    num = int (input ('\n\nDigite um número: '))
    if (num<0):
        break
    for c in range (1, 11):
        print (f'{num} X {c:3}: {num*c:5}')

    
#Caixa eletronico
print ('\n\n -- Bem vindo ao caixa eletronico!! --')
saque = int (input('\n\nQual será o valor sacado: '))
valor = saque

nota50 = nota20 = nota10 = nota1 = 0
while True:
    print (valor)
    if (valor == 0):
        break
    elif (valor >= 50):
        nota50+=1
        valor -= 50
    elif (valor >= 20):
        nota20+=1
        valor -= 20
    elif (valor >= 10):
        nota10+=1
        valor -= 10
    elif (valor >= 1):
        nota1+=1
        valor -= 1
        
    
print (f'Total de notas para {saque} reais: \n - {nota50} notas de 50 reais\n - {nota20} notas de 20 reais\n - {nota10} notas de 10 reais\n - {nota1} notas de 1 real')
