n = input('Digite seu nome: ')
i = input('Digite sua idade: ')

if n and i:
    print(f'Seu nome é {n}' )
    print(f'Seu nome ao contrario é {n[::-1]}')
    if ' ' in n:
        print('Seu nome tem espaco')
    else:
        print('seu nome nao tem espaco')
    print(f'Seu nome contém {len(n)} letras')
    print(f'A primeira letra do seu nome é: {n[0]}')
    print(f'A ultima letra dos eu nome é: {n[-1]}')
else:
    print('Nao digitou nada')
    



      