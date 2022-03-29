from clientes import Cliente

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

joao = Cliente('Joao', '98888-8888')
conta_joao = Conta([joao], 1000)
conta_joao.saque(10001)