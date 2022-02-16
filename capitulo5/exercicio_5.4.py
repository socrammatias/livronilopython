fim = int(input('Digite o ultimo numero a imprimir: '))
i = 0
while i <= fim:
    if i % 2 == 1: # vai printar apenas os impares pois se sobrar numeros numa divisao de 2 eh impar
        print(i)
    i += 1