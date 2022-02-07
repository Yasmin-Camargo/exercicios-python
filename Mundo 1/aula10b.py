#ler um ano e dizer se ele é bissexto
ano = int (input('Qual um ano: '))

if (ano%4==0):
    print ('{} é um ano bissexto!'.format(ano))
else:
    print ('{} não é um ano bissexto'.format(ano))
    