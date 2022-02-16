qtd_c_dia = int(input('Digite a quantidade de cigarro fumado por dia: '))
anos = int(input('Quantos anos voce fuma: '))
# perde 10 minutos de vida a cada cigarro

resultado_minutos = qtd_c_dia * 10 * anos * 365
resultado_dia = resultado_minutos / (24 * 60)
print(f'A quantidade de dias ja perdido eh de {resultado_dia:2.0f}')