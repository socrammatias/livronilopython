class Televisao:
    def __init__(self, min=2, max=40):
        self.ligada = False
        self.canal = min # valor que vai determinar o primeiro canal
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

tv = Televisao(min=10, max=20)
tv.muda_canal_baixo()
print(tv.canal)

tv1 = Televisao(min=1, max=15)
tv1.muda_canal_baixo()
print(tv1.canal)