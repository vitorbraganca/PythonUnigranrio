#Pedra, papel e tesoura     🖐 ✌ ✊
escolha = """
==============================
1 - PEDRA ✊
2 - PAPEL ✋
3 - TESOURA ✌
==============================
{} ESCOLHE: """
j1_escolha = int(input(escolha.format('JOGADOR 1')))
j2_escolha = int(input(escolha.format('JOGADOR 2')))
if (j1_escolha == 1) and (j2_escolha == 3):
    print('='*30)
    print('JOGADOR 1 ESMAGOU A TESOURA COM SUA PEDRA!!! ✊')
elif (j1_escolha == 3) and (j2_escolha == 2):
    print('='*30)
    print('JOGADOR 1 PICOTOU O PAPEL COM SUA TESOURA!!! ✌')
elif (j1_escolha == 2) and (j2_escolha == 1):
    print('='*30)
    print('JOGADOR 1 EMBRULHOU A PEDRA COM SEU PAPEL!!! ✋')
#
if (j2_escolha == 1) and (j1_escolha == 3):
    print('='*30)
    print('JOGADOR 2 ESMAGOU A TESOURA COM SUA PEDRA!!! ✊')
elif (j2_escolha == 3) and (j1_escolha == 2):
    print('='*30)
    print('JOGADOR 2 PICOTOU O PAPEL COM SUA TESOURA!!! ✌')
elif (j2_escolha == 2) and (j1_escolha == 1):
    print('='*30)
    print('JOGADOR 2 EMBRULHOU A PEDRA COM SEU PAPEL!!! ✋')
elif (j1_escolha == j2_escolha):
    print('='*30)
    print('HOUVE UM EMPATE!!! ')
