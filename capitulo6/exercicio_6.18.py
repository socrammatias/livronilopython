string = input()
d = {}
for letra in string:
    if letra in d: # se a letra ja estiver no dicionario
        d[letra] += 1 # soma mais um
    else:
        d[letra] = 1 # se nao mantem o valor padrao
print(d)