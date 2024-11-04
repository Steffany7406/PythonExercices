#Com base nos dados do usuário, defina se o score é bom ou se precisa melhorar.

result = input('Qual foi o seu score no jogo? (Em números) ')

def verificar_score():
    if int(result) >= 85:
        print('Parabéns! Você fez um excelente trabalho!')
    elif int(result) >= 70:
        print('Você fez um bom trabalho, mas pode melhorar!')
    else:
        print('Você precisa melhorar!')

verificar_score()