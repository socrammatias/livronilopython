pares = open('/home/marco/Documents/livro-nilo/pares.txt','r')
novopar = open('par_invertido.txt','w')

L = pares.readlines()
L.reverse()
for x in L:
    novopar.write(x)

pares.close()
novopar.close()