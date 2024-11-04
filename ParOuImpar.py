""" 
Faça um script que leia um número e que defina se o número é par
ou ímpar.
"""
# Solicitando o número ao usuário
num = int(input("Digite um número: "))

# Verificando se o número é par ou ímpar
def definindo_par():
    if num % 2 == 0:
        print(f"O número {num} é par.")
    else:
        print(f"O número {num} é ímpar.")

definindo_par()