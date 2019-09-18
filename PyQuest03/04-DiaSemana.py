#dia de semana
while True:
    dia = int(input('Insira um numero inteiro para saber o dia da semana: (999 para parar) '))
    if dia == 1: print('Domingo')
    elif dia == 2: print('Segunda')
    elif dia == 3: print('Terça')
    elif dia == 4: print('Quarta')
    elif dia == 5: print('Quinta')
    elif dia == 6: print('Sexta')
    elif dia == 7: print('Sabado')
    elif dia == 999: break
    else: print('Dia invalido')
print('FIM.')
