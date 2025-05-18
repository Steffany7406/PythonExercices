players = [
    {'player': "Anthony Edwards", 'time': "Minnesota", 'shirt': 5, 'points': 1015, 'assistence': 207, 'reboots': 242, 'pfalts': 92, 'blocked': 34},
    {'player': "Kevin Durant", 'time': "Phoenix Suns", 'shirt': 35, 'points': 29400, 'assistence': 4702, 'reboots': 7566, 'pfalts': 2045, 'blocked': 1216},
    {'player': "Joel Embiid", 'time': "Philadelphia 76ers", 'shirt': 21, 'points': 12500, 'assistence': 1658, 'reboots': 4987, 'pfalts': 1369, 'blocked': 738},
    {'player': "LeBron James", 'time': "Los Angeles Lakers", 'shirt': 23, 'points': 40500, 'assistence': 11100, 'reboots': 11300, 'pfalts': 2632, 'blocked': 1092},
    {'player': "Stephen Curry", 'time': "Golden State Warriors", 'shirt': 30, 'points': 25400, 'assistence': 6540, 'reboots': 4820, 'pfalts': 1232, 'blocked': 384},
    {'player': "Jayson Tatum", 'time': "Boston Celtics", 'shirt': 0, 'points': 13400, 'assistence': 2243, 'reboots': 4293, 'pfalts': 92, 'blocked': 34},
    {'player': "Shai Gilgeous-Alexander", 'time': "Oklahoma City Thunder", 'shirt': 2, 'points': 782, 'assistence': 187, 'reboots': 178, 'pfalts': 92, 'blocked': 32},
    {'player': "Giannis Antetokounmpo", 'time': "Milwaukee Bucks", 'shirt': 34, 'points': 20500, 'assistence': 4288, 'reboots': 8530, 'pfalts': 2531, 'blocked': 1064},
    {'player': "Luka Doncic", 'time': "Dallas Mavericks", 'shirt': 77, 'points': 12900, 'assistence': 3700, 'reboots': 3881, 'pfalts': 1028, 'blocked': 203},
    {'player': "Nicola Jokic", 'time': "Denver Nuggets", 'shirt': 15, 'points': 16200, 'assistence': 5383, 'reboots': 8141, 'pfalts': 1995, 'blocked': 533}
]

# Extraindo e imprimindo a posição dos jogadores
positions = [player['time'] for player in players]
print("Player Positions: ", positions)

# Atualizando a estatística de um jogador
for player in players:
    if player['player'] == "Jayson Tatum":
        player['pfalts'] += 200 
        player['blocked'] += 1

# Calculando as estatísticas
total_points = sum(player['points'] for player in players)
total_reb = sum(player['reboots'] for player in players)
total_ast = sum(player['assistence'] for player in players)
number_play = len(players)

media_pts = total_points / number_play
media_reb = total_reb / number_play
media_assi = total_ast / number_play

print(f"\nMédia de pontos: {media_pts:.2f}")
print(f"Média de Reboots: {media_reb:.2f}")
print(f"Média de assistências: {media_assi:.2f}")

#Player Positions:  ['Minnesota', 'Phoenix Suns', 'Philadelphia 76ers', 'Los Angeles Lakers', 'Golden State Warriors', 'Boston Celtics', 'Oklahoma City Thunder', 'Milwaukee Bucks', 'Dallas Mavericks', 'Denver Nuggets']

#Média de pontos: 17259.70
#Média de Reboots: 5393.80
#Média de assistências: 4000.80
