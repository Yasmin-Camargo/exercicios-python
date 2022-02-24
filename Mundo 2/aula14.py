#programa que lê o sexo e se aceita F/M
sexo=1
while (sexo != 'F' and sexo!= 'M'):
    sexo = str (input('Qual o seu sexo: ').upper())
    if (sexo != 'F' and sexo!= 'M'):
        print ('\n\nTente novamente, sexo inválido!!')
        
#menu de opções
op = 0
while (op != 5):
    n1 = int (input ('\n\n\nDigite o primeiro número: '))
    n2 = int (input ('Digite o segundo número: '))
    print ('\nMENU')
    print ('[1] Somar')
    print ('[2] Multiplicar')
    print ('[3] Maior')
    print ('[4] Menor')
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
        if (n1>n2):
            print ('\n{} é maior que {}'.format(n2,n1))
    if (op == 4):
        if (n1==n2):
            print ('\nOs dois números são iguais')
        elif (n1>n2):
            print ('\n{} é menor que {}'.format(n2,n1))
        else:
            print ('\n{} é menor que {}'.format(n1,n2))
    