#   Idade diversos com porcentagem
qntd_menor = 0
qntd_maior = 0
qntd_total = 0
print('Digite 999 para parar a qualquer momento.')
while True:
    idade = int(input('Insira a idade: '))
    if idade == 999:
        break
    elif idade < 18:
        qntd_menor += 1
    elif idade >= 18:
        qntd_maior += 1
    qntd_total += 1
pctg_maior = (qntd_maior / qntd_total) * 100
pctg_menor = (qntd_menor / qntd_total) * 100
print('{} PESSOAS CADASTRADAS | {}% MAIORES DE IDADE e {}% MENORES DE IDADE'.format(qntd_total, pctg_maior, pctg_menor))
