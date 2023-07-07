nome = "carro"

tamanhonome = len(nome)

n = 0

nome1 = ""

while n < len(nome):
    i = f'/{nome[n]}'
    nome1 += i
    n += 1

print(nome1)