#2: quantidade alunos
while True:
    aluns_m = int(input('Quantidade de alunos do sexo masculino: '))
    aluns_f = int(input('Quantidade de alunos do sexo feminino: '))
    aluns_apv = int(input('Quantidade de alunos aprovados: '))
    if (aluns_apv < 0) or (aluns_f < 0) or (aluns_m < 0): print('Quantidade nao pode ser negativa. Tente novamente')
    else: break
aluns_tot = aluns_m + aluns_f
pctg_m = (aluns_m / aluns_tot) * 100
pctg_f = (aluns_f / aluns_tot) * 100
pctg_apv = (aluns_apv / aluns_tot) * 100
print('Alunos totais: {} | Sendo, {:.2f}% alunos do sexo masculino, {:.2f}% alunos do sexo feminino e {:.2f}% alunos aprovados.'.format(aluns_tot, pctg_m, pctg_f, pctg_apv))