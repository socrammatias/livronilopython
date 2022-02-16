qtd_km = float(input('Digite a quantiddade de Km percorrido: '))
# 60 reais por dia
# 0,15 por km rodado

qtd_dias = int(input('Digite a quantida de dias que o carro foi alugado: '))

valor = (qtd_km * 0.15) + qtd_dias * 60
print(f'O valor a ser pago eh de {valor}')