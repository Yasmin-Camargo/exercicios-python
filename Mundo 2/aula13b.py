#ler uma frase e dizer se ela é ou não um palindromo
fraselida = str (input('Digite uma frase: '))
frase = fraselida.replace(' ','').lower()
teste = ''
for c in range(len(frase)-1,0-1,-1):
    teste+=frase[c]
    
if (frase == teste):
    print ('\nA frase "{}" é um palindromo'.format(fraselida))
else:
    print ('\nA frase "{}" não é um palindromo'.format(fraselida),end='\n\n')
    

#ler o nome, idade e sexo de 4 pessoas e mostrar a média de idade, o nome do homen mais velho e quantas mulheres tem menos de 20 anos
media_idade=0
mais_velho_idade=0
mais_velho_nome=''
mulheres = 0
mulheres_idade = 0
for c in range (1, 4+1):
    print ('\nPessoa {}'.format(c))
    nome = str (input(' Digite o nome: '))
    idade = int (input(' Digite a idade: '))
    sexo = str (input(' Digite o sexo \n   [F] - feminino  \n   [M] - Masculino: \n     ')).lower().strip()
    
    media_idade += idade
    
    if (sexo == 'f'):
        mulheres += 1
        if (idade < 20):
            mulheres_idade += 1
    else:
        if (idade > mais_velho_idade):
            mais_velho_idade = idade
            mais_velho_nome = nome

print ('\nMédia de idade do grupo: {:.2f} anos'.format(media_idade/4))
print ('O homen mais velho é {} com {} anos'.format(mais_velho_nome,mais_velho_idade))
print ('No grupo a {} mulheres e {} são menores de 20 anos'.format(mulheres,mulheres_idade))