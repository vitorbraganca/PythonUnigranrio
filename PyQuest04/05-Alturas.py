#   Alturas
baixa = 0   #   Abaixo de 1.6
media = 0   #   Entre 1.6 e 1.8
alta = 0    #   Acima de 1.8
qntd = 0
print('Digite 999 a qualquer momento para parar.')
while True:
    altura = float(input('Insira a altura em metros: '))
    if altura == 999:
        break
    elif (altura >= 0) and (altura < 1.6):
        baixa += 1
    elif(altura >= 1.6) and (altura < 1.8):
        media += 1
    elif altura > 1.8:
        alta += 1
    else:
        print('Altura invalida, tente novamente.')
    qntd+=1  #  Contador de pessoas
print('{} Pessoas cadastradas | {} pessoas com altura inferior a 1.6m | {} pessoas com altura entre 1.6m e 1.8m | {} pessoas com altura superior a 1.8m'.format(qntd, baixa, media, alta))