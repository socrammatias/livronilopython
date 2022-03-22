#!/usr/bin/env python3
qtd = int(input())
lista_arquivos = []
for x in range(qtd):
    lista_arquivos.append(input('Digite o nome do arquivo: '))
print('Arquivos salvos! Hora de imprimir...')
for arquivo in lista_arquivos:
    arqs = open(arquivo, 'r')
    for linha in arqs:
        print(linha)

arqs.close()
