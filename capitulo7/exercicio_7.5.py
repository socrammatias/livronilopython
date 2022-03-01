primeira = input()
segunda = input()
terceira = ''

for letra in primeira:
    if letra not in segunda:
        terceira += letra

print(terceira)