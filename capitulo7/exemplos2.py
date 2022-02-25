# Contar a quantidade de ocorrencias dentro de uma string, seja a letra ou uma palavra em si

loja = 'Americanas'
print(loja.count('a')) # vai printar a quantidade de vezes que a palavra a aparece na string
frase = 'Um tigre, dois tigres, tres tigres'
print(frase.count('tigres'))

# Caso eu queira pesquisar uma string dentro da variavel eu posso utilizar find

palavra = 'Sistemas'
print(palavra.find('m')) # vai printar o indice exato onde a letra ou palavra desejada começa
print(palavra.find('temas'))

# Caso eu queira pesquisar uma string dentro da variavel e quero começar de um x indice

print(palavra.find('mas', 3)) # começando no indice 3

'''Caso eu coloque uma palavra ou um indice que nao esteja na variavel etc,
a minha acao ira retornar o valor -1 que ate entao esta me dizendo que nao 
possui o que eu quero'''