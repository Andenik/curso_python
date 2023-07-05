"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Digite seu nome: ')

nomet = len(nome)

if nomet <= 4:
    print('seu nome e curto')
elif nomet < 6:
    print('seu nome e normal')
elif nomet > 6:
    print('seu nome e grande')