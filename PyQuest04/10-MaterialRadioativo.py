tempo = 0
massa = float(input('Insira a massa do material em gramas: '))
while massa > 500:
    tempo += 50
    massa = massa / 2
min = tempo / 60
print('Levou {:.2f} segundos ou {:.2f} minutos ate que a massa final atingisse {:.2f} gramas'.format(tempo, min, massa))
