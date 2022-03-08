def maior(a, b):
    if a > b:
        return a
    if b > a:
        return b
    if a == b:
        return a
print(maior(5, 6))
print(maior(2, 1))
print(maior(7, 7))