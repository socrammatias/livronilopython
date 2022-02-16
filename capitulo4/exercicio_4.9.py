valor = float(input('Digite o valor da casa: '))
salario = float(input('Digite o valor do seu salario: '))
anos = int(input('Digite a quantidade de anos a pagar a casa: '))
meses = anos * 12
prestacao = valor / meses
condicao = salario * 0.3

if prestacao > condicao:
    print('Reprovado')
else:
    print(f'O valor da sua prestacao eh R$:{prestacao:5.2f}')