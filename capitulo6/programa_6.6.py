l = []
while True:
    n = int(input('Digite um valor (0 vai sair): '))
    if n == 0:
        break
    l.append(n)
x = 0
while x < len(l):
    print(l[x])
    x = x + 1
    