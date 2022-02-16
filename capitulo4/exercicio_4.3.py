a = int(input('Digite um numero'))
b = int(input('Digite um numero'))
c = int(input('Digite um numero'))

if a > b and c < a:
    print('A eh o maior')
if b > a and c < b:
    print('B eh o maior')
if c > a and b < c:
    print('C eh o maior')