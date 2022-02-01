import random

#Sortear quatro alunos, mostrar quem deve apagar o quadro e a ordem de apresentação dos trabalhos
n1 = str (input('Digite o nome do primeiro aluno: '))
n2 = str (input('Digite o nome do segundo aluno: '))
n3 = str (input('Digite o nome do terceiro aluno: '))
n4 = str (input('Digite o nome do quarto aluno: '))

shuffledList = random.sample([n1, n2, n3, n4], k=len([n1, n2, n3, n4]))

print ('\n{} voce foi escolhido para apagar o quadro'.format(random.choice(seq=[n1,n2,n3,n4])))
print ('Ordem do sorteio para apresentação dos trabalhos: {}'.format(shuffledList))


