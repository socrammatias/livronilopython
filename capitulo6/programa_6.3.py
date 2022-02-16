numeros = [0, 0, 0, 0, 0]
x = 0
while x < 5:
    numeros[x] = int(input(f'Digite o numero {x + 1}: '))
    x = x + 1
while True:
    escolhido = int(input('Que posicao voce quer imprimir? (0 para sair): '))
    if escolhido == 0:
        break
    print(f'Voce escolheu o numero {numeros[escolhido - 1]}')
    '''Na linha acima o autor faz um otimo raciocinio, que eh pegar o valor escolhido
    e subtrair por 1 que assim vai pegar o indice correto do numero desejado pelo usuario.'''