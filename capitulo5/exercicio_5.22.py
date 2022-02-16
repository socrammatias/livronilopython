while True:
    print('''Deseja o que?\n
    1-Soma
    2-Subtrair
    3-Multiplicar
    4-Dividir
    5-Sair
    ''')
    escolher = int(input('Digite qual a opcao escolhida: '))
    if escolher == 5:
        break
    elif escolher > 1 or escolher < 5:
        i = 1
        qual = int(input('Qual o numero da tabuada: '))
    while i <= 10:
        if escolher == 1:
            print(f'Soma de {qual} + {i} = {qual + i}')
        elif escolher == 2:
            print(f'O valor de {qual} - {i} = {qual - i}')
        elif escolher == 3:
            print(f'O valor de {qual} * {i} = {qual * i}')
        elif escolher == 4:
            print(f'O valor de {qual} / {i} = {qual / i}')
        i = i + 1
    else:
        print('Valor incorreto')