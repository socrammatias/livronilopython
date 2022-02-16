preco = 0
pagar = 0
while True:
    codigo = int(input('Digite o codigo do produto: '))
    preco = 0
    if codigo == 0:
        break 
    elif codigo == 1:
        preco = 0.50
    elif codigo == 2:
        preco = 1
    elif codigo == 3:
        preco = 4
    elif codigo == 5:
        preco = 7
    elif codigo == 9:
        preco = 8
    if preco != 0:
        quantidade = int(input('Digite a quantidade comprada: '))
        pagar = pagar + (preco * quantidade)
    else:
        print('Codigo invalido.')
print(f'O valor total eh de R$: {pagar}')