deposito = float(input('Digite o valor do deposito: '))
taxa = int(input('Digite a taxa de juros: '))
i = 1
saldo = deposito # acumulador
while i <= 24:
    saldo = saldo + (saldo * (taxa / 100))
    i += 1
    print(f'A taxa de saldo do mes é {saldo:5.2f}')
print(f'O ganho obtido com os juros foram de: R$:{saldo - deposito:8.2f}')
'''Peguei o valor do deposito e armazenei em uma nova variavel, na variavel saldo fiz com que 
acumulasse os 24 valores (24 meses) um por um e no final mostrei um o valor total que vai ser pago 
e o valor so de juros.'''