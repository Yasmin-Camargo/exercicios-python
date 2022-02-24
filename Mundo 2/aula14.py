from time import sleep

#programa que lê o sexo e só aceita F/M
sexo=1
while (sexo != 'F' and sexo!= 'M'):
    sexo = str (input('Qual o seu sexo: ').upper().strip())
    if (sexo != 'F' and sexo!= 'M'):
        print ('\n\nTente novamente, sexo inválido!!')
        
#menu de opções
n1 = int (input ('\n\n\nDigite o primeiro número: '))
n2 = int (input ('Digite o segundo número: '))
op = 6
while (op != 5):
    print ('\nMENU')
    print ('[1] Somar')
    print ('[2] Multiplicar')
    print ('[3] Maior')
    print ('[4] Escolher novos números')
    print ('[5] Sair do programa')
    op = int (input('Escolha uma opção: '))
    
    if (op == 1):
        print ('\n{} + {} = {}'.format(n1,n2,n1+n2))
    if (op == 2):
        print ('\n{} X {} = {}'.format(n1,n2,n1*n2))
    if (op == 3):
        if (n1==n2):
            print ('\nOs dois números são iguais')
        elif (n1>n2):
            print ('\n{} é maior que {}'.format(n1,n2))
        elif (n2>n1):
            print ('\n{} é maior que {}'.format(n2,n1))
    if (op == 4):
        n1 = int (input ('\n\n\nDigite o primeiro número: '))
        n2 = int (input ('Digite o segundo número: '))
    sleep (2)
        
        
#sequencia de fibonaci
num = int (input ('Digite um número: '))
cont=2
n2=1
n1=1
temp=0
print ('\n\n{} primeiros elementos da sequência de fibonacci: '.format(num))
print ('    1\n    1')
while (cont<=num):
    print ('    {}'.format(n1+n2))
    cont += 1
    temp = n1
    n1 = n2
    n2 = temp + n2