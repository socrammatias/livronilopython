primeira = 'AAACTBF'
segunda = 'CBT'
terceira = ''
for letra in primeira: # para cada letra 
    if letra in segunda: # se a letra estiver na variavel segunda
        terceira += letra # a variavel terceira vai receber essa letra
    
print(terceira)
