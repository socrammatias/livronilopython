l = [1, 7, 2, 4]
menor = l[0]
for e in l:
    if e < menor:
        menor = e
print(f'Maior elemento eh {menor}')