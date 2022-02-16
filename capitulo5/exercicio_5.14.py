valor = 0
i = 0
while True:
    n = int(input('Digite o numero: '))
    if n == 0: # se eu digitar 0 ele vai parar o programa e vai parar de contar sem somar o numero 0 como digitado
        break
    valor += n
    i += 1 # vai contar quantas vezes rodou o while e quantas vezes eu digitei o numero
print(f'A soma total dos numeros digitados foram {valor}')
print(f'Voce digitou um total de {i} numeros.')
print(f'A media dos numeros digitados eh {valor / i}')

