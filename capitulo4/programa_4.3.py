salario = float(input('Digite o salario para calculo do imposto: '))
base = salario
imposto = 0

if base > 3000:
    imposto = imposto + ((base - 3000) * 0.35) # declarando o valor do imposto
    base = 3000
if base > 1000:
    imposto = imposto + ((base - 1000) * 0.20)

print(f'Salario: R${salario:5.2f} Imposto a pagar de R$: {imposto:5.2f}')

'''Explicando o codigo, o calculo do imposto eh assim se o salario(variavel base) for maior que
3000 teremos o calculo com 35% ou seja 0.35 subtraimos o salario(variavel base) pelo valor minimo
necessario para taxar o imposto e com isso o resultado vai gerar o imposto, o mesmo ocorre em 
imposto de 20% '''