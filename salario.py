""" 
Elabore um programa que efetue o cálculo de um aumento salarial
respeitando o seguinte critério: se salário for menor ou igual a
R$500,00, aumento de 15%; se salário for maior que R$500,00 mas
menor ou igual a R$1.000,00, aumento de 12,5%; se salário for
maior que R$1.000,00, aumento de 10%.
"""
salario = float(input('Informe seu salário: R$'))

def aumento(salario):
    if salario <= 500:
        print(f'O seu salário atual é {salario * 1.15:.3f}')
    elif salario <= 1000:
        print(f'O seu salário atual é {salario * 1.125:.3f}')
    else:
        print(f'O seu salário atual é {salario * 1.10:.3f}')

aumento(salario)