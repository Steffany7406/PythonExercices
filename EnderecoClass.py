class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero

class Pessoa:
    def __init__(self, nome, idade, endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

    def pessoa_Info(self):
        return f'Nome: {self.nome}, Idade: {self.idade} anos \nMora em: {self.endereco.rua}, {self.endereco.numero}'

endereco =  Endereco('Rua 1', 123)
matricula = Pessoa('Steffany', 24, endereco)
print(matricula.pessoa_Info())
