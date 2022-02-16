divida = float(input('Digite o valor da divida: '))
juros = float(input('DIgite o valor do juros: '))
d_mensal = float(input('DIgite o valor do pagamento mensal: '))
i = 1
saldo = divida
while i <= 24:
    saldo = saldo + (saldo * (juros / 100)) + d_mensal
    print(f'Saldo mes {i} eh de R$:{saldo:5.2f}')
    i += 1
print(f'O ganho obtido com o juros foi de {saldo-d_mensal:8.2f}')