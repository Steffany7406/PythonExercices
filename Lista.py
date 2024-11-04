
#Crie um array com 10 números inteiros. Exiba apenas os números pares presentes no array.

# 1. Crie um array com 10 números inteiros.
lista = [0, 25, 81, 36, 14, 37, 15, 56, 99, 22, 74]
# 2. Exiba apenas os números pares presentes no array.
print([num for num in lista if num % 2 == 0])  
# 3. Utilize a função filter() para filtrar os números pares.
print(list(filter(lambda x: x % 2 == 0, lista))) 
# 4. Utilize a função list() para converter a sequência de números pares em uma lista.
print(list(filter(lambda x: x % 2 == 0, lista)))
# 5. Exiba a lista de números pares.
print(lista)

