# programa que recolhe uma frase e faz a contagem de letras e informa ao usuario a letra que mais apareceu

# x = letra que apareceu mais vezes
# z = letra que apareceu mais vezes no momento 
# y = quantidaade de letras

frase = input('Digite uma frase para contagem: ')

i = 0
x = ''
y = 0

while i < len(frase):
    letra_atual = frase[i]
    z = frase.count(letra_atual)
    
    if letra_atual == ' ': # eliminar espaco da contagem
        i += 1
        continue

    if y < z: # contagem das letras
        y = z
        x = letra_atual
    
    i += 1

print(f'A letra que aparaceu mais vezes foi {x.capitalize()}, apareceu {y}x.')