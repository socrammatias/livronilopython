salario = float(input('Digite o seu salario: '))
base = salario
if base > 1250:
    aumento = base * (10 / 100)
    salario_t = salario + aumento
if base <= 1250:
    aumento = base * (15 / 100)
    salario_t = salario + aumento

print(f'Seu salario eh de R$:{salario} e seu aumento eh de R$:{aumento} totalizando R$:{salario_t}')