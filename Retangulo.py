class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_Area(self):
        return self.altura * self.largura;

reta = Retangulo(15, 25)
print(reta.calcular_Area()) 

# Criar uma classe com input com o valor que calula a area do retangulo 
class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

        