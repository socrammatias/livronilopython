distancia = int(input('Digite a distancia desejada: '))

if distancia <= 200:
    cobrar = 0.50
    valor = distancia * 0.50
    print(f'O total a ser pago eh de R$: {valor:5.2f}')
else:
    cobrar1 = 0.45
    valor1 = distancia * 0.45
    print(f'O total a ser pago eh de R$: {valor1:5.2f}')
