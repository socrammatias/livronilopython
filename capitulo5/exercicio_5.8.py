n1 = int(input('Digite o numero 1: '))
n2 = int(input('Digite o numero 2: '))
sla = n1 # salvando numa variavel o numero que eu desejo somar varias vezes
i = 0
x = 1
while x <= sla: # enquanto x for menor que valor de n1
    print(f'Voce escolheu o numero {n2}')
    i += n2 # o i intera o valor de n2 a cada repeticao ou seja ele soma o valor ex 5 + 5 + 5 + 5 + 5
    print(i)
    x += 1