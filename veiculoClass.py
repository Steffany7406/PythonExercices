class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def exibir_Detalhes(self):
        print(f'Marca: {self.marca}, Modelo: {self.modelo} e Ano: {self.ano}')

myCar = Carro('Volkswagem', 'T-Cross', 2023)
myCar.exibir_Detalhes()
#--------------------------------

class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def Infor(self):
        print(f'Marca: {self.marca} e Modelo: {self.modelo}')  

class Moto(Veiculo):
    def __init__(self, marca, modelo, cilindrada):
        super().__init__(marca, modelo)
        self.cilindrada = cilindrada

    def mostrar_Mais(self):
        print(f'Cilindradas: {self.cilindrada}')

moto = Moto('Honda', 'CBR500R', 510)
moto.Infor()
moto.mostrar_Mais()               