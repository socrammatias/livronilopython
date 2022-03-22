#!/usr/bin/env python3
LARGURA = 79
with open('entrada.txt') as entrada:
    for linha in entrada.readlines():
        if linha[0] == ';':
            continue
        elif linha[0] == '>':
            print(linha[1:].rjust(LARGURA))
        elif linha[0] == '*':
            print(linha[1:].center(LARGURA))
        elif linha[0] == '=':
            print(linha[0] * 40)
        elif linha[0] == '.':
            input('Aperta enter')
        else:
            print(linha)
