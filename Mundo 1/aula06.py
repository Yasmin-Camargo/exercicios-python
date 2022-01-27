#testando os métodos de teste de tipo is

num = input ("Digite alguma coisa: ")
print ("\nÉ um numero: {}".format(num.isnumeric()))
print ("É carctere alfanuméricos: {}".format(num.isalnum()))
print ("É um caracter alfabético: {}".format(num.isalpha()))
print ("É um caracter ASCII: {}".format(num.isascii()))
print ("É um espaço: {}".format(num.isspace()))
print ("É um caracter que pode ser impresso: {}".format(num.isprintable()))
print ("É um numero decimal: {}".format(num.isdecimal()))
print ("É um digito: {}".format(num.isdigit()))
print ("É uma letra minuscula: {}".format(num.islower()))
print ("É uma letra maiuscula: {}".format(num.isupper()))
print ("Esta capitalizado: {}".format(num.istitle()))


#exercicio para somar dois números
print("\n\n")
a = int (input ("Digite um número: "))
b = int (input ("Digite outro número: "))
print ("A soma de {} + {} = {}".format(a,b,a+b))