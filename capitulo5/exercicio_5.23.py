while True:
    ler = int(input('Digite um numero: '))
    i = ler
    resto = ler % 2
    if resto == 0:
        print(f'{ler} nao eh primo')
    if resto > 0:
        print(f'{ler} eh primo')
    elif ler == 2:
        print(f'{ler} eh primo')