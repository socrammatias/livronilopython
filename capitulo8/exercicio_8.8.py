def mdc(a, b):
    if b == 0:
        return a
    else:
        return mdc(b, a%b)

def mmc(a, b):
    return abs(a*b) / mdc(a, b)

print(f'O resultado do mmc é {mmc(10, 5)}')