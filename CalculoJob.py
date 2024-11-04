"""
Faça um Programa que pergunte quanto você
ganha por hora e o número de horas trabalhadas no
mês. Calcule e mostre o total do seu salário no
referido mês.

"""
funcionario = float(input("Qual é o valor que você ganha por hora? R$"))
horas_trabalhadas = float(input("Quantas horas você trabalhou no mês? "))

def calcular_salario(valor_por_hora, horas_trabalhadas):
    salario = valor_por_hora * horas_trabalhadas
    return salario

# Calcular o salário
salario_funcionario = calcular_salario(funcionario, horas_trabalhadas)

# Exibir o salário
print(f"O salário do funcionário é R${salario_funcionario:.2f}")
