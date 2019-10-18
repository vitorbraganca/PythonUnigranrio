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
            break
        elif opcao == 102:
            valor+= 7.3
            break
        elif opcao == 103:
            valor+= 5.0
            break
        else:
            print('Item invalido. Nada acrescentado.')
            break
    print('Valor parcial: R${:.2f}'.format(valor))
    repetir = input('Deseja adicionar algo mais? |SIM (s) ou NAO (n)|:   ')
    repetir = repetir.upper()
    if (repetir == 'NAO') or (repetir == 'N'): break
print('Valor total: R${:.2f}'.format(valor))
