class Cliente:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

class Conta:
    def __init__(self, clientes, numero, saldo=0):
        self.saldo = 0
        self.clientes = clientes
        self.numero = numero
        self.operacoes = []
        self.deposito(saldo)
    def resumo(self):
        print(f'CC Numero: {self.numero} Saldo: {self.saldo:10.2f}')
        for x in self.clientes:
            print(f'Informacoes: {x.nome} {x.telefone}\n')
    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.operacoes.append(['SAQUE', valor])
        else:
            print('SALDO INSUFICIENTE')
    def deposito(self, valor):
        self.saldo += valor
        self.operacoes.append(['DEPOSITO', valor])
    def extrato(self):
        print(f'EXTRATO CC Nº {self.numero}\n')
        for o in self.operacoes:
            print(f'{o[0]:10s} {o[1]:10.2f}')
        print(f'Saldo: {self.saldo:10.2f}\n')

João = Cliente('João','333')
José = Cliente('José','444')

João = Conta([João], 123, 500)
José = Conta([José], 456, 500)

João.resumo()
José.resumo()