# Ler um número e mostrar cada um dos digitos separados 
# unidade , dezena, centena e milhar

num = int (input('Digite um número: '))
uni = num // 1 % 10
dez = num // 10 % 10
cen = num // 100 % 10
mil = num // 1000 % 10

print ('Undidade: {}'.format(uni))
print ('Dezena: {}'.format(dez))
print ('Centena: {}'.format(cen))
print ('Milhar: {}'.format(mil))


#ler o nome de uma cidade e dizer se começa ou não com  a palavra SANTO
cidade = str (input('\n\nDigite o nome da sua cidade: ')).strip()
lista = cidade.split()
print ('Sua cidade começa com a palavra Santo? {}'.format('santo' in lista[0].lower()))

#ler o nome de uma pessoa e dizer se possui silva no nome
nome = str(input('\n\nDigite seu nome completo: ')).strip()
print ('Você possui silava no seu nome: {}'.format('silva' in nome.lower()))

