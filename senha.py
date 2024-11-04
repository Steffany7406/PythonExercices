
#Escreva um programa que continua pedindo ao usuário para
#inserir uma senha até que a senha correta seja digitada.

senha = input('Digite sua senha: ')

while senha != '1234':
    senha = input('Senha incorreta! Digite novamente: ')
    
print('Acesso Permitido! Bem-vindo!')

"""
def verificar_senha(senha):
    if senha == '240851':
        print('Bem-vindo ao sistema!')
    else:
        print("Senha inválida! Tente novamente!")
"""