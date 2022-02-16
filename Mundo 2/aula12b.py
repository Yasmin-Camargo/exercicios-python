#Ler a idade de um jovem e informar se ele deve se alistar, se esta na hora ou se já passou o tempo de alistamente
idade = int(input('\n\nDigite a sua idade jovem: '))
if (idade==18):
    print ('Você deve se alistar!')
elif (idade<18):
    print ('Você poderá se alistar daqui {} anos'.format(18-idade))
else:
    print ('Você não pode mais se alistar, pois já passou {} anos do seu alistamento'.format(idade-18))


#Ler ano de nascimento de um atleta e mostrar a categoria de acordo com a idade
import datetime

idade = int (input('Digite o seu ano de nascimento: '))
ano = datetime.datetime.now()
ano = int(ano.strftime("%Y"))
print (ano)
idade = ano - idade

print ('\nSua idade: {} anos'.format(idade))
if (idade<=9):
    print(' - Categoria Mirim')
elif (idade>9 and idade<=14):
    print(' - Categoria Infantil')
elif (idade>14 and idade<=19):
    print(' - Categoria Junior')
elif (idade>19 and idade<=20):
    print(' - Categoria Senior')
else:
    print(' - Categoria Master')