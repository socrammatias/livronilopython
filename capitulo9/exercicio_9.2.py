#!/usr/bin/env python3
import sys
a = sys.argv[1]
inicio = int(sys.argv[2])
fim = int(sys.argv[3])
arquivo = open(a,'r')
for linha in arquivo.readlines()[inicio-1:fim]:
    print(linha[:-1])
arquivo.close()