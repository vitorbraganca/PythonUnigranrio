massa = float(input('Insira a massa em quilogramas (kg): '))
altura = float(input('Insira a altura em metros (m): '))
indice = massa / (altura**2) # Calculo IMC
print('IMC = {:.2f}'.format(indice))