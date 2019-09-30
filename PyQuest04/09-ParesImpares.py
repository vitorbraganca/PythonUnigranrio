# Quantidade numeros pares/impares
qntd_impar = 0
qntd_par = 0
qntd_total = 0
print('Digite 000 para parar a qualquer momento.')
while True:
    num = int(input('Insira o numero: '))
    if num == 000:
        break
    elif (num % 2) == 1 :
        qntd_impar += 1
    else:
        qntd_par += 1
    qntd_total += 1
print('{} VALORES DIGITADOS | {} PARES e {} IMPARES.'.format(qntd_total, qntd_par, qntd_impar))
