# 1: Automovel consome 12km/ litro
tempo_gasto = float(input('Tempo gasto na viagem (em horas): '))
vel_med =  float(input('Velocidade média na viagem (em km/h)'))
distancia = tempo_gasto * vel_med
consumo = distancia/12
print(f'Velocidad media: {vel_med} km/h| Tempo gasto: {tempo_gasto} horas | Distancia percorrida: {distancia} km | Consumo: {consumo} litros')