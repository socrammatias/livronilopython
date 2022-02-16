notas = [0, 0, 0, 0, 0, 0, 0]
x = 0
soma = 0 # soma ta vazia porque iremos iterar os valores dentro da variavel soma
while x < 7:
    notas[x] = float(input('Digite sua nota: ')) # a cada INDICE vamos adicionar um valor
    soma = soma + notas[x] # soma vai iterar os valores da notas de cada indice
    x = x + 1 # contador padrao
x = 0 # temos que resetar aqui para percorrermos os valores dentro da lista novamente
while x < 7:
    print(f'Nota {x} : {notas[x]}')
    x += 1
print(f'A sua media eh: {soma / x}')