matriz = [[None, None, None, None, None],
          [None, 'A', None, None, None],
          [None, None, None, None, 'C'],
          [None, None, 'B', None, 'D'],
          [None, None, None, None, None]]

origem = (3, 0)
destino = (1, 1)

def distancia(ponto1, ponto2):
    x1, y1 = ponto1
    x2, y2 = ponto2
    return abs(x1 - x2) + abs(y1 - y2)

distancia_percorrida = distancia(origem, destino)
print(f"A distância percorrida é {distancia_percorrida} dronômetros")
