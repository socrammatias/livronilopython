def valida(string, min, max):
    return len(string) >= min and len(string) <= max


print(valida('paralelepipedo',6, 20))
print(valida('batata',1, 4))
print(valida('chicken',5, 10))