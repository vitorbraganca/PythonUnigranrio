#INSS / IR
while True:
    salb = float(input('Insira o valor do salário bruto: R$'))
    if (salb >= 0): break
    else: print('Salario bruto nao pode ser negativo. Tente novamente')
tx_inss = salb * 0.1
tx_ir = salb * 0.25
tx_sind = salb * 0.05
tx_total = (tx_inss + tx_ir + tx_sind)
sallqd = salb - tx_total
desconto = """SALÁRIO BRUTO: R${:.2f}
========== CONTRIBUIÇÕES ==========
       INSS:      R${:.2f}
IMPOSTO DE RENDA: R${:.2f}
    SINDICATO:    R${:.2f}
      TOTAIS:     R${:.2f}
=================================== 
SALÁRIO LÍQUIDO:  R${:.2f}     
"""
print(desconto.format(salb, tx_inss, tx_ir, tx_sind, tx_total, sallqd))