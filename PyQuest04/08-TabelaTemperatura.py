# Tabela Celsius -> Farenheit
farnht = 0
i = 100
for i in range(150):
    farnht += 1
    celsius = (5 / 9) * (farnht - 32)
    print('{:.2f}°F = {:.2f}°C'.format(farnht, celsius))
    print('-'*20)
