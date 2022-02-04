#ler uma frase e dizer:
# - quantas vezes aparece a letra a
# - em que posição ela aparece a primeira vez
# - em que posição ela aparece a última vez

frase = str (input('Digite uma frase: ')).lower().strip()
print ('\nA letra a aparece {} vezes na frase'.format(frase.count('a')))
print ('A primeira vez que a letra a aparece é na posição {}'.format(frase.find('a')+1))
print ('A última vez que a letra a aparece é na posição {}'.format(frase.rfind('a')+1))


#Ler o nome completo de uma pessoa e mostrar o primeiro e o ultimo nome
nome = str (input('\nDigite seu nome completo: '))
nome = nome.split()
print ('Primeiro nome: {}'.format(nome[0]))
print ('Último nome: {}'.format(nome[int(len(nome) - 1)]))