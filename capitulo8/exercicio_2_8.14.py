# Uma implementacao pessoal na dificuldade do exercicio
# usarei uma wordlist e irei selecionar uma palavra aleatoria
import random
lista_palavra = []
with open('capitulo8/wordlist.txt') as wordlist: # passando o caminho absoluto para evitar erro
    data = wordlist.read().split('\n') # removendo a quebra de linha
    for linha in data:
        lista_palavra.append(linha)
tamanho = len(lista_palavra)
palavra = lista_palavra[random.randint(0, tamanho)].lower()
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
    print("X==:==\nX :  ")
    print("X 0  " if erros >= 1 else "X")
    linha2 = ""
    if erros == 2:
        linha2 = "  |  "
    elif erros == 3:
        linha2 = " |  "
    elif erros >= 4:
        linha2 = " |/  "
    print(f'X{linha2}')
    linha3 = ""
    if erros == 5:
        linha3 += " /   "
    if erros == 6:
        linha3 += " / \ "
    print(f"{linha3}")
    print("X\n===========")
    if erros == 6:
        print('Enforcado!')
        print(f'A palavra secreta era {palavra.strip()}')
        break
