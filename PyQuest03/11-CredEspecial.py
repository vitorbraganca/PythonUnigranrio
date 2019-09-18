# Credito especial
while True:
    saldo = float(input('Saldo medio no ultimo ano: R$'))
    if (saldo >= 0) and (saldo < 200):
        cred = 0
        break
    elif (saldo >= 201) and (saldo < 400):
        cred = saldo * 0.2
        break
    elif (saldo >= 401) and (saldo < 600):
        cred = saldo * 0.3
        break
    elif (saldo >= 601):
        cred = saldo * 0.4
        break
    else:
        print('Saldo nao pode ser negativo, tente novamente.')
print(' Saldo medio: R${:.2f}     | Credito especial: R${:.2f}'.format(saldo, cred))
