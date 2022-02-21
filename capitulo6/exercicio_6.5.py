# Simulador fila de banco 
ultimo = 10
fila = list(range(1, ultimo+1))
while True:
    print(f'Existem {len(fila)} clientes na fila.')
    print(f'Fila atual: {fila}')
    print('Digite f para adicionar um cliente na fila.')
    print('Aperte A para realizar um atendimento ou S para sair.')
    operacao = input('Digite o tipo de operacao: ')
    x = 0
    sair = False
    while x < len(operacao):
        if operacao[x] == 'A':
            if len(fila) > 0:
                atendido = fila.pop(0)
            else:
                print('Fila vazia')
        elif operacao[x] == 'F':
            ultimo += 1
            fila.append(ultimo)
        elif operacao[x] == 'S':
            sair = True
            break
        else:
            print('Operacao invalida.')
        x = x + 1
    if sair:
        break