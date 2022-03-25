#!/usr/bin/env python3
agenda = []
def pede_nome():
    return input('Nome: ')
def pede_telefone():
    return input('Telefone: ')
def mostra_dados(nome, telefone):
    print(f'Nome: {nome}, Telefone: {telefone}')
def pede_nome_arquivo():
    return input('Nome do arquivo: ')
def pesquisa(nome):
    mnome = nome.lower()
    for p, e in enumerate(agenda):
        if e[0].lower() == mnome:
            return p
    return None
def novo():
    global agenda
    nome = pede_nome()
    telefone = pede_telefone()
    agenda.append([nome, telefone])
def apaga():
    global agenda
    nome = pede_nome()
    op = int(input('Voce tem certeza dessa decisao?\n1- Sim 2- Nao: '))
    if op == 1:
        p = pesquisa(nome)
        if p is not None:
            del agenda[0]
        else:
            print('Nome não encontrado')
    else:
        print('Operacao cancelada')

def altera():
    op = int(input('Voce tem certeza dessa decisao?\n1- Sim 2- Nao: '))
    if op == 1:
        p = pesquisa(pede_nome())
        if p is not None:
            nome = agenda[p][0]
            telefone = agenda[p][1]
            print('Encontrado')
            mostra_dados(nome, telefone)
            nome = pede_nome()
            telefone = pede_telefone()
            agenda[p] = [nome, telefone]
        else:
            print('Nome nao encontrado')
    else:
        print('Operacao cancelada')
def lista():
    print('Agenda')
    for pos, e in enumerate (agenda):
        print(f'Posicao {pos} ', end='')
        mostra_dados(e[0], e[1])
    print('-----\n')

def le():
    global agenda
    nome_arquivo = pede_nome_arquivo()
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        agenda = []
        for l in arquivo.readlines():
            nome, telefone = l.strip().split('#')
            agenda.append([nome, telefone])
def grava():
    nome_arquivo = pede_nome_arquivo()
    with open(nome_arquivo, 'w', enconding='utf-8') as arquivo:
        for e in agenda:
            arquivo.write(f'{e[0]}#{e[1]}\n')

def valida_faixa_inteiro(pergunta, inicio, fim):
    while True:
        try:
            valor = int(input(pergunta))
            if inicio <= valor <= fim:
                return valor
        except ValueError:
            print(f'Valor invalido, favor digitar entre {inicio} e {fim}')
def ordena():
    global agenda
    agenda = agenda.sort()
    return agenda 
def menu():
    print(f'''
    1- Novo
    2- Altera
    3- Apaga
    4- Lista
    5- Grava
    6- Lê
    7- Ordenar a agenda
    Atualmente possuimos {len(agenda)} numeros na agenda
    0- Sair
''')

    return valida_faixa_inteiro('Escolha uma opcao: ', 0, 6)

while True:
    opcao = menu()
    if opcao == 0:
        break
    elif opcao == 1:
        novo()
    elif opcao == 2:
        altera()
    elif opcao == 3:
        apaga()
    elif opcao == 4:
        lista()
    elif opcao == 5:
        grava()
    elif opcao == 6:
        le()
    elif opcao == 7:
        ordena()
