lista = [33, 54, 89]
x = 0 
pergunta = int(input('Digite o numero que voce vai procurar. '))
while x < len(lista):
    if lista[x] == pergunta:
        print('O numero desejado esta na lista.')
    else:
        print('O numero desejado nao esta na lista')
        break
    x += 1