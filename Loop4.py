
""" 
Escreva um código que imprima a tabuada de 1 a 10, de forma
organizada e clara. A saída precisa ser semelhante ao exemplo
abaixo:
1 x 3 = 3
"""

# Iniciando o loop para imprimir a tabuada de 1 a 10
for i in range(1, 11):
    # Iniciando o loop para imprimir a tabuada de cada número de 1 a
    for j in range(1, 11):
        # Imprimindo a tabuada de cada número
        print(f"{i} x {j} = {i * j}")
        print("\n")  # Imprimindo uma linha em branco após cada tabuada

       