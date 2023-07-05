''' ano bisexto = ano divisivel por 4, anos terminados em 00 
podem ser divididos por 100/400 '''
# pedir ano ao usuario
# verificar se o ano e divisivel por 400 / 100 / 4
# caso nao seja, informar que nao e um ano bisexto

import sys

ano = input('Digete o ano: ')

if ano.isdigit():
    ano = int(ano)
else:
    print('isto nao e um numero')
    sys.exit()

anobi = ano % 400 or ano % 100
anobi3 = ano % 4

if anobi == 0:
    print('ano bisexto')
elif anobi3 == 0:
    print('ano bisexto')
else:
    print('ano nao bisexto')