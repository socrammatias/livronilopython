valor = float(input('Digite o valor: '))
desconto = int(input('Digite o percentual do desconto: '))

valor -= valor * (desconto / 100)
print(valor)