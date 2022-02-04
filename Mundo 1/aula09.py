#Ler o nome completo de uma pessoa e mostrar:
# - o nome com todas letras maiúsculas
# - o nome com todas letras minúsculas
# - quantas letras sem espaços
# - quantas letra tem o primeiro nome

nome = str (input('Digite seu nome: ')).strip()
lista = nome.split()
print ('\nSeu nome com todas letras maiúsculas: {}'.format(nome.upper()))
print ('Seu nome com todas letras minúsculas: {}'.format(nome.lower()))
print ('Quantas letras seu nome possui sem espaços: {}'.format(len(nome.replace(' ',''))))
print ('Quantas letras tem seu primeiro nome: {} tem {} letras'.format(lista[0], len(lista[0])))


