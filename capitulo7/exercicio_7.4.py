palavra = input()

contador = {}
for letra in palavra:
    contador[letra] = contador.get(letra, 0) + 1

for chave, valor in contador.items():
    print(f'{chave} : {valor}x')