# Função para calcular distância entre dois pontos (latitude, longitude) pela fórmula de Haversine

import math

def haversine(coord1, coord2):
  R = 6371 #Raio da terra em KM

  lat1, lon1 = coord1
  lat2, lon2 = coord2

  phi1 = math.radians(lat1)
  phi2 = math.radians(lat2)

  delta_phi = math.radians(lat2 - lat1)
  delta_lambda = math.radians(lon2 - lon1)

  a = math.sin(delta_phi / 2)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2)**2
  c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

  distance = R * c
  return distance

minha_localizacao = (-23.55052, -46.633308) #São Paulo, BR.

friend1 = (40.712776, -74.005974) #NY, EUA
friend2 = (48.856613, 2.352222) #Paris, França
friend3 = (-34.603722, -58.381592) #Buenos Aires, Argentina

print("Localização dos Amigos:")
print(f"Amigo = {friend1}")
print(f"Amigo = {friend2}")
print(f"Amigo = {friend3}")
