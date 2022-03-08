def pesquise(lista, valor):
    i = 0
    while i < len(lista):
        if valores[i] == valor:
            return i
        i += 1
    else:
        return None
valores = [1, 2, 3, 7, 8, 12, 20, 32, 37]
print(pesquise(valores, 12))