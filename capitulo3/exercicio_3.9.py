dia = int(input('Digite o dia: '))
hora = int(input('Digite a hora: '))
minutos = int(input('Digite os minutos: '))
segundos = int(input('Digite os segundos: '))
# dia tem 24 horas 
# cada hora tem 3600 segundos (60 * 60)
# cada minuto tem 60 segundos
total = dia * 24 * 3600 + hora * 3600 + minutos * 60 + segundos
print(total)