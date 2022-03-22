#!/usr/bin/env python3
dicio = {}
nome_arquivo = input('Digite o nome do arquivo: ')
arquivo = open(nome_arquivo, 'r')
for palavra in arquivo:
    palavra = palavra.rstrip('\n')
    dicio[palavra] = dicio.get(palavra, 0) + 1
arquivo.close()
print(dicio)
