#Distancia ponto a ponto
from math import sqrt
xA, yA = [int(x) for x in input("Coordenadas do ponto P (separadas por ESPAÇO): ").split()]
xB, yB = [int(x) for x in input("Coordenadas do ponto Q (separadas por ESPAÇO): ").split()]
distAB = sqrt((xA-xB)**2 + ((yA-yB)**2))
print('A distância entre esses dois pontos é de {:.2f} unidades de medida.'.format(distAB))