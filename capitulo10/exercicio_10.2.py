class Televisao:
    def __init__(self, canal_inicial, min, max): # metodo construtor
        self.ligada = False
        self.canal = canal_inicial # atributo
        self.cmin = min
        self.cmax = max
    def muda_canal_cima(self):
        if self.canal + 1 <= self.cmax:
            self.canal += 1
    def muda_canal_baixo(self):
        if self.canal -1 >= self.cmin:
            self.canal -= 1

tv = Televisao(5, 1, 99) # declarando que esta comecando no canal 2
print(tv.canal)
tv.muda_canal_cima()
print(tv.canal)