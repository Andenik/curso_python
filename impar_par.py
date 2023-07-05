"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero = input('Digite um numero: ')

numero = int(numero)

print(numero)

if numero % 2 == 0:
    print('Numero par')
else:
    print('Numero impar')