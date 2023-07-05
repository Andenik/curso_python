"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

horas = int(input('digite o horario sem minutos: '))

tarde = horas >= 12 and horas <= 17

noite = horas >= 18 and horas <=23

if horas <= 11:
    print('bom dia')
elif tarde:
    print('boa tarde')
elif noite:
    print('boa noite')
else:
    print('nao digitou as horas certo')

