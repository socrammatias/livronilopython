lista = [10, 22, 33, 54, 89]
x = 0
y = 0 
pergunta = int(input('Digite o numero que voce vai procurar. '))
pergunta2 = int(input('Digite o segundo valor que voce vai procurar.'))
while x < len(lista):
    if lista[x] == pergunta:
        print('O numero desejado esta na lista.')
    if lista[y] == pergunta2:
        print('O segundo numero desejado foi encontrado.')
    else:
        print('O numero dois nao desejado nao foi encontrado.')
    x += 1