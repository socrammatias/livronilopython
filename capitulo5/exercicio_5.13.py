divida = float(input('Divida: '))
taxa = float(input('Juros: '))
pagamento = float(input('Pagamento mensal: '))
mes = 1
if (divida * (taxa / 100) > pagamento):
    print('Sua divida nao sera paga nunca, pois o juros sao superiores. ')
else:
    saldo = divida # armazenando o valor da divida no saldo
    juros_pago = 0
    while saldo > pagamento:
        juros = saldo * taxa / 100
        saldo = saldo + juros - pagamento # acumulando o valor sendo pago
        juros_pago = juros_pago + juros
        print(f'Saldo da divida no mes {mes} é de R$:{saldo:6.2f}')
        mes = mes + 1
print(f'Para pagar uma divida de R${divida}, a {taxa:5.2f} % de juros.')
print(f'Voce precisara de {mes - 1} meses pagando um total de R${juros_pago:8.2f} de juros')
print(f'No ultimo mes, voce teria um saldo residual de R${saldo:8.2f} a pagar. ')