def write_liked_songs_to_file(file_name):
    lines = [
        'Liberian Girl by Michael Jackson\n',
        'Bones By Imagine Dragons\n',
        'Little Less Conversation by Elvis Presley\n',
        'Shake it off by Mariah Carey\n'
    ]
    # Usando gerenciador de contexto para garantir fechamento do arquivo
    with open(file_name, 'w') as file:
        file.writelines(lines)

write_liked_songs_to_file('liked_songs.txt')

# Abrir e ler o arquivo com gerenciador de contexto
with open('liked_songs.txt', 'r') as file:
    content = file.read()
    print(content)
