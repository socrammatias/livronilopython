primeira = input()
segunda = input()
terceira = ''

for letra in primeira:
    if letra not in segunda:
        terceira += letra
for letra in segunda:
    if letra not in primeira:
        terceira += letra

if terceira == '':
    print('Vazia')
else:
    print(f'Os caracteres diferentes sao {terceira}')

