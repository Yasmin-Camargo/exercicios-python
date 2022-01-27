#Quantos dolares posso comprar?
n1 = float (input ('Quando de dinheiro vc têm na sua carteira: '))
print ('Você pode comprar USS {:.2f} dolares'.format(n1/3.27), end='\n\n\n')


#Calcula a area e a quantidade de tinta necessária para pintar uma parede
n2 = float (input ('Digite a largura da parede em metros: '))
n3 = float (input ('Digite a altura da parede em metros: '))
print ('\nArea da parede: {} m²'.format(n2*n3))
print ('Quantidade de tinta necessária: {} l'.format((n2*n3)/2), end='\n\n\n')


#Preço do produto com 5% de desconto
n4 = float (input ('Digite o preço do produto: '))
print ('Novo preço, com 5% de desconto: R${:.2f}'.format(n4-(n4*(5/100))), end='\n\n\n')


#Novo salário com 15% de aumento
n5 = float (input ('Digite o seu salário: '))
print ('Novo salário com 15% de aumento: R${:.2f}'.format(n5+(n5*(15/100))))