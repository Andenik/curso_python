while True:
    numero1 = input('digite um numero: ')
    numero2 = input('digete outro numero: ')
    operador = input('digite o operador (+,-,/,*): ')

    if numero1.isdigit() and numero2.isdigit():
        ...
    else:
        print('Algo digitado nao e um  numero')

    if operador == '+':
        resultado1 = int(numero1) + int(numero2)
        print(resultado1)
    elif operador == '-':
        resultado2 = int(numero1) - int(numero2)
        print(resultado2)
    elif operador == '/':
        resultado3 = int(numero1) / int(numero2)
        print(resultado3)
    elif operador == '*':
        resultado4 = int(numero1) * int(numero2)
        print(resultado4)
    else:
        print('algo deu errado, digite apenas um operador')
    
    sair = input('Voce quer sair ? [s]im: ').lower().startswith('s')

    if sair is True:
        break

