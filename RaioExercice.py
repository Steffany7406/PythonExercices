import math

class Esfera:
    def __init__(self, cor, raio):
        self.cor = cor
        self.raio = raio

    def volume(self):
        vol = (4/3) * math.pi * (self.raio**3)
        return vol

    def area(self):
        area = 4 * math.pi * (self.raio**2)
        return area

bola = Esfera('Vermelha', 4)
bola1 = Esfera('Azul', 7)

print(f"\nO volume da esfera {bola.cor} é {bola.volume():.2f}cm^3")
print(f"O volume da esfera {bola.cor} é {bola.volume():.2f}cm^2")