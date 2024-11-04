'''
Faça um Programa que peça as 4 notas bimestrais e
mostre a média.
'''
nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))
nota3 = float(input('Informe a terceira nota: '))
nota4 = float(input('Informe a quarta nota: '))

media = (nota1 + nota2 + nota3 + nota4) / 4
print(f'A média das notas é {media:.2f}')  # O :.2f  é para mostrar apenas 2 casas decimais.

def resultado():
    if media  >= 7:
        print('Aluno Aprovado')
    elif media < 7 and media >= 4:
        print('Aluno em Recuperação')
    else:
        print('Aluno Reprovado')

resultado() 
