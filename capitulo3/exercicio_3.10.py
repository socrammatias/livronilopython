salario = int(input('Digite o salario: '))
porcentagem = int(input('Digite a porcentagem: '))

salario += salario * (porcentagem / 100)
print('Seu salario agora eh de: ' + str(salario))