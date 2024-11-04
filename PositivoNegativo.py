""" 
Escreva um código usando if...else que verifique se um
número é positivo, negativo ou zero.
"""
# Entrada de dados
num = float(input('Digite o número desejado: '))

# Verificação do número
if num > 0:
    print(f'O número {num} é positivo')
elif num < 0:
    print(f'O número {num} é negativo')
else:
    print(f'O número {num} é zero')