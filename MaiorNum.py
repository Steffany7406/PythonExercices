""" 
Faça um script que leia três números inteiros e mostre o maior
deles.
"""

# Recebendo os valores dos números inteiros
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

# Comparando os números inteiros
def  comparar_numeros(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        print(f"O maior número é {num1}")
    elif num2 > num1 and num2 > num3:
        print(f"O maior número é {num2}")
    else:
        print(f"O maior número é {num3}")

comparar_numeros()

#Outra Forma
maior = max(num1, num2, num3)
print(f'O maior número é {maior}')