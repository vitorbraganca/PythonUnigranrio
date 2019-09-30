tempo = 0
massa = float(input('Insira a massa do material em gramas: '))
while massa > 500:
    tempo += 1
    massa = massa / 2
total = tempo * 50
min = total / 60
print('Levou {:.2f} segundos ou {:.2f} minutos ate que a massa final atingisse {:.2f} gramas'.format(total, min, massa))
