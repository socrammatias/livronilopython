t = [ -10, -8, 0, 1, 2, 5, -2, -4]
maxima = t[0]
menor = t[0]
media = t[0]
for i in t:
    if i > maxima:
        maxima = i
    for j in t:
        if i < menor:
            menor = i
    for k in t:
        media = media + k

media = media / len(t)
print(f'A media da temperatura eh {media:5.2f}')
print(f'A menor temperatura eh {menor}')
print(f'Temperatura maxima eh {maxima}')