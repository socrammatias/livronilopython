kwh = int(input('Digite a quantidade de kwh: '))
tipo = input('Qual o tipo de instalacao? \nR-Residencia'
'\nI-Industria\nC-Comercio\nDigite aqui: ')

if tipo == 'R':
    if kwh > 500:
        print(f'Total a pagar R$:{kwh * 0.65:5.2f}')
    else:
        print(f'Total a pagar R$:{kwh * 0.40:5.2f}')
elif tipo == 'C':
    if kwh > 1000:
        print(f'Total a pagar R$:{kwh * 0.60:5.2f}')
    else:
        print(f'Total a pagar R$:{kwh * 0.55:5.2f}')
elif tipo == 'I':
    if kwh > 5000:
        print(f'Total a pagar R$:{kwh * 0.60:5.2f}')
    else:
        print(f'Total a pagar R$:{kwh * 0.55:5.2f}')