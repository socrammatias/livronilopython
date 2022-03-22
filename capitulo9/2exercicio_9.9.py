#!/usr/bin/env python3
import sys

if len(sys.argv) < 2:
    print('Operacao incorreta')

for x in sys.argv[1:]:
    arquivo = open(x,'r')
    for linha in arquivo:
        print(linha)
    arquivo.close()
