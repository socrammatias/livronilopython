v_inicial = set([10, 20, 30, 40])
v_alterada = set([100, 200, 300, 40, 400])

print(f'Os novos elementos sao esses: {v_alterada - v_inicial}')
print(f'Os elementos que foram removidos sao: {v_inicial - v_alterada}')
print(f'Os elemntos que nao mudaram sao: {v_inicial & v_alterada}')


