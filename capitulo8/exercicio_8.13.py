def verifica(opcoes):
    opcoes = opcoes.lower()
    while True:
        oi = input().lower()
        if oi in opcoes:
            print(f'A letra digitada {oi} esta na opcao.')
            break
        print(f'A letra digitada {oi} nao esta na opcao.')
        continue
    return oi

print(verifica('abcde'))