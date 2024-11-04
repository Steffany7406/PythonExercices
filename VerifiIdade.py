""" 
Escreva um código if e else que define com base na informação do usuário se ele é maior ou menor de idade.
"""
idade = input('Digite sua idade: ')
idade = int(idade)

def verificar_idade():
    if idade >= 18:
        print("Ok! Bem-vindo ao Jogo!")
    else:
        print("Opa! Esse jogo é apenas para maiores!") 

verificar_idade()        