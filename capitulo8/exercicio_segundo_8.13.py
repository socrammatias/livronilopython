import random
n = random.randint(1, 10)
for tentativa in range(1, 3+1):
    x = int(input('Digite um numero de 1 a 10: '))
    if x == n:
        print('Voce acertou!')
        print(f'A resposta é {n}')
        break
else:
    print('Voce errou!')
    print('{} tentativa'.format(tentativa))
    if tentativa == 3:
        print(f'A resposta é {n}')