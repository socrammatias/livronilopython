s = 'tigre'
s.ljust(20) # passando a quantidade de espacos para a esquerda
s.rjust(20) # passando a quantidade de espacos para a direita

print(s.ljust(20, '-')) # passando um novo parametro que vai completar os espacos com a string que eu mandei
print(s.rjust(20, '-')) 

''' O metodo split quebra uma string a partir do caracter usado como parametro e nos devolve uma lista com
as substrings'''

frase = 'O rato, caiu no chao, e depois comeu o queijo'
print(frase.split(',')) # como meu parametro foi a virgula, onde for encontrada virgula na minha string
# ela sera fatiada e retornada numa lista
print(frase.split(' ')) # onde tiver espacos em branco sera uma nova substrings retornada na lista tambem

'''Outro metodo interessante é o splitlines que vai separar a string por linha.'''
frase2 = 'Eu\namo\nPython' # nesse exemplo eu quebrei as linhas com \n e com isso cada linha vai para a lista separadamente
print(frase2.splitlines())

f = 'um tigre, dois tigres, tres tigres'
''' O primeiro parametro do metodo replace eh a string que queremos substituir, e o segundo
eh o conteudo que vai substituir'''

print(f.replace('tigre', 'gatinho')) # troquei a palavra tigre por gatinho

'''O metodo strip, remove os espacos em branco colocados na string, rstrip remove os espacos em branco a direita
lstrip remove os espacos em branco a esquerda e strip remove TODOS os espacos em branco.'''

nome = ' Lucas'
print(nome.strip()) # o output que teremos eh a palavra Lucas sem os espaços
nome = '     Lucas      '
print(nome.rstrip()) # removendo os espacos em branco a direita
nome = '  Ola    ' 
print(nome.lstrip())
