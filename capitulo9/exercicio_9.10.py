#!/usr/bin/env python3

import sys

if len(sys.argv) < 2:
    print('Operacao invalida!!')

for arq in sys.argv[1:]:
    novo = open('novotxt','w')
    arquivos = open(arq, 'r')
    for linha in arquivos:
        novo.write(linha)
    arquivos.close()
novo.close()
