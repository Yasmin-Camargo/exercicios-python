print ('\033[7;40mCores em Pyhon\033[m')
print ('Olá {}mundo{}'.format('\033[4;34m', '\033[m'))
cores = {'limpa':'\033[m',
         'vermelho': '\033[31m',
         'amarelo': '\033[33m',
         }
print ('Testando {}cores no pyhom{} de {}diferentes modos{}'.format(cores['amarelo'], cores['limpa'], cores['vermelho'], cores['limpa']))