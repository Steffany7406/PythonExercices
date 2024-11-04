""" 
Um homem decidiu ir à uma revenda comprar um carro. Ele deseja
comprar um carro hatch, e a revenda possui, além de carros hatch,
sedans, motocicletas e caminhonetes. 
Utilizando uma estrutura switch/case, caso o comprador queira o hatch, retorne: “Compra
efetuada com sucesso”. 
Nas outras opções, retorne: “Tem certeza que não prefere este modelo?”. 
Caso seja especificado um modelo que não está disponível, retorne no console: “Não trabalhamos com
este tipo de automóvel aqui”.
"""
# Definindo as opções disponíveis
opcoes_disponiveis = ["hatch", "sedan", "motocicleta", "caminhonete"]
print(opcoes_disponiveis)

# Definindo a opção escolhida pelo comprador
opcao_escolhida = input("Informe a escolha do modelo que deseja comprar: ")

def compra_carro(opcao_escolhida):
    Switcher = {
        'hatch': 'Compra efetuada com sucesso!',
        'sedan': 'Tem certeza que não prefere este modelo?',
        'motocicleta': 'Tem certeza que não prefere este modelo?',
        'caminhonete': 'Tem certeza que não prefere este modelo?',
    }
    return Switcher.get(opcao_escolhida, 'Não trabalhamos com esse tipo de modelo!')

mensagem = compra_carro(opcao_escolhida)
print(mensagem)


"""Outra forma:

Definindo a função para realizar a compra

def realizar_compra(opcao_escolhida):
# Utilizando um switch/case para realizar a compra
    if opcao_escolhida == "hatch":
        print("Compra efetuada com sucesso.")
    elif opcao_escolhida in opcoes_disponiveis:
        print("Tem certeza que não prefere este modelo?")
    else:
        print("Não trabalhamos com este tipo de automóvel aqui.")
Chamando a função para realizar a compra
realizar_compra(opcao_escolhida)
"""