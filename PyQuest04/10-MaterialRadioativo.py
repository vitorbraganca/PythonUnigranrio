tempo = 0
massa = float(input('Insira a massa do material: '))
while massa > 0.50:
    tempo += 1
    massa = massa / 2
total = tempo * 50
min = total / 60
print('Levou {:.2f} segundos ou {:.2f} minutos.'.format(total, min))