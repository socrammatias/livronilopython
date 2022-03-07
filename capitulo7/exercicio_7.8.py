lista_p = ['Batata','Frango','Carro','Fusca','Tiroteio',
          'Notebook', 'Computador', 'Calculadora', 'Nerd',
          'Policial', 'Rede','Comprar','Mulher', 'Adulto',
          'Tempo', 'Trampo','Vender','Teclado', 'Mouse']
numero = int(input('Digite um numero: '))
indice = (numero * 776) % len(lista_p)
palavra = lista_p[indice].lower().strip()
acertos = []
digitadas = []
erros = 0
for x in range(100):
    print()

while True:
    senha = ''
    for letra in palavra:
        senha += letra if letra in acertos else '.'
    print(senha)
    if senha == palavra:
        print('Voce acertou!')
        break
    tentativa = input('Digite a letra: ').lower().strip()
    if tentativa in digitadas:
        print('Voce ja digitou essa letra.')
        continue
    else:
        digitadas += tentativa
        if tentativa in palavra:
            acertos += tentativa
        else:
            erros += 1
            print('Voce errou.')
    print("X==:==\nX  :  ")
    print("X  0  " if erros >= 1 else "X")
    linha2 = ""
    if erros == 2:
        linha2 = "  |  "
    elif erros == 3:
        linha2 = "  |  "
    elif erros >= 4:
        linha2 = " \|/  "
    print(f'X{linha2}')
    linha3 = ""
    if erros == 5:
        linha3 += "  /   "
    if erros == 6:
        linha3 += "  / \ "
    print(f"{linha3}")
    print("X\n===========")
    if erros == 6:
        print('Enforcado!')
        print(f'A palavra secreta era {palavra}')
        break