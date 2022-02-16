a = []
b = []
while True:
    v = int(input('Digite os valores (0 vai parar): '))
    if v == 0:
        break
    a.append(v)
while True:
    v2 = int(input('Digite os valores da segunda lista (0 vai parar): '))
    if v2 == 0:
        break
    b.append(v2)

c = []
c.extend(a + b) 
'''o extend me faz concatenar listas sem criar uma lista dentro de outra
tambem serve para adicionar mais de um elemento, pois se eu adicionar mais de um elemento
utilizando o append, eu irei ter uma lista dentro de outra lista'''
x = 0 
while x < len(c):
    print(f'{x}:{c[x]}')
    x += 1