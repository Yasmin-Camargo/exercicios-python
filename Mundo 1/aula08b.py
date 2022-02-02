from random import choice,shuffle

#Sortear quatro alunos, mostrar quem deve apagar o quadro e a ordem de apresentação dos trabalhos
n1 = str (input('Digite o nome do primeiro aluno: '))
n2 = str (input('Digite o nome do segundo aluno: '))
n3 = str (input('Digite o nome do terceiro aluno: '))
n4 = str (input('Digite o nome do quarto aluno: '))

print ('\nO aluno escolhido para apagar o quadro foi: {}'.format(choice([n1,n2,n3,n4])))

lista = [n1,n2,n3,n4]
shuffle(lista)
print ('\nOrdem do sorteio para apresentação dos trabalhos: ')
print (lista)


