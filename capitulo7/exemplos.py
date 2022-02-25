# contar o numero de elementos 

a = 'O rato roeu a roupa do rei de roma'
print(a.count('a')) # duas ocorrencias da letra A maiscula

#sla = input('Digite uma palavra em maisculo: ').lower()
#print(sla)
#sla2 = input('Digite uma palavra em minusculo: ').upper()
#print(sla2)

# Verificar se uma palavra pertence a uma string

palavra = 'Gato'
print('Gato' in palavra)
print('GATO' in palavra)

frutas = ['Maça', 'Pera','Abacate']
print('Pera' in frutas) # verificando se uma palavra pertence a lista

# sempre bom lembrar que uma letra maiscula eh diferente de uma minuscula 

# Verificar se uma palavra nao pertence a uma string

nome = 'Pedro'
print('Pedro' is not nome) # False caso esteja dentro
print('pedro' is not nome) # True caso nao esteja 
