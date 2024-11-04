#Escreva um programa que usa um loop while para imprimir todos os números ímpares entre 1 e 20.

num = 1
while num <= 20:
    if num % 2 != 0:
        print(num)
    num += 1    