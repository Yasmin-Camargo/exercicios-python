#Mostrar número Antecessor e sucessor
n1 = int (input ('Digite um número: '))
print ('Sucesssor: {:>5} \nAntecessor: {:>4}'.format(n1+1,n1-1))

#Dobro, triplo e raiz quadrada
print ('\nDobro: {:>9} \nTriplo: {:>8} \nRaiz quadrada: {:.3f}'.format(n1*2,n1*3,n1**(1/2)),end='\n\n\n')

#Média aluno
n2 = float (input ('Digite um número: '))
n3 = float (input ('Digite outro número: '))
print ('A média é: {:.1f}'.format((n2+n3)/2), end='\n\n\n')

#conversão metros, centimetros e milimetros
n3 = float (input ('Digite um numero em metros: '))
print ('Em centimetros: {:.1f} cm \nEm milimitros: {:.1f} mm'.format(n3*100, n3*1000), end='\n\n\n')


#tabuada
n4 = int (input ('Digite um número: '))
print ('\nTabuada do {}'.format(n4))
print ('{} X 1: {:5}'.format(n4,n4*1))
print ('{} X 2: {:5}'.format(n4,n4*2))
print ('{} X 3: {:5}'.format(n4,n4*3))
print ('{} X 4: {:5}'.format(n4,n4*4))
print ('{} X 5: {:5}'.format(n4,n4*5))
print ('{} X 6: {:5}'.format(n4,n4*6))
print ('{} X 7: {:5}'.format(n4,n4*7))
print ('{} X 8: {:5}'.format(n4,n4*8))
print ('{} X 9: {:5}'.format(n4,n4*9))
print ('{} X 10: {:4}'.format(n4,n4*10))