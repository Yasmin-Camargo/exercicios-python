#Programa para aprovar empréstimo bancário: ler o valor da casa, o salário e em quantos anos ela vai pagar. Retornar o valor da prestação mensal.
casa = float (input ('Digite o valor da sua casa: '))
salario = float (input ('Digite o valor do seu salário: '))
anos = int (input ('Digite a quantidade de anos que você pretende pagar: '))

if (casa/anos > salario*(30/100)):
    print ('\nSeu empréstimo foi negado!')
    print ('Sua prestação excedeu 30% do seu sálario')
else:
    print ('\nSeu empréstimo foi aprovado!')
    print ('\nValor da sua prestação mensal: R${:.2f}'.format(casa/anos))
    
    
#Ler um número e converter para binario, octal ou hexadecimal de acordo com o usuário
num = int (input('\n\n\nDigite um número inteiro: '))
op = int (input('\n 1.Binário\n 2.Octal\n 3.Hexadecimal\nEscolha uma base de conversão: '))
 
if (op == 1):
    bin = bin(num)
    print ('\n\nO número {} em binário é: {}'.format(num,bin[2:]))
elif (op == 2):
    oct = oct(num)
    print ('\n\nO número {} em octal é: {}'.format(num,oct[2:]))
elif (op == 3):
    hex = hex(num)
    print ('\n\nO número {} em hexadecimal é: {}'.format(num,hex[2:]))
else:
    print ('Opção Inválida!')
    


 