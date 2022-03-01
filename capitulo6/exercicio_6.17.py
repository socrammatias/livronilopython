estoque = {"tomate": [1000, 2.30],
           "alface": [500, 0.45],
           "batata": [2001, 1.20],
           "feijao": [100, 1.50]}

produto = input('Digite o nome do produto')
qtd = int(input('Quantidade: '))
venda = [[produto, qtd]]
total = 0
print('Vendas: \n')
for operacao in venda:
    produto, quantidade = operacao
    preco = estoque[produto][1]
    custo = preco * quantidade
    print(f'{produto:9s}: {quantidade:3d} x {preco:6.2f} = {custo:6.2f}')
    estoque[produto][0] -= quantidade
    total += custo

print(f'Custo total: {total:21.2f}\n')
print(f'Estoque:\n')
for chave, dados in estoque.items():
    print('Descricao: ', chave)
    print('Quantidade: ', dados[0])
    print(f'Preço:  {dados[1]:6.2f}')