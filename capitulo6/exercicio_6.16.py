lista = [7, 4, 3, 12, 8]
n = len(lista)

for j in range(n - 1):
    for i in range(n - 1):
        if lista[i] < lista[i + 1]:
            aux = lista[i]
            lista[i] = lista[i + 1]
            lista[i + 1] = aux

for e in lista:
    print(e)