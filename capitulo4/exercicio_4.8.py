op = int(input('Qual operacao voce deseja realizar\n1-Soma\n2-Subtracao\n'
'3-Multiplicar\n4-Dividir\n'))
n1 = int(input('Digite o numero 1: '))
n2 = int(input('Digite o numero 2: '))
if op == 1:
    print('Você escolheu Somar')
    a = (n1 + n2)
    print(a)
elif op == 2:
    print('Voce escolheu Subtrair')
    a = (n1 - n2)
    print(a)
elif op == 3:
    print('Voce escolheu Multiplicar')
    a = (n1 * n2)
    print(a)
elif op == 4:
    print('Voce escolheu Dividir')
    a = (n1 / n2)
    print(a)
else:
    print('Valor invalido.')