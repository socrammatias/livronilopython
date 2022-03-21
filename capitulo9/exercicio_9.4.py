#!/usr/bin/env python3
import sys
n1 = open(sys.argv[1],'r')
n2 = open(sys.argv[2],'r')
saida = open(sys.argv[3],'w')

if len(sys.argv) < 4 or len(sys.argv) > 5:
    print('erro')
for linha in n1:
    saida.write(linha)
for linha in n2:
    saida.write(linha)

saida.close()
n1.close()
n2.close()
print('Gravado!')