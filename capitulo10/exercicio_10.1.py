class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 2
        self.tamanho = 30
        self.marca = 'LG'
    
tv = Televisao()
tv.ligada = True
tv.canal = 1
tv.tamanho = 15
tv.marca = 'Samsung'

print(f'A televisao esta ligada? {tv.ligada}')
print(f'O canal atual é {tv.canal}')
print(f'O tamanho da televisao eh : {tv.tamanho}')
print(f'A marca da televisao eh : {tv.marca}')