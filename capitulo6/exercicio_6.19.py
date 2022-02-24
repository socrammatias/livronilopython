a = set([1, 2, 3, 4, 5, 10, -2, -1])
b = set([3, 1, 10, -1, 9, 0, 13])
c = set()

primeira = a - b
segunda = b - a
c = a & b

print(f'O valor existente apenas na primeira lista eh {primeira}')
print(f'O valor existente apenas na segunda lista eh {segunda}')
print(f'O valor existente nas duas listas (comum) eh {c}')
print(f'Elementos nao repetidos nas duas listas: {a ^ b}')