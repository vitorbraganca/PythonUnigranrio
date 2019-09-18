# Lanchonete
valor = 0
while True:
    while True:
        opcao = int(input("""
    ============================================================
    ESPECIFICAÇÃO     |   CÓDIGO    | PREÇO
    Cachorro Quente   |     100     |   R$ 5,20
    Hambúrguer        |     101     |   R$ 5,20
    Cheeseburguer     |     102     |   R$ 7,30
    Refrigerante      |     103     |   R$ 5,00
    ============================================================
    
    OPÇÃO: """))
        if (opcao == 100) or (opcao == 101):
            valor += 5.2
            print('Valor parcial: {:.2f}'.format(valor))
            break
        elif opcao == 102:
            valor+= 7.3
            print('Valor parcial: {:.2f}'.format(valor))
            break
        elif opcao == 103:
            valor+= 5.0
            print('Valor parcial: {:.2f}'.format(valor))
            break
        else:
            print('Valor parcial: {:.2f}'.format(valor))
            break
    repetir = input('Deseja adicionar algo mais? |SIM (s) ou NAO (n)|:   ')
    repetir = repetir.upper()
    if (repetir == 'NAO') or (repetir == 'N'): break
print('Valor total: {:.2f}'.format(valor))
