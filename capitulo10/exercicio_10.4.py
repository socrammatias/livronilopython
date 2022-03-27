class Televisao:
    def __init__(self, min=2, max=14):
        self.ligada = False
        self.canal = min # pois vai ser o primeiro canal
        self.cmin = min
        self.cmax = max
    def muda_canal_cima(self):
        if self.canal + 1 <= self.cmax:
            self.canal += 1
        else:
            self.canal = self.cmin
    def muda_canal_baixo(self):
        if self.canal -1 >= self.cmin:
            self.canal -= 1
        else:
            self.canal = self.cmax

tv = Televisao()
print(tv.canal)
tv.muda_canal_cima()
print(tv.canal)