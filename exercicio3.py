"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero = input('Digite um numero: ')

print(numero)

numero = int(numero)

if numero is int:
    print('Voce digitou um numero nao inteiro')

numero = numero / 2

print(numero)

if numero is int():
    print('Numero par')
    if numero is float():
        print('Numero impar')