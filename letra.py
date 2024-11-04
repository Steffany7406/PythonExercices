"""
Faça um programa que verifique se uma letra digitada num campo de
input é vogal ou consoante.
"""
def verificar_letra():
    letra = input('Digite uma letra: ').lower
    vogais = 'aeiou'
    if letra == vogais:
        print(f'Essa letra é uma vogal')
    else:
        print(f'Essa letra é uma consoante')

verificar_letra()        
