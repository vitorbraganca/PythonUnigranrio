#gratificacao
while True:
    salb = float(input('Insira o valor do salário bruto: R$'))
    if (salb >= 0): break
    else: print('Salario bruto nao pode ser negativo. Tente novamente')
if (salb < 2000): grat = salb * 0.05
elif (salb >= 2000) and (salb < 2500): grat = salb * 0.1
elif (salb >= 2500) and (salb <= 3000): grat = salb * 0.15
else: grat = salb * 0.2
sallqd = salb + grat
print('Gratificação = R${:.2f}      |    Salário Líquido = R${:.2f}'.format(grat, sallqd))