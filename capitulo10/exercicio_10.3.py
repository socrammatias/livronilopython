class Televisao:
    def __init__(self, min, max):
        self.ligada = False
        self.canal = 2
        self.cmin = min
        self.cmax = max
    def muda_canal_cima(self):
        if self.canal + 1 <= self.cmax:
            self.canal += 1
        if self.canal + 1 > self.cmax:
            self.canal = self.cmin
    def muda_canal_baixo(self):
        if self.canal -1 >= self.cmin:
            self.canal -= 1
        if self.canal - 1 < self.cmin:
            self.canal = self.cmax

tv = Televisao(2, 10)
tv.muda_canal_baixo()
print(tv.canal)
tv.muda_canal_cima()
print(tv.canal)