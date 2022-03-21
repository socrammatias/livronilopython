pares = open('/home/marco/Documents/livro-nilo/pares.txt','r')
novopar = open('pares2.txt','w')
for linha in pares:
    x = pares.readlines()[::-1]
    for a in x:
        novopar.write(a)

novopar.close()
pares.close()

