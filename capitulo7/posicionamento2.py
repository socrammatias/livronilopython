'''Se voce passar um parametro tanto para strip, quanto para rstrip ou lstrip
o parametro passado sera utilizado para remover'''

frase = "...///Olá\\\..."
print(frase.strip("."))
print(frase.lstrip("."))
print(frase.rstrip("."))
lista_nomes = ['Lucas','Amedeo']

print('Oi meu nome eh {0[0]}, ola meu nome eh {0[1]}'.format(lista_nomes))
