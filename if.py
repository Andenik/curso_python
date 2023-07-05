numero1 = input('digite um numero: ')
numero2 = input('digite outro numero: ')



if numero1 > numero2:
    print(f'o valor de {numero1=} e maior que {numero2=}')
elif numero1 < numero2:
    print(f'o valor de {numero2=} e maior que o valor de {numero1=}')
elif numero1 == numero2:
    print(f'os numeros sao iguais')
else:
    print('vc nao digitou nada')
