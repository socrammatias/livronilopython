with open('pareseimpares.txt','w') as parimpar:
    with open('pares.txt','r') as pares, open('impares.txt','r') as impares:
        for linha in pares:
            if int(linha) % 2 == 0:
                parimpar.write(linha)
                for linha in impares:
                    if int(linha) % 2 == 1:
                        parimpar.write(linha)